# Problem Introduction
# The goal in this problem is to find the last digit of a sum of the first 𝑛 Fibonacci numbers.
# Problem Description
# Task. Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 1018.
# Output Format. Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.

def calc_fib(n):
    num = [0,1]
    for i in range(2,n+1):
        num.append((num[i-1]%10+num[i-2]%10)%10)
    return sum(num)

def fibonacci_sum(n):
    return calc_fib(n)%10

n = int(input())
print(fibonacci_sum(n))