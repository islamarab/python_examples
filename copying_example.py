# Bad way
list_a = [1, 2, 3, 4, 5]
list_b = list_a

list_a[0] = -10
print(list_a)
print(list_b)

# Recommended way
import copy
list_a = [1, 2, 3, 4, 5]
list_b = copy.copy(list_a)
# shallow copies (also possible)
# list_b = list(list_a)
# list_b = list_a[:]
# list_b = list_a.copy()

list_b[0] = -10
print(list_a)
print(list_b)

# 2D array
import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.deepcopy(list_a)
# list_b = list(list_a)
# list_b = list_a[:]
# list_b = list_a.copy()

list_a[0][0]= -10
print(list_a)
print(list_b)