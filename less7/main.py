
import time
import multiprocessing

'''
class Process(multiprocessing.Process):
    def run(self):
        print("Hi")


pr = Process()
pr.start()
'''


def test():
    for _ in range(3):
        print(f"{multiprocessing.current_process().name} - {time.ctime()}")
        time.sleep(1)


pr = multiprocessing.Process(target=test(), name="prc-1")
pr.start()

print(f"{pr.pid} is {pr.is_alive()}")

time.sleep(10)
pr.terminate()
