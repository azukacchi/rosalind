import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'dataset_240214_13.txt')) as f:
    (s,k) = (i for i in f.read().strip().split())

k = int(k)
# s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
# k = 4

kmer = {}

for i in [s[index : index + k] for index in range(0, len(s)-k+1)]:
    if i not in kmer:
        kmer[i] = 1
    else: kmer[i] += 1

max_value = max(kmer.values())
print(' '.join([key for key, value in kmer.items() if value == max_value]))
