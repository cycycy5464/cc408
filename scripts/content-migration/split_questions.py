#!/usr/bin/env python3
"""
Split monolithic exam content files into individual question files.
Reads content/exam/408quiz/{year}/content.md, generates content/question/{year}-{abbr}-{num}.md

Handles two question marker formats:
  1. ##### N (standard markdown header)
  2. N. (X分) or N、（X分） (inline text, common in comprehensive section)

Usage: python split_questions.py --all | --year YYYY
"""
import re, os, sys

QUESTIONS_DIR = r"E:\programcc408\cc408\content\question"
QUIZ_DIR = r"E:\programcc408\cc408\content\exam\408quiz"

SUBJECT_MAP = {
    "数据结构": "ds",
    "计算机组成原理": "co",
    "操作系统": "os",
    "计算机网络": "cn"
}

def parse_subject_cn(name):
    for key in SUBJECT_MAP:
        if key in name:
            return key
    return name.strip()

def inspect_question_line(line):
    """Check if a line contains an inline question number like '43. (7分)' or '45、(10分)'"""
    m = re.match(r'^\s*(\d{2})\s*[.、．]\s*(?:\(|（)(\d+)\s*分(?:\)|）)', line)
    if m:
        return int(m.group(1))
    return None

def detect_question_type(content):
    if re.search(r'正确答案[：:]\s*[ABCDabcd]', content):
        return "choice"
    return "comprehensive"

def split_year(year):
    year_str = str(year)
    filepath = os.path.join(QUIZ_DIR, year_str, "content.md")

    if not os.path.exists(filepath):
        print(f"NOT FOUND: {filepath}")
        return 0

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove frontmatter
    fm_match = re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL)
    if fm_match:
        content = content[fm_match.end():]

    # Normalize line endings
    content = content.replace('\r\n', '\n')

    # Step 1: Collect subject section boundaries
    # Split by #### subject header
    sections = []
    current_subject = None
    current_lines = []

    for line in content.split('\n'):
        if line.startswith('#### '):
            if current_subject and current_lines:
                sections.append((current_subject, '\n'.join(current_lines)))
            subject_cn = parse_subject_cn(line[5:])
            current_subject = subject_cn
            current_lines = []
        else:
            current_lines.append(line)

    if current_subject and current_lines:
        sections.append((current_subject, '\n'.join(current_lines)))

    # Step 2: Extract questions from each section
    questions = []  # list of (number, subject_cn, content, type)

    for subject_cn, section_text in sections:
        if not subject_cn:
            continue

        lines = section_text.split('\n')

        # First pass: split by ##### N markers
        q_blocks = re.split(r'^#####\s+(\d+)', section_text, flags=re.MULTILINE)

        # Process blocks from ##### split
        i = 0
        while i < len(q_blocks):
            block = q_blocks[i].strip()
            if not block:
                i += 1
                continue

            # Try to match: number followed by content
            if re.match(r'^\d+$', block) and i + 1 < len(q_blocks):
                q_num = int(block)
                q_text = q_blocks[i + 1].strip()
                i += 2

                # Check if this block contains inline questions (like 43. (7分))
                sub_questions = split_inline_questions(q_text, q_num)
                for sq_num, sq_text in sub_questions:
                    q_type = detect_question_type(sq_text)
                    difficulty = 4 if q_type == "comprehensive" else 3
                    questions.append((sq_num, subject_cn, sq_text, q_type, difficulty))
            else:
                # Content without explicit number - check for inline questions
                sub_questions = split_inline_questions(block, None)
                if sub_questions:
                    for sq_num, sq_text in sub_questions:
                        q_type = detect_question_type(sq_text)
                        difficulty = 4 if q_type == "comprehensive" else 3
                        questions.append((sq_num, subject_cn, sq_text, q_type, difficulty))
                i += 1

    # Step 3: Write question files
    count = 0
    written = set()

    for q_num, subject_cn, q_text, q_type, difficulty in questions:
        if q_num in written:
            continue
        written.add(q_num)

        # Override subject by question number range for comprehensives
        # Standard 408 format: 41-42 DS, 43-44 CO, 45-46 OS, 47 CN
        if q_num >= 41:
            if q_num <= 42:
                subject_cn = "数据结构"
            elif q_num <= 44:
                subject_cn = "计算机组成原理"
            elif q_num <= 46:
                subject_cn = "操作系统"
            elif q_num <= 47:
                subject_cn = "计算机网络"

        subject_ab = SUBJECT_MAP.get(subject_cn, "ds")
        filename = f"{year_str}-{subject_ab}-{q_num:03d}.md"

        fm = f"""---
title: "{year_str} {subject_cn} 第{q_num}题"
date: 2026-07-07
type: question
years:
  - "{year_str}"
subjects:
  - "{subject_cn}"
knowledge_points:
  - "{subject_cn}"
question_type: "{q_type}"
difficulty: {difficulty}
source: "408真题"
number: {q_num}
---

"""
        outpath = os.path.join(QUESTIONS_DIR, filename)
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(fm + q_text + '\n')
        count += 1
        print(f"  {filename}")

    return count


def split_inline_questions(text, default_number):
    """
    Split text that may contain inline question markers like:
      '43. (7分) ... 44. (10分) ...'
    Also handles escaped chars: '45 \. \(7分\) ...'
    Returns list of [(number, text), ...]
    """
    # Match both normal and escaped formats:
    # "43. (7分)", "45 \. \(7分\)", "44、（10分）"
    pattern = r'(?:^|\n)\s*(\d{2})\s*(?:\\?[.、．])\s*(?:\\?\(|\\?（)(\d+)\s*分(?:\\?\)|\\?）)'

    parts = re.split(pattern, text)

    if len(parts) < 4:
        # No inline questions found
        if default_number:
            return [(default_number, text)]
        return []

    result = []
    # parts[0] = content before first inline match
    first_num = int(parts[1])
    if default_number and default_number <= first_num:
        # parts[0] belongs to the default number (from #####)
        result.append((default_number, parts[0].strip()))
        i = 1
    else:
        # parts[0] is standalone
        if parts[0].strip() and default_number:
            result.append((default_number, parts[0].strip()))
        i = 1

    while i + 2 < len(parts):
        q_num = int(parts[i])
        q_text = parts[i + 2].strip()
        result.append((q_num, q_text))
        i += 3

    return result


if __name__ == "__main__":
    total = 0
    years_to_split = []

    if "--all" in sys.argv:
        years_to_split = list(range(2009, 2026))
    elif "--year" in sys.argv:
        idx = sys.argv.index("--year")
        years_to_split = [int(sys.argv[idx + 1])]
    else:
        print("Usage: python split_questions.py --all | --year YYYY")
        sys.exit(1)

    for year in years_to_split:
        print(f"\nSplitting {year}...")
        c = split_year(year)
        total += c
        print(f"  -> {c} questions")

    print(f"\nTotal: {total} questions across {len(years_to_split)} years")
