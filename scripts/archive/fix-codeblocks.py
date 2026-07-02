#!/usr/bin/env python3
"""Fix mis-wrapped code blocks: unwrap list items wrongly wrapped in ```c """
import os, re

DOCS_DIR = 'content/docs'

def fix_code_blocks(text):
    """Find code blocks that are actually list items and unwrap them."""
    def fix_block(match):
        block = match.group(1)
        lines = block.strip().split('\n')
        # Check if majority of non-empty lines are list items or plain text
        non_empty = [l for l in lines if l.strip()]
        list_like = [l for l in non_empty if l.strip().startswith('* ') or l.strip().startswith('- ') or l.strip().startswith('1.') or l.strip().startswith('2.')]
        # Also check if lines are short prose (not code)
        prose_like = [l for l in non_empty if not any(kw in l for kw in [';', '{', '}', '=', '#include', 'int ', 'char ', 'void ', 'printf'])]
        if len(list_like) > len(non_empty) * 0.4 or (len(prose_like) > len(non_empty) * 0.7 and len(non_empty) > 1):
            # Unwrap: return as regular markdown without code fence
            return block.strip() + '\n\n'
        return match.group(0)

    text = re.sub(r'\`\`\`c\n(.*?)\n\`\`\`', fix_block, text, flags=re.DOTALL)
    return text

stats = {'checked': 0, 'fixed': 0}
for root, dirs, files in os.walk(DOCS_DIR):
    for fname in files:
        if not fname.endswith('.md') or fname == '_index.md':
            continue
        path = os.path.join(root, fname)
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        new_text = fix_code_blocks(text)
        if new_text != text:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_text)
            stats['fixed'] += 1
        stats['checked'] += 1

    c = stats['checked']; f = stats['fixed']
print(f'Checked {c} files, fixed {f}')
