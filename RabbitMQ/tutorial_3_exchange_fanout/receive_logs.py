import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

# exclusive=True oznacza, ze gdy consumer bedzie zamkniety, to kolejka razem z nim
# queue='' oznacza losowa nazwe kolejki
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue # tu odbieramy losową nazwe kolejki

#powiazanie exchange z kolejka
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] {body}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

