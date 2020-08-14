from difflib import ndiff

contenido1 = open('t1.txt').readlines()
contenido2 = open('t2.txt').readlines()

print("".join(ndiff(contenido1, contenido2)))
