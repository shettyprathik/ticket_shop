from src import app
from flask_jwt_extended import get_jwt_identity
from common.middleware.jwt import verify_jwt


@app.route("/api/users/current_user")
@verify_jwt
def current_user():
    curr_usr = get_jwt_identity()
    return {"current_user": curr_usr}
