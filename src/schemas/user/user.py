from uuid import UUID

from pydantic.v1 import EmailStr
from schemas.core_model import CoreModel


class UserBase(CoreModel):
    name: str
    email: str


class User(UserBase):
    sid: UUID


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str


class UserFilter(UserBase):
    pass
