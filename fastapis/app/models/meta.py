from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


## Data Modal -> Meta Data -> Fuel Type
class FuelType(SQLModel, table=True):
    __tablename__ = "fuel_type"
    id: int = Field(primary_key=True)
    name_cn: str
    name_en: str
    name_abbr: str
    cf: float

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name_cn": "液化天然气",
                    "name_en": "Liquefied Natural Gas",
                    "name_abbr": "LNG",
                    "cf": 2.75,
                }
            ]
        }
    }


## Data Modal -> Meta Data -> Ship Type
class ShipType(SQLModel, table=True):
    __tablename__ = "ship_type"
    id: int = Field(primary_key=True)
    name_cn: str
    name_en: str
    code: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name_cn": "散货船",
                    "name_en": "Bulk carrier",
                    "code": "I001",
                }
            ]
        }
    }


class TimeZone(SQLModel, table=True):
    __tablename__ = "time_zone"
    id: int = Field(primary_key=True)
    name_cn: str
    name_en: str
    explaination: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name_cn": "中国标准时间",
                    "name_en": "China Standard Time",
                    "explaination": "UTC+8",
                }
            ]
        }
    }


class Equipment(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name_cn: str
    name_en: str
    explaination: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    vessel_id: Optional[int] = Field(default=None, foreign_key="vessel.id")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 123,
                    "name_cn": "主机b",
                    "name_en": "Main Engine",
                    "explaination": "船舶的主动力设备",
                    "created_at": "2024-11-26T12:00:00",
                }
            ]
        }
    }
