from threading import Thread
import time
from random import randint


class MiThread(Thread):

    def __init__(self, name, duration):
        Thread .__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        print("Thread '" + self.name + "' iniciado")
        time.sleep(self.duration)
        print("Thread '" + self.name + "' finalizado")


t1 = MiThread("t#1", randint(1, 10))
t2 = MiThread("t#2", randint(1, 10))
t3 = MiThread("t#3", randint(1, 10))

t1.start()
t2.start()
t3.start()
