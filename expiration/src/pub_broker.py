import pika
from src.config import Config
from common.events.utils import bind_q_to_exchange, declare_queue
from common.events.types import ExchangeType, EventType, get_events

expiration_event = EventType.Expiration()
qs = get_events(expiration_event)

broker_connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=Config.BROKER_HOST, port=5672, credentials=Config.BROKER_CRED, virtual_host=Config.BROKER_VHOST))

publish_channel = broker_connection.channel()
publish_channel.exchange_declare(
    exchange=ExchangeType.EXPIRATION, exchange_type='direct')
declare_queue(publish_channel, qs)
bind_q_to_exchange(publish_channel, qs, ExchangeType.EXPIRATION)
