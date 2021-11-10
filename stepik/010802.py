# We say that a k-mer Pattern appears as a substring of Text with at most d mismatches
# if there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern,
# i.e., HammingDistance(Pattern, Pattern') ≤ d. Our observation that a DnaA box may appear with
# slight variations leads to the following generalization of the Pattern Matching Problem.

# Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.

# Input: Strings Pattern and Text along with an integer d.
# Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'dataset_240221_4.txt')) as f:
    a = f.read().strip()

# a = '''ATTCTGGA
# CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
# 3'''

(pattern,text,d) = (i for i in a.split('\n'))
d = int(d)

def HammingDistance(a,b):
    return sum([1 for i,j in zip(a,b) if i!=j])

count = 0
pos = []
for i in [text[index : index + len(pattern)] for index in range(len(text)-len(pattern)+1)]:
    # print(i)
    if HammingDistance(pattern,i) <= d:
        pos.append(count)
    count+=1

print(*pos)
     