from models.user import User
from router.abstract_router import AbstractRouter
from schemas.user import user


class UserRouter(AbstractRouter[User, user.User, user.UserCreate, user.UserUpdate, user.UserFilter]):
    pass


user_router = UserRouter()
