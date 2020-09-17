from flask import request
from src import app
from src.models.ticket import Ticket
from common.middleware.jwt import verify_jwt
from common.errors.not_found_error import NotFoundError
from common.errors.token_error import TokenError
from common.middleware.current_user import get_current_user
from common.middleware.request_validator import request_validator
from src.validators.ticket_validator import TicketReqVal


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

    existing_ticket.update(**request.valid_body.dict())
    existing_ticket.save()

    return existing_ticket.response()
