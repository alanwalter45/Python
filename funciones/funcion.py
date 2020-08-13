def suma(a, b):
    return a + b


resultado = suma(5, 3)
print(resultado)

resultado = suma(b=10, a=3)
print(resultado)

valores = (5, 3)
resultado = suma(*valores)
print(resultado)

valores = {'a': 15, 'b': 3}
resultado = suma(**valores)
print(resultado)


def resta(a, *, b):
    return a - b


print(resta(5, b=20))
