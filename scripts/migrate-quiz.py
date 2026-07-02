#!/usr/bin/env python3
"""
migrate-quiz.py
将 csgraduates-main 的 408quiz 真题 Markdown 文件适配到 cc408 项目格式。

用法:
    python scripts/migrate-quiz.py \
        --src "D:/内容整理/csgraduates-main/study_methods/408quiz" \
        --dst "content/exam/408quiz" \
        [--img-src "D:/内容整理/csgraduates-main/static/images"] \
        [--img-dst "static/images"]

功能:
    1. 复制并修正知识点内链前缀 (/study_methods/tags/ → /exam/tags/)
    2. 修正知识库内链前缀 (/data_structure/ → /docs/data-structure/ 等)
    3. 补全/更新 frontmatter（title、date、type、layout）
    4. 可选：同步图片资源到 static/images/
"""

import os
import re
import shutil
import argparse
from pathlib import Path

# ── 命令行参数 ────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser(description="迁移 csgraduates 408quiz 内容到 cc408")
parser.add_argument("--src",     required=True, help="csgraduates 的 408quiz 目录路径")
parser.add_argument("--dst",     required=True, help="cc408 目标目录，如 content/exam/408quiz")
parser.add_argument("--img-src", default=None,  help="csgraduates 的 static/images 目录（可选）")
parser.add_argument("--img-dst", default=None,  help="cc408 的 static/images 目录（可选）")
parser.add_argument("--dry-run", action="store_true", help="只打印计划，不实际写文件")
args = parser.parse_args()

SRC     = Path(args.src)
DST     = Path(args.dst)
IMG_SRC = Path(args.img_src) if args.img_src else None
IMG_DST = Path(args.img_dst) if args.img_dst else None
DRY_RUN = args.dry_run

if not SRC.exists():
    print(f"[ERROR] 源目录不存在: {SRC}")
    exit(1)

if not DRY_RUN:
    DST.mkdir(parents=True, exist_ok=True)

# ── 内链替换规则 ─────────────────────────────────────────────────────────────
LINK_MAP = [
    # 知识点标签内链
    ("/study_methods/tags/408quiz/",    "/exam/tags/408quiz/"),
    # 知识库章节内链（csgraduates 路径 → cc408 路径，按需调整）
    ("/data_structure/",                "/docs/data-structure/"),
    ("/constitution_principle/",        "/docs/computer-org/"),
    ("/operating_system/",              "/docs/os/"),
    ("/computer_network/",              "/docs/network/"),
    # share 页引用
    ("/study_methods/408quiz/share",    "/exam/408quiz/share"),
]

# ── 年份推断（文件名如 2025.md → "2025"）────────────────────────────────────
def guess_year(filename: str) -> str | None:
    m = re.fullmatch(r"(\d{4})", filename)
    return m.group(1) if m else None

# ── frontmatter 注入/替换 ────────────────────────────────────────────────────
def patch_frontmatter(content: str, fname: str) -> str:
    year = guess_year(fname)
    has_fm = content.strip().startswith("---")

    if has_fm:
        # 已有 frontmatter：只补充缺失字段
        fm_end = content.index("---", 3)
        fm_body = content[3:fm_end]
        rest    = content[fm_end + 3:]

        if "type:" not in fm_body:
            fm_body += "type: exam\n"
        if "layout:" not in fm_body and year:
            fm_body += "layout: exam-single\n"

        return f"---\n{fm_body}---{rest}"

    else:
        # 无 frontmatter：新建
        if year:
            fm = (
                f"---\n"
                f'title: "{year} 年 408 真题"\n'
                f"date: {year}-12-26\n"
                f"type: exam\n"
                f"layout: exam-single\n"
                f"---\n\n"
            )
        else:
            fm = (
                "---\n"
                "type: exam\n"
                "layout: exam-single\n"
                "---\n\n"
            )
        return fm + content

# ── 主循环：处理每个 .md 文件 ────────────────────────────────────────────────
processed = []
skipped   = []

for src_file in sorted(SRC.iterdir()):
    if src_file.suffix.lower() != ".md":
        skipped.append(src_file.name)
        continue

    dst_file = DST / src_file.name

    with open(src_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 替换内链
    for old, new in LINK_MAP:
        content = content.replace(old, new)

    # 补全 frontmatter
    fname_stem = src_file.stem
    content = patch_frontmatter(content, fname_stem)

    if DRY_RUN:
        print(f"[DRY-RUN] {src_file.name} → {dst_file}")
    else:
        with open(dst_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✓ {src_file.name} → {dst_file}")

    processed.append(src_file.name)

# ── 可选：同步图片 ────────────────────────────────────────────────────────────
if IMG_SRC and IMG_DST:
    if not IMG_SRC.exists():
        print(f"\n[WARN] 图片源目录不存在，跳过图片同步: {IMG_SRC}")
    else:
        if not DRY_RUN:
            IMG_DST.mkdir(parents=True, exist_ok=True)
        img_count = 0
        for img_file in IMG_SRC.iterdir():
            if img_file.is_file():
                dst_img = IMG_DST / img_file.name
                if DRY_RUN:
                    print(f"[DRY-RUN] IMG {img_file.name} → {dst_img}")
                else:
                    shutil.copy2(img_file, dst_img)
                img_count += 1
        print(f"\n✓ 图片同步完成，共 {img_count} 个文件 → {IMG_DST}")

# ── 汇总 ─────────────────────────────────────────────────────────────────────
print(f"\n{'='*50}")
print(f"处理完成：{len(processed)} 个 .md 文件 → {DST}")
if skipped:
    print(f"已跳过（非 .md）：{', '.join(skipped)}")
print(f"\n下一步：")
print(f"  1. 运行 `hugo server` 本地预览 /exam/408quiz/")
print(f"  2. 对比 https://www.csgraduates.com/study_methods/408quiz/ 检查样式")
print(f"  3. 如有知识库内链不匹配，在脚本 LINK_MAP 中补充规则后重新运行")
