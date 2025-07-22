import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict

BASE_URL = "https://archive.eclipse.org/tracecompass/doc/stable/org.eclipse.tracecompass.doc.user/User-Guide.html"
OUTPUT_DIR = "tracecompass-docs"

def parse_toc_list(ul_tag, prefix=""):
    """
    Recursively parse nested <ul> lists of ToC.
    Return list of tuples: (section_number, full_url, fragment)
    """
    sections = []
    count = 0
    for li in ul_tag.find_all("li", recursive=False):
        count += 1
        section_num = f"{prefix}{count}" if prefix == "" else f"{prefix}.{count}"
        a = li.find("a", href=True)
        if not a:
            continue
        href = a['href']
        full_url = urljoin(BASE_URL, href.split('#')[0])
        frag = href.split('#')[1] if '#' in href else None
        sections.append((section_num, full_url, frag))
        # Recurse if nested <ul>
        nested_ul = li.find("ul")
        if nested_ul:
            sections.extend(parse_toc_list(nested_ul, section_num))
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


def get_output_path(base_url, frag=None):
    parsed = urlparse(base_url)
    path = parsed.path.split("/org.eclipse.tracecompass.doc.user/")[-1]
    if path.endswith(".html"):
        path = path[:-5]
    if frag:
        path += f"_{frag}"
    return os.path.join(OUTPUT_DIR, path + ".md")

# Fetch ToC page
print("Fetching ToC page...")
resp = requests.get(BASE_URL)
if resp.status_code != 200:
    raise RuntimeError(f"Failed to load ToC: {BASE_URL}")
soup = BeautifulSoup(resp.content, "html.parser")

# Build map: base HTML → list of fragments
fragment_map = defaultdict(set)
for a in soup.select('a[href*=".html"]'):
    href = a['href']
    full_url = urljoin(BASE_URL, href)
    parts = full_url.split('#', 1)
    base = parts[0]
    frag = parts[1] if len(parts) == 2 else None
    if "org.eclipse.tracecompass.doc.user/" in base:
        fragment_map[base].add(frag)

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
        if frag is None:
            content = soup.body
            markdown = html_to_markdown(str(content))
            out_path = get_output_path(base_url)
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
            out_path = get_output_path(base_url, frag)

        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"  ✓ Saved {out_path}")
