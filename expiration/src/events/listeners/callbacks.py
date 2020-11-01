import json
from datetime import datetime
from src.tasks.expire import order_expire
from common.events.types import EventType


def order_expire_callback(ch, method, props, body):
    body = json.loads(body)
    print(body, flush=True)
    expires_at = datetime.fromisoformat(body['data']['expires_at'])
    delay = (expires_at -
             datetime.now()).total_seconds()
    print(delay, flush=True)

    order_expire.apply_async(
        (body['data']['id'],), countdown=delay)

    ch.basic_ack(delivery_tag=method.delivery_tag)
