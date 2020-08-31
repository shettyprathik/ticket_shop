from src import app

@app.route('/api/users/signup')
def signup():
    return 'signup'
