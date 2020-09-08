from flask import Flask
from src.config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine(app)
from src.routes import current_user, signup, signout, signin
from src.middleware import error_handler
