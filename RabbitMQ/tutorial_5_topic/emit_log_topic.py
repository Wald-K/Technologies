import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# deklaracja exchanga
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# severity - to będzie routing_key decydujący do której kolejki trafi wiadomość
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)

print(f" [x] Sent {routing_key}:{message}")
connection.close()


