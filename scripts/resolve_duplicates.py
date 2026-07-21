"""Resolve ds/co duplicates: keep better file, fix subject, delete worse."""
import glob, re, os

question_dir = os.path.join(os.path.dirname(__file__), '..', 'content', 'question')
years = ['2011', '2012']

for year in years:
    ds_files = {f.split('-')[-1].split('.')[0]: f for f in glob.glob(os.path.join(question_dir, f'{year}-ds-0*.md'))}
    co_files = {f.split('-')[-1].split('.')[0]: f for f in glob.glob(os.path.join(question_dir, f'{year}-co-0*.md'))}
    overlap = sorted(set(ds_files.keys()) & set(co_files.keys()), key=int)
    
    for num in overlap:
        with open(ds_files[num], 'r', encoding='utf-8') as f: ds = f.read()
        with open(co_files[num], 'r', encoding='utf-8') as f: co = f.read()
        
        ds_opts = len(re.findall(r'^[A-D]\\.', ds, re.MULTILINE))
        co_opts = len(re.findall(r'^[A-D]\\.', co, re.MULTILINE))
        ds_body = len(ds[ds.find('---', ds.find('---')+3)+3:].strip())
        co_body = len(co[co.find('---', co.find('---')+3)+3:].strip())
        
        ds_score = ds_opts * 10 + min(ds_body, 1000)
        co_score = co_opts * 10 + min(co_body, 1000)
        
        keep_ds = ds_score >= co_score
        
        if keep_ds:
            keep_fp = ds_files[num]
            del_fp = co_files[num]
            # Fix subject in ds file
            ds = re.sub(r'(subjects:\s*\n\s*-\s*["\']?)组成原理(["\']?)', r'\1计算机组成原理\2', ds)
            with open(keep_fp, 'w', encoding='utf-8') as f:
                f.write(ds)
        else:
            keep_fp = co_files[num]
            del_fp = ds_files[num]
        
        # Delete the worse file
        os.remove(del_fp)
        kept = os.path.basename(keep_fp)
        deleted = os.path.basename(del_fp)
        print(f'{year} Q{num}: keep [{kept}] delete [{deleted}]')
    
    # After deletion, fix subjects for remaining ds- files in co range (12-22)
    for fp in sorted(glob.glob(os.path.join(question_dir, f'{year}-ds-0*.md'))):
        with open(fp, 'r', encoding='utf-8') as f:
            text = f.read()
        if '组成原理' in text and '计算机组成原理' not in text:
            text = re.sub(r'(subjects:\s*\n\s*-\s*["\']?)组成原理(["\']?)', r'\1计算机组成原理\2', text)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f'  Fix subject: {os.path.basename(fp)}')
