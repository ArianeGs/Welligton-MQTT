import pika
credentials = pika.PlainCredentials('username', 'password')
parameters = pika.ConnectionParameters(credentials=credentials)