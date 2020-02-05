from threading import Thread, Event
import numpy as np
from time import sleep

''' Przykład 1

evnt = Event()

def increase_by_one(array):
    print('Waiting for event')
    l = evnt.wait()
    print('increase by 1')
    for i in range(len(array)):
        array[i] += 1




if __name__ == "__main__":
    data = np.zeros((100000, 1))
    t = Thread(target=increase_by_one, args=(data,))
    t2 = Thread(target=increase_by_one, args=(data,))

    t.start()
    t2.start()

    for i in range(len(data)):
        data[i] += 1
    
    print('Data ready')
    evnt.set()

    t.join()
    t2.join()

    print(data[0])
    print(np.mean(data))

'''


   
    
evnt = Event()

def increase_by_one(array):
    while True:
        if evnt.is_set():
            print('time is over')
            break
        
        for i in range(len(array)):          
            array[i] += 1
        sleep(0.1)


if __name__ == "__main__":
    data = np.ones((10000, 1))
    t = Thread(target=increase_by_one, args=(data,))
    t.start()

    print('Going to sleep')
    sleep(10)
    print('Wake up')
    evnt.set()

    t.join()

    print(data[0])
    print(np.mean(data))