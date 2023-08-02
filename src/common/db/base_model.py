import uuid
from sqlalchemy import UUID, Column
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr


@as_declarative()
class BaseModel:
    sid = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        primary_key=True,
        index=True,
        default=lambda: uuid.uuid4().hex,
    )

    @declared_attr
    def __table__name(self):
        return self.__name__.lower()

