# Problem Introduction
# Now, we would like to find the last digit of a partial sum of Fibonacci numbers:
# 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.
# Problem Description
# Task. Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛,
# find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 +
# · · · + 𝐹𝑛.
# Input Format. The input consists of two non-negative integers 𝑚 and 𝑛 separated by a space.
# Constraints. 0 ≤ 𝑚 ≤ 𝑛 ≤ 1018.
# Output Format. Output the last digit of 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.

num = [0,1]

def calc_fib(n):
    for i in range(2,n+1):
        num.append((num[i-1]%10+num[i-2]%10)%10)
    return num

def fibonacci_sum(n,m):
    return sum(calc_fib(n)[m:])%10

m,n = map(int, input().split())
print(fibonacci_sum(n,m))