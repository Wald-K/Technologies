from celery import Celery
import time

app = Celery('task', broker='amqp://localhost//', backend='db+postgresql://postgres:@localhost/sandbox')


@app.task
def reverse(string):
    time.sleep(30)
    return string[::-1]

