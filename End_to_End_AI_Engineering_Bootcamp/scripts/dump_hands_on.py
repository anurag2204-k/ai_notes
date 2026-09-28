import os
import sys
import json
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

CODE_DIR = r"C:\Users\anurag\Desktop\End-to-End AI Engineering Bootcamp\code"
out_dir = r"c:\Users\anurag\Desktop\notes\End_to_End_AI_Engineering_Bootcamp\scripts"

hands_on_data = {}
for sd in sorted(os.listdir(CODE_DIR)):
    sd_path = os.path.join(CODE_DIR, sd)
    if os.path.isdir(sd_path):
        for f in os.listdir(sd_path):
            if 'hands-on' in f.lower():
                fp = os.path.join(sd_path, f)
                soup = BeautifulSoup(open(fp, encoding='utf-8', errors='ignore').read(), 'html.parser')
                hands_on_data[f"{sd}/{f}"] = {
                    "text": soup.get_text('\n', strip=True),
                    "links": [{"text": a.get_text().strip(), "href": a["href"].strip()} for a in soup.find_all("a", href=True)]
                }

with open(os.path.join(out_dir, "hands_on_extracted.json"), "w", encoding="utf-8") as f:
    json.dump(hands_on_data, f, indent=2, ensure_ascii=False)

print(f"Dumped {len(hands_on_data)} hands-on sections.")
for k, v in hands_on_data.items():
    print(f"Key: {k}")
    print("Links:", [l['text'] for l in v['links']])
