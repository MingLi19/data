from datetime import date

from pydantic import BaseModel


class Location(BaseModel):
    PCDate: date  # 日期字段
    latitude: float
    longitude: float
