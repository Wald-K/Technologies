import sys
import pika

#establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# create a queue named 'hello'
channel.queue_declare(queue='hello') # deklaracja kolejki


message = ' '.join(sys.argv[1:]) or 'Hello world'

channel.basic_publish(exchange='', # empty string as default exchange
                      routing_key='hello', # queue name needs to be specified in the routing_key
                      body=message)

print(f'[x] Send: {message}')

