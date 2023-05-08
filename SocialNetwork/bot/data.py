import dataclasses
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    confirm_password: str


@dataclass(init=False)
class Post:
    pk: int
    title: str
    content: str

    def __init__(self, **kwargs):
        names = set([field.name for field in dataclasses.fields(self)])

        for k, v in kwargs.items():
            if k in names:
                setattr(self, k, v)
