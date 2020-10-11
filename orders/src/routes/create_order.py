from src import app
from flask import request
from src.models.order import Order
from src.models.ticket import Ticket
from common.errors.not_found_error import NotFoundError
from common.errors.bad_request_error import BadRequestError
from common.middleware.jwt import verify_jwt
from common.middleware.current_user import get_current_user
from common.middleware.request_validator import request_validator
from src.validators.order_validator import OrderReqVal


@app.route('/api/orders', methods=['POST'])
@verify_jwt
@get_current_user
@request_validator(OrderReqVal)
def create_order():
    req_val_bd = request.valid_body.dict()
    existing_ticket = Ticket.objects(id=req_val_bd['ticket_id']).first()

    if not existing_ticket:
        raise NotFoundError("Ticket not found")

    if existing_ticket.is_reserved():
        raise BadRequestError("Ticket is reserved")

    new_order = Order(
        user_id=request.current_user['id'], ticket=existing_ticket)
    new_order.save()
    resp = new_order.response()
    return resp
