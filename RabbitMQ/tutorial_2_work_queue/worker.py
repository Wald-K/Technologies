import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) # deklaracja kolejki, durable - gdy rabbit zawiesi się
                                                        # i ponownie wstanie, to odtworzy kolejkę

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body): # funkcja callbacku służąca do odbioru informacji z kolejki
    print(f'[x] received {body}')
    time.sleep(body.count(b'.'))
    print('[x] done')
    ch.basic_ack(delivery_tag=method.delivery_tag) # gdy usługa worker umrze, to dzięki braku ACK
                                                    # następny przejmie zadanie


channel.basic_qos(prefetch_count=1) # aby rozdzielać zadania do wolnego workera a nie po kolei
                                    # czyli nie dawaj więcej niż 1 zadania do workera
                                    # - więc dopóki nie wykona, to nie otrzyma nowego

channel.basic_consume(queue='task_queue',
                      on_message_callback=callback)

print('[*] waiting for a new message')

channel.start_consuming()