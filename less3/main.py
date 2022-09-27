import threading

locker = threading.RLock()


def inc_value():
    print("Block threading")
    locker.acquire()
    print("Unblock threading")


t1 = threading.Thread(target=inc_value())
t2 = threading.Thread(target=inc_value())
t1.start()
t2.start()
