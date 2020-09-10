from flask import Flask
from src.config import Config
from flask_mongoengine import MongoEngine
from flask_jwt_extended import (
    JWTManager, create_access_token, set_access_cookies, verify_jwt_in_request, get_jwt_identity)

app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine(app)
jwt = JWTManager(app)

from src.routes import current_user, signup, signout, signin
from src.middleware import error_handler
