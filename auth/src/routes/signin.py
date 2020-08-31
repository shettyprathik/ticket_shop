from src import app

@app.route('/api/users/signin')
def signin():
    return 'siginin'
