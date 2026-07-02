# DS Source to CC408 Content Converter
# Run from /e/programcc408/cc408/

import os
import re
import shutil

SRC_DIR = '_tmp/ds_source'
DST_DIR = 'content/docs/data-structure'

# Title → file mapping for chapters
CHAPTER_MAP = {
    '绪论.md': ('ch00-intro/introduction.md', 0, '绪论'),
    '绪论-数据结构基本概念.md': ('ch00-intro/basic-concepts.md', 1, '数据结构基本概念'),
    '绪论-算法基本概念.md': ('ch00-intro/algorithm-concepts.md', 2, '算法基本概念'),
    '线性表.md': ('ch01-linear-list/linear-list-index.md', 3, '线性表概述'),
    '线性表-定义和基本操作.md': ('ch01-linear-list/definition.md', 4, '线性表定义与基本操作'),
    '线性表-顺序表示.md': ('ch01-linear-list/sequential-list.md', 5, '顺序表'),
    '线性表-链式表示.md': ('ch01-linear-list/linked-list.md', 6, '链表'),
    '栈.md': ('ch02-stack-queue/stack.md', 7, '栈'),
    '队列.md': ('ch02-stack-queue/queue.md', 8, '队列'),
    '栈和队列的应用.md': ('ch02-stack-queue/application.md', 9, '栈和队列的应用'),
    '线性数据结构.md': ('ch02-stack-queue/linear-data-structure.md', 10, '线性数据结构'),
    '字符串.md': ('ch03-string/string-index.md', 11, '串概述'),
    '字符串-定义和实现.md': ('ch03-string/definition.md', 12, '串的定义与实现'),
    '字符串-模式匹配.md': ('ch03-string/pattern-matching.md', 13, '串的模式匹配'),
    '数组和特殊矩阵.md': ('ch03-string/array-matrix.md', 14, '数组和特殊矩阵'),
    '树.md': ('ch04-tree/tree.md', 15, '树'),
    '树与二叉树.md': ('ch04-tree/tree-and-binary-tree.md', 16, '树与二叉树'),
    '二叉树.md': ('ch04-tree/binary-tree.md', 17, '二叉树'),
    '树的应用.md': ('ch04-tree/tree-applications.md', 18, '树的应用'),
    '图.md': ('ch05-graph/graph-index.md', 19, '图概述'),
    '图-定义.md': ('ch05-graph/definition.md', 20, '图的定义'),
    '图-算法和应用.md': ('ch05-graph/algorithms.md', 21, '图的算法和应用'),
    '查找.md': ('ch06-search/search-index.md', 22, '查找概述'),
    '查找-数组查找.md': ('ch06-search/array-search.md', 23, '数组查找'),
    '查找-树形查找.md': ('ch06-search/tree-search.md', 24, '树形查找'),
    '查找-散列表查找.md': ('ch06-search/hash-search.md', 25, '散列表查找'),
    '排序.md': ('ch06-search/sort-index.md', 26, '排序概述'),
    '排序-内部排序.md': ('ch07-sort/internal-sort.md', 27, '内部排序'),
    '排序-外部排序.md': ('ch07-sort/external-sort.md', 28, '外部排序'),
}

# Create directories
all_dirs = set(os.path.dirname(os.path.join(DST_DIR, v[0])) for v in CHAPTER_MAP.values())
for d in all_dirs:
    os.makedirs(d, exist_ok=True)

os.makedirs('static/images/docs/data-structure', exist_ok=True)

# Define difficulty and tags based on chapter
def get_frontmatter(title, weight, tags_extra, filename):
    # Determine tags from title
    tags = []
    if '绪论' in title or '基本概念' in title or '算法' in title or '概述' in title:
        tags = ['基础概念']
    elif '线性表' in title or '顺序' in title or '链' in title:
        tags = ['线性表']
    elif '栈' in title or '队列' in title:
        tags = ['栈', '队列']
    elif '串' in title or '字符串' in title or '模式匹配' in title:
        tags = ['串', '字符串']
    elif '树' in title or '二叉树' in title:
        tags = ['树', '二叉树']
    elif '图' in title:
        tags = ['图']
    elif '查找' in title or '散列' in title or '哈希' in title:
        tags = ['查找', '哈希']
    elif '排序' in title:
        tags = ['排序']

    diff = 1 if ('绪论' in title or '概述' in title or '基本' in title or weight <= 3) else \
           2 if (weight <= 18) else 3

    return f'''---
title: "{title}"
date: 2026-06-25
weight: {weight}
tags: [{', '.join(tags)}]
difficulty: {diff}
prerequisites: []
subject: data-structure
chapter: {weight // 10 + 1}
chapter_title: "{tags_extra}"
---

'''


def process_code_blocks(text):
    """Convert indented code blocks to fenced code blocks."""
    # Handle code blocks that use 4-space indent
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Detect 4-space indent code (common in original markdown)
        if line.startswith('    ') and line.strip():
            # Start of code block - collect all consecutive indented lines
            code_lines = []
            while i < len(lines) and lines[i].startswith('    '):
                code_lines.append(lines[i][4:])  # Remove 4-space indent
                i += 1
            # Output as fenced code block
            result.append('```c')
            result.extend(code_lines)
            result.append('```')
            result.append('')
            continue
        else:
            result.append(line)
        i += 1
    return '\n'.join(result)


def fix_image_paths(text, src_filename):
    """Fix image paths to reference static dir."""
    # Handle: ![](../images/xxx.svg) → ![](/images/docs/data-structure/xxx.svg)
    text = re.sub(
        r'!\[\]\(\.\./images/([^)]+)\)',
        r'![](/images/docs/data-structure/\1)',
        text
    )
    # Handle: ![alt](filename.assets/image.png) → ![](/images/docs/data-structure/image.png)
    stem = os.path.splitext(src_filename)[0]
    text = re.sub(
        rf'!\[([^\]]*)\]\({re.escape(stem)}\.assets/([^)]+)\)',
        r'![](/images/docs/data-structure/\2)',
        text
    )
    return text


def convert_file(src_file, dst_path, weight, title, tags_extra):
    """Convert a source markdown file to cc408 format."""
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the first line if it's just "# Title" (we'll add our own title)
    content = re.sub(r'^# .+\n?', '', content, count=1)

    # Remove priority markers
    content = re.sub(r'^[🔥💡]+\s*(高|低|中)优先级\s*\n', '', content, re.MULTILINE)

    # Process code blocks
    content = process_code_blocks(content)

    # Fix image paths
    content = fix_image_paths(content, os.path.basename(src_file))

    # Generate frontmatter
    fm = get_frontmatter(title, weight, tags_extra, os.path.basename(src_file))

    full_content = fm + content.strip() + '\n'

    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(full_content)

    print(f'  OK {os.path.basename(src_file)} -> {dst_path}')


count = 0
for chinese_name, (rel_path, weight, tags_extra) in CHAPTER_MAP.items():
    src = os.path.join(SRC_DIR, chinese_name)
    dst = os.path.join(DST_DIR, rel_path)
    if os.path.exists(src):
        title = tags_extra
        convert_file(src, dst, weight, title, tags_extra)
        count += 1
    else:
        print(f'  MISSING: {chinese_name}')

print(f'\nDone! Converted {count} files.')
