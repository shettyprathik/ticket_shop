from common.errors.custom_error import CustomError


class TokenError(CustomError):

    def __init__(self, reason="Not Authorized"):
        super().__init__(reason)
        self.reason = reason

    @property
    def status_code(self):
        return 401

    def serialize_errors(self):
        return [{"message": self.reason}]
