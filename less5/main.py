import random
import time
import threading
from threading import currentThread


def test(barrier):
    slp = random.randint(5, 10)
    time.sleep(slp)
    print(f"Thread [{currentThread().name}] started in ({time.ctime()})")

    barrier.wait()
    print(f"Thread [{currentThread().name}] overcame the barrier ({time.ctime()})")


bar = threading.Barrier(5)
for i in range(5):
    threading.Thread(target=test, args=(bar,), name=f"thr-{i}").start()
