class Persona:
    hambre = 3
    @classmethod
    def comer(cls):
        cls.hambre = 15

class Hombre(Persona):
    pass

class Mujer(Persona):
    pass

#region aqui
""" Persona.hambre = 10

jose = Hombre()
jose.comer()
print(jose.hambre)

mauricio = Hombre()
#mauricio.comer()
print(mauricio.hambre) """

#endregion

Persona.comer()
print(Persona.hambre)

p = Hombre()
print(p.hambre)