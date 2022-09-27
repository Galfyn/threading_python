
import time
import random
from multiprocessing import Process, Event, Condition

cond = Event()


def f1():
    while True:
        cond.wait()
        print("Get event")


def f2():
    for i in range(100):
        if i % 10 == 0 and i != 0:
            cond.set()
        else:
            print(f"f2: {i}")
        time.sleep(0.5)


Process(target=f1).start()
Process(target=f2).start()
