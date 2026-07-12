"""Test the batch_fix functions"""
import sys
sys.path.insert(0, 'tasks/真题修复')
from batch_fix import fix_code_block_language, fix_table_spacing

# Test 1: code block with ```c (already has c tag)
test1 = 'text\n\n```c\nint main() {\n    return 0;\n}\n```\nmore\n'
print("=== Test 1: ```c already tagged ===")
print(repr(fix_code_block_language(test1)))

# Test 2: code block with ``` (plain, no language tag)
test2 = 'text\n\n```\nint main() {\n    return 0;\n}\n```\nmore\n'
print("\n=== Test 2: plain ``` should become ```c ===")
print(repr(fix_code_block_language(test2)))

# Test 3: the exact 2009-ds-042 pattern
test3 = ' 3）算法实现 \n\n```c\nint FindElement(Node *head, int k)\n{\n    return 1;\n}\n```\n'
print("\n=== Test 3: 2009-ds-042 pattern ===")
result = fix_code_block_language(test3)
print(repr(result))
print("---")
print(result)
