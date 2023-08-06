from sqlalchemy import Column, String, Enum, ForeignKey, Integer, DateTime
import datetime

from sqlalchemy.orm import relationship

from common.db.base_model import BaseModel
from common.enums import SocialNetworks

POST_SCHEMA = "post"


class Post(BaseModel):
    __tablename__ = "post"
    __table_args__ = {
        "schema": POST_SCHEMA,
        "comment": "Table with .."
    }

    content = Column(String, comment='content of the post')
    name_images = Column(String, comment="name images")
    soc_network = Column(Enum(SocialNetworks), comment="type social network")
    author = Column(Integer, ForeignKey("user.sid"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_editor = Column(Integer, ForeignKey("user.sid"), default=None, nullable=True)
    workflow_id = Column(Integer, ForeignKey("workflow.sid"))

    workflow = relationship("Workflow", back_populates="post")
