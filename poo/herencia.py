class Plastico:
    def __init__(self, color):
        self.color = color.capitalize()

    def verDetalle(self):
        return f"Plastico COLOR {self.color}"


class Vaso(Plastico):
    def __init__(self, logo, color):
        super().__init__(color)
        self.logo = logo


v = Vaso('.::V::.', 'azul')
print(v.verDetalle())
