import json

with open("scratch/raw_data_summary.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== ARXIV PAPERS ===")
seen_arxiv = set()
for fname, info in data.items():
    if "links" in info:
        for l in info["links"]:
            if "arxiv.org" in l["url"]:
                u = l["url"].split("?")[0]
                if u not in seen_arxiv:
                    seen_arxiv.add(u)
                    print(f"{fname:<40} | {l['text']} -> {u}")
