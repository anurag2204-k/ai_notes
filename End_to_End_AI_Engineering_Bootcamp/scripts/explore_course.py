import os
import sys
import json
import zipfile
import fitz
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\anurag\Desktop\End-to-End AI Engineering Bootcamp"
CODE_DIR = os.path.join(ROOT_DIR, "code")

# 1. Parse names.txt
names_file = os.path.join(ROOT_DIR, "names.txt")
video_names = []
if os.path.exists(names_file):
    with open(names_file, "r", encoding="utf-8", errors="ignore") as f:
        video_names = [line.strip() for line in f if line.strip()]

# 2. List all root mp4 files
root_files = os.listdir(ROOT_DIR)
videos = []
for f in root_files:
    if f.lower().endswith(".mp4"):
        sz = os.path.getsize(os.path.join(ROOT_DIR, f))
        videos.append({"filename": f, "size": sz})

# 3. Explore code directory
code_items = os.listdir(CODE_DIR)

# 4. Explore PDFs in code
pdfs_info = {}
for item in code_items:
    if item.lower().endswith(".pdf"):
        pdf_path = os.path.join(CODE_DIR, item)
        doc = fitz.open(pdf_path)
        pages = []
        for i, page in enumerate(doc):
            txt = page.get_text()
            pages.append({"page_num": i+1, "text": txt[:500], "full_len": len(txt)})
        pdfs_info[item] = {
            "num_pages": len(doc),
            "sample_pages": pages[:10]
        }

# 5. Explore notebooks inside main zip
main_zip = os.path.join(CODE_DIR, "ai-engineering-bootcamp-cohort-4-main.zip")
zip_notebooks = []
all_zip_files = []
if os.path.exists(main_zip):
    with zipfile.ZipFile(main_zip, "r") as z:
        all_zip_files = z.namelist()
        for name in all_zip_files:
            if name.endswith(".ipynb"):
                try:
                    raw = z.read(name).decode("utf-8", errors="ignore")
                    nb_json = json.loads(raw)
                    cells = nb_json.get("cells", [])
                    headings = []
                    for c in cells:
                        if c.get("cell_type") == "markdown":
                            for line in c.get("source", []):
                                if line.strip().startswith("#"):
                                    headings.append(line.strip())
                    zip_notebooks.append({
                        "path": name,
                        "num_cells": len(cells),
                        "headings": headings[:15]
                    })
                except Exception as e:
                    zip_notebooks.append({"path": name, "error": str(e)})

# 6. Explore each Sprint directory and its HTML files
sprint_dirs = [d for d in code_items if os.path.isdir(os.path.join(CODE_DIR, d))]
sprint_dirs.sort()

sprints_data = {}
for sd in sprint_dirs:
    sd_path = os.path.join(CODE_DIR, sd)
    files = sorted(os.listdir(sd_path))
    sprint_files_data = []
    for f in files:
        f_path = os.path.join(sd_path, f)
        if f.lower().endswith(".html"):
            with open(f_path, "r", encoding="utf-8", errors="ignore") as fp:
                soup = BeautifulSoup(fp.read(), "html.parser")
                title = soup.title.string.strip() if soup.title and soup.title.string else f
                
                # Extract headers
                headers = [h.get_text().strip() for h in soup.find_all(["h1", "h2", "h3"]) if h.get_text().strip()]
                
                # Extract links
                links = []
                for a in soup.find_all("a", href=True):
                    href = a["href"].strip()
                    txt = a.get_text().strip()
                    if href and not href.startswith("javascript:") and not href.startswith("#"):
                        links.append({"text": txt, "href": href})
                
                # Extract paragraphs sample
                body_text = soup.get_text(separator="\n", strip=True)
                
                sprint_files_data.append({
                    "filename": f,
                    "title": title,
                    "headers": headers,
                    "links": links,
                    "text_length": len(body_text),
                    "summary_preview": body_text[:1200]
                })
        else:
            sprint_files_data.append({
                "filename": f,
                "type": "non-html",
                "size": os.path.getsize(f_path)
            })
    sprints_data[sd] = sprint_files_data

# Also check root html file
root_html = {}
if os.path.exists(os.path.join(CODE_DIR, "Setting up your development environment..html")):
    p = os.path.join(CODE_DIR, "Setting up your development environment..html")
    with open(p, "r", encoding="utf-8", errors="ignore") as fp:
        soup = BeautifulSoup(fp.read(), "html.parser")
        headers = [h.get_text().strip() for h in soup.find_all(["h1", "h2", "h3"]) if h.get_text().strip()]
        links = [{"text": a.get_text().strip(), "href": a["href"].strip()} for a in soup.find_all("a", href=True) if a["href"].strip()]
        root_html["Setting up your development environment..html"] = {
            "title": soup.title.string.strip() if soup.title and soup.title.string else "Setting up your development environment",
            "headers": headers,
            "links": links,
            "text": soup.get_text(separator="\n", strip=True)
        }

output_data = {
    "root_dir": ROOT_DIR,
    "code_dir": CODE_DIR,
    "video_names": video_names,
    "videos_count": len(videos),
    "videos": sorted(videos, key=lambda x: x["filename"]),
    "pdfs": pdfs_info,
    "zip_notebooks": zip_notebooks,
    "all_zip_files_count": len(all_zip_files),
    "sprints": sprints_data,
    "root_html": root_html
}

out_path = r"c:\Users\anurag\Desktop\notes\End_to_End_AI_Engineering_Bootcamp\scripts\course_inventory.json"
with open(out_path, "w", encoding="utf-8") as out_fp:
    json.dump(output_data, out_fp, indent=2, ensure_ascii=False)

print(f"Inventory completed. Saved to {out_path}")
print(f"Sprints identified: {len(sprints_data)}")
for k, v in sprints_data.items():
    print(f"  {k}: {len(v)} files")
print(f"PDFs: {list(pdfs_info.keys())}")
print(f"Notebooks in zip: {len(zip_notebooks)}")
