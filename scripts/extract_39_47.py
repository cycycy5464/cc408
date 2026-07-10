#!/usr/bin/env python3
import re, os, sys, shutil, tempfile

QUESTIONS_DIR = r"E:\programcc408\cc408\content\question"
SOURCE_FILE = r"D:\内容整理\csgraduates-main\study_methods\408quiz\2025\content.md"
YEAR = "2025"

SUBJECT_MAP = {"数据结构": "ds", "计算机组成原理": "co", "操作系统": "os", "计算机网络": "cn"}

def parse_subject_cn(name):
    for key in SUBJECT_MAP:
        if key in name:
            return key
    return name.strip()

def detect_question_type(content):
    if re.search(r'正确答案[：:]\s*[ABCDabcd]', content):
        return "choice"
    return "comprehensive"

def safe_write_file(filepath, content):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except PermissionError:
        try:
            os.remove(filepath)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except (PermissionError, OSError):
            try:
                fd, tmppath = tempfile.mkstemp(suffix='.md', dir=QUESTIONS_DIR)
                with os.fdopen(fd, 'w', encoding='utf-8') as f:
                    f.write(content)
                shutil.move(tmppath, filepath)
                return True
            except Exception:
                return False

def main():
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n')

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

    print(f"DEBUG: Found {len(sections)} sections")
    for s_cn, s_text in sections:
        print(f"  Section: '{s_cn}' ({len(s_text)} chars)")

    questions = []
    for subject_cn, section_text in sections:
        if not subject_cn:
            continue
        q_blocks = re.split(r'^#####\s+(\d+)', section_text, flags=re.MULTILINE)
        i = 0
        while i < len(q_blocks):
            block = q_blocks[i].strip()
            if not block:
                i += 1
                continue
            if re.match(r'^\d+$', block) and i + 1 < len(q_blocks):
                q_num = int(block)
                q_text = q_blocks[i + 1].strip()
                i += 2
                questions.append((q_num, subject_cn, q_text))
            else:
                i += 1

    questions.sort(key=lambda x: x[0])
    print(f"DEBUG: Found {len(questions)} total questions")
    for q_num, scn, qt in questions:
        subj_suffix = ""
        if q_num >= 41:
            if q_num <= 42: subj_suffix = " [override: ds]"
            elif q_num <= 44: subj_suffix = " [override: co]"
            elif q_num <= 46: subj_suffix = " [override: os]"
            elif q_num <= 47: subj_suffix = " [override: cn]"
        print(f"  q{q_num}: subject='{scn}'{subj_suffix}")
        if 45 <= q_num <= 47:
            print(f"    content preview: {qt[:80]}...")

    target = [q for q in questions if 39 <= q[0] <= 47]
    print(f"DEBUG: {len(target)} target questions (39-47)")

    def get_subject_for_number(q_num):
        if q_num >= 41:
            if q_num <= 42: return "数据结构"
            elif q_num <= 44: return "计算机组成原理"
            elif q_num <= 46: return "操作系统"
            elif q_num <= 47: return "计算机网络"
        return None

    results = []
    for q_num, subject_cn, q_text in target:
        override = get_subject_for_number(q_num)
        if override:
            subject_cn = override
        subject_ab = SUBJECT_MAP.get(subject_cn, "ds")
        filename = f"{YEAR}-{subject_ab}-{q_num:03d}.md"
        q_type = detect_question_type(q_text)
        difficulty = 4 if q_type == "comprehensive" else 3
        fm = f"""---
title: "{YEAR} {subject_cn} 第{q_num}题"
date: 2026-07-07
type: question
years:
  - "{YEAR}"
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
        ok = safe_write_file(outpath, fm + q_text + '\n')
        results.append((filename, ok))
        print(f"  {'OK' if ok else 'FAIL'} {filename}")

    print("\nFinal Summary:")
    for fn, ok in results:
        print(f"  {'✓' if ok else '✗'} {fn}")

if __name__ == "__main__":
    main()
