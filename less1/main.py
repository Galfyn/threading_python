import time
import threading


def get_data(data, value):
    for _ in range(value):
        print(f"[{threading.currentThread().name}] - {data} ")
        time.sleep(1)


thr_lst = []

for i in range(3):
    thr = threading.Thread(target=get_data, args=(str(time.time()), i,), name=f"thr-{i}")
    thr_lst.append(thr)
    thr.start()


for i in thr_lst:
    i.join()

print("Finish")
