name = "alanwalter45"


def imprimir_nombre(name):
    name = "esteban"
    print(name)


imprimir_nombre(name)
print(name)


def imprimir_nombre2():
    global name
    name = "esteban"
    print(name)


imprimir_nombre2()
print(name)
