import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\anurag\Desktop\notes\End_to_End_AI_Engineering_Bootcamp\scripts\hands_on_extracted.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, v in data.items():
    print(f"*** {k} ***")
    lines = [line.strip() for line in v['text'].splitlines() if line.strip()]
    # filter out navigation noise
    meaningful = []
    skip = False
    for l in lines:
        if "Home" in l or "Inbox" in l or "announcements" in l or "💭questions" in l:
            continue
        meaningful.append(l)
    print("\n".join(meaningful[:40]))
    print("="*60)
