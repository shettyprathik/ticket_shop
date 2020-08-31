from custom_error import CustomError


class DatabaseConnectionError(CustomError):
    reason = "Error Connecting to Database"

    @property
    def status_code(self):
        return 500

    def serialize_errors(self) -> str:
        return [{"message": self.reason}]


if __name__ == "__main__":
    a = DatabaseConnectionError()
    print(a.status_code)
    print(a.serialize_errors())
