"""Restore missing content in question files from crawled data."""
import glob, re, json, os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
question_dir = os.path.abspath(os.path.join(script_dir, '..', '..', '..', 'content', 'question'))
crawled_dir = os.path.abspath(os.path.join(script_dir, '..', '..', '..', 'tasks', '408-crawler', 'crawled_data'))

years = sys.argv[1:] if len(sys.argv) > 1 else ['2011','2012']

for year in years:
    # Load crawled data
    crawled_file = os.path.join(crawled_dir, f'{year}.json')
    if not os.path.exists(crawled_file):
        print(f'No crawled data for {year}, skipping')
        continue
    
    with open(crawled_file, 'r', encoding='utf-8') as f:
        crawled = json.load(f)
    
    cq = crawled.get('questions', {})
    ca = crawled.get('answers', {})
    ce = crawled.get('explanations', {})
    
    files = sorted(glob.glob(os.path.join(question_dir, f'{year}-*.md')))
    fixed_count = 0
    
    for fp in files:
        with open(fp, 'r', encoding='utf-8') as f:
            text = f.read()
        original = text
        fname = os.path.basename(fp)
        
        # Extract question number from filename (e.g., 2011-ds-002.md → 2)
        num_match = re.search(r'-(\d+)\.md$', fname)
        if not num_match:
            continue
        qnum = str(int(num_match.group(1)))  # remove leading zeros
        
        is_choice = 'question_type: "choice"' in text
        
        if not is_choice:
            continue
        
        # Check if options exist
        has_options = bool(re.search(r'^[A-D]\\\.', text, re.MULTILINE))
        
        if not has_options and qnum in cq:
            qdata = cq[qnum]
            options = qdata.get('options', {})
            stem = qdata.get('stem', '')
            
            # Find where to insert options: before [tag_link]
            tag_idx = text.find('[tag_link]')
            if tag_idx < 0:
                # Also try before 正确答案
                ans_idx = text.find('正确答案')
                insert_idx = ans_idx if ans_idx > 0 else len(text)
            else:
                insert_idx = tag_idx
            
            # Look for link line before insertion point
            # We want to insert after any tag links but before [tag_link]
            before_text = text[:insert_idx].rstrip()
            
            # Build options block
            opt_lines = []
            for letter in ['A', 'B', 'C', 'D']:
                opt_text = options.get(letter, '').strip()
                if opt_text:
                    opt_lines.append(f'{letter}\\. {opt_text}')
            
            if opt_lines:
                opt_block = '\n' + '\n'.join(opt_lines) + '\n'
                text = text[:insert_idx] + opt_block + text[insert_idx:]
                print(f'  [restore options] {fname} (Q{qnum})')
        
        # Check for 正确答案 in choice files
        has_answer = bool(re.search(r'正确答案[：:]\s*[ABCDabcd]', text))
        if not has_answer and qnum in ca:
            answer = ca[qnum]
            # Insert after [tag_link] line
            tag_idx = text.find('[tag_link]')
            if tag_idx >= 0:
                # Find end of [tag_link] line
                eol = text.find('\n', tag_idx)
                after_tag = text[eol:] if eol >= 0 else ''
                # Check if there's already a blank line after [tag_link]
                if after_tag.startswith('\n\n'):
                    text = text[:eol] + f'\n\n正确答案：{answer}' + after_tag
                else:
                    text = text[:eol] + f'\n\n正确答案：{answer}\n' + after_tag.lstrip('\n')
                print(f'  [restore answer] {fname} (Q{qnum}: {answer})')
        
        if text != original:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(text)
            fixed_count += 1
    
    print(f'{year}: {fixed_count} files restored')
