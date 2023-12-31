from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from common.db.base_model import BaseModel

TOKENS_SCHEMA = "tokens"


class Tokens(BaseModel):
    __tablename__ = "tokens"
    __table_args__ = {
        "schema": TOKENS_SCHEMA,
        "comment": "Table with .."
    }

    token = Column(String, nullable=False, comment='token', unique=True)
    group_name = Column()
    user_owner = Column(Integer, ForeignKey("user.sid"), comment="token's owner")
    workflow_id = Column(Integer, ForeignKey("workflow.sid"))

    workflow = relationship("Workflow", back_populates="tokens")
