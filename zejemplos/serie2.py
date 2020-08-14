def Series(lista):
    serie=set(lista)
    print(serie)
    print(len(serie))

def pro(lista):
    suma=0
    for i in lista:
        suma += i
    promedio=suma/len(lista)
    return promedio,suma

#main
lista=[1,1,8,8,8,8,0,0,0,2,10,10]
Series(lista)
promedio,suma=pro(lista)
print(promedio)
print(suma)