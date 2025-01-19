from typing import Optional
from pydantic import BaseModel
from sqlmodel import Field

class PowerSpeedCurveBase(BaseModel):
    id: Optional[int] = None
    speed_water: float
    me_power: float
    vessel_id: int

class PowerSpeedCurveCreate(PowerSpeedCurveBase):
    model_config = {
        "json_schema_extra": {
            "examples": [{
                "speed_water": 10.0,
                "me_power": 1000.0,
                "vessel_id": 1
            }]
        }
    }

class PowerSpeedCurveUpdate(PowerSpeedCurveBase):
    model_config = {
        "json_schema_extra": {
            "examples": [{
                "speed_water": 12.0,
                "me_power": 1200.0,
                "vessel_id": 1
            }]
        }
    }

class PowerSpeedCurvePublic(PowerSpeedCurveBase):
    id: int
