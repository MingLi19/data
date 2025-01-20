from typing import Annotated, Generic, TypeVar

from pydantic import BaseModel, Field

Data = TypeVar("Data")


class ResponseModel(BaseModel, Generic[Data]):
    code: Annotated[int, Field(default=200)]
    data: Data
    message: Annotated[str, Field(default="获取数据成功")]
