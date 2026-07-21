# coding: utf-8
import os

YEAR = 2016
CONTENT_DIR = 'content/question'

fixed = 0
for fn in sorted(os.listdir(CONTENT_DIR)):
    if not fn.startswith(str(YEAR) + '-'):
        continue
    num_str = fn.replace('.md', '').split('-')[2]
    num_int = int(num_str)
    if num_int > 40:
        continue
    
    fp = os.path.join(CONTENT_DIR, fn)
    with open(fp, encoding='utf-8') as fh:
        lines = fh.readlines()
    
    # Find positions of all option lines
    opt_indices = []
    opt_lines = []
    for i, l in enumerate(lines):
        s = l.strip()
        if s[:2] in ['A.', 'B.', 'C.', 'D.'] or s[:3] in ['A\\', 'B\\', 'C\\', 'D\\'] and len(s) >= 3 and s[2] == '.':
            opt_indices.append(i)
            opt_lines.append((l, s[:2]))
    
    # Count per letter
    from collections import Counter
    letters = [ol[1] for ol in opt_lines]
    counts = Counter(letters)
    
    if max(counts.values()) <= 1:
        continue  # no duplicates
    
    # Dedup: keep only last occurrence of each letter
    # Remove first occurrence, keep last
    last_seen = {}
    for idx in reversed(opt_indices):
        l = lines[idx]
        s = l.strip()
        letter = s[:2]  # 'A.' or 'B.'
        if letter not in last_seen:
            last_seen[letter] = idx
    
    # Mark lines to remove
    remove_indices = set()
    for idx in opt_indices:
        l = lines[idx]
        s = l.strip()
        letter = s[:2]
        if idx != last_seen[letter]:
            remove_indices.add(idx)
    
    # Remove from bottom up to preserve indices
    new_lines = [l for i, l in enumerate(lines) if i not in remove_indices]
    
    with open(fp, 'w', encoding='utf-8') as fh:
        fh.writelines(new_lines)
    fixed += 1
    print('{}: removed {} duplicate lines'.format(fn, len(remove_indices)))

print('Total: {} files deduplicated'.format(fixed))
