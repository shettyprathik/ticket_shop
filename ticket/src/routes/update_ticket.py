from flask import request
from src import app
from src.pub_broker import publish_channel
from src.models.ticket import Ticket
from common.middleware.jwt import verify_jwt
from common.errors.not_found_error import NotFoundError
from common.errors.token_error import TokenError
from common.errors.bad_request_error import BadRequestError
from common.middleware.current_user import get_current_user
from common.middleware.request_validator import request_validator
from common.events.ticket.ticket_updated_event import TicketUpdatedEvent
from common.events.publish import publish_event
from src.validators.ticket_validator import TicketReqVal
import pika
from src.config import Config
from common.events.types import EventType, ExchangeType


@app.route('/api/tickets/<id_>', methods=['PUT'])
@verify_jwt
@get_current_user
@request_validator(TicketReqVal)
def upd_ticket(id_):
    existing_ticket = Ticket.objects(id=id_).first()

    if not existing_ticket:
        raise NotFoundError("Ticket not found")

    if existing_ticket.user_id != request.current_user['id']:
        raise TokenError('Not Authorized')

    if existing_ticket.order_id:
        raise BadRequestError("Cannot update reserved ticket")

    existing_ticket.modify(**request.valid_body.dict())
    existing_ticket.save()
    print(existing_ticket.response(), flush=True)
    publish_event(publish_channel, TicketUpdatedEvent(
        data=existing_ticket.response()))

    return {}, 204
