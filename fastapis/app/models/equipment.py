from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from app.models.equipment_fuel import EquipmentFuel
from app.models.vessel import Vessel

class Equipment(SQLModel, table=True):
    __tablename__ = "equipment"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, max_length=255, description="设备名称")
    type: str = Field(nullable=False, max_length=255, description="设备类型")
    vessel_id: int | None = Field(foreign_key="vessel.id", description="所属船")
    created_at: datetime | None = Field(default_factory=datetime.utcnow)

    vessel: Vessel = Relationship(back_populates="equipment")
    equipment_fuels: list[EquipmentFuel] = Relationship(back_populates="equipment", cascade_delete=True)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "Equipment A",
                    "type": "me",
                    "vessel_id": 1,
                    "created_at": "2024-12-07T00:00:00"
                }
            ]
        }
    }