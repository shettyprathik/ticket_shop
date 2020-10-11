from src import db
from src.models.order import Order
from common.events.types import EventType


class Ticket(db.Document):
    title = db.StringField(min_length=5, max_length=50, required=True)
    price = db.FloatField(min_value=1, required=True)
    user_id = db.StringField(required=True)

    def response(self):
        return {"id": str(self.id), "title": self.title, "price": self.price, "user_id": self.user_id}

    def is_reserved(self):
        order = Order.objects(ticket=self, status__nin=[
                              EventType.Orders.CANCELLED]).first()
        return not not order
