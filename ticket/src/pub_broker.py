import pika
from src.config import Config
from common.events.types import EventType

credentials = pika.PlainCredentials(
    username=Config.BROKER_USER, password=Config.BROKER_PASSWORD)

broker_connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=Config.BROKER_HOST, port=5672, credentials=credentials, virtual_host=Config.BROKER_VHOST))

publish_channel = broker_connection.channel()
