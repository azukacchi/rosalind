import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'dataset_240229_4.txt')) as f:
    (s,k) = (i for i in f.read().strip().split())

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

print(*Neighbors(s,int(k)))