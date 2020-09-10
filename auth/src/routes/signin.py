from flask import request, make_response
from src import app, create_access_token, set_access_cookies
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

    if not existing_usr.check_password(usr.password):
        raise BadRequestError('Invalid Credentials')

    resp = make_response(existing_usr.response())
    access_token = create_access_token(identity=existing_usr.response())
    set_access_cookies(resp, access_token)

    return resp
