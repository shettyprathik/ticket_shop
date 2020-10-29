from src.models.ticket import Ticket
from common.events.ticket.ticket_updated_event import TicketUpdatedEvent
from common.events.publish import publish_event
from src.pub_broker import publish_channel
import json


def order_created_callback(ch, method, props, body):
    body = json.loads(body)
    print(body, flush=True)

    existing_ticket = Ticket.objects(id=body['data']['ticket']['id']).first()

    if not existing_ticket:
        raise Exception("Ticket not found")

    existing_ticket.order_id = body['data']['id']
    existing_ticket.save()

    publish_event(publish_channel, TicketUpdatedEvent(
        data=existing_ticket.response()))

    ch.basic_ack(delivery_tag=method.delivery_tag)


def order_cancelled_callback(ch, method, props, body):
    body = json.loads(body)
    print(body, flush=True)

    existing_ticket = Ticket.objects(id=body['data']['ticket']['id']).first()

    if not existing_ticket:
        raise Exception('Ticket not found')

    existing_ticket.order_id = None
    existing_ticket.save()

    publish_event(publish_channel, TicketUpdatedEvent(
        data=existing_ticket.response()))

    ch.basic_ack(delivery_tag=method.delivery_tag)
