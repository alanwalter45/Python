from time import sleep

# generador
def cicloInfinito():
    count = 1
    while True:
        yield count
        count += 1

# iteracion
for i in cicloInfinito():
    print(i)
    sleep(1)
