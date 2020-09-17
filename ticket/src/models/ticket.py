from src import db


class Ticket(db.Document):
    title = db.StringField(min_length=5, max_length=50, required=True)
    price = db.FloatField(min_value=1, required=True)
    user_id = db.StringField(required=True)

    def response(self):
        return {"id": str(self.id), "title": self.title, "price": self.price}
