# Clump Finding Problem: Find patterns forming clumps in a string.

# Input: A string Genome, and integers k, L, and t.
# Output: All distinct k-mers forming (L, t)-clumps in Genome.

# How many different 9-mers form (500,3)-clumps in the E. coli genome?
# (In other words, do not count a 9-mer more than once.)

import re
import os
import time
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'E_coli.txt')) as f:
    # (s,k,L,t) = (i for i in f.read().strip().split())
    s = f.read().strip()
# k,L,t = int(k), int(L), int(t)

start = time.time()
# s = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
# k, L, t = 5,50,4
k = 9
L = 500
t = 3

kmers = defaultdict(list)

for i in range(len(s)-k):
    x = s[i:i+k]
    kmers[x].append(i)

kmer_t_times = [key for key, value in kmers.items() if len(value) >= t]

clump = []
for kmer in kmer_t_times:
    for i in range(len(kmers[kmer])-t+1):
        if kmers[kmer][i] + L - k >= kmers[kmer][i+t-1]:
            clump.append(kmer)

print(len(set(clump)))
print(f'Time: {time.time() - start}')