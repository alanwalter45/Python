"""Implementando un calculadora."""

from operaciones import add, sub, mul, div


while True:
    print("""Menu
    ---------------------
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Salir
    ----------------------""")
    try:
        opcion = int(input("Opcion: "))
        if opcion == 1:
            print('operacion: sumar A+B')
            a = float(input('A: '))
            b = float(input('B: '))
            print("Resultado: ", add(a, b))
        if opcion == 2:
            print('operacion: restar A-B')
            a = float(input('A: '))
            b = float(input('B: '))
            print("Resultado: ", sub(a, b))
        if opcion == 3:
            print('operacion: multiplicar A*B')
            a = float(input('A: '))
            b = float(input('B: '))
            print("Resultado: ", mul(a, b))
        if opcion == 4:
            print('operacion: sumar A/B')
            a = float(input('A: '))
            b = float(input('B: '))
            print("Resultado: ", div(a, b))
        if opcion == 5:
            break
    except Exception as ex:
        print('Mil disculpas el programa tuvo que cerrar porque ocurrio un error.')
    finally:
        input("<Presione [Enter] para continuar>")
