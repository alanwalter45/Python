def generadora():
    contador = 0
    while True:
        contador += 1
        yield contador

def generadora2():
    lista = [1,2,3,4,5]
    for item in lista:
        yield item
