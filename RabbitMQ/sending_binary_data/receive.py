import pika
from message import MessageDeserializer

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello') # deklaracja kolejki


def callback(ch, method, properties, body): # funkcja callbacku służąca do odbioru informacji z kolejki

    message = MessageDeserializer(body).deserialize_data()


    print(f'[x] received {message}')


channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print('[*] waiting for a new message')

channel.start_consuming()