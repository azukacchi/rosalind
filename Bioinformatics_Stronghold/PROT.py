##### Problem #####

# The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet
# (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols.
# Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

# The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

# Return: The protein string encoded by s.


##### Answer #####

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
