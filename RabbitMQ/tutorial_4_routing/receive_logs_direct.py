import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# exclusive=True oznacza, ze gdy consumer bedzie zamkniety, to kolejka razem z nim
# queue='' oznacza losowa nazwe kolejki
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue # tu odbieramy losową nazwe kolejki

severities = sys.argv[1:]

# gdy nie określono gdzie routing_key dla bindowania
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

#powiazanie exchange z kolejką - w pętli, ponieważ może być kilka parametrów routing_key dla tego połączenia
for severity in severities:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] {method}: {body}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
