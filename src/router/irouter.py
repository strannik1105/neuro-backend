from abc import ABC, abstractmethod
from typing import Type
from fastapi import APIRouter


class IRouter(ABC):
    # Property to get FastApi router, which allowing decorator to implement routes
    @property
    @abstractmethod
    def router(self) -> Type[APIRouter]:
        pass

    # Method which implements Fast Api routes
    @abstractmethod
    def routes(self):
        pass
