from src import db
from common.events import types
import datetime


class Order(db.Document):
    user_id = db.StringField()
    status = db.StringField(choices=tuple(
        types.get_events(types.EventType.Orders())), default=types.EventType.Orders.CREATED)
    expires_at = db.DateTimeField(
        default=datetime.datetime.now() + datetime.timedelta(minutes=15))
    ticket = db.ReferenceField('Ticket')

    def response(self):
        return {
            "id": str(self.id),
            "user_id": self.user_id,
            "status": self.status,
            "expires_at": str(self.expires_at),
            "ticket": self.ticket.response()
        }
