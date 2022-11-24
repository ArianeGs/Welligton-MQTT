import os, pika as py 

from pika.exchange_type import ExchangeType

#função para mensagem recebida, cada lavanderia tem uma numeração e nome
def on_message_received(ch, method, properties, body):
    print(f'02 - Lavanderia Caminho das Aves - Nova mensagem recebida: {body}')
    
#conexão com o cloudAMQP
connection_parameters =  os.environ.get('CLOUDAMQP_URL', 'amqps://sxhqckdt:ZidtJPJ9TH5DSpfCUPV_f8GLOJMqN0Qc@beaver.rmq.cloudamqp.com/sxhqckdt')
params = py.URLParameters(connection_parameters)

#Conexão Bloqueante
connection = py.BlockingConnection(params)
channel = connection.channel()

# realizar a conexão
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print('Aguarde as mensagens da matriz!')

channel.start_consuming()