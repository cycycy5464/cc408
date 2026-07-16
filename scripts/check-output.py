#!/usr/bin/env python3
"""Check actual output for OS Ch3"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os

output_dir = r"E:\programcc408\cc408\content\question\chapterExercises\os\chapter3-memory"

files = sorted([f for f in os.listdir(output_dir) if f.endswith('.md')])
print(f"Total files: {len(files)}")

# Check first 10 and last 10
print("\n=== First 10 files ===")
for f in files[:10]:
    filepath = os.path.join(output_dir, f)
    with open(filepath, 'r', encoding='utf-8') as fh:
        content = fh.read()
    # Extract answer line
    for line in content.split('\n'):
        if '正确答案' in line:
            print(f"  {f}: {line}")
            break

print("\n=== Last 10 files ===")
for f in files[-10:]:
    filepath = os.path.join(output_dir, f)
    with open(filepath, 'r', encoding='utf-8') as fh:
        content = fh.read()
    # Extract answer line
    for line in content.split('\n'):
        if '正确答案' in line:
            print(f"  {f}: {line}")
            break

# Count empty answers
empty_count = 0
for f in files:
    filepath = os.path.join(output_dir, f)
    with open(filepath, 'r', encoding='utf-8') as fh:
        content = fh.read()
    for line in content.split('\n'):
        if '正确答案：' in line and line.strip() == '正确答案：':
            empty_count += 1
            break

print(f"\nEmpty answers: {empty_count}/{len(files)}")
