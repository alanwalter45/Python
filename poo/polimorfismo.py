class Animal:
    def avanzar(self):
        print('avance base.')


class Perro(Animal):
    def avanzar(self):
        print('4 patas')


class Perico(Animal):
    def avanzar(self):
        print('2 patas')


class OtraClase:
    def otro_metodo(self):
        print('otro metodo...')


def mover(*animales):
    for animal in animales:
        if isinstance(animal, Animal):
            animal.avanzar()


perro = Perro()
perico = Perico()
otra_clase = OtraClase()

mover(perro, perico, otra_clase)
