from src.models.ticket import Ticket
from src.validators.ticket_validator import TicketReqVal
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
