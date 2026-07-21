# -*- coding: utf-8 -*-
"""
拆分模拟卷整卷 Markdown 为单题文件（原生 UTF-8，避免 PowerShell 无 BOM 编码问题）。

输入: content/exam/simulate/set-{N}.md  (整卷，由 E:\参考\2026-07\simulate-crawler.js 重抓生成)
输出: content/question/simulate-{set}-{abbr}-{num}.md  (单题，frontmatter 与原格式一致)

frontmatter 保留原格式（含 years: - "模拟卷"），正文原样保留（含 KaTeX）。
"""
import os
import re

ROOT = r"E:\programcc408\cc408"
SIM_DIR = os.path.join(ROOT, "content", "exam", "simulate")
OUT_DIR = os.path.join(ROOT, "content", "question")

SUBJECT_ABBR = {
    "数据结构": "ds",
    "计算机组成原理": "co",
    "操作系统": "os",
    "计算机网络": "cn",
}
DATE = "2026-07-08"


def write_q(set_num, subject, num, content):
    num_int = int(num)
    is_comp = num_int >= 41
    qtype = "comprehensive" if is_comp else "choice"
    diff = 4 if is_comp else 3
    abbr = SUBJECT_ABBR.get(subject, "xx")
    num_padded = f"{num_int:03d}"
    body = "\n".join(content).strip("\n")

    fm = (
        "---\n"
        f'title: "模拟卷{set_num} {subject} 第{num_int}题"\n'
        f"date: {DATE}\n"
        "type: question\n"
        "years:\n"
        '  - "模拟卷"\n'
        'source: "模拟题"\n'
        f"set: {set_num}\n"
        "subjects:\n"
        f'  - "{subject}"\n'
        "knowledge_points:\n"
        f'  - "{subject}"\n'
        f'question_type: "{qtype}"\n'
        f"difficulty: {diff}\n"
        f"number: {num_int}\n"
        "---\n"
    )
    out = fm + "\n" + body + "\n"
    fn = f"simulate-{set_num}-{abbr}-{num_padded}.md"
    with open(os.path.join(OUT_DIR, fn), "w", encoding="utf-8") as f:
        f.write(out)


def split_set(set_num):
    path = os.path.join(SIM_DIR, f"set-{set_num}.md")
    if not os.path.exists(path):
        print("MISSING:", path)
        return
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    cur_subject = ""
    cur_num = ""
    cur_content = []
    questions = []

    for line in lines:
        # 孤立的 --- 是科目之间的水平分隔线，不是题目内容，跳过
        if line.strip() == "---":
            continue
        m = re.match(r'^####\s+(.+?)\s*$', line)
        if m:
            cur_subject = m.group(1).strip()
            continue
        m = re.match(r'^#####\s+(\d+)', line)
        if m:
            if cur_num and cur_subject:
                questions.append((cur_subject, cur_num, cur_content))
            cur_num = m.group(1)
            cur_content = []
            continue
        if cur_num:
            cur_content.append(line)

    if cur_num and cur_subject:
        questions.append((cur_subject, cur_num, cur_content))

    for (subject, num, content) in questions:
        write_q(set_num, subject, num, content)
    print(f"Set {set_num}: {len(questions)} questions saved")


if __name__ == "__main__":
    for s in range(1, 9):
        split_set(s)
