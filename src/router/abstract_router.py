from typing import Generic, TypeVar, List
from uuid import UUID
from fastapi import APIRouter
from pydantic import BaseModel as PydanticBaseModel
from common.db.base_model import BaseModel
from router.irouter import IRouter
from schemas.msg import Msg

ModelType = TypeVar("ModelType", bound=BaseModel)
ModelSchemaType = TypeVar("ModelSchemaType", bound=PydanticBaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=PydanticBaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=PydanticBaseModel)
FilterSchemaType = TypeVar("FilterSchemaType", bound=PydanticBaseModel)


class AbstractRouter(
    IRouter,
    Generic[ModelType, ModelSchemaType, CreateSchemaType, UpdateSchemaType, FilterSchemaType]
):
    def __init__(self):
        self.__router = APIRouter()
        self.routes()

    @property
    def router(self):
        return self.__router

    def routes(self):
        @self.router.get("", response_model=List[ModelSchemaType])
        def get_all():
            pass

        @self.router.get("/{sid}", response_model=ModelSchemaType)
        def get(sid: UUID):
            pass

        @self.router.post("", response_model=CreateSchemaType)
        def create(obj: CreateSchemaType):
            pass

        @self.router.put("/{sid}", response_model=UpdateSchemaType)
        def update(sid: UUID, obj: UpdateSchemaType):
            pass

        @self.router.delete("/{sid}", response_model=Msg)
        def delete(sid: UUID):
            pass
