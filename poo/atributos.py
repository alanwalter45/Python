class Principal:
    nombre = "alan"

    def __init__(self, direccion):
        self.direccion = direccion


p = Principal("Calle reg. carabineros")
print(p.nombre.upper(), p.direccion)

Principal.nombre = "andrea"
p = Principal("Av. Jaime Mendoza")
print(p.nombre.upper(), p.direccion)
