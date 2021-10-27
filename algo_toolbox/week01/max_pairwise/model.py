n = int(input())
a = [int(x) for x in input().split()]

def maxPairwiseProduct(a):
    index_1, index_2 = 0,0

    for i in range(n):
        if a[i] > a[index_1]:
            index_1 = i

    if index_1 == 0:
        index_2 = 1
    else: index_2 = 0

    for i in range(n):
        if i != index_1 and a[i] > a[index_2]:
            index_2 = i
    return a[index_1]*a[index_2]

print(maxPairwiseProduct(a))