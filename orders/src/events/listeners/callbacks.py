from src.models.ticket import Ticket
from src.models.order import Order
from src.validators.ticket_validator import TicketReqVal
from common.events.types import EventType
from common.events.order.order_cancelled_event import OrderCancelledEvent
from common.events.publish import publish_event
from src.pub_broker import publish_channel
import json


def ticket_created_callback(ch, method, props, body):
    body = json.loads(body)
    print(body, flush=True)
    new_ticket = Ticket(**body['data'])
    new_ticket.save()
    print(method.delivery_tag, flush=True)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def ticket_updated_callback(ch, method, props, body):
    body = json.loads(body)
    print(body, flush=True)
    existing_ticket = Ticket.find_by_event(
        id=body['data']['id'], version=body['data']['version']).first()

    if not existing_ticket:
        raise Exception('Ticket not found')

    existing_ticket.modify(**body['data'])
    existing_ticket.save()

    ch.basic_ack(delivery_tag=method.delivery_tag)


def expiration_complete_callback(ch, method, props, body):
    body = json.loads(body)
    print("inside order expiration complete callback", flush=True)
    print(body, flush=True)
    existing_order = Order.objects(id=body['data']['order_id']).first()

    if not existing_order:
        raise Exception('Order not found')

    existing_order.modify(status=EventType.Order.CANCELLED)
    existing_order.save()

    publish_event(publish_channel, OrderCancelledEvent(
        data=existing_order.response()))

    ch.basic_ack(delivery_tag=method.delivery_tag)
