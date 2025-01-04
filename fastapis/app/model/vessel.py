from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.model.equipment import Equipment

from app.entity.company import Company
from app.entity.meta import ShipType, TimeZone


class VesselBase(SQLModel):
    name: str = Field(unique=True, nullable=False)  # 船名，必填且唯一
    mmsi: str = Field(unique=True, nullable=False)  # 海事识别号，必填且唯一
    build_date: str  # 建造日期，格式为 'YYYY-MM-DD'
    gross_tone: float  # 总吨位
    dead_weight: float  # 装载吨位
    new_vessel: bool  # 是否为新船
    hull_clean_date: str | None  # 船体清洁日期
    engine_overhaul_date: str | None  # 发动机检修日期
    newly_paint_date: str | None  # 新涂装日期
    propeller_polish_date: str | None  # 螺旋桨抛光日期


class Vessel(VesselBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    created_at: datetime = Field(default_factory=datetime.utcnow)

    equipments: list["Equipment"] = Relationship(back_populates="vessel")

    company_id: int | None = Field(default=None, foreign_key="company.id")
    company: Company | None = Relationship(back_populates="vessels")

    ship_type_id: int | None = Field(default=None, foreign_key="ship_type.id")
    ship_type: ShipType | None = Relationship(back_populates="vessel")

    time_zone_id: int | None = Field(default=None, foreign_key="time_zone.id")
    time_zone: TimeZone | None = Relationship(back_populates="vessel")


class VesselCreate(VesselBase):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "船名",
                    "mmsi": "海事识别号",
                    "build_date": "2024-12-06",
                    "gross_tone": 1.0,
                    "dead_weight": 2.0,
                    "new_vessel": True,
                    "hull_clean_date": "2024-12-06",
                    "engine_overhaul_date": "2024-12-06",
                    "newly_paint_date": "2024-12-06",
                    "propeller_polish_date": "2024-12-06",
                    "company_id": 1,
                    "ship_type": 3,
                    "time_zone": 4,
                }
            ]
        }
    }


class VesselUpdate(BaseModel):
    name: str = Field(unique=True, nullable=False)  # 船名，必填且唯一
    mmsi: str = Field(unique=True, nullable=False)  # 海事识别号，必填且唯一
    build_date: str  # 建造日期，格式为 'YYYY-MM-DD'
    gross_tone: float  # 总吨位
    dead_weight: float  # 装载吨位
    new_vessel: bool  # 是否为新船
    hull_clean_date: str | None  # 船体清洁日期
    engine_overhaul_date: str | None  # 发动机检修日期
    newly_paint_date: str | None  # 新涂装日期
    propeller_polish_date: str | None  # 螺旋桨抛光日期
    company_id: int  # 公司ID
    ship_type: int  # 船舶类型
    time_zone: int  # 时区

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "船名",
                    "mmsi": "海事识别号",
                    "build_date": "2024-12-06",
                    "gross_tone": 1.0,
                    "dead_weight": 2.0,
                    "new_vessel": True,
                    "hull_clean_date": "2024-12-06",
                    "engine_overhaul_date": "2024-12-06",
                    "newly_paint_date": "2024-12-06",
                    "propeller_polish_date": "2024-12-06",
                    "company_id": 1,
                    "ship_type": 3,
                    "time_zone": 4,
                }
            ]
        }
    }
