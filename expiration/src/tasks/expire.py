from src.pub_broker import publish_channel
from src import celery
from common.events.publish import publish_event
from common.events.expiration.expiration_complete_event import ExpirationCompleteEvent


@celery.task
def order_expire(order_id):
    print(f"inside order expire {order_id}", flush=True)
    publish_event(publish_channel, ExpirationCompleteEvent(
        data={"order_id": order_id}))
