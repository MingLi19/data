from pydantic import BaseModel

from app.entity.company import Company
from app.entity.equipment import Equipment
from app.entity.meta import ShipType, TimeZone
from app.model.equipment import EquipmentCreate


class VesselBase(BaseModel):
    name: str  # 船名，必填且唯一
    mmsi: str  # 海事识别号，必填且唯一
    build_date: str  # 建造日期，格式为 'YYYY-MM-DD'
    gross_tone: float  # 总吨位
    dead_weight: float  # 装载吨位
    new_vessel: bool  # 是否为新船
    hull_clean_date: str | None  # 船体清洁日期
    engine_overhaul_date: str | None  # 发动机检修日期
    newly_paint_date: str | None  # 新涂装日期
    propeller_polish_date: str | None  # 螺旋桨抛光日期
    company_id: int  # 公司ID
    ship_type_id: int  # 船舶类型
    time_zone_id: int  # 时区


class VesselCreate(VesselBase):
    equipments: list[EquipmentCreate] = []  # 船舶设备

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
                    "ship_type_id": 3,
                    "time_zone_id": 4,
                    "equipments": [
                        {
                            "name": "发动机",
                            "type": "me",
                            "fuel_type_ids": [1, 2],
                        },
                        {
                            "name": "柴油发电机",
                            "type": "dg",
                        },
                        {
                            "name": "锅炉",
                            "type": "blr",
                        },
                    ],
                }
            ]
        }
    }


class VesselUpdate(VesselBase):
    equipments: list[EquipmentCreate] = []  # 船舶设备

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "船名-新",
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
                    "ship_type_id": 3,
                    "time_zone_id": 4,
                    "equipments": [
                        {
                            "name": "发动机",
                            "type": "me",
                            "fuel_type_ids": [1, 2],
                        },
                        {
                            "name": "柴油发电机",
                            "type": "dg",
                        },
                        {
                            "name": "锅炉",
                            "type": "blr",
                        },
                    ],
                }
            ]
        }
    }


class VesselPublic(VesselBase):
    id: int
    company: Company
    ship_type: ShipType
    time_zone: TimeZone

    equipments: list[Equipment]
