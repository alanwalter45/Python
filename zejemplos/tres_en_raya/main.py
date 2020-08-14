from tablero import Tablero
from jugador import Jugador

if __name__ == '__main__':
    while True:
        print("MENU:\n"
              "1) Iniciar juego\n"
              "2) Ayuda\n"
              "3) Salir")
        opcion = int(input('opcion: '))
        if opcion == 1:
            nombre_jugador1 = input('Nombre del primer jugador: ')
            jugador1 = Jugador(nombre_jugador1)
            nombre_jugador2 = input('Nombre del segundo jugador: ')
            jugador2 = Jugador(nombre_jugador2)

            filas = 3
            columnas = 3
            tablero = Tablero(filas, columnas, jugador1, jugador2)
            print("Ingresa la posicion que desea rellenar:\n"
                  "1 2 3\n"
                  "4 5 6\n"
                  "7 8 9\n")
            opcion = int(input("opcion: "))
            break
        if opcion == 2:
            input("Bienvenido al apartado de ayuda:\n"
                  "Las fichas para el juego seran sorteadas al azar\n"
                  "Gana el jugador que pueda llenar 3 lugares continuos de forma diagonal,\n"
                  "horizontal o vertical.\n"
                  "----------------------\n"
                  "presione <Enter> para salir de la ayuda.")
        if opcion == 3:
            break
