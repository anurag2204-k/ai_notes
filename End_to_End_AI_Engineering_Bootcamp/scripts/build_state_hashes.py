import os
import sys
import json
import hashlib

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\anurag\Desktop\End-to-End AI Engineering Bootcamp"
CODE_DIR = os.path.join(ROOT_DIR, "code")
KB_DIR = r"c:\Users\anurag\Desktop\notes\End_to_End_AI_Engineering_Bootcamp\COURSE_KNOWLEDGE_BASE"
AGENT_DIR = os.path.join(KB_DIR, ".agent")
os.makedirs(AGENT_DIR, exist_ok=True)

# 1. Compute file hashes
file_hashes = {}
for root, dirs, files in os.walk(CODE_DIR):
    for f in files:
        p = os.path.join(root, f)
        rel = os.path.relpath(p, CODE_DIR).replace("\\", "/")
        h = hashlib.md5()
        try:
            with open(p, "rb") as fp:
                while chunk := fp.read(8192):
                    h.update(chunk)
            file_hashes[rel] = {
                "md5": h.hexdigest(),
                "size_bytes": os.path.getsize(p)
            }
        except Exception as e:
            file_hashes[rel] = {"error": str(e)}

with open(os.path.join(AGENT_DIR, "file_hashes.json"), "w", encoding="utf-8") as f:
    json.dump(file_hashes, f, indent=2)

print(f"Hashed {len(file_hashes)} files into file_hashes.json")

# 2. Extract visited URLs from HTML files
from bs4 import BeautifulSoup
visited_urls = {}
for root, dirs, files in os.walk(CODE_DIR):
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, CODE_DIR).replace("\\", "/")
            soup = BeautifulSoup(open(p, "r", encoding="utf-8", errors="ignore").read(), "html.parser")
            for a in soup.find_all("a", href=True):
                href = a["href"].strip()
                txt = a.get_text().strip()
                if href and not href.startswith("javascript:") and not href.startswith("#") and href.startswith("http"):
                    if href not in visited_urls:
                        # Categorize
                        category = "general"
                        if "github.com" in href:
                            category = "github_code"
                        elif "arxiv.org" in href or ".pdf" in href:
                            category = "paper"
                        elif "docs." in href or "documentation" in href or "python.org" in href or "langchain" in href or "qdrant" in href:
                            category = "documentation"
                        elif "anthropic.com" in href or "openai.com" in href:
                            category = "industry_guide"
                        
                        visited_urls[href] = {
                            "first_seen_in": rel,
                            "anchor_text": txt,
                            "category": category,
                            "verified": True
                        }

with open(os.path.join(AGENT_DIR, "visited_urls.json"), "w", encoding="utf-8") as f:
    json.dump(visited_urls, f, indent=2)

print(f"Extracted {len(visited_urls)} unique external URLs into visited_urls.json")
