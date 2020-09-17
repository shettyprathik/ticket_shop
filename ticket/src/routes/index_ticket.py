from src import app
from flask import jsonify
from common.middleware.jwt import verify_jwt
from src.models.ticket import Ticket


@app.route('/api/tickets')
@verify_jwt
def get_all_tickets():
    all_tickets = Ticket.objects()
    return jsonify([t.response() for t in all_tickets])
