
import time
from multiprocessing.managers import BaseManager


def get_time():
    return time.time()


BaseManager.register("get", callable=get_time())
manager = BaseManager(address=('', 4443), authkey=b'abc')
server = manager.get_server()
print('server started')
server.serve_forever()
