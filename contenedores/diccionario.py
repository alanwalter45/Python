estados_civiles = ('soltero', 'casado', 'divorciado')
info = {"nombre": "alan", "estado_civil": estados_civiles[0], "felicidad": 100}

for i, j in info.items():
    print("{}:{}".format(i, j))
