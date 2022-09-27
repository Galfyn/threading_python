
import time
import threading

cond = threading.Event()


def f1():
    while True:
        cond.wait()
        print("Get event!")


def f2():
    for i in range(100):
        if i % 10 == 0:
            cond.set()
        else:
            print(f"f1: {i}")
        time.sleep(0.2)


threading.Thread(target=f1).start()
threading.Thread(target=f2).start()
