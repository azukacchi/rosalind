# Reverse Complement Problem: Find the reverse complement of a DNA string.

# Input: A DNA string Pattern.
# Output: Patternrc , the reverse complement of Pattern.

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'dataset_240215_2.txt')) as f:
    s = f.read().strip()
# s = 'AAAACCCGGT'  
s = s[-1::-1].lower().replace('a','T').replace('t','A').replace('c','G').replace('g','C')
print(s)