#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将 content/question 下散落的题目按 source 重组到子目录：
  - 408真题  -> exam/<year>/
  - 模拟题   -> simulate/<set>/
  - 课后题   -> 已在 chapterExercises/（跳过）
同时移动同名 .assets/ 资源夹。

URL 稳定性由 hugo.yaml 中 permalink:
  question: '/question/:filename/'
保证（:filename 只取文件名，与目录无关）。

用法：
  python question_organize.py --dry-run          # 只打印计划，不移动
  python question_organize.py --year 2009        # 只处理 2009 真题 + 其 assets
  python question_organize.py --set 1             # 只处理 模拟题 set 1
  python question_organize.py                     # 全量处理
"""
import os
import re
import shutil
import argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QDIR = os.path.join(ROOT, "content", "question")

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def read_frontmatter(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm_text = m.group(1)
    fm = {}
    key = None
    list_mode = False
    for line in fm_text.splitlines():
        if not line.strip():
            continue
        # Detect consecutive single-line keys (priority map, etc.)
        m2 = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if m2:
            key = m2.group(1)
            val = m2.group(2).strip()
            if val == "":
                # 可能是列表的开始（下一行 - item）
                fm[key] = ""
                list_mode = True
            else:
                fm[key] = val.strip('"')
                list_mode = False
        elif re.match(r"^\s*-\s*(.*)$", line) and list_mode:
            item = re.match(r"^\s*-\s*(.*)$", line).group(1).strip().strip('"')
            if key:
                if not isinstance(fm.get(key), list):
                    fm[key] = [] if fm[key] == "" else [fm[key]]
                fm[key].append(item)
            list_mode = True
        else:
            # 续行（缩进）忽略
            list_mode = list_mode
    return fm, text


def unquote(v):
    if isinstance(v, list):
        return [x.strip().strip('"') for x in v]
    return v.strip().strip('"')


def target_dir(fm):
    src = unquote(fm.get("source", ""))
    if src == "408真题":
        years = unquote(fm.get("years", []))
        if isinstance(years, list) and years:
            return os.path.join(QDIR, "exam", str(years[0]))
        return None
    if src == "模拟题":
        s = unquote(fm.get("set", ""))
        if s:
            return os.path.join(QDIR, "simulate", str(s))
        return None
    # 课后题等：已在子目录或无需移动
    return None


def move_one(md_path, dry):
    fm, _ = read_frontmatter(md_path)
    tdir = target_dir(fm)
    if not tdir:
        return False
    base = os.path.basename(md_path)
    dest = os.path.join(tdir, base)
    if os.path.abspath(dest) == os.path.abspath(md_path):
        return False
    assets_src = md_path[: md_path.rfind(".md")] + ".assets"
    if dry:
        print(f"[DRY] {md_path}  ->  {dest}")
        return True
    os.makedirs(tdir, exist_ok=True)
    shutil.move(md_path, dest)
    if os.path.isdir(assets_src):
        shutil.move(assets_src, os.path.join(tdir, os.path.basename(assets_src)))
    return True
    base = os.path.basename(md_path)
    dest = os.path.join(tdir, base)
    if os.path.abspath(dest) == os.path.abspath(md_path):
        return False
    assets_src = md_path[: md_path.rfind(".md")] + ".assets"
    if dry:
        print(f"[DRY] {md_path}  ->  {dest}")
        return True
    os.makedirs(tdir, exist_ok=True)
    shutil.move(md_path, dest)
    if os.path.isdir(assets_src):
        shutil.move(assets_src, os.path.join(tdir, os.path.basename(assets_src)))
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--year", help="只处理该年份真题，如 2009")
    ap.add_argument("--set", help="只处理该套模拟题，如 1")
    args = ap.parse_args()

    count = 0
    for name in sorted(os.listdir(QDIR)):
        full = os.path.join(QDIR, name)
        if not name.endswith(".md"):
            continue
        if name == "_index.md":
            continue
        fm, _ = read_frontmatter(full)
        src = unquote(fm.get("source", ""))
        # 过滤
        if args.year:
            years = unquote(fm.get("years", []))
            y = years[0] if isinstance(years, list) and years else ""
            if not (src == "408真题" and str(y) == str(args.year)):
                continue
        if args.set:
            s = unquote(fm.get("set", ""))
            if not (src == "模拟题" and str(s) == str(args.set)):
                continue
        if move_one(full, args.dry_run):
            count += 1
    print(f"处理完成：共移动 {count} 个题目文件" + ("（DRY-RUN，未实际移动）" if args.dry_run else ""))


if __name__ == "__main__":
    main()
