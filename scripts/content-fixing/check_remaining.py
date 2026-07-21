"""检查剩余文件的选项行情况"""
import re, os, glob

BASE = 'D:/projet/cc408/cc408'
CONTENT = os.path.join(BASE, 'content', 'question')

for bn in ['2014-co-012.md', '2014-co-013.md', '2014-co-014.md',
           '2014-cn-033.md', '2014-cn-037.md', '2014-cn-039.md',
           '2014-co-022.md', '2014-ds-005.md', '2014-ds-009.md',
           '2014-os-024.md', '2014-os-027.md']:
    with open(os.path.join(CONTENT, bn), encoding='utf-8') as f:
        lines = f.read().split('\n')
    
    # Find all option lines
    opts = []
    for i, l in enumerate(lines):
        s = l.strip()
        if not s or len(s) < 2:
            continue
        first = s[0]
        second = s[1]
        if first in 'ABCD' and (second == '.' or (second == '\\' and len(s) > 2 and s[2] == '.')):
            opts.append((i+1, first, second == '.', s[:80]))
    
    print(f"\n{bn}:")
    for lineno, letter, is_plain, content in opts:
        fmt = "plain" if is_plain else "bslash"
        print(f"  L{lineno} [{fmt}] {letter}. {content}")
    
    # find tag_link
    for i, l in enumerate(lines):
        if '[tag_link]' in l:
            print(f"  L{i+1}: [tag_link]")
            break
