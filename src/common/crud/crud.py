from typing import Generic, TypeVar, Union, Dict, Any
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
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

    def update(
            self,
            db: Session,
            *,
            db_obj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, sid: Any) -> ModelType:
        obj = db.query(self.model).filter(self.model.sid == sid).first()
        db.delete(obj)
        db.commit()
        return obj
