from src import app
from flask import request
from common.middleware.jwt import verify_jwt
from common.middleware.current_user import get_current_user
from common.errors.not_found_error import NotFoundError
from src.models.order import Order


@app.route('/api/orders/<id_>')
@verify_jwt
@get_current_user
def get_order(id_):
    existing_order = Order.objects(
        user_id=request.current_user['id'], id=id_).first()

    if not existing_order:
        raise NotFoundError('Order not found')

    return existing_order.response()
