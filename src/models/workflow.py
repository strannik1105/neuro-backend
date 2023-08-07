import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Enum
from sqlalchemy.orm import relationship

from common.db.base_model import BaseModel
from common.enums import SocialNetworks

WORKFLOW_SCHEMA = "workflow"
POST_SCHEMA = "post"
MEANS_SCHEMA = "means"


class Workflow(BaseModel):
    __tablename__ = "workflow"
    __table_args__ = {
        "schema": WORKFLOW_SCHEMA,
        "comment": "Table with workflow"
    }

    owner_sid = Column(Integer, ForeignKey("user.sid"))
    team = Column(String, nullable=False)
    vk_api = Column(String, nullable=True, comment="vk api token")
    tg_api = Column(String, nullable=True, comment="tg api token")
    odnk_api = Column(String, nullable=True, comment="odnoklassniki api token")
    discord_api = Column(String, nullable=True, comment="discord api token")
    dzen_api = Column(String, nullable=True, comment="dzen api token")

    chat = relationship("Chat", back_populates="workflow")
    message = relationship("Message", back_populates="workflow")
    post = relationship("Post", back_populates="workflow")


class Means(BaseModel):
    __tablename__ = "means"
    __table_args__ = {
        "schema": MEANS_SCHEMA,
        "comment": "Table with means"
    }

    content = Column(String, nullable=False, comment="content of the letter")
    date = Column(DateTime, default=datetime.datetime.utcnow, comment="send date")


class Post(BaseModel):
    __tablename__ = "post"
    __table_args__ = {
        "schema": POST_SCHEMA,
        "comment": "Table with post"
    }

    content = Column(String, comment='content of the post')
    name_images = Column(String, comment="name images")
    soc_network = Column(Enum(SocialNetworks), comment="type social network")
    author = Column(Integer, ForeignKey("user.sid"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_editor = Column(Integer, ForeignKey("user.sid"), default=None, nullable=True)
    workflow_sid = Column(Integer, ForeignKey("workflow.sid"))

    workflow = relationship("Workflow", back_populates="post")
