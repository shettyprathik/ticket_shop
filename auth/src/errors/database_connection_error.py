from src.errors.custom_error import CustomError

class DatabaseConnectionError(CustomError):
    reason = "Error Connecting to Database"

    def __init__(self):
        super().__init__(self.reason)

    @property
    def status_code(self):
        return 500

    def serialize_errors(self):
        return [{"message": self.reason}]


if __name__ == "__main__":
    a = DatabaseConnectionError()
    print(a.status_code)
    print(a.serialize_errors())
