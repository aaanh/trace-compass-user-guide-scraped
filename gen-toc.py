import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

DOCS_ROOT = "tracecompass-docs"
SUMMARY_MD = "SUMMARY.md"
BASE_URL = "https://archive.eclipse.org/tracecompass/doc/stable/org.eclipse.tracecompass.doc.user/User-Guide.html"

# Helper to sanitize section names for folder names
def safe_name(name):
    # Replace problematic characters for folder names and links
    return name.replace('/', '_').replace(' ', '_').replace('"', '').replace("'", '')

def parse_toc_list(ol_tag, parent_names=None):
    if parent_names is None:
        parent_names = []
    sections = []
    for li in ol_tag.find_all("li", recursive=False):
        a = li.find("a", href=True)
        if not a:
            continue
        href = a['href']
        section_title = a.get_text(strip=True)
        section_names = parent_names + [section_title]
        frag = href.split('#')[1] if '#' in href else None
        sections.append({
            'section_names': section_names,
            'frag': frag
        })
        # Only get direct child <ol> for proper hierarchy
        nested_ol = li.find("ol", recursive=False)
        if nested_ol:
            sections.extend(parse_toc_list(nested_ol, section_names))
    return sections

def get_output_path(section_names, frag=None):
    safe_names = [safe_name(name) for name in section_names]
    dir_path = os.path.join(DOCS_ROOT, *safe_names)
    filename = "index.md"
    if frag:
        filename = f"index.md"
    return os.path.join(dir_path, filename)

def build_summary(sections):
    # Group by top-level part, skipping 'Table of contents'
    parts = {}
    for section in sections:
        part = section['section_names'][0]
        if part.strip().lower() == 'table of contents':
            continue
        parts.setdefault(part, []).append(section)

    lines = []
    for part, part_sections in parts.items():
        # Find the first section for this part to get the path
        first_section = part_sections[0]
        out_path = get_output_path(first_section['section_names'], first_section.get('frag'))
        rel_path = os.path.relpath(out_path, DOCS_ROOT)
        # Add the top-level entry as a list item (not a heading)
        lines.append(f"- [{part.replace('"', '').replace("'", '')}]({rel_path})")
        # Build a tree for this part
        def add_to_tree(tree, section):
            names = section['section_names'][1:]  # skip part
            frag = section['frag']
            node = tree
            for name in names[:-1]:
                for child in node.setdefault('children', []):
                    if child['title'] == name:
                        node = child
                        break
                else:
                    new_child = {'title': name, 'children': []}
                    node.setdefault('children', []).append(new_child)
                    node = new_child
            # Add leaf
            leaf = {'title': names[-1] if names else part, 'frag': frag, 'section_names': section['section_names']}
            node.setdefault('children', []).append(leaf)
        root = {'children': []}
        for section in part_sections:
            add_to_tree(root, section)
        # Get the path of the parent (top-level) file to avoid duplicate
        parent_path = rel_path
        def walk(node, depth=1):
            lines = []
            children = node.get('children', [])
            for child in children:
                indent = '  ' * depth
                if 'section_names' in child:
                    out_path = get_output_path(child['section_names'], child.get('frag'))
                    rel_path_child = os.path.relpath(out_path, DOCS_ROOT)
                    # Skip if this is the same as the parent path (avoid duplicate)
                    if rel_path_child == parent_path:
                        continue
                    # Remove quotation marks from titles for Markdown
                    title = child['title'].replace('"', '').replace("'", '')
                    lines.append(f"{indent}- [{title}]({rel_path_child})")
                if child.get('children'):
                    lines.extend(walk(child, depth + 1))
            return lines
        lines.extend(walk(root, 1))
    return lines

if __name__ == "__main__":
    print("Fetching ToC page...")
    resp = requests.get(BASE_URL)
    if resp.status_code != 200:
        raise RuntimeError(f"Failed to load ToC: {BASE_URL}")
    soup = BeautifulSoup(resp.content, "html.parser")
    main_ol = None
    for toc_selector in ['#toc ol', '.toc ol', 'ol.toc', 'ol']:
        main_ol = soup.select_one(toc_selector)
        if main_ol:
            break
    if not main_ol:
        print("[WARN] Could not find main ToC <ol>. Exiting.")
        exit(1)
    section_entries = parse_toc_list(main_ol)
    toc_lines = build_summary(section_entries)
    # Always write to src/SUMMARY.md for mdBook compatibility
    summary_path = os.path.join('src', 'SUMMARY.md')
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(toc_lines) + "\n")
    print(f"SUMMARY.md generated at {summary_path} with {len(toc_lines)} entries.") 