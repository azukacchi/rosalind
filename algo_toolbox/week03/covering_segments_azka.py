# Problem Description
# Task. Given a set of 𝑛 segments {[𝑎0, 𝑏0], [𝑎1, 𝑏1], . . . , [𝑎𝑛−1, 𝑏𝑛−1]} with integer coordinates on a line, find
# the minimum number 𝑚 of points such that each segment contains at least one point. That is, find a
# set of integers 𝑋 of the minimum size such that for any segment [𝑎𝑖, 𝑏𝑖] there is a point 𝑥 ∈ 𝑋 such
# that 𝑎𝑖 ≤ 𝑥 ≤ 𝑏𝑖.
# Input Format. The first line of the input contains the number 𝑛 of segments. Each of the following 𝑛 lines
# contains two integers 𝑎𝑖 and 𝑏𝑖 (separated by a space) defining the coordinates of endpoints of the 𝑖-th
# segment.
# Constraints. 1 ≤ 𝑛 ≤ 100; 0 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛

import numpy as np
s = '''3
100000000 1000000000
200000000 50000000
30000000 60000000'''
# s = '''4
# 4 7
# 1 3
# 2 5
# 5 6'''
pairs = s.split('\n')[1:]
pair = [i.split() for i in pairs]
min_max = []
for i in pair:
    min_max.append([int(j) for j in i])
    
min_max = np.array(min_max).T

sum_all = min_max.sum()
segment = []

while sum_all > 0:
    min_val = (min_max[1][min_max[1]>0]).min()
    segment.append(min_val)
    min_max = np.where((min_max[1]<=(min_max[1][min_max[1]>0]).min())|(min_max[0]<=(min_max[1][min_max[1]>0]).min()),0,min_max)
    sum_all = min_max.sum()

print(len(segment))
print(*segment)

