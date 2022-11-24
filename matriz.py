import pika as py
import sys, os

from pika.exchange_type import ExchangeType

# parametros para a conexao com o localhost.
connection_parameters =  os.environ.get('CLOUDAMQP_URL', 'amqps://sxhqckdt:ZidtJPJ9TH5DSpfCUPV_f8GLOJMqN0Qc@beaver.rmq.cloudamqp.com/sxhqckdt')
params = py.URLParameters(connection_parameters)
params.socket_timeout = 2
# conexao com BlockingConnection que cria uma camada bloqueante até que haja um retorno das mensagens.  
connection = py.BlockingConnection(params)

# conectar o canal
channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

# Antes de executar a matriz, deve executar as filiais:

# Abra vários terminais ou divida o terminal.

# [python .\{nome_do_arquivo.py}] pelo Command Prompt do console do Visual Studio Code. 

print("*** Verifique se as filiais estão conectadas para enviar mensagens pela matriz! ***")

#Assim, irão consumir o body do arquivo matriz.py simultaneamente.

# mensagem a ser enviada
for i in range(5):
    print("------------------------------------------")
    message = ' '.join(sys.argv[1:]) or input("Envie mensagens a rede de lavanderias: ")
    
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=message)
    print("\n [x] Sent %r" % message)
   
#canal que envia a mensagem
    channel.basic_publish(exchange='pubsub', routing_key='', body=message)
    
#encerrando a conexao
connection.close()