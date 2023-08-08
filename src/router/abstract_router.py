from typing import Generic, TypeVar, Type
from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel as PydanticBaseModel
from common.db.base_model import BaseModel
from router.irouter import IRouter

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=PydanticBaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=PydanticBaseModel)


class AbstractRouter(IRouter, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self):
        self.__router = APIRouter()
        self.routes()

    @property
    def router(self):
        return self.__router

    def routes(self):
        @self.router.get("")
        def get_all():
            pass

        @self.router.get("/{sid}")
        def get(sid: UUID):
            pass

        @self.router.post("")
        def create():
            pass

        @self.router.put("/{sid}")
        def update(sid: UUID):
            pass

        @self.router.delete("/{sid}")
        def delete(sid: UUID):
            pass
