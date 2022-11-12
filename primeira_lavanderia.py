import pika

from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f'01 - Lavanderia 2 de Julho - Nova menssagem recebida: {body}')
    
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print(' A Matriz enviou uma menssagem.')

channel.start_consuming()
    