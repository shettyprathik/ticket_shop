from src import app
from flask_jwt_extended import get_jwt_identity
from common.middleware.jwt import verify_jwt
from common.middleware.current_user import get_current_user
from flask import request


@app.route("/api/users/current_user")
@verify_jwt
@get_current_user
def current_user():
    return {"current_user": request.current_user}
