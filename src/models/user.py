import datetime
from sqlalchemy import Column, String, Integer, Enum, ForeignKey, DateTime
from common.db.base_model import BaseModel
from common.enums import Rate

USER_SCHEMA = "user"


class User(BaseModel):
    __tablename__ = "user"
    __table_args__ = {
        "schema": USER_SCHEMA,
        "comment": "Table with user",
    }

    name = Column(String, nullable=False, comment="name of user", index=True)
    surname = Column(String, nullable=True, comment="surname of user")
    email = Column(String, unique=True, index=True, nullable=False, comment="email")
    hashed_password = Column(String, nullable=False, comment="passwd")
    workflow_id = Column(Integer, ForeignKey("workflow.sid"))
    rate = Column(Enum(Rate), default=Rate.BASE, comment="rate profile")
    until_the_next_date = Column(Integer, default=100, comment='number tokens before next rate')
    registration_at = Column(DateTime, default=datetime.datetime.utcnow, comment='date registration')
