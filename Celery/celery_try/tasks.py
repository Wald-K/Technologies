from celery import Celery
import time

app = Celery('tasks', broker='amqp://localhost//', backend='db+postgresql://postgres:!QAZ2wsx@localhost/sandbox')

@app.task
def reverse(string):
    return string[::-1]


@app.task
def long_task(n):
    for i in range(n):
        time.sleep(i)
        print(f"email send nr {i}")
    return ("all email sent")

