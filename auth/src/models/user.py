from src import db
from src.utils.password import hash_password, check_password


class User(db.Document):
    email = db.EmailField()
    password = db.StringField()

    def response(self):
        return {"id": str(self.id), "email": self.email}

    def hash_password(self):
        self.password = hash_password(self.password)
        return self

    def check_password(self, password):
        return check_password(self.password, password)
