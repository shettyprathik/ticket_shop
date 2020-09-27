import pika
from src.config import Config
from common.events.types import EventType, ExchangeType
from threading import Thread


def declare_queue(ch, qs):
    for q in qs:
        ch.queue_declare(q)


def bind_q_to_exchange(ch, qs, exchange):
    for q in qs:
        ch.queue_bind(exchange=exchange, queue=q)


def callback(ch, method, props, body):
    print("*" * 70, flush=True)
    print("Consuming", flush=True)
    print(body, flush=True)
    print("*" * 70, flush=True)


ticket_event = EventType.Ticket()
qs = [getattr(ticket_event, attr) for attr in dir(ticket_event) if not callable(
    getattr(ticket_event, attr)) and not attr.startswith("__")]


credentials = pika.PlainCredentials(
    username=Config.BROKER_USER, password=Config.BROKER_PASSWORD)

broker_connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=Config.BROKER_HOST, port=5672, credentials=credentials, virtual_host=Config.BROKER_VHOST))

consume_channel = broker_connection.channel()
consume_channel.exchange_declare(
    exchange=ExchangeType.TICKET, exchange_type='direct')
declare_queue(consume_channel, qs)

bind_q_to_exchange(consume_channel, qs, ExchangeType.TICKET)

consume_channel.basic_consume(queue=EventType.Ticket.CREATED,
                              on_message_callback=callback, auto_ack=True)
consume_channel.basic_consume(queue=EventType.Ticket.UPDATED,
                              on_message_callback=callback, auto_ack=True)

consume_channel.start_consuming()
# thread = Thread(target=consume_channel.start_consuming)
# thread.start()
