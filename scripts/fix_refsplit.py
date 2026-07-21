#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 split_subquestions 早期版本在 "(1)、(2)" 这类引用上产生的误拆：
把 "X(1)、\n\n(2) Y" 重新合并为 "X(1)、(2) Y"。
仅作用于当前 git 已改动的综合题文件，未作改动则不动。
"""
import re
import os
import subprocess

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
QUESTION_DIR = os.path.abspath(os.path.join(ROOT, "content", "question"))

# 匹配：行尾为 "(N)、" 或 "（N）、"，其后紧跟（可含空行）一个独立小问标记 "(M)" / "（M）"
PAT = re.compile(
    r"(.*?[（(]\d+[）)][、])\s*\n(?:\s*\n)*\s*([（(]\d+[）)])"
)


def fix_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if 'question_type: "comprehensive"' not in text:
        return False
    new = PAT.sub(r"\1\2", text)
    if new != text:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        return True
    return False


def main():
    out = subprocess.run(
        ["git", "diff", "--name-only", "--", "content/question/"],
        cwd=ROOT, capture_output=True, text=True,
    )
    files = [os.path.join(ROOT, l.strip()) for l in out.stdout.splitlines() if l.strip()]
    fixed = 0
    for fp in files:
        if fix_file(fp):
            fixed += 1
            print("  fixed:", os.path.relpath(fp, ROOT))
    print(f"共修复 {fixed} 个文件的引用误拆。")


if __name__ == "__main__":
    main()
