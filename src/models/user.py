from common.db.base_model import BaseModel

USER_SCHEMA = 'user'


class User(BaseModel):
    __tablename__ = "task"
    __table_args__ = {
        "schema": USER_SCHEMA,
        "comment": "Table with all tasks",
    }

    name: str
    email: str
    phone: str
    password: str
