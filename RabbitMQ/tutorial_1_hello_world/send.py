import pika

# establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# create a queue named 'hello'
channel.queue_declare(queue='hello') # deklaracja kolejki



channel.basic_publish(exchange='', # empty string as default exchange
                      routing_key='hello', # queue name needs to be specified in the routing_key
                      body='Hello world')

print('[x] send hello world message')


