from flask import Flask
from src.config import Config
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine(app)
jwt = JWTManager(app)

from src.routes import create_order, update_order, show_order, index_order
from common.middleware.error_handler import handle_error


app.errorhandler(Exception)(handle_error)
