import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'dataset_240214_6.txt')) as f:
    (s,t) = (i for i in f.read().strip().split())
    
def FrequentWords(s,t):
    return len([str(m.start()+1) for m in re.finditer(f'(?={t})', s)])

print(FrequentWords(s,t))
