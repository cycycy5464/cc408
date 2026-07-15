#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将综合题里粘连在同一行的小问 (1)(2)(3) / （1）（2） / 1）2） 拆成独立行。

规则（依据 tasks/真题修复/修复标准.md 3.3 子问题分段）：
- 仅处理 question_type: "comprehensive" 的文件。
- 仅对"真实小问"做换行，并通过多重守卫避免误伤：
  * (N) / （N）：标记后紧跟数字（如二进制进位 "(0)1001"）视为算式，不拆；
            标记前的字符若为数字或 "."（如 "10.2.128.100）"）视为 IP/编号，不拆。
  * N）：标记前的字符若为数字 / "." / "≥≤=、，。）：]>" 等（如 IP、范围 "（≥2）"），不拆；
            且标记后紧跟数字也不拆。
  * 标记后紧跟 、，和或及与）] 等，视为"引用/枚举"（如 "(1)、(2) 根据..."），不拆。
  * 标记前为 图/表/示/如/见/参/下 等，视为"图(1)/表(1)"引用，不拆。
  * 表格行（以 | 开头）整体跳过，不拆。
- 不改动 frontmatter、选择题与已独立成行的小问。
- 拆出的每一小问独占一行，小问之间以空行分隔，确保 Goldmark 渲染为独立 <p>。

用法：
  python split_subquestions.py            # 试运行，打印将改动的 files 与样例 diff
  python split_subquestions.py --apply    # 真正写入文件
