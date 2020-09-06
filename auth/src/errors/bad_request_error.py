from src.errors.custom_error import CustomError


class BadRequestError(CustomError):

    def __init__(self, reason='Bad request error'):
        super().__init__(reason)
        self.reason = reason

    @property
    def status_code(self):
        return 400

    def serialize_errors(self):
        return [{"message": self.reason}]
