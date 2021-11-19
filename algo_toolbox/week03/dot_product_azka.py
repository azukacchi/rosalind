import numpy as np
import itertools
s = '''3
10000 3000 -5000
-2000 4000 10000'''

(a,b) = (b for b in s.split('\n')[1:])
(a,b) = ([int(i) for i in a.split()], [int(i) for i in b.split()])

a = np.array(a)
b = np.array(b)

# for i in range(300):
#     a = np.append(a,a)
#     b = np.append(b,b)
# print(a)    

a = np.tile(a,30)
b = np.tile(b,30)

max_product = 0
for n in list(itertools.permutations(b, len(b))):
    if a.dot(n) > max_product:
        max_product = a.dot(n)
    
print(max_product)