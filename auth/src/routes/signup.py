from flask import request, make_response
from src import app, create_access_token, set_access_cookies
from src.validators.user_request_validator import UsrReqValid
from src.validators.request_validator import request_validator
from src.models.user import User
from src.errors.bad_request_error import BadRequestError


@app.route('/api/users/signup', methods=['POST'])
@request_validator(UsrReqValid)
def signup():

    usr = request.valid_body

    existing_usr = User.objects(email=usr.email).first()
    if existing_usr:
        raise BadRequestError('Existing User')

    new_usr = User(**usr.dict())
    new_usr.hash_password()
    new_usr.save()

    resp = make_response(new_usr.response())
    access_token = create_access_token(identity=str(new_usr.id))
    set_access_cookies(resp, access_token)

    return resp, 201
