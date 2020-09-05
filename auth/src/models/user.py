from pydantic import BaseModel


class UserSchema(BaseModel):
    email: str
    password: str

    class Config:
        extra = 'forbid'


if __name__ == "__main__":
    print(UserSchema(email='abcd@gmail.com', password='abcd').dict())
