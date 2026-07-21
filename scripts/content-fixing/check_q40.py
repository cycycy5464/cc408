import json

with open('tasks/408-crawler/crawled_data/2014.json', encoding='utf-8') as f:
    data = json.load(f)

# Look at raw HTML for Q40
questions = data.get('questions', {})
q40 = questions.get('40')
if q40 is not None:
    print(f"type: {type(q40).__name__}")
    print(f"repr: {repr(q40)[:300]}")
else:
    print("q40 not in questions")

# Try to find any field containing Q40
for key, val in data.items():
    if isinstance(val, dict) and '40' in val:
        print(f"Field '{key}': {type(val['40']).__name__}")
        rep = repr(val['40'])[:200]
        print(f"  content: {rep}")
