from flask import Flask

app = Flask(__name__)

from src.routes import current_user, signup, signout, signin
from src.middleware import error_handler
