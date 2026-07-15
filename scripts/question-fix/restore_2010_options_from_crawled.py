"""从 crawled_data/2010.json 恢复 2010 年选择题选项
用法: python scripts/restore_2010_options_from_crawled.py [--dry-run]
"""
import json, re, os, sys, glob

DRY_RUN = '--dry-run' in sys.argv
ROOT = 'D:/projet/cc408/cc408'

# 加载爬虫数据
with open(f'{ROOT}/tasks/408-crawler/crawled_data/2010.json', 'r', encoding='utf-8') as f:
    crawled = json.load(f)

def question_number_from_file(filepath):
    """从文件名提取题号，如 2010-ds-012.md → 12, 2010-cn-034.md → 34"""
    m = re.search(r'-(\d+)\.md$', filepath)
    return int(m.group(1)) if m else None

def load_current(filepath):
    path = os.path.join(ROOT, filepath)
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def find_insert_position(text):
    """找到 [tag_link] 之前的插入位置"""
    parts = text.split('---', 2)
    if len(parts) < 3:
        return -1
    body = parts[2]
    tag_pos = body.find('[tag_link]')
    if tag_pos >= 0:
        return len(parts[0]) + len(parts[1]) + 6 + tag_pos
    return -1

def has_options(text):
    """检查是否已有 A/B/C/D 选项"""
    return bool(re.search(r'^[A-D]\\\.', text, re.MULTILINE)) or bool(re.search(r'^[A-D]\.\s', text, re.MULTILINE))

def build_options_block(qdata):
    """从 crawled JSON 构造选项文本块"""
    opts = qdata.get('options', {})
    if not opts:
        return None
    lines = []
    for letter in ['A', 'B', 'C', 'D']:
        text = opts.get(letter, '').strip()
        if text:
            lines.append(f'{letter}\\. {text}')
    return '\n'.join(lines) if len(lines) >= 2 else None

def main():
    # 获取所有 2010 年 choice 文件
    pattern = f'{ROOT}/content/question/2010-*.md'
    files = sorted(glob.glob(pattern))
    
    restored = 0
    skipped_has_opts = 0
    skipped_no_data = 0
    skipped_non_choice = 0
    errors = []
    
    for fpath in files:
        fname = os.path.basename(fpath)
        content = load_current(f'content/question/{fname}')
        if content is None:
            continue
        
        # 只处理选择题
        if 'question_type: "choice"' not in content:
            skipped_non_choice += 1
            continue
        
        # 跳过已有选项的
        if has_options(content):
            skipped_has_opts += 1
            continue
        
        # 从文件名提取题号
        qnum = question_number_from_file(fname)
        if qnum is None or str(qnum) not in crawled['questions']:
            skipped_no_data += 1
            continue
        
        qdata = crawled['questions'][str(qnum)]
        opts_block = build_options_block(qdata)
        if opts_block is None:
            skipped_no_data += 1
            continue
        
        # 找到插入位置
        pos = find_insert_position(content)
        if pos < 0:
            errors.append(f'{fname}: 找不到插入位置')
            continue
        
        # 注入选项
        new_content = content[:pos] + '\n' + opts_block + '\n' + content[pos:]
        
        if DRY_RUN:
            print(f'  [DRY] {fname} (Q{qnum}): +{len(opts_block.split(chr(10)))}选项')
        else:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'  [OK] {fname} (Q{qnum}): 已恢复 {len(opts_block.split(chr(10)))} 个选项')
            restored += 1
    
    total_missing = (sum(1 for f in files if 'question_type: "choice"' in (open(os.path.join(ROOT, 'content/question', os.path.basename(f)), 'r', encoding='utf-8').read()) if not has_options(open(os.path.join(ROOT, 'content/question', os.path.basename(f)), 'r', encoding='utf-8').read()) ))
    
    print(f'\n=== 2010 年选项恢复结果 ===')
    print(f'已恢复: {restored}')
    print(f'已有选项(跳过): {skipped_has_opts}')
    print(f'非选择题(跳过): {skipped_non_choice}')
    print(f'爬虫无数据/图标题(跳过): {skipped_no_data}')
    if errors:
        print(f'错误: {len(errors)}')
        for e in errors:
            print(f'  ✗ {e}')

if __name__ == '__main__':
    main()
