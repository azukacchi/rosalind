import numpy as np
import itertools
import os
# import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'rosalind_iprb.txt')) as f:
    a = f.read()

# start = time.time()
# k,m,n = 2,2,2
(k,m,n) = (int(i) for i in a.split())

GG = np.array([0,0])
Gg = np.array([0,1])
gg = np.array([1,1])
pools = ['GG','Gg','gg']

repeat_times = {'GG':k, 'Gg':m, 'gg':n} 

result = [i for i in pools for j in range(repeat_times[i])]
# print(result)

pools = np.empty((1,2))
for i in result:
    if i == 'GG':
        pools = np.vstack((pools,np.array([0,0])))
    elif i == 'Gg':
        pools = np.vstack((pools,np.array([0,1])))
    else:
        pools = np.vstack((pools,np.array([1,1])))
pools = pools[1:]
# print(pools)
# print(len(pools))

result = np.empty((2,2))
pools_comb = list(itertools.combinations(pools, 2))
# print('pools_comb :\n',pools_comb)
for i in pools_comb:
    result = np.vstack((result, np.multiply.outer(i[0],i[1])))
    
result = result[2:]
print(1-result.reshape(1,-1).sum()/result.reshape(1,-1).shape[1])
# print(f'Time: {time.time() - start}')
