from datetime import datetime

from sqlmodel import Field, SQLModel

from .vessel import Relationship, Vessel


class EquipmentBase(SQLModel):
    name: str | None
    type: str | None
    vessel_id: int | None = Field(default=None, primary_key=True)

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
