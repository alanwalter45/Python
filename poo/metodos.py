class Principal:
    """ Demostrando los metodos. """

    def __init__(self):
        print('inicializador...')

    def mensaje(self):
        print('mensaje enviado correctamente!')

    @staticmethod
    def email():
        print('verificando si existe un email registrado.')


Principal().mensaje()
Principal.email()
Principal().email()
