fecha = int(input('intr. la fecha conformada por 8 numeros: '))
anho = fecha % 10000
fecha = fecha // 10000
mes = fecha % 100
fecha = fecha // 100
dia = fecha % 100
print(f"dia: {dia} mes:{mes} anho:{anho}")
