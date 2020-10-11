from src import app
from flask import jsonify, request
from common.middleware.jwt import verify_jwt
from common.middleware.current_user import get_current_user
from src.models.order import Order


@app.route('/api/orders')
@verify_jwt
@get_current_user
def get_orders():
    all_orders = Order.objects(user_id=request.current_user['id'])
    return jsonify([orders.response() for orders in all_orders])
