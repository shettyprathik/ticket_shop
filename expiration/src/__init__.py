from celery import Celery
from src.config import Config

celery = Celery('src', broker=Config.BROKER_URL, include=['src.tasks.expire'])

if __name__ == "__main__":
    celery.start()
