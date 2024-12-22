from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from models.vessel import Vessel


class EquipmentBase(SQLModel):
    name: Optional[str] = None
    type: Optional[str] = None
    vessel_id: Optional[int] = Field(foreign_key="vessel.id")  # 外键关联到船舶

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "发动机",
                    "type": "柴油机",
                    "vessel_id": 1,
                }
            ]
        }
    }


class Equipment(EquipmentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # 反向关系到船舶（Vessel）
    vessel: Optional["Vessel"] = Relationship(back_populates="equipments")


class EquipmentCreate(EquipmentBase):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "发动机",
                    "type": "柴油机",
                    "vessel_id": 1,
                }
            ]
        }
    }


class EquipmentUpdate(SQLModel):
    name: str | None
    type: str | None
