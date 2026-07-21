# coding: utf-8
import glob, os

files = sorted(glob.glob('content/question/2016-*.md'))

# Check 4 options for all 40 choices
bad = []
for f in files:
    fn = os.path.basename(f)
    num = int(fn.split('-')[2].replace('.md', ''))
    if num > 40: continue
    with open(f, encoding='utf-8') as fh:
        text = fh.read()
    lines = text.split('\n')
    counts = {}
    for l in lines:
        s = l.strip()
        if len(s) >= 2 and s[0] in 'ABCD':
            ch2 = s[1]
            ch3 = s[2] if len(s) >= 3 else ''
            if ch2 == '.' or (ch2 == chr(92) and ch3 == '.'):
                counts[s[0]] = counts.get(s[0], 0) + 1
    if not all(counts.get(c, 0) == 1 for c in 'ABCD'):
        bad.append(fn + ' ' + str({k: v for k,v in counts.items() if v != 1}))
    
    # Check D-[tag_link] blank line
    d_idx = -1
    tag_idx = -1
    for i, l in enumerate(lines):
        s = l.strip()
        if len(s) >= 2 and s[0] == 'D':
            ch2 = s[1]
            ch3 = s[2] if len(s) >= 3 else ''
            if ch2 == '.' or (ch2 == chr(92) and ch3 == '.'):
                d_idx = i
        if '[tag_link]' in l:
            tag_idx = i
            break
    if d_idx >= 0 and tag_idx >= 0 and tag_idx - d_idx <= 1:
        bad.append(fn + ' D-tag gap=' + str(tag_idx - d_idx))

print(f'Choices: {40 - len(bad)}/40 OK')
if bad:
    for b in bad:
        print('  ' + b)

# Check comprehensive tag_link
comp_ok = 0
for f in files:
    fn = os.path.basename(f)
    num = int(fn.split('-')[2].replace('.md', ''))
    if num < 41: continue
    with open(f, encoding='utf-8') as fh:
        text = fh.read()
    if '[tag_link]' in text:
        comp_ok += 1
    else:
        print(fn + ': MISSING tag_link')
print(f'Comprehensive: {comp_ok}/7 with tag_link')
