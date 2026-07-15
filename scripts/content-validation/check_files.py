"""Check files for content issues that could cause Hugo .Summary errors"""
import os, glob

QUESTION_DIR = 'content/question'

touched = [
    '2009-ds-002.md', 'simulate-2-co-015.md',
    '2014-ds-041.md', 'simulate-1-ds-041.md', 'simulate-2-ds-041.md',
    'simulate-5-ds-041.md', 'simulate-6-ds-041.md', 'simulate-7-ds-041.md',
    'simulate-8-ds-041.md',
    '2009-ds-006.md', '2009-ds-009.md', '2009-cn-037.md', '2009-cn-047.md',
    '2009-co-044.md',
    '2014-ds-042.md', '2014-os-045.md', '2014-os-046.md',
    '2017-cn-035.md', '2020-cn-037.md', '2022-cn-036.md', '2022-cn-040.md',
    '2022-cn-047.md', '2022-co-019.md', '2022-co-043.md', '2022-co-044.md',
]
for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    for subj in ['cn', 'co', 'os', 'ds']:
        for n in ['043', '044', '045', '047', '041', '042']:
            touched.append(f'simulate-{i}-{subj}-{n}.md')
touched = list(set(touched))

error_files = []
for fn in sorted(touched):
    path = os.path.join(QUESTION_DIR, fn)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    row_issues = []

    # 1. unclosed code fences
    count = content.count('```')
    if count % 2 != 0:
        row_issues.append(f'unclosed code fences ({count})')

    # 2. very long unbroken text lines
    for i, line in enumerate(content.split('\n'), 1):
        stripped = line.strip()
        if stripped.startswith('---') or stripped.startswith('```'):
            continue
        if ' ' not in stripped and len(stripped) > 200:
            row_issues.append(
                f'L{i}: long unbroken text ({len(stripped)} chars)'
            )
            break

    # 3. file too big
    if len(content) > 100000:
        row_issues.append(f'file too large ({len(content)} bytes)')

    # 4. odd dollar signs
    dc = content.count('$')
    if dc > 0 and dc % 2 != 0:
        row_issues.append(f'unclosed LaTeX $ ({dc} total)')

    # 5. smart quotes or unusual chars in content
    for ch in ['\u201c', '\u201d', '\u2018', '\u2019']:
        if ch in content:
            row_issues.append(f'smart quote char found: {repr(ch)}')
            break

    if row_issues:
        error_files.append((fn, row_issues))
        print(f'  \u26a0\ufe0f {fn}:')
        for iss in row_issues:
            print(f'    \u2717 {iss}')
    else:
        print(f'  \u2713 {fn}')

if error_files:
    print(f'\nFound {len(error_files)} files with potential issues')
