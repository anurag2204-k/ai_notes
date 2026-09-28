import json

with open("scratch/raw_data_summary.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== YOUTUBE VIDEOS ===")
seen_yt = set()
for fname, info in data.items():
    if "links" in info:
        for l in info["links"]:
            if "youtube.com" in l["url"] or "youtu.be" in l["url"]:
                u = l["url"]
                if u not in seen_yt:
                    seen_yt.add(u)
                    print(f"{fname:<40} | {l['text']} -> {u}")

print("\n=== NOTEBOOKLM AUDIO OVERVIEWS ===")
seen_nlm = set()
for fname, info in data.items():
    if "links" in info:
        for l in info["links"]:
            if "notebooklm.google.com" in l["url"]:
                u = l["url"]
                if u not in seen_nlm:
                    seen_nlm.add(u)
                    print(f"{fname:<40} | {l['text']} -> {u}")
