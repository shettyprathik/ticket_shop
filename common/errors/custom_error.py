class CustomError(Exception):

    def __init__(self,reason='Custom Error'):
        super().__init__(reason)

    @property
    def status_code(self):
        pass

    def serialize_errors(self):
        pass

if __name__ == "__main__":
    a = CustomError()
