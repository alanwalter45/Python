from time import sleep


def cicloInfinito():
    count = 1
    while True:
        yield count
        count += 1


for i in cicloInfinito():
    print(i)
    sleep(1)
