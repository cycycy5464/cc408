# coding: utf-8
YEAR = 2016
CONTENT_DIR = 'content/question'

import os
for fn in sorted(os.listdir(CONTENT_DIR)):
    if not fn.startswith(str(YEAR) + '-'):
        continue
    with open(os.path.join(CONTENT_DIR, fn), encoding='utf-8') as f:
        lines = f.readlines()
    for i, l in enumerate(lines):
        if '[tag_link]' in l:
            print(fn, 'L{}: {}'.format(i+1, repr(l.rstrip())))
            for j in range(max(0,i-3), min(len(lines), i+3)):
                print('  L{}: {}'.format(j+1, repr(lines[j].rstrip()[:70])))
            print()
            break
