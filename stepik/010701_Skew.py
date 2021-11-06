# Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.

# Input: A DNA string Genome.
# Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).

import numpy as np
import os
import time
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'dataset_240220_10.txt')) as f:
    s = f.read().strip()
start = time.time()
# s = 'CATGGGCATCGGCCATACGCC'
# s = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'

skew = np.array([i for i in s])
# print(skew)
score = np.where(skew=='G',1,np.where(skew=='C',-1,0))
# print(score)
a = np.insert(score, 0, 0)

a = np.cumsum(a)
min_values = a.min()
print(' '.join([str(key) for key, value in enumerate(a) if value == min_values]))
print(f'Time: {time.time() - start}')
# plt.plot(range(1,len(a)+1),a)
# plt.show()