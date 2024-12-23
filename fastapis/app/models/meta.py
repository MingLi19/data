from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.vessel import Vessel


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

    vessel: list["Vessel"] = Relationship(back_populates="ship_type")

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

    vessel: list["Vessel"] = Relationship(back_populates="time_zone")

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
