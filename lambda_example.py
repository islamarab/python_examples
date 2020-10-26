add10 = lambda x: x + 10
print(add10(5))

# map
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

a = [1, 2, 3, 4, 5]
b = filter(lambda x: x%2==0, a)
print(list(b))
