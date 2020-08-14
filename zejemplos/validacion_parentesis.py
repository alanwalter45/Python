""" Escribir una clase en python para encontrar la validezde una cadena de parentesis
los parentesis deben aparecer en el orden correcto """

simbolos = {
    'parentesis': ['(', ')'],
    'corchetes': ['[', ']'],
    'llaves': ['{', '}']
}
cadena = "{{{}}}"
exito = True
for key, value in simbolos.items():
    encontrados = 0
    encontrados += cadena.count(value[0])
    encontrados -= cadena.count(value[1])
    if encontrados != 0:
        exito = False
        print(f'(invalido) - falta completar {key}')

if exito:
    print('valido')
