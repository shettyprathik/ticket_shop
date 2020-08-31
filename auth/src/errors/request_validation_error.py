from custom_error import CustomError


class RequestValidationError(CustomError):
    errors = []

    @property
    def status_code(self):
        return 400

    def serialize_errors(self) -> str:
        return list(map(lambda err: {"message": err.msg, "field": err.param}, self.errors))


if __name__ == "__main__":
    a = RequestValidationError()
    print(a.status_code)
    print(a.serialize_errors())
