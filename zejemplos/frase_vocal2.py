"""Escriba un programa que pida una frase y una vocal y cambie todas\
las vocales de la frase por la vocal (Una forma de hacerlo es convertir la\
frase en una lista y hacer el cambio en la lista)."""

frase = input('frase: ')
vocal = input('vocal: ')

vocales = 'aeiou'
vocales_mayusculas = 'AEIOU'
frase_nueva = ''

for letra in frase:
    if letra in vocales:
        frase_nueva += vocal
    elif letra in vocales_mayusculas:
        frase_nueva += vocal.upper()
    else:
        frase_nueva += letra

print(frase_nueva)
