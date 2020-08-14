# Escriba un programa que pida una frase y una vocal y cambie todas las
# vocales de la frase por la vocal (una forma de hacerlo es convertir la frase
# en una lista y hacer el cambio en la lista.

frase = input('frase: ')
vocal = input('vocal de reemplazo: ')

for i in frase:
    if i in ['a', 'e', 'i', 'o', 'u']:
        frase = frase.replace(i, vocal)
print(frase)
