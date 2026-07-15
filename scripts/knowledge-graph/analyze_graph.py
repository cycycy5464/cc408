#!/usr/bin/env python3
import os, re, json

content_dir = "E:/programcc408/cc408/content/docs"
subjects = {}

for root, dirs, files in os.walk(content_dir):
    rel = os.path.relpath(root, content_dir)
    parts = rel.split(os.sep)
    if len(parts) < 2:
        continue
    subject, chapter = parts[0], parts[1]
    m = re.match(r"ch(\d+)", chapter)
    if not m:
        continue
    ch = int(m.group(1))
    subjects.setdefault(subject, {}).setdefault(ch, [])
    for f in files:
        if f == "_index.md":
            continue
        fp = os.path.join(root, f)
        with open(fp, encoding="utf-8") as h:
            c = h.read()
        t = re.search(r'^title:\s*"?(.*?)"?$', c, re.MULTILINE)
        title = t.group(1).strip().strip('"') if t else f
        subjects[subject][ch].append({"file": fp, "title": title})

print("Subjects:", list(subjects.keys()))
total_nodes = 0
total_edges = 0
for sub, chs in sorted(subjects.items()):
    sorted_ch = sorted(chs.keys())
    cnt = sum(len(v) for v in chs.values())
    print(f"\n=== {sub} ({cnt} files, {len(sorted_ch)} chapters) ===")
    for i, ch in enumerate(sorted_ch):
        titles = [x["title"] for x in chs[ch]]
        print(f"  ch{ch:02d}: {titles}")
        if i > 0:
            prev_ch = sorted_ch[i-1]
            n_prev = len(chs[prev_ch])
            n_cur = len(titles)
            total_edges += n_prev * n_cur
    total_nodes += cnt

print(f"\n--- Total: {total_nodes} nodes, ~{total_edges} edges ---")
