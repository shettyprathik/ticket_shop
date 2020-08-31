from src import app
from src.errors.request_validation_error import RequestValidationError

@app.route('/api/users/signup')
def signup():
    raise RequestValidationError([{'msg':'request test','param':'request test param'}])
