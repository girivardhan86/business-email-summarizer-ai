# inspect_jsonl.py
import json
from pathlib import Path

p = Path("data/cleaned_for_training.jsonl")

print("Path exists:", p.exists())
print("Path absolute:", p.resolve())
print("File size (bytes):", p.stat().st_size if p.exists() else "N/A")

if not p.exists():
    raise SystemExit("File not found. Move the file to data/ or update the INPUT path.")

count = 0
parsed = 0
first_good = None
keys_seen = set()
with p.open("r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if not line.strip():
            continue
        count += 1
        try:
            obj = json.loads(line)
            parsed += 1
            if i < 5:
                print(f"\n--- line {i+1} parsed keys: {list(obj.keys())} ---")
                for k,v in obj.items():
                    print(f"{k}: {str(v)[:200]!r}")
            keys_seen.update(obj.keys())
            if first_good is None and any(obj.get(k) for k in ("text","email","body","content","prompt")):
                first_good = obj
        except Exception as e:
            print("JSON parse error on line", i+1, ":", e)
        if i >= 20:
            break

print("\nTotal non-empty lines seen (count):", count)
print("Successfully parsed lines:", parsed)
print("Keys seen in first ~20 lines:", keys_seen)
if first_good:
    print("\nSample detected text field(s):")
    for k in ("text","email","body","content","prompt"):
        if k in first_good:
            print(f" {k} (len={len(str(first_good[k]))}):", str(first_good[k])[:300])
else:
    print("No example containing common text fields (text/email/body/content/prompt) found in those lines.")
