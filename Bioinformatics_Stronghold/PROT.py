import os
# import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'rosalind_prot.txt')) as f:
    a = f.read().strip()

# start = time.time()
# a = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
rna = [a[index : index + 3] for index in range(0, len(a), 3)]
# print(rna)
codons = {
"UUU" : "F",
"CUU" : "L",
"AUU" : "I",
"GUU" : "V",
"UUC" : "F",
"CUC" : "L",
"AUC" : "I",
"GUC" : "V",
"UUA" : "L",
"CUA" : "L",
"AUA" : "I",     
"GUA" : "V",
"UUG" : "L",
"CUG" : "L",
"AUG" : "M",
"GUG" : "V",
"UCU" : "S",
"CCU" : "P",
"ACU" : "T",
"GCU" : "A",
"UCC" : "S",
"CCC" : "P",
"ACC" : "T",
"GCC" : "A",
"UCA" : "S",
"CCA" : "P",
"ACA" : "T",
"GCA" : "A",
"UCG" : "S",
"CCG" : "P",
"ACG" : "T",
"GCG" : "A",
"UAU" : "Y",
"CAU" : "H",
"AAU" : "N",
"GAU" : "D",
"UAC" : "Y",
"CAC" : "H",
"AAC" : "N",
"GAC" : "D",
"UAA" : "",
"CAA" : "Q",
"AAA" : "K",
"GAA" : "E",
"UAG" : "",
"CAG" : "Q",
"AAG" : "K",
"GAG" : "E",
"UGU" : "C",
"CGU" : "R",
"AGU" : "S",
"GGU" : "G",
"UGC" : "C",
"CGC" : "R",
"AGC" : "S",
"GGC" : "G",
"UGA" : "",
"CGA" : "R",
"AGA" : "R",
"GGA" : "G",
"UGG" : "W",
"CGG" : "R",
"AGG" : "R",
"GGG" : "G"
}

# def end_of_loop():
#     return
# protein = list(end_of_loop() if n in (['UAA','UAG','UGA']) else codons[n] for n in rna)
# print(''.join(protein[:protein.index(None)]))

print(''.join([codons[n] for n in rna]))
# print(f'Time: {time.time() - start}')
