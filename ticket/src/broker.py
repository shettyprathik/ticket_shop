import pika
from src.config import Config
from common.events.types import EventType


def declare_queue(ch, qs):
    for q in qs:
        ch.queue_declare(q.value)


def bind_q_to_exchange(ch, qs, exchange):
    for q in qs:
        ch.queue_bind(exchange=exchange, queue=q.value)


def callback(ch, method, props, body):
    print("*" * 70, flush=True)
    print("Consuming", flush=True)
    print(body, flush=True)
    print("*" * 70, flush=True)


qs = [q for q in EventType.Ticket]
exchange = 'ticket'
credentials = pika.PlainCredentials(
    username=Config.BROKER_USER, password=Config.BROKER_PASSWORD)
broker_connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=Config.BROKER_HOST, port=5672, credentials=credentials, virtual_host=Config.BROKER_VHOST))
channel = broker_connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='direct')
declare_queue(channel, qs)
bind_q_to_exchange(channel, qs, exchange)
channel.basic_consume(queue=EventType.Ticket.CREATED.value,
                      on_message_callback=callback, auto_ack=True)
channel.start_consuming()
