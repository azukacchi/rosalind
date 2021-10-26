##### Problem #####

# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
# then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement sc of s.


##### Answer #####

# import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'rosalind_revc.txt')) as f:
    a = f.read()
# a = 'AAAACCCGGT'

# start = time.time()
a = a[-1::-1].lower()
a = a.replace('a','T').replace('t','A').replace('c','G').replace('g','C')

print(a)

# print(f'Time: {time.time() - start}')
