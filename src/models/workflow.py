from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from common.db.base_model import BaseModel

WORKFLOW_SCHEMA = "workflow"


class Workflow(BaseModel):
    __tablename__ = "workflow"
    __table_args__ = {
        "schema": WORKFLOW_SCHEMA,
        "comment": "Table with .."
    }

    owner = Column(Integer, ForeignKey("user.sid"))
    team = Column(String, nullable=False)
    vk_api = Column(String, nullable=True, comment="vk api token")
    tg_api = Column(String, nullable=True, comment="tg api token")
    odnk_api = Column(String, nullable=True, comment="odnoklassniki api token")
    discord_api = Column(String, nullable=True, comment="discord api token")
    dzen_api = Column(String, nullable=True, comment="dzen api token")

    chat = relationship("Chat", back_populates="workflow")
    message = relationship("Message", back_populates="workflow")
    post = relationship("Post", back_populates="workflow")
