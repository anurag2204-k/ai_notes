import json

with open("scratch/raw_data_summary.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for fname, info in data.items():
    if "links" in info:
        for l in info["links"]:
            if "canva.com" in l["url"]:
                print(f"{fname:<65} | {l['text']} -> {l['url']}")
    if fname.endswith(".txt") and "canva.com" in info.get("content", ""):
        print(f"{fname:<65} | slides txt -> {info['content']}")
