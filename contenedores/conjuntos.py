a = set([1, 2])
a.add(5)
print(a)

b = frozenset(a)
print(type(b))
