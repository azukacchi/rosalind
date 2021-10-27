##### Problem #####

# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
# is the number of corresponding symbols that differ in s and t. See Figure 2.

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t).


##### Answer #####

import os
# import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'rosalind_hamm.txt')) as f:
    a = f.read()

# start = time.time()
# a = '''GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT'''

a = a.split('\n')

unmatched = sum([1 for i,j in zip(a[0],a[1]) if i!=j])
        
print(unmatched)
# print(f'Time: {time.time() - start}')
