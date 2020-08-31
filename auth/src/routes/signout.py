from src import app

@app.route('/api/users/signout')
def signout():
    return "signout"
