# Problem Description
# Task. Given two integers 𝑎 and 𝑏, find their greatest common divisor.
# Input Format. The two integers 𝑎, 𝑏 are given in the same line separated by space.
# Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2 · 109.
# Output Format. Output GCD(𝑎, 𝑏).

# a = 280851538
# b = 11803010
a,b = map(int,input().split())

def gcd(a,b):
    (min_num, max_num) = (i for i in sorted([a,b]))
    while min_num>1:
        if max_num%min_num>0:
            max_num,min_num = min_num,max_num%min_num
        else: break
    return min_num

print(gcd(a,b))