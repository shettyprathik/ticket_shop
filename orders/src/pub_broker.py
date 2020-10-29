import pika
from src.config import Config
from common.events.utils import bind_q_to_exchange, declare_queue
from common.events.types import ExchangeType, EventType, get_events

order_event = EventType.Order()
qs = get_events(order_event)

broker_connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=Config.BROKER_HOST, port=5672, credentials=Config.BROKER_CRED, virtual_host=Config.BROKER_VHOST))

publish_channel = broker_connection.channel()
publish_channel.exchange_declare(
    exchange=ExchangeType.ORDER, exchange_type='direct')
declare_queue(publish_channel, qs)
bind_q_to_exchange(publish_channel, qs, ExchangeType.ORDER)
