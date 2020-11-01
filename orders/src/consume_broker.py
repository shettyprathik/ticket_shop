import pika
from src.config import Config
from src.events.listeners.callbacks import ticket_created_callback, ticket_updated_callback, expiration_complete_callback
from common.events.types import EventType, ExchangeType, get_events
from common.events.utils import declare_queue, bind_q_to_exchange
from threading import Thread


ticket_event = EventType.Ticket()
qs = get_events(ticket_event)

broker_connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=Config.BROKER_HOST, port=5672, credentials=Config.BROKER_CRED, virtual_host=Config.BROKER_VHOST))

consume_channel = broker_connection.channel()
consume_channel.exchange_declare(
    exchange=ExchangeType.TICKET, exchange_type='direct')
declare_queue(consume_channel, qs)
bind_q_to_exchange(consume_channel, qs, ExchangeType.TICKET)

consume_channel.basic_consume(queue=EventType.Ticket.CREATED,
                              on_message_callback=ticket_created_callback)
consume_channel.basic_consume(queue=EventType.Ticket.UPDATED,
                              on_message_callback=ticket_updated_callback)


# consume_channel.start_consuming()
thread = Thread(target=consume_channel.start_consuming)
thread.start()


expiration_event = EventType.Expiration()
qs = get_events(expiration_event)

broker_connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=Config.BROKER_HOST, port=5672, credentials=Config.BROKER_CRED, virtual_host=Config.BROKER_VHOST))

consume_channel = broker_connection.channel()
consume_channel.exchange_declare(
    exchange=ExchangeType.EXPIRATION, exchange_type='direct')
declare_queue(consume_channel, qs)
bind_q_to_exchange(consume_channel, qs, ExchangeType.EXPIRATION)

consume_channel.basic_consume(queue=EventType.Expiration.COMPLETE,
                              on_message_callback=expiration_complete_callback)
thread = Thread(target=consume_channel.start_consuming)
thread.start()
