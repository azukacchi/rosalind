# Problem Description
# Task. The goal in this problem is to find the minimum number of coins needed to change the input value
# (an integer) into coins with denominations 1, 5, and 10.
# Input Format. The input consists of a single integer 𝑚.
# Constraints. 1 ≤ 𝑚 ≤ 10^3.
# Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚

from math import floor
coins = [10,5,1]
total_coins = dict(zip(coins,[0,0,0]))
m = 1000

for i in coins:
    if floor(m/i)>0:
        total_coins[i] += floor(m/i)
        m -= total_coins[i]*i

print(sum(total_coins.values()))
    
