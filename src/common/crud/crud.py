from typing import Generic, TypeVar
from pydantic import BaseModel as PydanticBaseModel
from sqlalchemy.orm import Session, Query

from common.db.base_model import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=PydanticBaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=PydanticBaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    @staticmethod
    def get_all_query(db: Session) -> Query:
        return db.query(ModelType)

    def get_all(self, db: Session) -> list:
        return self.get_all_query(db).all()

    def get(self, db, *args, sid):
        return self.get_all_query(db).filter(ModelType)
