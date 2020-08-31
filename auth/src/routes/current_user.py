from src import app
from src.errors.not_found_error import NotFoundError

@app.route("/api/users/current_user")
def current_user():
    raise NotFoundError()
