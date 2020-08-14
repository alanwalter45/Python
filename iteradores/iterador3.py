class iterador:

    def __init__(self):
        self.lista = [1, 2, 3, 4, 5]
        self.len = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.len == len(self.lista) - 1:
            raise StopIteration
        self.len += 1
        return self.lista[self.len]


i = iterador()
print(next(i), next(i))
for item in i:
    print(item)
