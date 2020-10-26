import sys


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def first(n):
    nums = []
    for i in range(n):
        nums.append(i)
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

def first_generator(n):
    num = 0
    for i in range(n):
        yield i

print(sys.getsizeof(firstn(1000))) # 9024
print(sys.getsizeof(first(1000))) # 9024
print(sys.getsizeof(firstn_generator(1000))) # 88
print(sys.getsizeof(first_generator(1000))) # 88


# List comprehension vs generator

# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))