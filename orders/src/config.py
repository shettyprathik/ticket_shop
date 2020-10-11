import os


class Config:
    MONGODB_DB = 'ticket'
    MONGODB_HOST = 'ticket-mongo-cluster-ip-srv'
    MONGODB_PORT = 27017

    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_TOKEN_EXPIRES = 30 * 60
    JWT_SECRET_KEY = os.environ['JWT_KEY']
    JWT_COOKIE_CSRF_PROTECT = False

    BROKER_HOST = 'rabbitmq-cluster-ip-service'
    BROKER_USER = os.environ['BROKER_USER']
    BROKER_PASSWORD = os.environ['BROKER_PASSWORD']
    BROKER_VHOST = os.environ['BROKER_VHOST']