"""
import re
import sys
import glob
import os
import difflib

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
QUESTION_DIR = os.path.abspath(os.path.join(ROOT, "content", "question"))

RE_PAREN = re.compile(r"\(\s*(\d+)\s*\)")     # (N)
RE_FULL = re.compile(r"（\s*(\d+)\s*）")       # （N）
RE_CLOSE = re.compile(r"(\d+)\s*）")           # N）
REF_AFTER = set("、，和或及与）]")
REF_BEFORE = set("图表示如见参下")
EXCL_BEFORE = set("0123456789.≥≤=、，。）：）]>〈")
SENT_PUNCT = set("。；：！？，、\n")
PREFIX_RE = re.compile(r"^(\s*(?:>\s*)*)")


SUPER = set("⁰¹²³⁴⁵⁶⁷⁸⁹")  # 上标数字，如 2¹⁶ 中的 ¹⁶


def _is_super(ch):
    return ch in SUPER


def _after_skip_digit(body, end):
    i = 0
    s = body[end:]
    while i < len(s) and s[i] in " \t":
        i += 1
    return i < len(s) and s[i].isdigit()


def _after_skip_set(body, end, charset):
    i = 0
    s = body[end:]
    while i < len(s) and s[i] in " \t":
        i += 1
    return i < len(s) and s[i] in charset


def classify(body):
    """返回 body 中所有真实小问标记的位置列表（按出现顺序）。"""
    results = []
    for rx, kind in ((RE_PAREN, "paren"), (RE_FULL, "full"), (RE_CLOSE, "close")):
        for m in rx.finditer(body):
            if _is_real(body, m, kind):
                results.append(m)
    results.sort(key=lambda m: m.start())
    return results


def _is_real(body, m, kind):
    num = int(m.group(1)) if m.groups() else 0
    # 真实小问编号通常很小；大数字多为括号里的数值说明，如 "（65536）"
    if num >= 20:
        return False
    if kind in ("paren", "full"):
        # 标记后紧跟数字 -> 算式/进位，不拆，如 "(0)1001"
        if _after_skip_digit(body, m.end()):
            return False
        # 标记后紧跟枚举/引用标点 -> 如 "(1)、(2) 根据..." 中的引用，不拆
        if _after_skip_set(body, m.end(), REF_AFTER):
            return False
        if kind == "paren":
            b = body[: m.start()].rstrip()
            if b and (b[-1].isdigit() or b[-1] == "."):
                return False
        # 标记前为 ASCII 字母 -> 函数/大 O 记法，如 "O(1)"，不拆
        b = body[: m.start()].rstrip()
        if b and (b[-1].isascii() and b[-1].isalpha()):
            return False
        # 标记前为图/表/示/如/见/参/下 等 -> 图(1)/表(1) 引用，不拆
        if b and b[-1] in REF_BEFORE:
            return False
        # 标记前为枚举/引用标点 -> 如 "(1)、(2)" 中的 (2) 是引用而非独立小问，不拆
        if b and b[-1] in REF_AFTER:
            return False
        # 标记前为数字/上标/数学符号 -> 数值表达式中的括号，如 "2¹⁶（65536）"，不拆
        if b and (b[-1].isdigit() or _is_super(b[-1]) or b[-1] in "×=+−-*/^²¹"):
            return False
        return True
    # close: N）  —— 极易与括号闭合（如 （R1）/ O(len2）/ BGP4）/ （乘 2）/ 0～5）混淆，
    # 故仅当其位于行首或紧跟句末标点时才视为真实小问。
    if _after_skip_digit(body, m.end()):
        return False
    b = body[: m.start()].rstrip()
    if b and b[-1] in EXCL_BEFORE:
        return False
    if not b or b[-1] in SENT_PUNCT:
        return True
    return False


def starts_with_marker(line):
    core = PREFIX_RE.sub("", line)
    if not core.strip() or core.lstrip().startswith("|"):
        return False
    for rx, kind in ((RE_PAREN, "paren"), (RE_FULL, "full"), (RE_CLOSE, "close")):
        m = rx.match(core)
        if m and _is_real(core, m, kind):
            return True
    return False


def split_line(line):
    pm = PREFIX_RE.match(line)
    prefix = pm.group(1)
    body = line[len(prefix):]
    if not body.strip() or body.lstrip().startswith("|"):
        return None
    real = classify(body)
    if not real:
        return None
    positions = []
    for idx, m in enumerate(real):
        if idx == 0:
            if m.start() > 0:
                positions.append(m.start())
        else:
            positions.append(m.start())
    if not positions:
        return None
    segments = []
    prev = 0
    for p in positions:
        segments.append(body[prev:p])
        prev = p
    segments.append(body[prev:])
    return [prefix + seg.rstrip() for seg in segments]


def process_file(path, apply):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if 'question_type: "comprehensive"' not in text:
        return None
    if text.startswith("---"):
        end = text.find("\n---", 3)
        fm = text[: end + 4] if end != -1 else ""
        body = text[end + 4:] if end != -1 else text
    else:
        fm, body = "", text

    lines = body.split("\n")
    new_lines = []
    changed = False
    in_fence = False  # 跳过围栏代码块（```），避免改动其中的代码
    for ln in lines:
        if ln.strip().startswith("```"):
            in_fence = not in_fence
            new_lines.append(ln)
            continue
        if in_fence:
            new_lines.append(ln)
            continue
        res = split_line(ln)
        if res is None:
            new_lines.append(ln)
        else:
            changed = True
            new_lines.extend(res)

    final = []
    for k, ln in enumerate(new_lines):
        if k > 0 and starts_with_marker(ln):
            if final[-1].strip() != "":
                final.append("")
        final.append(ln)

    if "\n".join(final) == body:
        return None
    new_body = "\n".join(final)
    if apply:
        with open(path, "w", encoding="utf-8") as f:
            f.write(fm + new_body)
    return text, fm + new_body


def main():
    apply = "--apply" in sys.argv
    files = sorted(glob.glob(os.path.join(QUESTION_DIR, "*.md")))
    changed_files = []
    samples = []
    for fp in files:
        r = process_file(fp, apply)
        if r is not None:
            changed_files.append(fp)
            samples.append((fp, r[0], r[1]))
    print(f"共扫描 {len(files)} 个文件，将{'写入' if apply else '改动'} {len(changed_files)} 个综合题文件。")
    for fp in changed_files:
        print("  -", os.path.relpath(fp, ROOT))
    # 始终把将要改动的相对路径列表写入文件，便于精确回滚
    listpath = os.path.join(os.path.dirname(__file__), "tmp_files.txt")
    with open(listpath, "w", encoding="utf-8") as lf:
        for fp in changed_files:
            lf.write(os.path.relpath(fp, ROOT) + "\n")
    if not apply:
        allpath = os.path.join(os.path.dirname(__file__), "tmp_alldiff.txt")
        with open(allpath, "w", encoding="utf-8") as af:
            for fp, old, new in samples:
                af.write("\n### " + os.path.relpath(fp, ROOT) + "\n")
                for d in difflib.unified_diff(old.splitlines(), new.splitlines(), lineterm="", n=1):
                    af.write(d + "\n")
        print("全部 diff 已写入 tasks/tmp_alldiff.txt")


if __name__ == "__main__":
    main()
