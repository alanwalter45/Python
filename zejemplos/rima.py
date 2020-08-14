palabra = input('escriba la primera palabra: ')
palabra2 = input('escriba la segunda palabra: ')

if palabra[-3:] == palabra2[-3:]:
    print('rima')
elif palabra[-2:] == palabra2[-2:]:
    print('rima un poco')
else:
    print('no riman')
