import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello') # deklaracja kolejki


def callback(ch, method, properties, body): # funkcja callbacku służąca do odbioru informacji z kolejki
    print(f'[x] received {body}')
    time.sleep(body.count(b'.'))
    print('[x] done')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1) # aby rozdzielać zadania do wolnego workera a nie po kolei


channel.basic_consume(queue='hello',
                      on_message_callback=callback)

print('[*] waiting for a new message')

channel.start_consuming()