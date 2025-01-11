from enum import Enum

from sqlmodel import SQLModel


class EquipmentType(str, Enum):
    me = "me"
    dg = "dg"
    blr = "blr"


class EquipmentBase(SQLModel):
    name: str
    type: EquipmentType


class EquipmentCreate(EquipmentBase):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "发动机",
                    "type": "me",
                },
            ]
        }
    }


class EquipmentUpdate(SQLModel):
    name: str | None
    type: str | None
