##### Problem #####
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word;
# the length of a string is the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

##### Answer #####

# import sys
# import random
# import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# text = 
with open(os.path.join(BASE_DIR, 'rosalind_dna.txt')) as f:
    a = f.read()
    
# start = time.time()

print(a.count('A'),a.count('C'),a.count('G'),a.count('T'))
# print(f'Time: {time.time() - start}')
