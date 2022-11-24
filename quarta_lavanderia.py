import pika as py

from pika.exchange_type import ExchangeType

#função para mensagem recebida, cada lavanderia tem uma numeração e nome
def on_message_received(ch, method, properties, body):
    print(f'04 - Lavanderia Bairro das Rosas - Nova mensagem recebida: {body}')
    
connection_parameters = py.ConnectionParameters('localhost')

connection = py.BlockingConnection(connection_parameters)

channel = connection.channel()

# realizar a conexão
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

# consumo da mensagem pela função on_message_received
channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print('Aguarde as mensagens da matriz!')

channel.start_consuming()