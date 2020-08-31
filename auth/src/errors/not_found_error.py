from custom_error import CustomError


class NotFoundError(CustomError):
    reason = "Not Found"

    @property
    def status_code(self):
        return 404

    def serialize_errors(self) -> str:
        return [{"message": self.reason}]


if __name__ == "__main__":
    a = NotFoundError()
    print(a.status_code)
    print(a.serialize_errors())
