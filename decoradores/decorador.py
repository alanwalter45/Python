import time as time00


def log(fun):
    count = 0
    time = time00.time()

    def registrar(a, b):
        print("task{}@{}".format(count, time))
        return fun(a, b)
    return registrar


@log
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b


print(suma(4, 5))

print(log(resta)(100,10))

