import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict

BASE_URL = "https://archive.eclipse.org/tracecompass/doc/stable/org.eclipse.tracecompass.doc.user/User-Guide.html"
OUTPUT_DIR = "tracecompass-docs"

def parse_toc_list(ol_tag, prefix="", parent_names=None):
    """
    Recursively parse nested <ol> lists of ToC.
    Return list of tuples: (section_number, section_names, full_url, fragment)
    section_names is a list of section names from root to this section.
    """
    if parent_names is None:
        parent_names = []
    sections = []
    count = 0
    for li in ol_tag.find_all("li", recursive=False):
        count += 1
        section_num = f"{prefix}{count}" if prefix == "" else f"{prefix}.{count}"
        a = li.find("a", href=True)
        if not a:
            continue
        href = a['href']
        full_url = urljoin(BASE_URL, href.split('#')[0])
        frag = href.split('#')[1] if '#' in href else None
        section_title = a.get_text(strip=True)
        section_names = parent_names + [section_title]
        sections.append((section_num, section_names, full_url, frag))
        # Recurse if nested <ol>
        nested_ol = li.find("ol")
        if nested_ol:
            sections.extend(parse_toc_list(nested_ol, section_num, section_names))
    return sections



def html_to_markdown(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.select("header, footer, nav, .navbar, #toc, #header, #footer"):
        tag.decompose()
    for tag in soup(["script", "style"]):
        tag.decompose()

    # Use soup directly if soup.body is None
    container = soup.body if soup.body else soup

    result = ""
    for elem in container.descendants:
        if elem.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(elem.name[1])
            result += f"\n{'#' * level} {elem.get_text(strip=True)}\n"
        elif elem.name == "p":
            result += f"\n{elem.get_text(strip=True)}\n"
        elif elem.name == "li":
            result += f"- {elem.get_text(strip=True)}\n"
    return result.strip()


def get_output_path(section_names, frag=None):
    # Use section names to build directory structure, save as index.md
    safe_names = [name.replace('/', '_').replace(' ', '_') for name in section_names]
    dir_path = os.path.join(OUTPUT_DIR, *safe_names)
    filename = "index.md"
    if frag:
        filename = f"index.md"
    return os.path.join(dir_path, filename)

# Fetch ToC page
print("Fetching ToC page...")
resp = requests.get(BASE_URL)
if resp.status_code != 200:
    raise RuntimeError(f"Failed to load ToC: {BASE_URL}")
soup = BeautifulSoup(resp.content, "html.parser")

# Parse ToC for section numbers and URLs
# Try to find the main ToC <ol> more robustly
main_ol = None
# Try common ToC containers
for toc_selector in ['#toc ol', '.toc ol', 'ol.toc', 'ol']:  # order: id, class, fallback
    main_ol = soup.select_one(toc_selector)
    if main_ol:
        break
if not main_ol:
    print("[WARN] Could not find main ToC <ol>. Exiting.")
    exit(1)
section_entries = parse_toc_list(main_ol)

# Build map: (base HTML, frag) -> (section number, section names)
section_map = dict()
for section_num, section_names, full_url, frag in section_entries:
    section_map[(full_url, frag)] = (section_num, section_names)

# Build map: base HTML → list of fragments (for fetching)
fragment_map = defaultdict(set)
for (full_url, frag) in section_map:
    fragment_map[full_url].add(frag)

print(f"Found {len(fragment_map)} unique base HTML pages")

# Process each HTML file + its fragments
for base_url, frags in fragment_map.items():
    print(f"Processing {base_url} with {len(frags)} fragments")
    resp = requests.get(base_url)
    if resp.status_code != 200:
        print(f"  ✘ Failed to fetch {base_url}")
        continue
    soup = BeautifulSoup(resp.content, "html.parser")

    for frag in frags:
        section_info = section_map.get((base_url, frag), None)
        if not section_info:
            print(f"  ⚠ No section info for {base_url}#{frag}")
            continue
        section_num, section_names = section_info
        if frag is None:
            content = soup.body
            markdown = html_to_markdown(str(content))
            out_path = get_output_path(section_names)
        else:
            target = soup.find(id=frag)
            if not target or target.name not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                print(f"  ⚠ Skipping #{frag} (not a heading)")
                continue
            level = int(target.name[1])
            section = [target]
            for sib in target.find_all_next():
                if sib.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] and int(sib.name[1]) <= level:
                    break
                section.append(sib)
            markdown = html_to_markdown(''.join(str(tag) for tag in section))
            out_path = get_output_path(section_names, frag)

        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"  ✓ Saved {out_path}")
