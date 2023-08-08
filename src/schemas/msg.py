from pydantic import BaseModel as PydanticBaseModel


class Msg(PydanticBaseModel):
    msg: str
