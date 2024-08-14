import pika
import json

def send_message(queue, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='', routing_key=queue, body=json.dumps(message))

    connection.close()

def receive_message(queue, callback):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue=queue)
    
    def on_message(ch, method, properties, body):
        message = json.loads(body)
        callback(message)

    channel.basic_consume(queue=queue, on_message_callback=on_message, auto_ack=True)
    channel.start_consuming()
