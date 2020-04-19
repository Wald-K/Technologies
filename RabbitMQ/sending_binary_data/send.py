import pika
from message import BearingsMessageSerializer

bearings = [10.5, 40.6, 247.9]

data = BearingsMessageSerializer().serialize_data(bearings)


# establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# create a queue named 'hello'
channel.queue_declare(queue='hello') # deklaracja kolejki



channel.basic_publish(exchange='', # empty string as default exchange
                      routing_key='hello', # queue name needs to be specified in the routing_key
                      body=data)

print('[x] send hello world message')


