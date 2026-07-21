# coding: utf-8
import re, os

# Check ALL 2015 choice files for duplicates
content_dir = 'content/question'
files = sorted(os.listdir(content_dir))

for fn in files:
    if not fn.startswith('2015-'):
        continue
    fp = os.path.join(content_dir, fn)
    with open(fp, encoding='utf-8') as f:
        text = f.read()
    opts = re.findall(r'^([A-D])[.\\\\]', text, re.MULTILINE)
    
    # Group by letter
    counts = {}
    for o in opts:
        counts[o] = counts.get(o, 0) + 1
    
    issues = []
    for letter, count in counts.items():
        if count > 1:
            issues.append(f'{letter}x{count}')
    
    if issues:
        print(f'{fn}: {", ".join(issues)}')
