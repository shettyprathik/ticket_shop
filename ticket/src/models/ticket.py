from src import db


class Ticket(db.Document):
    title = db.StringField(min_length=5, max_length=50, required=True)
    price = db.FloatField(min_value=1, required=True)
    user_id = db.StringField(required=True)
    order_id = db.StringField(default=None)
    version = db.IntField(default=0)

    def response(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "price": self.price,
            "user_id": self.user_id,
            "order_id": self.order_id,
            "version": self.version
        }

    def update_version_if_record_exists(self):
        if not self.id:
            return

        existing_record = Ticket.objects(id=self.id)
        if existing_record:
            self.version += 1

    def save(self, *args, **kwargs):
        self.update_version_if_record_exists()
        super().save(*args, **kwargs)
