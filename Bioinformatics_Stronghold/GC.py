##### Problem #####
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'.
# For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

# DNA strings must be labeled when they are consolidated into a database.
# A commonly used method of string labeling is called FASTA format.
# In this format, the string is introduced by a line that begins with '>', followed by some labeling information.
# Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx",
# where "xxxx" denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.


##### Answer #####

import os
# import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'rosalind_gc.txt')) as f:
    a = f.read()

# a = '''>Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT'''

# start = time.time()
a=a.split('>')
# print(a)
c=[i.split('\n') for i in a][1:]
# print(c)
# print([''.join(e) for d in c for e in d])
labels = [b[0] for b in c]
# print(labels)
for i,j in enumerate(c):
    c[i] = [v for v in j if v != '']
    c[i] = ''.join([v for v in c[i] if v[0] != 'R'])  
# print(c)

contents = {}
for label,segment in zip(labels,c):
    c_count = segment.count('C')
    g_count = segment.count('G')
    # print(label)
    contents[label] = (c_count+g_count)/len(segment)
    # print((c_count+g_count)/len(segment))

# print(contents)

print(list(contents.keys())[list(contents.values()).index(max(contents.values()))])
print(max(contents.values())*100)

# print(f'Time: {time.time() - start}')
