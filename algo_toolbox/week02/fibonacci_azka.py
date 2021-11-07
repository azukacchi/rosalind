# Problem Description
# Task. Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛.
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 45.
# Output Format. Output 𝐹𝑛.

num = [0,1]

def calc_fib(n):
    for i in range(2,n+1):
        num.append(num[i-1]+num[i-2])
    # print(num[1:])
    return num[n]

n = int(input())
print(calc_fib(n))
