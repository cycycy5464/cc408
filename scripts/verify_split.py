#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""验证 split_subquestions 的处理结果：
1) 处理后的文件中，真实小问标记 (N)/(N）/(N） 应各自独占一行（行首）。
2) 不应出现“夹在词中”的标记，例如 图(1)/O(1)/(R1) 等被拆开的情况。
"""
import re
import sys
import os
import glob

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
QUESTION_DIR = os.path.abspath(os.path.join(ROOT, "content", "question"))
sys.path.insert(0, os.path.dirname(__file__))
import split_subquestions as S  # noqa: E402


def find_markers(line):
    core = S.PREFIX_RE.sub("", line)
    res = []
    for rx, kind in ((S.RE_PAREN, "paren"), (S.RE_FULL, "full"), (S.RE_CLOSE, "close")):
        for m in rx.finditer(core):
            if S._is_real(core, m, kind):
                res.append((m.start(), kind))
    return res


def main():
    problems = []
    files = sorted(glob.glob(os.path.join(QUESTION_DIR, "*.md")))
    for fp in files:
        r = S.process_file(fp, False)
        if r is None:
            continue
        new_text = r[1]
        for lineno, line in enumerate(new_text.split("\n"), 1):
            core = S.PREFIX_RE.sub("", line)
            if not core.strip() or core.lstrip().startswith("|"):
                continue
            markers = find_markers(line)
            if not markers:
                continue
            for pos, kind in markers:
                if pos != 0:
                    problems.append((fp, lineno, kind, line.strip()[:80]))
                    break
    if problems:
        print(f"发现 {len(problems)} 处“标记未置于行首 / 疑似误拆”:")
        for fp, ln, kind, snippet in problems[:60]:
            print(f"  {os.path.relpath(fp, ROOT)}:{ln} [{kind}] {snippet}")
    else:
        print("OK：所有综合题文件的转换结果中，真实小问标记均位于行首，未见夹词误拆。")


if __name__ == "__main__":
    main()
