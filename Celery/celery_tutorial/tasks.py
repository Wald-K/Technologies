from celery import Celery
from time import sleep

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='db+postgresql://postgres:Test@720318@localhost/sandbox')

@app.task
def add(x, y):
    sleep(10)
    return x + y




