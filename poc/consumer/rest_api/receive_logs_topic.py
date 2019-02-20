#!/usr/bin/env python
import pika
import sys
import json
import time
import couchbase_n1ql as n1ql

_ip_address = 'localhost'
_exchange_name = 'couchbase_post'
_exchange_type = 'topic'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=_ip_address))
channel = connection.channel()

channel.exchange_declare(exchange=_exchange_name,
                         exchange_type=_exchange_type)

result = channel.queue_declare(exclusive=True, durable=True)
queue_name = result.method.queue

binding_keys = ['info', 'warning']

for binding_key in binding_keys:
    channel.queue_bind(exchange=_exchange_name,
                        queue=queue_name,
                        routing_key=binding_key)

print(' [*] Waiting.')

def callback(ch, method, properties, body):
    print(" [x] routing_key: %r, body:%r" % (method.routing_key, body))
    _body = body
    print(json.loads(_body))
    _body_loads = json.loads(_body)
    time.sleep(5)
    n1ql.couchbase_get()

    print(json.dumps(_body_loads))
    print(' [*] Done.')
    ch.basic_qos(prefetch_count=1)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()