import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello') # deklaracja kolejki


def callback(ch, method, properties, body): # funkcja callbacku służąca do odbioru informacji z kolejki
    print(f'[x] received {body}')


channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print('[*] waiting for a new message')

channel.start_consuming()