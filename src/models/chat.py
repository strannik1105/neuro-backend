from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime

from common.db.base_model import BaseModel

CHAT_SCHEMA = "chat"
MESSAGE_SCHEMA = "message"


class Chat(BaseModel):
    __tablename__ = "chat"
    __table_args__ = {
        "schema": CHAT_SCHEMA,
        "comment": "Table with .."
    }

    members = relationship("User")
    workflow_id = Column(Integer, ForeignKey("workflow.sid"))

    workflow = relationship("Workflow", back_populates="chat")


class Message(BaseModel):
    __tablename__ = "message"
    __table_args__ = {
        "schema": MESSAGE_SCHEMA,
        "comment": "Table with .."
    }

    sended_at = Column(DateTime, default=datetime.datetime.utcnow)
    sender = Column(Integer, ForeignKey("user.sid"))
    workflow_id = Column(Integer, ForeignKey("workflow.sid"))

    workflow = relationship("Workflow", back_populates="message")
