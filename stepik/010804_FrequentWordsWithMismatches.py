# Solve the Frequent Words with Mismatches Problem.

# Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
# Output: All most frequent k-mers with up to d mismatches in Text.

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'dataset_240221_9.txt')) as f:
    (text,k,d) = (i for i in f.read().strip().split())

# s = '''ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4 1'''
# (text,k,d) = (i for i in s.strip().split())
k,d = int(k),int(d)

kmer = {}

def FrequentWordsWithMismatches(text,k,d):
    patterns = []
    for pattern in [text[index : index + k] for index in range(0, len(text)-k+1)]:
        neighborhood = list(Neighbors(pattern,d))
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor not in kmer:
                kmer[neighbor] = 1
            else: kmer[neighbor] +=1
    m = max(kmer.values())
    for pat in kmer:
        if kmer[pat] == m:
            patterns.append(pat)
    return patterns
        

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

print(*FrequentWordsWithMismatches(text,k,d))
