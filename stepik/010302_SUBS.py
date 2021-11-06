# Code Challenge: Solve the Pattern Matching Problem.

# Input: Two strings, Pattern and Genome.
# Output: A collection of space-separated integers specifying all starting positions
# where Pattern appears as a substring of Genome.

import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'Vibrio_cholerae.txt')) as f:
    # (t,s) = (i for i in f.read().strip().split())
    s = f.read().strip()

t = 'CTTGATCAT'

# s = 'GATATATGCATATACTT'
# t = 'ATAT'
print(' '.join([str(m.start()) for m in re.finditer(f'(?={t})', s)]))