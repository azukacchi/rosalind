# We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi.
# For example, CGAAT and CGGAC have two mismatches.
# The number of mismatches between strings p and q is called the Hamming distance between these strings
# and is denoted HammingDistance(p, q).

# Hamming Distance Problem: Compute the Hamming distance between two strings.

# Input: Two strings of equal length.
# Output: The Hamming distance between these strings.

import os
# import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'dataset_240221_3.txt')) as f:
    a = f.read()

# start = time.time()
# a = '''GGGCCGTTGGT
# GGACCGTTGAC'''

a = a.split('\n')

unmatched = sum([1 for i,j in zip(a[0],a[1]) if i!=j])
        
print(unmatched)
# print(f'Time: {time.time() - start}')