from datetime import date

from pydantic import BaseModel


class EquipmentFuelCreate(BaseModel):
    name: str
    type: str
    fuel_type_ids: list[int]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "主机", "type": "me", "fuel_type_ids": [1]},
                {"name": "副机", "type": "dg", "fuel_type_ids": [1, 7]},
                {"name": "锅炉", "type": "blr", "fuel_type_ids": [1, 7]},
            ]
        }
    }


class VesselCreate(BaseModel):
    name: str
    mmsi: str
    ship_type: int
    build_date: date
    gross_tone: float
    dead_weight: float
    new_vessel: bool
    dock_repaire_date: date | None
    engine_overhaul_date: date | None
    newly_paint_date: date | None
    time_zone: int
    equipment_fuel: list[EquipmentFuelCreate]
    company_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "八打雁",
                    "mmsi": "477401900",
                    "ship_type": 4,
                    "build_date": "2019-11-01",
                    "gross_tone": 26771.0,
                    "dead_weight": 35337.0,
                    "new_vessel": False,
                    "dock_repaire_date": "2021-01-01",
                    "engine_overhaul_date": "2021-01-01",
                    "newly_paint_date": "2021-01-01",
                    "time_zone": 1,
                    "equipment_fuel": [
                        {"name": "主机", "type": "me", "fuel_type_ids": [1]},
                        {"name": "副机", "type": "dg", "fuel_type_ids": [1, 7]},
                        {"name": "锅炉", "type": "blr", "fuel_type_ids": [1, 7]},
                    ],
                    "company_id": 1,
                }
            ]
        }
    }
