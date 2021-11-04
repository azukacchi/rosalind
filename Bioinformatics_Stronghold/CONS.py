# Problem
# A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns.
# Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

# Say that we have a collection of DNA strings, all having the same length n.
# Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the
# jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

# A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position;
# the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix.
# Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

# A T C C A G C T
# G G G C A A C T
# A T G G A T C T
# DNA Strings	A A G C A A C C
# T T G G A A C T
# A T G C C A T T
# A T G G C A C T
# A   5 1 0 0 5 5 0 0
# Profile	C   0 0 1 4 2 0 6 1
# G   1 1 6 3 0 1 0 0
# T   1 5 0 0 0 1 1 6
# Consensus	A T G C A A C T
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)


##### Answer #####

import numpy as np
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'rosalind_cons.txt')) as f:
    a = f.read()

start = time.time()
# a = '''>Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT'''
a=a.split('>')

c=[i.split('\n') for i in a][1:]

labels = [b[0] for b in c]

for i,j in enumerate(c):
    c[i] = [v for v in j if v != '']
    c[i] = ''.join([v for v in c[i] if v[0] != 'R']) 

c = np.array([i for b in c for i in b]).reshape(len(c),-1)

a_count = np.where(c=='A',1,0).sum(axis=0)
c_count = np.where(c=='C',1,0).sum(axis=0)
g_count = np.where(c=='G',1,0).sum(axis=0)
t_count = np.where(c=='T',1,0).sum(axis=0)

c = np.array([a_count,c_count,g_count,t_count])

c_max = np.argmax(c, axis=0)

print(''.join(np.where(c_max==0,'A',np.where(c_max==1,'C',np.where(c_max==2,'G','T')))))
print(f'A: {" ".join([str(i) for i in a_count])}')
print(f'C: {" ".join([str(i) for i in c_count])}')
print(f'G: {" ".join([str(i) for i in g_count])}')
print(f'T: {" ".join([str(i) for i in t_count])}')

# print(f'Time: {time.time() - start}')
