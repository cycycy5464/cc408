#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
只读扫描模拟卷某套（set-N）的四类格式问题，输出分类报告供人工审核。
不修改任何文件。
用法: python scan_set_issues.py <N>        # N=1..8
"""
import glob
import os
import re
import sys

BASE = "content/question"

# 选项格式正则（注意：单个反斜杠用 \\\\ 表示）
OPT_RE = re.compile(r"^[A-D]\\\. ")         # 正确：A\. （反斜杠+点+空格）
OPT_BAD_RE = re.compile(r"^[A-D]\. ")         # 错误：A. （无反斜杠）
OPT_LINE_RE = re.compile(r"^[A-D][\\. ]")     # 任意选项起始行


def detect(fpath):
    t = open(fpath, encoding="utf-8").read()
    name = os.path.basename(fpath)
    iss = {"gen": [], "img": [], "tbl": [], "code": []}

    # ---- 通用格式 ----
    if "\r" in t:
        iss["gen"].append("换行符含 \\r（需统一为 \\n）")
    if "\u200b" in t:
        iss["gen"].append("含零宽空格 \\u200b（mojibake 如 ��）")

    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if m:
        fm = m.group(1)
        fl = fm.split("\n")
        for i, l in enumerate(fl):
            if l.strip() == "" and 0 < i < len(fl) - 1:
                iss["gen"].append("frontmatter 字段间有空行")
                break

    tl = t.count("[tag_link]")
    if tl == 0:
        iss["gen"].append("缺少 [tag_link]（综合题需有）")
    elif tl > 1:
        iss["gen"].append(f"重复 [tag_link] x{tl}")

    if "quizDB" in t or "indexedDB" in t or "toggleSolutionDetail" in t:
        iss["gen"].append("JS 注入（quizDB/IndexedDB/收藏代码）")

    # 跨题污染：解析区出现第二个（N 分）题号
    fen = re.findall(r"（\d+\s*分）", t)
    if len(fen) >= 2:
        iss["gen"].append("跨题污染（解析区出现第二个（N 分）题号，含下一题内容）")
    if "查看答案与解析" in t or "收藏" in t:
        if "查看答案与解析" in t:
            iss["gen"].append("残留 UI 文本（查看答案与解析/收藏）")

    # 选择题选项
    is_choice = 'question_type: "choice"' in t
    if is_choice:
        lines = t.split("\n")
        opt_idx = [i for i, l in enumerate(lines) if OPT_LINE_RE.match(l)]
        correct = [i for i in opt_idx if OPT_RE.match(lines[i])]
        badfmt = [i for i in opt_idx
                  if OPT_BAD_RE.match(lines[i]) and not OPT_RE.match(lines[i])]
        if badfmt:
            iss["gen"].append("选项格式异常（应为 A\\. 带反斜杠）")
        # 选项间空行
        for a, b in zip(opt_idx, opt_idx[1:]):
            if any(lines[k].strip() == "" for k in range(a + 1, b)):
                iss["gen"].append("选项间有空行（Goldmark 会拆分段落）")
                break
        if len(correct) != 4 and not badfmt:
            iss["gen"].append("选项数量疑似不全（应 4 项连续）")

    # ---- 图像 ----
    if "[图片]" in t:
        iss["img"].append("[图片] 占位符未替换为真实 ![...] 引用")

    for mm in re.finditer(r"\[([^\]]*)\]\(([^)]*)\)", t):
        target = mm.group(2).strip()
        ok_start = target.startswith(("/", "http", "#", "mailto"))
        suspicious = ("," in target or "（" in target or " " in target
                      or target == mm.group(1).strip())
        if not ok_start and suspicious:
            iss["img"].append(f"破损链接 [{mm.group(1)}]({target})")

    for mm in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", t):
        p = mm.group(1)
        if p.startswith("/cc408/"):
            local = "static" + p[len("/cc408"):]
            if not os.path.exists(local):
                iss["img"].append(f"图片路径缺失: {p}")

    # 提及图示但无图片引用 → 疑似缺图
    has_img_ref = ("[图片]" in t) or bool(re.search(r"!\[", t))
    if re.search(r"如下图所示|如图所示|见下图|见上图|下图所示", t) and not has_img_ref:
        iss["img"].append("疑似缺图（提及图示但无图片引用）")

    # ---- 表格 ----
    lines = t.split("\n")
    tbl_rows = [i for i, l in enumerate(lines)
                if l.strip().startswith("|") and "|" in l.strip()[1:-1]]
    if tbl_rows:
        for i in tbl_rows:
            s = lines[i].strip()
            if "---" in s:
                if (i - 1 >= 0 and lines[i - 1].strip().startswith("|")
                        and "---" not in lines[i - 1]
                        and (i - 2 >= 0 and lines[i - 2].strip() == "")):
                    iss["tbl"].append("表头与分隔行之间有空行")
                    break
        for i in tbl_rows:
            s = lines[i].strip()
            if "---" not in s:
                if i > 0 and lines[i - 1].strip() and not lines[i - 1].strip().startswith("|"):
                    iss["tbl"].append("表格前缺空行（文本被吸入）")
                    break
                if i + 1 < len(lines) and lines[i + 1].strip() and not lines[i + 1].strip().startswith("|"):
                    iss["tbl"].append("表格后缺空行")
                    break
    else:
        body = re.sub(r"```.*?```", "", t, flags=re.S)
        if re.search(r"目的网络|子网掩码|下一跳|机器码|LSI|路由表|邻接矩阵|"
                     r"虚页号|页帧|页框|组相联|直接映射|命中率", body):
            iss["tbl"].append("疑似散落表格数据（需构造 MD 表格）")

    # ---- 代码 ----
    body = re.sub(r"```.*?```", "", t, flags=re.S)
    if re.search(r"\b(int|char|void|struct|typedef|return|for|while|do|switch|"
                 r"case|break|continue|malloc|free|sizeof|printf|scanf|#include)\b", body):
        iss["code"].append("疑似裸露代码（未用 ```c 包裹）")

    return name, iss


def main():
    if len(sys.argv) < 2:
        print("usage: python scan_set_issues.py <setN>")
        sys.exit(1)
    n = sys.argv[1]
    files = sorted(glob.glob(f"{BASE}/simulate-{n}-*.md"))
    if not files:
        print(f"未找到 content/question/simulate-{n}-*.md")
        sys.exit(1)

    cats = {"gen": [], "img": [], "tbl": [], "code": []}
    per_file = {}
    for f in files:
        name, iss = detect(f)
        if any(iss.values()):
            per_file[name] = iss
            for k in cats:
                if iss[k]:
                    cats[k].append(name)

    out = []
    out.append(f"=== 模拟卷 set {n} 扫描报告 ===")
    out.append(f"文件总数: {len(files)}，有问题文件: {len(per_file)}\n")

    titles = {
        "gen": "一、模拟卷通用格式（frontmatter/选项/跨题污染/JS/换行/零宽空格）",
        "img": "二、图像（[图片]占位/破损链接/路径缺失/疑似缺图）",
        "tbl": "三、表格格式（MD 表格/间距/散落数据）",
        "code": "四、代码格式（裸露代码未 ```c 包裹）",
    }
    for k in ["gen", "img", "tbl", "code"]:
        out.append(f"【{titles[k]}】  命中 {len(cats[k])} 个文件")
        if cats[k]:
            for fn in cats[k]:
                items = [x for x in per_file[fn][k]]
                out.append(f"  - {fn}: {'; '.join(items)}")
        out.append("")

    out.append("--- 逐文件汇总（供审核补充）---")
    for fn in sorted(per_file):
        allitems = []
        for k in ["gen", "img", "tbl", "code"]:
            allitems += [f"[{k}] {x}" for x in per_file[fn][k]]
        out.append(f"{fn}:")
        for it in allitems:
            out.append(f"    * {it}")

    report_text = "\n".join(out)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    # 写 UTF-8 文件供审核
    rep_path = f"tasks/真题修复/scan-report-set{n}.md"
    with open(rep_path, "w", encoding="utf-8") as fh:
        fh.write(report_text + "\n")
    print(f"[scan] set {n}: {len(files)} files, {len(per_file)} with issues")
    print(f"[scan] report saved -> {rep_path} (UTF-8, open to review)")
    for k in ["gen", "img", "tbl", "code"]:
        print(f"        {titles[k].split('（')[0]}: {len(cats[k])}")


if __name__ == "__main__":
    main()
