n = int(input('numero: '))
for _ in iter(int, 1):
    print(n, end=", ")
    n += 2.5
    if n > 1000:
        break
