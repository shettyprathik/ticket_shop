from src import app
from src.pub_broker import publish_channel
from common.events.publish import publish_event
from common.events.types import EventType
from common.events.order.order_cancelled_event import OrderCancelledEvent
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

    existing_order.status = EventType.Order.CANCELLED
    existing_order.save()

    publish_event(publish_channel, OrderCancelledEvent(
        data={
            "id": str(existing_order.id),
            "ticket": {
                "id": str(existing_order.ticket.id),
            },
            "version": existing_order.version
        }))

    return {}, 204
