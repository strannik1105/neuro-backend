import datetime
from sqlalchemy import Column, String, DateTime

from common.db.base_model import BaseModel

MEANS_SCHEMA = "means"


class Means(BaseModel):
    __tablename__ = "means"
    __table_args__ = {
        "schema": MEANS_SCHEMA,
        "comment": "Table with .."
    }

    content = Column(String, nullable=False, comment="content of the letter")
    date = Column(DateTime, default=datetime.datetime.utcnow, comment="send date")
