from src import app
from common.middleware.jwt import verify_jwt
from common.errors.not_found_error import NotFoundError
from src.models.ticket import Ticket


@app.route('/api/tickets/<id_>')
@verify_jwt
def get_ticket(id_):
    existing_ticket = Ticket.objects(id=id_).first()

    if existing_ticket:
        return existing_ticket.response()

    raise NotFoundError('Ticket not found')
