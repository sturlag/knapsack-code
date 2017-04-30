from knapsack import algorithm_A,Element
from knapsack_opt import opt


test1 = [Element(x,x) for x in [0.3, 0.4, 0.6]]
sol1 = 1.0

test2 = [Element(x,x) for x in [0.5,0.5]]
sol2 = 1.0

test3 = [Element(x,x) for x in [0.2,0.9,0.4,0.35]]
sol3 = 0.95


# print opt(test1)[1]
# print opt(test2)[1]
print opt(test3)[1]
