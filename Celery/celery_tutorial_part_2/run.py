from proj.tasks import add
import threading
from time import sleep


r = add.delay(19, 100)

def sleeper(r):
    while not r.ready():
        print('without result')
        sleep(1)
    print(r.get())



t_1 = threading.Thread(target=sleeper, args=(r,))
t_1.start()
# t_1.join()