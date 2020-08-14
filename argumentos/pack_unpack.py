def imp(*list):
    print(list)


def imp2(a, b, c):
    print(a, b, c)


a = {1, 2, 3, 4, 5, 5, 4, 3}
imp(a)
imp(1,2,3,4)
b = (1, 2, 3)
imp2(*b)
