import datetime

from sqlalchemy import Column, String, Integer, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from common.db.base_model import BaseModel
from common.enums import Rate

USERXWORKFLOW_SCHEMA = "user_workflow"


class UserXWorkflow(BaseModel):
    __tablename__ = "user_workflow"
    __table_args__ = {
        "schema": USERXWORKFLOW_SCHEMA,
        "comment": "Table with user_workflow",
    }

    user_sid = Column(Integer, ForeignKey("user.sid"))
    workflow_sid = Column(Integer, ForeignKey("workflow.sid"))
