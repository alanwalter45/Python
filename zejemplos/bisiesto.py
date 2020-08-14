def bisiesto(anho):
    if anho%4==0:
        if anho%100==0:
            if anho%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def bisiesto2(valor):
    if valor%400==0:
        return True
    elif valor%4==0 and valor%100!=0:
        return True
    else:
        return False

lista1 = []
lista2 = []
for i in range(1582,2021):
    if bisiesto(i)==True:
        lista1.append(i)
    if bisiesto2(i)==True:
        lista2.append(i)

if lista1==lista2:
    print("listas iguales")
