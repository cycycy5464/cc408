# coding: utf-8
import os

YEAR = 2016
CONTENT_DIR = 'content/question'

for fn in sorted(os.listdir(CONTENT_DIR)):
    if not fn.startswith(str(YEAR) + '-'):
        continue
    num = int(fn.split('-')[2].replace('.md', ''))
    if num < 41:
        continue
    fp = os.path.join(CONTENT_DIR, fn)
    with open(fp, encoding='utf-8') as fh:
        lines = fh.readlines()
    issues = []
    code_fence_count = 0
    for i, l in enumerate(lines):
        s = l.strip()
        if s.startswith('```'):
            code_fence_count += 1
            if s == '```':
                # Check if this is start or end
                if code_fence_count % 2 == 1:  # odd = start
                    # Get prev line content
                    prev_content = lines[i-1].strip() if i > 0 else ''
                    # Check if prev line is code or explanation
                    if not prev_content.startswith('```'):
                        issues.append(f'L{i+1}: bare start fence (no language)')
    print(f'{fn}: {"; ".join(issues) if issues else "OK"}')
