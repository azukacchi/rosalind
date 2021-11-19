# Problem Description
# Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
# Input Format. The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
# The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the
# value and the weight of 𝑖-th item, respectively.
# Constraints. 1 ≤ 𝑛 ≤ 10^3, 0 ≤ 𝑊 ≤ 2 · 10^6; 0 ≤ 𝑣𝑖 ≤ 2 · 10^6, 0 < 𝑤𝑖 ≤ 2 · 10^6 for all 1 ≤ 𝑖 ≤ 𝑛. All the
# numbers are integers.
# Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute
# value of the difference between the answer of your program and the optimal value should be at most
# 10^−3. To ensure this, output your answer with at least four digits after the decimal point (otherwise
# your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

from collections import defaultdict
text = '''4 60
60 20
60 20
100 50
120 30'''
# text = '''1 10
# 500 30'''
# text = '''3 200000
# 60 20
# 100 50
# 120 30'''

(n, w) = (int(i) for i in text.strip().split()[:2])

items_weight = defaultdict()
items_value = defaultdict()

item_count = 0
for i in text.strip().split('\n')[1:]:
    (item_val,item_weight) = (int(y) for y in i.split())
    items_weight[item_count] = item_weight
    items_value[item_count] = round(item_val/item_weight,4) 
    item_count += 1

items_value_sorted = dict(sorted(items_value.items(), key=lambda item: item[1], reverse=True))

vals = 0
for item in items_value_sorted.keys():
    if w>0:
        if items_weight[item] <= w:
            vals += items_value_sorted[item]*items_weight[item]
            w -= items_weight[item]
        else:
            vals += items_value_sorted[item]*w
            w -= w

print(vals)
        