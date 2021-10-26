##### Problem ######

# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t.


##### Answer ######

# import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'rosalind_rna.txt')) as f:
    a = f.read()
# a = 'GATGGAACTTGACTACGTAAATT'
    
# start = time.time()
a = a.replace('T','U')
print(a)

# print(f'Time: {time.time() - start}')
