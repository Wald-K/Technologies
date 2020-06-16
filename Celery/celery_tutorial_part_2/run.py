from proj.tasks import add, get_man_name
import threading
from time import sleep
from proj.library import Man

'''
r = add.delay(19, 100)

def sleeper(r):
    while not r.ready():
        print('without result')
        sleep(1)
    print(r.get())



t_1 = threading.Thread(target=sleeper, args=(r,))
t_1.start()
'''

name = 'Wald'
r = get_man_name.delay(name)
while not r.ready():
    print('without result')
    sleep(1)
print(r.get().name)

