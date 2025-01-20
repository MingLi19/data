from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, SQLModel

if TYPE_CHECKING:
    pass


class PowerSpeedCurveBase(SQLModel):
    speed_water: float
    me_power: float


class PowerSpeedCurve(PowerSpeedCurveBase, table=True):
    __tablename__ = "power_speed_curve"
    id: int = Field(primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    vessel_id: int = Field(foreign_key="vessel.id")

    model_config = {
        "json_schema_extra": {"examples": [{"id": 1, "speed_water": 10.0, "me_power": 1000.0, "vessel_id": 1}]}
    }


class PowerSpeedCurveCreate(PowerSpeedCurveBase):
    pass


class PowerSpeedCurvePublic(PowerSpeedCurveBase):
    pass
