from __future__ import absolute_import, unicode_literals

from .celery import app
from time import sleep

from .library import Man


@app.task
def add(x, y):
    sleep(10)
    return x + y

@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def get_man_name(name):
    m = Man('Wald')
    sleep(10)
    return m