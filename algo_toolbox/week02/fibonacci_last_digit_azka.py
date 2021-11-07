# Problem Description
# Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 107.
# Output Format. Output the last digit of 𝐹𝑛.


def calc_fib(n):
    a,b = 0,1
    for i in range(2,n+1):
        a,b = b,(b%10+a%10)%10
    return b

n = int(input())
print(calc_fib(n))
