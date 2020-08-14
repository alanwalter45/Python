c0 = int(input('c0: '))
if c0 > 1:
    pasos = 0
    while c0 != 1:
        if c0 % 2 != 0:
            c0 = 3*c0+1
        else:
            c0 = c0 // 2
        print(c0)
        pasos += 1
else:
    print("valor de c0 incorrecto")
print("pasos = ",pasos)