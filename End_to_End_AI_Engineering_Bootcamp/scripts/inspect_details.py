import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\anurag\Desktop\notes\End_to_End_AI_Engineering_Bootcamp\scripts\course_inventory.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("===== HANDS-ON SECTIONS & ASSIGNMENTS =====")
for sprint_name, files in data['sprints'].items():
    print(f"\n### {sprint_name}")
    for file_info in files:
        fn = file_info['filename']
        if 'hands-on' in fn.lower():
            print(f"File: {fn}")
            print("Headers:", file_info.get('headers', []))
            print("Links:")
            for l in file_info.get('links', []):
                print(f"  - {l['text']} => {l['href']}")
            print("Preview:\n" + file_info.get('summary_preview', '')[:500])
            print("-" * 50)

print("\n===== ALL FILES PER SPRINT =====")
for sprint_name, files in data['sprints'].items():
    print(f"\n### {sprint_name} ({len(files)} files)")
    for f in files:
        print(f"  - {f['filename']} (len={f.get('text_length', 0)})")

print("\n===== PDF SLIDES & INFO REVIEWS =====")
for pdf_name, pinfo in data['pdfs'].items():
    print(f"\n### PDF: {pdf_name} ({pinfo['num_pages']} pages)")
    for sp in pinfo['sample_pages'][:3]:
        print(f"  Page {sp['page_num']}: {sp['text'][:200].replace(chr(10), ' ')}")

print("\n===== NOTEBOOKS IN MAIN REPO =====")
for nb in data['zip_notebooks']:
    print(f"  - {nb['path']} ({nb['num_cells']} cells) | Headings: {nb['headings'][:3]}")
