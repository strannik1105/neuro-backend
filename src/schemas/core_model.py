import orjson
import pytz
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from pydantic.v1 import root_validator


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


def datetime_with_tz(dt: datetime) -> str:
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=pytz.UTC)

    return dt.strftime("%Y-%m-%dT%H:%M:%S%z")


class CoreModel(BaseModel):
    """
    Базовая модель
    """

    def serializable_dict(self, **kwargs):
        default_dict = super().dict(**kwargs)
        return jsonable_encoder(default_dict)

    @root_validator()
    def drop_microseconds(cls, data: dict) -> dict:
        fields = {
            k: v.replace(microsecond=0)
            for k, v in data.items()
            if isinstance(v, datetime)
        }
        return {**data, **fields}

    class Config:
        orm_mode = True
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        json_encoders = {datetime: datetime_with_tz}
