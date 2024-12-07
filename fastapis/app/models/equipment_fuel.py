from enum import Enum

from sqlmodel import Field, SQLModel, Relationship

from models.equipment import Equipment
from models.meta import FuelType


class EquipmentType(str, Enum):
    me = "me"
    dg = "dg"
    blr = "blr"


class EquipmentFuel(SQLModel, table=True):
    __tablename__ = "equipment_fuel"

    id: int | None = Field(default=None, primary_key=True)
    equipment_id: int = Field(foreign_key="equipment.id", ondelete="CASCADE")
    fuel_type_id: int = Field(foreign_key="fuel_type.id")

    equipment: Equipment = Relationship(back_populates="equipment_fuel")
    fuel_type: FuelType = Relationship(back_populates="equipment_fuel")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "equipment_id": 1,
                    "fuel_type_id": 1
                }
            ]
        }
    }
