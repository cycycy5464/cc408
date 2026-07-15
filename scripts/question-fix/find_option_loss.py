"""对比 4cf9d6c (好) vs c3c8178 (坏)，找出选项丢失的文件"""
import subprocess, re

r = subprocess.run(
    ['git', 'diff', '--name-only', '4cf9d6c', 'c3c8178', '--', 'content/question/*.md'],
    capture_output=True, text=True, cwd='D:/projet/cc408/cc408'
)
changed = [f for f in r.stdout.strip().split('\n') if f]
print(f'修改文件总数: {len(changed)}')

lost = []
kept = []
new_created = []
other = []
for f in changed:
    old = subprocess.run(['git', 'show', f'4cf9d6c:{f}'], capture_output=True, text=True,
                         cwd='D:/projet/cc408/cc408').stdout
    new = subprocess.run(['git', 'show', f'c3c8178:{f}'], capture_output=True, text=True,
                         cwd='D:/projet/cc408/cc408').stdout
    # 检测选项: A\. 或 A. 格式 （在4cf9d6c中可能是 A\. 或 A\\）
    old_opts = bool(re.search(r'^A[\\\.]*\.[ \t]', old, re.MULTILINE))
    new_opts = bool(re.search(r'^A[\\\.]*\.[ \t]', new, re.MULTILINE))
    
    if old_opts and not new_opts:
        lost.append(f)
    elif old_opts and new_opts:
        kept.append(f)
    elif not old_opts:
        new_created.append(f)
    else:
        other.append(f)

print(f'选项丢失: {len(lost)}')
print(f'选项保留: {len(kept)}')
print(f'新增文件(旧无不涉及): {len(new_created)}')
print(f'其他: {len(other)}')
print()
if lost:
    print('=== 丢失选项的文件 ===')
    for f in lost[:20]:
        print(f'  {f}')
    if len(lost) > 20:
        print(f'  ... 还有 {len(lost)-20} 个')
