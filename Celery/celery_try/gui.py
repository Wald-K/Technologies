from tkinter import *
from tasks import long_task
import threading
import time
import random

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

accum = 0
lock = threading.Lock()

# def long_task_function(n):
#     for i in range(n):
#         time.sleep(i)
#         print(f"email send nr {i}")
#     return ("all email sent")
#
# def clicked_with_celery():
#     print('Now clicked')
#     lbl.configure(text="Button was clicked !!")
#     x = long_task.delay(5)
#     z = x.get()
#     lbl.configure(text="Result is "+ z)



# def long_task_function_for_threading(n, label_result):
#     myname = threading.currentThread().getName()
#     for i in range(n):
#         time.sleep(i)
#         print(f"{myname} send: email send nr {i}")
#     label_result.configure(text=f'{n}: {myname}')

def task_function_for_threading(n, label_result):
    myname = threading.currentThread().getName()
    global accum

    # lock.acquire()
    buff = accum

    for i in range(n):
        time.sleep(i)
        print(f"{myname} send: email send nr {i}")

    accum = buff + 1
    # lock.release()
    # label_result.configure(text=f'{n}: {myname}')
    print(f'thread {myname} finished. Global={accum}')


def clicked_with_threading(label):
    print('Now clicked')
    for i in range(3):
        param = random.randint(3, 5)
        # param = 4
        t = threading.Thread(target=task_function_for_threading, args=(param, label))
        t.start()




# btn = Button(window, text="Click Me", command=clicked_with_celery)
btn = Button(window, text="Click Me", command=lambda: clicked_with_threading(lbl))



btn.grid(column=1, row=0)

txt = Entry(window, width=10)
txt.grid(column=0, row=1)

window.mainloop()