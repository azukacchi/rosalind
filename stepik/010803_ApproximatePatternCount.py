# Computing Countd(Text, Pattern) simply requires us to compute the Hamming distance between
# Pattern and every k-mer substring of Text, which is achieved by the following pseudocode.

#    ApproximatePatternCount(Text, Pattern, d)
#         count ← 0
#         for i ← 0 to |Text| − |Pattern|
#             Pattern′ ← Text(i , |Pattern|)
#            if HammingDistance(Pattern, Pattern′) ≤ d
#                 count ← count + 1
#         return count

# Input: Strings Pattern and Text as well as an integer d.
# Output: Countd(Text, Pattern).

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'dataset_240221_6.txt')) as f:
    a = f.read().strip()

# a = '''GAGG
# TTTAGAGCCTTCAGAGG
# 2'''

(pattern,text,d) = (i for i in a.split('\n'))
d = int(d)

def HammingDistance(a,b):
    return sum([1 for i,j in zip(a,b) if i!=j])

count = 0
total = 0
for i in [text[index : index + len(pattern)] for index in range(len(text)-len(pattern)+1)]:
    # print(i)
    if HammingDistance(pattern,i) <= d:
        total+=1
    count+=1

print(total)
     