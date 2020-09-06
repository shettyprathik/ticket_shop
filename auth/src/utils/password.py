from werkzeug.security import generate_password_hash, check_password_hash


class Password:

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password_hash, password):
        return check_password_hash(password_hash, password)


if __name__ == "__main__":
    a = Password()
    a.hash_password('a')
    print(a.password)
    print(a.check_password(generate_password_hash('a'), 'a'))
