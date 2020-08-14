def serie(lista: list):
    count = 0
    while len(lista):
        elemento = lista[0]
        cantidad = lista.count(elemento)
        for _ in range(cantidad):
            lista.remove(elemento)
        count += 1
    return count

lista = [1, 1, 8, 8, 8, 8, 0, 0, 0, 2, 10, 10]
print(serie(lista))
