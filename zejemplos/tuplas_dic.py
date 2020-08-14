def tuplas_a_diccionario(l):
    dicc = dict()
    for i in l:
        if i[0] in dicc:
            dicc[i[0]] += [i[1]]
        else:
            dicc[i[0]] = [i[1]]
    return dicc


lista = [('a', 'alan'), ('a', 'walter'),
         ('b', 'raul'), ('a', '45'),
         ('b', 'gil'), ('a', '.'),
         ('b', '66'), ('a', 20)]
print(tuplas_a_diccionario(lista))
