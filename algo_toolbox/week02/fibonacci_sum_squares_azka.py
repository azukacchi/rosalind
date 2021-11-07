# Problem Description
# Task. Compute the last digit of 𝐹02 + 𝐹12 + · · · + 𝐹𝑛2.
# Input Format. Integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 1018.
# Output Format. The last digit of 𝐹02 + 𝐹12 + · · · + 𝐹𝑛2.

def pisano_period(m):
    a,b,c=0,1,1
    for i in range(m*m):
        c = (a+b)%m
        a = b
        b = c
        if (a==0)&(b==1):
            return i+1
    return c

def calc_fib(n):
    a,b = 0,1
    for i in range(2,n+1):
        a,b = b,(b%10+a%10)%10
    return b

def get_fibonacci_huge(n,m=60):
    rem = n%pisano_period(m)
    return calc_fib(rem)%m

def fibonacci_sum(n):
    fib_n = get_fibonacci_huge(n)
    fib_n_plus_one = get_fibonacci_huge(n+1)
    return (fib_n*fib_n_plus_one)%10

n = int(input())
print(fibonacci_sum(n))