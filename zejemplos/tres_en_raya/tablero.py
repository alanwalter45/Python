from random import random


class Tablero:
    def __init__(self, filas, columnas, jugador1, jugador2):
        self.filas = filas
        self.columnas = columnas
        self.jugador1 = jugador1
        fichas = self.sortear_fichas()
        self.jugador1.ficha = fichas[0]
        self.jugador2 = jugador2
        self.jugador2.ficha = fichas[1]
        self.tabla = list()

    def sortear_fichas(self):
        if random() <= 0.5:
            return ('X', '0')
        else:
            return ('0', 'X')

    def dibujar_tablero(self):
        for _ in range(self.filas):
            fila = []
            for _ in range(self.columnas):
                fila.append('*')
            self.tabla.append(fila)
        self.mostrar_tablero()

    def mostrar_tablero(self):
        for i in self.tabla:
            print(*i)

    def modificar_casilla(self, ficha, posicion):
        if posicion >= 1 and posicion <= 3:
            self.tabla[0][posicion-1] = ficha
        elif posicion >= 4 and posicion <= 6:
            self.tabla[1][posicion-3] = ficha
        elif posicion >= 7 and posicion <= 9:
            self.tabla[1][posicion-6] = ficha

    def es_jugada_ganadora(self):
        exito = False
        if self.tabla[0][0] == self.tabla[0][1] == self.tabla[0][2]:
            exito = True
        elif self.tabla[1][0] == self.tabla[1][1] == self.tabla[1][2]:
            exito = True
        elif self.tabla[2][0] == self.tabla[2][1] == self.tabla[2][2]:
            exito = True
        elif self.tabla[0][0] == self.tabla[1][1] == self.tabla[2][2]:
            exito = True
        elif self.tabla[2][0] == self.tabla[1][1] == self.tabla[0][2]:
            exito = True
        elif self.tabla[0][0] == self.tabla[1][0] == self.tabla[2][0]:
            exito = True
        elif self.tabla[0][1] == self.tabla[1][1] == self.tabla[2][1]:
            exito = True
        elif self.tabla[2][0] == self.tabla[1][2] == self.tabla[2][2]:
            exito = True
        return exito
