from random import choice
from time import sleep
from flask import Flask
from flask_celery import make_celery
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['CELERY_BROKER_URL']= 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'db+postgresql://postgres:!QAZ2wsx@localhost/sandbox'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:!QAZ2wsx@localhost/sandbox'

# dodane bo było ostrzeżenie
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

celery = make_celery(app)

db = SQLAlchemy(app)

class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.String(50))

@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'Request was sent'

@app.route('/insertdata')
def insert_data():
    insert.delay()

    return 'I sent the data to DataBase !!!!'


@celery.task(name='celery_example.reverse')
def reverse(string):
    return string[::-1]

@celery.task(name='celery_example.insert')
def insert():
    for _ in range(500):
        data = ''.join(choice('ABCDE') for _ in range(5))
        result = Results()
        result.data = data
        db.session.add(result)
    sleep(10)
    db.session.commit()


if __name__ == '__main__':
   app.run(debug=True)

