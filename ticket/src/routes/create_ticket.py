from flask import request
from src import app
from src.models.ticket import Ticket
from common.middleware.jwt import verify_jwt
from common.middleware.request_validator import request_validator
from src.validators.ticket_validator import TicketReqVal


@app.route('/api/tickets', methods=['POST'])
@verify_jwt
@request_validator(TicketReqVal)
def create_ticket():
    ticket = request.valid_body
    new_ticket = Ticket(**ticket.dict(), user_id=123)
    return new_ticket.response(), 201
