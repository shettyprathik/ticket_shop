import os
import pika


class Config:

    BROKER_HOST = 'rabbitmq-cluster-ip-service'
    BROKER_USER = os.environ['BROKER_USER']
    BROKER_PASSWORD = os.environ['BROKER_PASSWORD']
    BROKER_VHOST = os.environ['BROKER_VHOST']
    BROKER_CRED = pika.PlainCredentials(
        username=BROKER_USER, password=BROKER_PASSWORD)
    BROKER_URL = f'amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}/{BROKER_VHOST}'
