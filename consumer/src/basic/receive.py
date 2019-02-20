#!/usr/bin/env python
import pika

_queue_name = 'hello'
_ip_address = 'localhost'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address))
channel = connection.channel()


channel.queue_declare(queue=_queue_name)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue=_queue_name,
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()