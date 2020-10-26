from itertools import product, permutations, combinations, \
    combinations_with_replacement, accumulate, groupby
import operator

a = [1, 2, 3]
# b = [3, 4]
prod = product(a, a)
print("product", list(prod))

perm = permutations(a, 2)
print("permutations", list(perm))

comb = combinations(a, 2)
print("combinations", list(comb))

comb_r = combinations_with_replacement(a, 2)
print("combinations_with_replacement", list(comb_r))

acc = accumulate(a, func=operator.mul)
print("a", a)
print("accumulate", list(acc))

group_by = groupby(a, key=lambda x:x>2)
print("groupby")
for key, value in group_by:
    print(key, list(value))