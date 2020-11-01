import pika
from src.config import Config
from src.events.listeners.callbacks import order_expire_callback
from common.events.types import EventType, ExchangeType, get_events
from common.events.utils import bind_q_to_exchange, declare_queue
from threading import Thread


expiration_event = EventType.Expiration()
qs = get_events(expiration_event)

broker_connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=Config.BROKER_HOST, port=5672, credentials=Config.BROKER_CRED, virtual_host=Config.BROKER_VHOST))

consume_channel = broker_connection.channel()
consume_channel.exchange_declare(
    exchange=ExchangeType.EXPIRATION, exchange_type='direct')
declare_queue(consume_channel, qs)

bind_q_to_exchange(consume_channel, qs, ExchangeType.EXPIRATION)

consume_channel.basic_consume(queue=EventType.Expiration.START_COUNTER,
                              on_message_callback=order_expire_callback)

# consume_channel.start_consuming()
thread = Thread(target=consume_channel.start_consuming)
thread.start()
