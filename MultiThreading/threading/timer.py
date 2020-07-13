import threading, time

def f1():
    print(time.ctime())



def foo(data):
    # print(data + time.ctime())
    t1 = threading.Timer(10, f1)
    t1.start()
    return t1





data = 'To jest dana:'
# t1 = threading.Timer(1, f1, args=(data,))
# t1.start()
t = foo(data)

