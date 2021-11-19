# Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.

# Input: A DNA string Genome.
# Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).

import numpy as np
import os
from collections import defaultdict
import time
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'Salmonella_enterica.txt')) as f:
    text = f.read().strip()
start = time.time()
# s = 'CATGGGCATCGGCCATACGCC'
# s = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'

skew = np.array([i for i in text])
# print(skew)
score = np.where(skew=='G',1,np.where(skew=='C',-1,0))
# print(score)
a = np.insert(score, 0, 0)


a = np.cumsum(a)
min_values = a.min()
pos = [key for key, value in enumerate(a) if value == min_values]
# print(' '.join([str(i) for i in pos]))

L = 500
k = 9
beginning_pos,end_pos = min(pos)-L+k,max(pos)+L
# print(beginning_pos,end_pos)
# # print(f'Time: {time.time() - start}')
# # plt.plot(range(1,len(a)+1),a)
# # plt.show()

def REVC(s):
    return s[-1::-1].lower().replace('a','T').replace('t','A').replace('c','G').replace('g','C')

def FrequentWordsWithMismatches(text,k,d):
    patterns = []
    kmer = {}
    for pattern in [text[index : index + k] for index in range(0, len(text)-k+1)]:
        neighborhood = list(Neighbors(pattern,d))
        # print(neighborhood)
        for neighbor in neighborhood:
            if neighbor not in kmer:
                if REVC(neighbor) in kmer:
                    kmer[REVC(neighbor)] += 1
                    kmer[neighbor] = 2
                else:
                    kmer[neighbor] = 1
                    kmer[REVC(neighbor)] = 1
            else:
                if REVC(neighbor) in kmer:
                    kmer[REVC(neighbor)] += 1
                kmer[neighbor] +=1
    m = max(kmer.values())

    for pat in kmer:
        if kmer[pat] == m:
            patterns.append(pat)
    # print(m)
    return m,patterns
        

def HammingDistance(a,b):
    return sum([1 for i,j in zip(a,b) if i!=j])

def Neighbors(pattern,d):
    if d == 0:
        return {pattern}
    if len(pattern)==1:
        return {'A','C','G','T'}
    Neighborhood = set()
    SuffixNeighbors = Neighbors(pattern[1:],d)
    # print(SuffixNeighbors)
    for i in SuffixNeighbors:
        if HammingDistance(pattern[1:],i)<d:
            for nucleotide in ['A','C','G','T']:
                Neighborhood.add(nucleotide+i)
        else: Neighborhood.add(pattern[0]+i)
    return Neighborhood


text = text[beginning_pos:end_pos]

count_sub = 0
sub_dict = dict()
for subtext in [text[index : index + L] for index in range(0, len(text)-L+1)]:
    sub_dict[count_sub] = FrequentWordsWithMismatches(subtext,9,1)[0]
    count_sub+=1

# print(sub_dict)
max_kmer = max(sub_dict.values())
sub_texts = []
for pat in sub_dict:
        if sub_dict[pat] == max_kmer:
            sub_texts.append(pat)

# print(min(sub_texts))
print(text[min(sub_texts):min(sub_texts)+L])
print(f'Time: {time.time() - start}')
