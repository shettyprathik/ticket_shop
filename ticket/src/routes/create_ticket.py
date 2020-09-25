from flask import request
from src import app
from src.pub_broker import publish_channel
from src.models.ticket import Ticket
from common.middleware.jwt import verify_jwt
from common.middleware.request_validator import request_validator
from common.middleware.current_user import get_current_user
from common.events.types import EventType, ExchangeType
from src.validators.ticket_validator import TicketReqVal
import pika
from src.config import Config

# pika.URLParameters(f"amqp://{Config.BROKER_USER}:{Config.BROKER_PASSWORD}@rabbitmq-cluster-ip-service:5672/{Config.BROKER_VHOST}")


@app.route('/api/tickets', methods=['POST'])
@verify_jwt
@get_current_user
@request_validator(TicketReqVal)
def create_ticket():
    ticket = request.valid_body
    new_ticket = Ticket(**ticket.dict(), user_id=request.current_user['id'])
    new_ticket.save()
    print(new_ticket.id, flush=True)
    publish_channel.basic_publish(
        exchange=ExchangeType.TICKET, routing_key=EventType.Ticket.CREATED, body='TicketCreated')
    return new_ticket.response(), 201
