from common.errors.custom_error import CustomError


class RequestValidationError(CustomError):
    errors = []

    def __init__(self, errors, reason='Invalid request parmaters'):
        super().__init__(reason)
        self.reason = reason
        self.errors = errors

    @property
    def status_code(self):
        return 400

    def serialize_errors(self):
        return list(map(lambda err: {"message": err['msg'], "field": err['loc'][0]}, self.errors))


if __name__ == "__main__":
    a = RequestValidationError(
        [{'msg': 'request test', 'loc': ('request test param',)}])
    print(a.status_code)
    print(a.serialize_errors())
