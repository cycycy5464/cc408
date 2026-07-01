#!/usr/bin/env python3
"""Convert csgraduates-main content to cc408 format (quiz, simulate, code)"""
import os, re, shutil, sys

SRC = r'D:\内容整理\csgraduates-main'
DST = 'content'
DST_EXAM = f'{DST}/exam'
DST_CODE = f'{DST}/code'

def clean_content(text):
    """Clean source text - remove Source line, fix internal links"""
    text = re.sub(r'^> Source:.*\n?', '', text, flags=re.MULTILINE)
    # Fix csgraduates internal links: absolute paths
    text = re.sub(r'\(https?://www\.csgraduates\.com[^)]+\)', '(#)', text)
    # Fix relative links like [链表](/study_methods/tags/...)
    text = re.sub(r'\[([^\]]+)\]\(/[^)]+\)', r'\1', text)
    # Fix anchor-only links
    text = re.sub(r'\[([^\]]+)\]\(#[^)]+\)', r'\1', text)
    return text

def convert_quiz():
    """Convert 408quiz yearly exams to cc408 format"""
    quiz_src = f'{SRC}/study_methods/408quiz'
    quiz_dst = f'{DST_EXAM}/408quiz'
    os.makedirs(quiz_dst, exist_ok=True)

    years = sorted([d for d in os.listdir(quiz_src) if d.isdigit() and os.path.isdir(f'{quiz_src}/{d}')])
    count = 0
    for year in years:
        src_file = f'{quiz_src}/{year}/content.md'
        if not os.path.exists(src_file):
            continue
        with open(src_file, 'r', encoding='utf-8') as f:
            text = f.read()

        # Extract title
        title_match = re.search(r'^# (.+)', text)
        title = title_match.group(1).strip() if title_match else f'{year}年408真题'

        # Clean content
        text = clean_content(text)
        text = re.sub(r'^# .+\n?', '', text, count=1)

        fm = f'''---
title: "{title}"
date: 2026-07-01
type: exam_collection
subject: "408"
source: "408真题"
year: {year}
difficulty: 3
tags: [真题, 408]
---

'''
        dst_file = f'{quiz_dst}/{year}.md'
        with open(dst_file, 'w', encoding='utf-8') as f:
            f.write(fm + text.strip() + '\n')
        count += 1
        print(f'  OK {year}年真题')

    # Create index
    index = f'''---
title: "📝 408真题 (2009-2026)"
date: 2026-07-01
type: section
---

历年408统考真题，共{count}年完整收录。
'''
    with open(f'{quiz_dst}/_index.md', 'w', encoding='utf-8') as f:
        f.write(index)

    print(f'\nConverted {count} years of exam quizzes')
    return count

def convert_simulate():
    """Convert simulation exams"""
    sim_src = f'{SRC}/study_methods/408simulate'
    sim_dst = f'{DST_EXAM}/simulate'
    os.makedirs(sim_dst, exist_ok=True)

    sets = sorted([d for d in os.listdir(sim_src) if d.isdigit() and os.path.isdir(f'{sim_src}/{d}')],
                  key=lambda x: int(x))
    count = 0
    for s in sets:
        src_file = f'{sim_src}/{s}/content.md'
        if not os.path.exists(src_file):
            continue
        with open(src_file, 'r', encoding='utf-8') as f:
            text = f.read()

        title_match = re.search(r'^# (.+)', text)
        title = title_match.group(1).strip() if title_match else f'模拟卷{s}'

        text = clean_content(text)
        text = re.sub(r'^# .+\n?', '', text, count=1)

        fm = f'''---
title: "{title}"
date: 2026-07-01
type: exam_collection
subject: "408"
source: "模拟题"
difficulty: 3
tags: [模拟题, 408]
---

'''
        dst_file = f'{sim_dst}/set-{s}.md'
        with open(dst_file, 'w', encoding='utf-8') as f:
            f.write(fm + text.strip() + '\n')
        count += 1
        print(f'  OK 模拟卷{s}')

    index = f'''---
title: "📝 408模拟卷"
date: 2026-07-01
type: section
---

408全真模拟卷，共{count}套。
'''
    with open(f'{sim_dst}/_index.md', 'w', encoding='utf-8') as f:
        f.write(index)

    print(f'\nConverted {count} simulation exams')
    return count

def convert_code():
    """Convert algorithm implementations"""
    code_src = f'{SRC}/code'
    code_dst = f'{DST_CODE}'
    os.makedirs(code_dst, exist_ok=True)

    algos = sorted([d for d in os.listdir(code_src) if os.path.isdir(f'{code_src}/{d}') and d not in ['.git']])
    count = 0
    for algo in algos:
        src_file = f'{code_src}/{algo}/content.md'
        if not os.path.exists(src_file):
            continue
        with open(src_file, 'r', encoding='utf-8') as f:
            text = f.read()

        title_match = re.search(r'^# (.+)', text)
        title = title_match.group(1).strip() if title_match else algo

        text = clean_content(text)
        text = re.sub(r'^# .+\n?', '', text, count=1)

        # Determine subject based on content
        subject_map = {
            'banker': 'os', 'clock': 'os', 'lru': 'os', 'monitor': 'os',
            'philosopher': 'os', 'producer_consumer': 'os', 'reader_writer': 'os', 'spinlock': 'os',
        }
        subject = subject_map.get(algo, 'data-structure')

        fm = f'''---
title: "{title}"
date: 2026-07-01
type: code
subject: {subject}
tags: [算法, C语言, {algo}]
difficulty: 2
---

'''
        dst_file = f'{code_dst}/{algo}.md'
        with open(dst_file, 'w', encoding='utf-8') as f:
            f.write(fm + text.strip() + '\n')
        count += 1
        print(f'  OK {title}')

    index = f'''---
title: "💻 算法实现"
date: 2026-07-01
type: section
---

经典408算法C语言实现，共{count}个算法。
'''
    with open(f'{code_dst}/_index.md', 'w', encoding='utf-8') as f:
        f.write(index)

    print(f'\nConverted {count} code algorithms')
    return count

if __name__ == '__main__':
    print('=== Converting 408 Quiz ===')
    q = convert_quiz()
    print('\n=== Converting Simulation ===')
    s = convert_simulate()
    print('\n=== Converting Code ===')
    c = convert_code()
    print(f'\n{"="*30}\nTotal: {q} quizzes, {s} simulations, {c} code files')
