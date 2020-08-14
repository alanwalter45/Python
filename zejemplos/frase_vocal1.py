"""Escriba un programa que pida una frase y una vocal y cambie todas\
las vocales de la frase por la vocal (Una forma de hacerlo es convertir la\
frase en una lista y hacer el cambio en la lista)."""

frase = input('frase: ')
vocales = 'aeiou'

while True:
    vocal = input('vocal: ')
    if len(vocal) == 1 and vocal in vocales:
        break
    else:
        print('<por favor ingrese una vocal>')

for item in vocales:
    if item != vocal:
        cantidad = frase.count(item)
        frase = frase.replace(item, vocal, cantidad)
print(frase)
