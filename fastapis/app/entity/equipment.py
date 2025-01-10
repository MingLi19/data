from datetime import datetime

from sqlmodel import Field, Relationship

from app.entity.vessel import Vessel
from app.model.equipment import EquipmentBase


class Equipment(EquipmentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    vessel_id: int | None = Field(default=None, foreign_key="vessel.id")
    vessel: Vessel | None = Relationship(back_populates="equipments")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "发动机",
                    "type": "柴油机",
                }
            ]
        }
    }
