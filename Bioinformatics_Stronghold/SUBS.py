import re
import os
# import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'rosalind_subs.txt')) as f:
    (s,t) = (i for i in f.read().strip().split())

# start = time.time()
# s = 'GATATATGCATATACTT'
# t = 'ATAT'
print(' '.join([str(m.start()+1) for m in re.finditer(f'(?={t})', s)]))
# print(f'Time: {time.time() - start}')
