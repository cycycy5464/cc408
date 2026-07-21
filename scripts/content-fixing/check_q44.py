import json

with open('tasks/408-crawler/crawled_data/2014.json', encoding='utf-8') as f:
    data = json.load(f)

# Look at questions field
questions = data.get('questions', {})
q44 = questions.get('44')
if q44:
    print(f"type={type(q44).__name__}")
    if isinstance(q44, dict):
        for k, v in q44.items():
            val_str = repr(v)[:200]
            print(f"  {k}: {val_str}")
else:
    print("q44 not in questions")

# Try other fields
for key in data:
    if key in ('year', 'url'):
        continue
    val = data[key]
    if isinstance(val, dict) and '44' in val:
        print(f"\n{key} has Q44: type={type(val['44']).__name__}")
        print(f"  {repr(val['44'])[:500]}")
