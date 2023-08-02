from typing import Generic, TypeVar
from fastapi import HTTPException
from psycopg2 import errors
from pydantic import BaseModel as PydanticBaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, Query
from common.db.base_model import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=PydanticBaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=PydanticBaseModel)
UniqueViolation = errors.lookup("23505")


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: ModelType):
        self.__model = model

    def get_all_query(self, db: Session) -> Query:
        return db.query(self.__model)

    def get_all(self, db: Session) -> list:
        return self.get_all_query(db).all()

    def get(self, db, *, sid):
        return self.get_all_query(db).filter(self.__model.sid == sid)

    def create(self, db, *, obj: CreateSchemaType) -> ModelType:
        try:
            db_obj = self.model(**obj)
            db.add(db_obj)
            db.commit()
        except IntegrityError as e:
            if isinstance(e.orig, UniqueViolation):
                raise HTTPException(status_code=401)
            raise e
