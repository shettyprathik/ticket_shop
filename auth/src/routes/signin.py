from flask import request
from src import app
from src.validators.user_request_validator import UsrReqValid
from src.validators.request_validator import request_validator
from src.models.user import User
from src.errors.bad_request_error import BadRequestError


@app.route('/api/users/signin', methods=['POST'])
@request_validator(UsrReqValid)
def signin():

    usr = request.valid_body

    existing_usr = User.objects(email=usr.email).first()
    if not existing_usr:
        raise BadRequestError('Sign Up')

    return "Sign in"
