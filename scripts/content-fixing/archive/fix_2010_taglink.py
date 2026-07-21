"""Fix 2010 question files: separate [tag_link], 正确答案, and analysis text with blank lines."""
import re, os, glob

question_dir = os.path.join(os.path.dirname(__file__), '..', 'content', 'question')
files = glob.glob(os.path.join(question_dir, '2010-*.md'))

fixed = 0
taglink_fixed = 0
answer_fixed = 0

for fp in sorted(files):
    with open(fp, 'r', encoding='utf-8') as f:
        text = f.read()
    
    original = text
    fname = os.path.basename(fp)
    
    # 1. Add blank line between [tag_link] and 正确答案：X
    #    Pattern: "[tag_link]\n正确答案：" → "[tag_link]\n\n正确答案："
    #    But NOT when "正确答案" is part of analysis text
    text = re.sub(
        r'(\[tag_link\])\n(正确答案[：:])',
        r'\1\n\n\2',
        text
    )
    
    # 2. Normalize excessive blank lines: reduce 3+ consecutive blank lines to 1
    #    Specifically between [tag_link] and 正确答案
    text = re.sub(
        r'(\[tag_link\])\n{3,}(正确答案[：:])',
        r'\1\n\n\2',
        text
    )
    
    # 3. Add blank line between 正确答案：X and the analysis text that follows
    #    Pattern: "正确答案：[A-D]\n非空文本" → "正确答案：[A-D]\n\n非空文本"
    #    Only if there isn't already a blank line
    text = re.sub(
        r'(正确答案[：:]\s*[ABCDabcd])\n(?!\n)',
        r'\1\n\n',
        text,
        flags=re.MULTILINE
    )
    # Clean up triple blank lines caused by combination of above
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 4. Fix 2010-ds-003.md: unescaped options
    if '2010-ds-003' in fp:
        text = text.replace('A.     B.     C.     D.', 'A\\.     B\\.     C\\.     D\\.')
    
    if text != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(text)
        fixed += 1
        if '[tag_link]' in original and '[tag_link]\n\n' in text:
            taglink_fixed += 1
        print(f'  Fixed: {fname}')

print(f'\nTotal files processed: {len(files)}')
print(f'Files modified: {fixed}')
print(f'Tag_link separation applied: {taglink_fixed}')
