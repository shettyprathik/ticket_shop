from src import app

@app.route("/api/users/current_user")
def current_user():
    return 'user'
