from flask import Flask
from src.config import Config
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine(app)
jwt = JWTManager(app)

from src.routes import current_user, signup, signout, signin
from common.middleware.error_handler import handle_error


app.errorhandler(Exception)(handle_error)
