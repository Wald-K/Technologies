import threading

loops_count = 10_000
total_value = 0

lock = threading.Lock()
lock1 = threading.Lock()

def add_10():
    global total_value
    lock.acquire()
    for i in range(loops_count):
        total_value += 10
    lock.release()

def substract_3():
    global total_value
    lock.acquire()
    for i in range(loops_count):
        total_value -= 3
    lock.release()

def substract_7():
    global total_value
    lock.acquire()
    for i in range(loops_count):
        total_value -= 7
    lock.release()

if __name__ == '__main__':

    good = 0
    bad = 0

    for i in range(1000):

        t_1 = threading.Thread(target = add_10)
        t_2 = threading.Thread(target = substract_3)
        t_3 = threading.Thread(target = substract_7)

        t_1.start()
        t_2.start()
        t_3.start()

        t_1.join()
        t_2.join()
        t_3.join()

        if total_value == 0:
            good += 1
        else:
            bad += 1
        total_value = 0

    print(f'Dobrze {good}, Źle {bad}')