from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

<<<<<<< HEAD:fastapis/app/models/equipment.py
from models.vessel import Vessel


class EquipmentBase(SQLModel):
    name: Optional[str] = None
    type: Optional[str] = None
    vessel_id: Optional[int] = Field(foreign_key="vessel.id")  # 外键关联到船舶
=======
from app.entity.vessel import Vessel


class EquipmentBase(SQLModel):
    name: str | None
    type: str | None


class Equipment(EquipmentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    vessel_id: int | None = Field(default=None, foreign_key="vessel.id")
    vessel: Vessel | None = Relationship(back_populates="equipments")
>>>>>>> origin/main:fastapis/app/model/equipment.py

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


<<<<<<< HEAD:fastapis/app/models/equipment.py
class Equipment(EquipmentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # 反向关系到船舶（Vessel）
    vessel: Optional["Vessel"] = Relationship(back_populates="equipments")


=======
>>>>>>> origin/main:fastapis/app/model/equipment.py
class EquipmentCreate(EquipmentBase):
    vessel_id: int | None = Field(default=None, foreign_key="vessel.id")
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
