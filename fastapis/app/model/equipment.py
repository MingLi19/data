from sqlmodel import SQLModel


class EquipmentBase(SQLModel):
    name: str | None
    type: str | None


class EquipmentCreate(EquipmentBase):
    pass

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


class EquipmentUpdate(SQLModel):
    name: str | None
    type: str | None
