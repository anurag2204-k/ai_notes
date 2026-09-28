import json

with open("scratch/raw_data_summary.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== GITHUB REPOSITORIES ===")
seen_github = set()
for fname, info in data.items():
    if "links" in info:
        for l in info["links"]:
            if "github.com" in l["url"]:
                u = l["url"].split("?")[0]
                if u not in seen_github:
                    seen_github.add(u)
                    print(f"{fname:<40} | {l['text']} -> {u}")

print("\n=== GOOGLE DRIVE LINKS ===")
seen_drive = set()
for fname, info in data.items():
    if "links" in info:
        for l in info["links"]:
            if "drive.google.com" in l["url"]:
                u = l["url"]
                if u not in seen_drive:
                    seen_drive.add(u)
                    print(f"{fname:<40} | {l['text']} -> {u}")
