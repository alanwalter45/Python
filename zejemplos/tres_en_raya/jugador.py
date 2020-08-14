class Jugador:
    def __init__(self, nombre_jugador):
        self.nombre_jugador = nombre_jugador
        self.mi_ficha = ''

    @property
    def ficha(self):
        return self.mi_ficha

    @ficha.setter
    def ficha(self, value):
        self.mi_ficha = value
