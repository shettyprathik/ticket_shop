from src import app
from flask_jwt_extended import unset_jwt_cookies
from flask import jsonify


@app.route('/api/users/signout', methods=['POST'])
def signout():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp
