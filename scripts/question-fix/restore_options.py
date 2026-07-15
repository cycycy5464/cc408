"""从 4cf9d6c 恢复选择题选项到当前文件
用法: python scripts/restore_options.py [--dry-run] [--limit N]
"""
import subprocess, re, os, sys, glob

DRY_RUN = '--dry-run' in sys.argv
LIMIT = None
for a in sys.argv:
    if a.startswith('--limit='):
        LIMIT = int(a.split('=')[1])

ROOT = 'D:/projet/cc408/cc408'

def get_old_content(filepath):
    """从 4cf9d6c 获取文件内容"""
    r = subprocess.run(['git', 'show', f'4cf9d6c:{filepath}'],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        return None
    return r.stdout

def extract_options(text):
    """提取所有选项项，支持同行多选项格式（A\.内容 B\.内容 在同一行）"""
    lines = text.split('\n')
    opts = []
    for line in lines:
        stripped = line.rstrip()
        # 匹配行首为 A\.（有反斜杠转义点）
        if re.match(r'^[A-D]\\\.', stripped):
            # 一行内可能有多项选项（如 A\.xxx B\.xxx C\.xxx D\.xxx）
            # 用 (?=[A-D]\\.) 拆分；注意转义正确：在raw string中 \\\\. = \\ + \.
            parts = re.split(r'(?=[A-D]\\\.)', stripped)
            for part in parts:
                part = part.strip()
                if part and re.match(r'^[A-D]\\\.', part):
                    opts.append(part)
        # 匹配行首为 A. 内容（无转义，点后跟空格/结束）
        elif re.match(r'^[A-D]\.\s', stripped) or re.match(r'^[A-D]\.$', stripped):
            opts.append(stripped)
    return opts

def question_type(text):
    """从 frontmatter 提取 question_type"""
    m = re.search(r'question_type:\s*"?(\w+)"?', text)
    return m.group(1) if m else ''

def find_insert_position(text):
    """找到插入选项的最佳位置: 题干内容之后, [tag_link] 之前"""
    # 找正文开始（frontmatter 结束后的第一个非空行）
    parts = text.split('---', 2)
    if len(parts) < 3:
        return -1
    body = parts[2]
    
    # 优先在 [tag_link] 之前插入
    tag_pos = body.find('[tag_link]')
    if tag_pos >= 0:
        # 在 tag_link 之前（包括前面的空行）
        return len(parts[0]) + len(parts[1]) + 6 + tag_pos  # +6 for '---\n'
    
    return -1

def inject_options(current_text, opts_lines, insert_pos):
    """在指定位置注入选项"""
    if insert_pos < 0:
        return current_text
    
    # 选项文本（前后加空行）
    opts_block = '\n' + '\n'.join(opts_lines) + '\n'
    
    new_text = current_text[:insert_pos] + opts_block + current_text[insert_pos:]
    return new_text

def main():
    # 获取 4cf9d6c 中的文件列表
    r = subprocess.run(['git', 'ls-tree', '-r', '--name-only', '4cf9d6c'],
                       capture_output=True, text=True, cwd=ROOT)
    old_files = set(r.stdout.strip().split('\n'))
    
    # 只处理 question 目录下的文件
    question_files = sorted([f for f in old_files if f.startswith('content/question/') and f.endswith('.md')])
    print(f'4cf9d6c 中共 {len(question_files)} 个问题文件')
    
    restored = 0
    skipped_no_opts = 0
    skipped_already = 0
    skipped_not_choice = 0
    errors = []
    
    for i, filepath in enumerate(question_files):
        if LIMIT and i >= LIMIT:
            break
        
        # 读当前文件
        current_path = os.path.join(ROOT, filepath)
        if not os.path.exists(current_path):
            skipped_no_opts += 1
            continue
        
        with open(current_path, 'r', encoding='utf-8') as f:
            current = f.read()
        
        # 只处理选择题
        if question_type(current) != 'choice':
            skipped_not_choice += 1
            continue
        
        # 检查当前是否已有选项
        if extract_options(current):
            skipped_already += 1
            continue
        
        # 获取旧版本
        old = get_old_content(filepath)
        if not old:
            errors.append(f'{filepath}: 无法读取旧版本')
            continue
        
        old_opts = extract_options(old)
        if len(old_opts) < 4:
            skipped_no_opts += 1
            continue
        
        # 找到插入位置并注入
        pos = find_insert_position(current)
        if pos < 0:
            errors.append(f'{filepath}: 找不到插入位置')
            continue
        
        new_content = inject_options(current, old_opts, pos)
        
        if DRY_RUN:
            print(f'  [DRY] {os.path.basename(filepath)}: +{len(old_opts)}选项 → {pos}')
        else:
            with open(current_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            restored += 1
        
        if i < 5 or (i % 100 == 0):
            print(f'  [{i+1}/{len(question_files)}] {os.path.basename(filepath)}: {"待恢复" if DRY_RUN else "已恢复"} {len(old_opts)}选项')
    
    print(f'\n=== 结果 ===')
    print(f'已恢复: {restored}')
    print(f'已有选项(跳过): {skipped_already}')
    print(f'非选择题(跳过): {skipped_not_choice}')
    print(f'旧版也无选项(跳过): {skipped_no_opts}')
    print(f'错误: {len(errors)}')
    for e in errors[:5]:
        print(f'  ✗ {e}')

if __name__ == '__main__':
    main()
