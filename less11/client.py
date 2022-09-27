
import time
from multiprocessing.managers import BaseManager

BaseManager.register("get")
manager = BaseManager(address=("127.0.0.1", 4443), authkey=b"abc")
manager.connect()
print('client connected')

res = manager.get()
print('result:', res)

