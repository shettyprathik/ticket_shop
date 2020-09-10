from src import app, get_jwt_identity
from src.utils.jwt import verify_jwt


@app.route("/api/users/current_user")
@verify_jwt
def current_user():
    curr_usr = get_jwt_identity()
    return curr_usr
