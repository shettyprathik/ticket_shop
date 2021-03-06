import os


class Config:
    MONGODB_DB = 'auth'
    MONGODB_HOST = 'auth-mongo-cluster-ip-srv'
    MONGODB_PORT = 27017

    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_TOKEN_EXPIRES = 30 * 60
    JWT_SECRET_KEY = os.environ['JWT_KEY']
    JWT_COOKIE_CSRF_PROTECT = False
