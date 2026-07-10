import os
import glob

base_dir = 'E:/programcc408/cc408/content/question'
years = ('2010','2011','2012','2013','2015','2016','2017','2018','2019','2020','2021','2023','2024','2025')
count = 0

for f in glob.glob(os.path.join(base_dir, '*.md')):
    name = os.path.basename(f)
    if not name.startswith(years):
        continue
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    if '[tag_link]' in text:
        continue
    text = text.replace('正确答案', '[tag_link]\n正确答案')
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(text)
    count += 1

print(f"Updated {count} files")
