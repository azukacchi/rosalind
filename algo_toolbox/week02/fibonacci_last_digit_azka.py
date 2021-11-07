# Problem Description
# Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 107.
# Output Format. Output the last digit of 𝐹𝑛.

num = [0,1]

def calc_fib(n):
    for i in range(2,n+1):
        num.append((num[i-1]%10+num[i-2]%10)%10)
    return num[n]

n = int(input())
print(calc_fib(n))