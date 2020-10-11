from src import app
from common.events.types import EventType
from common.middleware.current_user import get_current_user
from common.middleware.jwt import verify_jwt
from common.errors.not_found_error import NotFoundError
from src.models.order import Order


@app.route('/api/orders/<id_>', methods=['DELETE'])
@verify_jwt
@get_current_user
def delete_order(id_):
    existing_order = Order.objects(id=id_).first()

    if not existing_order:
        raise NotFoundError('Order not found')

    existing_order.status = EventType.Orders.CANCELLED
    existing_order.save()

    return {}, 204
