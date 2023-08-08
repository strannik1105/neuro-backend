from models.user import User
from router.abstract_router import AbstractRouter
from schemas.user.user import UserCreate, UserUpdate


class UserRouter(AbstractRouter[User, UserCreate, UserUpdate]):
    pass


user_router = UserRouter()
