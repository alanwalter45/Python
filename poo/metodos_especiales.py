class Otro:
    def __str__(self):
        return "Otra manera de mostrar"

    def __repr__(self):
        return "x.Y.z"

    def __bool__(self):
        return False

    def __len__(self):
        return 10


o = Otro()
print(":::"+str(o))
print(o)
print(repr(o))
if bool(o) == False:
    print('es falso')

print(len(o))
