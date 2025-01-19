from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

class PowerSpeedCurve(SQLModel, table=True):
    __tablename__ = "power_speed_curve"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    speed_water: float
    me_power: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    vessel_id: int = Field(foreign_key="vessel.id")
