# Problem Description
# Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
# Input Format. The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space).
# Constraints. 1 ≤ 𝑛 ≤ 1018, 2 ≤ 𝑚 ≤ 103.
# Output Format. Output 𝐹𝑛 mod 𝑚.

m,n = map(int,input().split())

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
    num = [0,1]
    for i in range(2,n+1):
        num.append(num[i-1]+num[i-2])
    # print(num[1:])
    return num[n]

def get_fibonacci_huge(n,m):
    rem = n%pisano_period(m)
    return calc_fib(rem)%m
    
print(get_fibonacci_huge(m,n))