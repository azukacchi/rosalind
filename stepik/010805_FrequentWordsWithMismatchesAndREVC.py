# Frequent Words with Mismatches and Reverse Complements Problem:
# Find the most frequent k-mers (with mismatches and reverse complements) in a string.

# Input: A DNA string Text as well as integers k and d.
# Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern)+ Countd(Text, Patternrc) over all possible k-mers.

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'dataset_240221_10.txt')) as f:
    (text,k,d) = (i for i in f.read().strip().split())

# s = '''AAAAAAAAAA
# 2 1'''
# (text,k,d) = (i for i in s.strip().split())
k,d = int(k),int(d)

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