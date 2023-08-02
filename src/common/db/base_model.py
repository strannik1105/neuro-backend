from sqlalchemy import UUID
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr


@as_declarative()
class BaseModel:
    id: UUID

    @declared_attr
    def __table__name(self):
        return self.__name__.lower()

