import pika
import sys

from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')
    
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

for i in range(5):
    message = ' '.join(sys.argv[1:]) or input('Informe uma mensagem as lavanderias:')

    if(message != "Send"):
        channel.basic_publish(exchange='',
                            routing_key='hello',
                            body=message)
        print(" [x] Sent %r" % message)

        channel.basic_publish(exchange='pubsub', routing_key='', body=message)
    else:
        break
connection.close()