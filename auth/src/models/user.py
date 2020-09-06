from pydantic import BaseModel, constr, ValidationError
from src.utils.password import Password


class UserModel(BaseModel, Password):
    email: constr(regex=r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
    password: constr(min_length=4, max_length=20)

    class Config:
        extra = 'forbid'


if __name__ == "__main__":
    try:
        a = UserModel(email='abcd@gmail.com', password='sfsdk')
        print(a)
        a.hash_password(a.password)
        print(a)
        print(a.check_password(a.password, 'sfsdk'))
        print(UserModel(email='abcd@gmail.com', password='sfsdk').dict())
    except ValidationError as e:
        print(e.errors())
