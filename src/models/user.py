from sqlalchemy import Column, String
from common.db.base_model import BaseModel

USER_SCHEMA = "user"


class User(BaseModel):
    __tablename__ = "task"
    __table_args__ = {
        "schema": USER_SCHEMA,
        "comment": "Table with all tasks",
    }

    name = Column(String, nullable=False, comment="name of user", index=True)
    email = Column(String, unique=True, index=True, nullable=False, comment="email")
    hashed_password = Column(String, nullable=False, comment="passwd")
