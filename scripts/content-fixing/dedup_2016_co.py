# coding: utf-8
import os

YEAR = 2016
CONTENT_DIR = 'content/question'

for fn in sorted(os.listdir(CONTENT_DIR)):
    if not fn.startswith(str(YEAR) + '-'):
        continue
    num_str = fn.replace('.md', '').split('-')[2]
    num_int = int(num_str)
    if num_int > 40:
        continue
    
    fp = os.path.join(CONTENT_DIR, fn)
    with open(fp, encoding='utf-8') as fh:
        text = fh.read()
    
    lines = text.split('\n')
    
    # Find option line indices by letter
    opt_by_letter = {}
    for i, l in enumerate(lines):
        s = l.strip()
        if not s:
            continue
        if s[0] not in 'ABCD':
            continue
        # Check A. (plain dot) or A\. (backslash dot)
        ch2 = s[1] if len(s) >= 2 else ''
        ch3 = s[2] if len(s) >= 3 else ''
        is_option = (ch2 == '.') or (ch2 == '\\' and ch3 == '.')
        if is_option:
            opt_by_letter.setdefault(s[0], []).append(i)
    
    # Check for duplicates
    dups_found = False
    to_remove = set()
    for letter, indices in opt_by_letter.items():
        if len(indices) > 1:
            dups_found = True
            for idx in indices[:-1]:
                to_remove.add(idx)
    
    if not dups_found:
        continue
    
    new_lines = [l for i, l in enumerate(lines) if i not in to_remove]
    out = '\n'.join(new_lines)
    
    with open(fp, 'w', encoding='utf-8') as fh:
        fh.write(out)
    print('{}: removed {} duplicate lines'.format(fn, len(to_remove)))
