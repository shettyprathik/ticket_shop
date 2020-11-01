from src import db
from src.config import Config
from common.events import types
import datetime


class Order(db.Document):
    user_id = db.StringField()
    status = db.StringField(choices=tuple(
        types.get_events(types.EventType.Order())), default=types.EventType.Order.CREATED)
    expires_at = db.DateTimeField(
        default=datetime.datetime.now() + datetime.timedelta(minutes=Config.ORDER_EXPIRE_TIME_MIN))
    ticket = db.ReferenceField('Ticket')
    version = db.IntField(default=0)

    def response(self):
        return {
            "id": str(self.id),
            "user_id": self.user_id,
            "status": self.status,
            "expires_at": str(self.expires_at),
            "ticket": self.ticket.response(),
            "version": self.version
        }

    def update_version_if_record_exists(self):
        if not self.id:
            return

        existing_record = Order.objects(id=self.id)
        if existing_record:
            self.version += 1

    def save(self, *args, **kwargs):
        self.update_version_if_record_exists()
        super().save(*args, **kwargs)
