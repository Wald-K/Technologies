import sys
import pika

#establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# create a queue named 'task_queue'
channel.queue_declare(queue='task_queue', durable=True) # deklaracja kolejki urable - gdy rabbit zawiesi się
                                                        # i ponownie wstanie, to odtworzy kolejkę


message = ' '.join(sys.argv[1:]) or 'Hello world'

channel.basic_publish(exchange='', # empty string as default exchange
                      routing_key='hello', # queue name needs to be specified in the routing_key
                      body=message,
                      properties=pika.BasicProperties(
                            delivery_mode=2,  # gdy się rabbit zawiesi, to odtworzy tę wiadomość
                      ))

print(f'[x] Send: {message}')

