from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from .vessel import Vessel  # 导入 Vessel 类


class EquipmentBase(SQLModel):
    name: str | None
    type: str | None
    vessel_id: int | None = Field(
        default=None, foreign_key="vessel.id"
    )  # 外键，关联到 Vessel 表

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

    # 关联 Vessel 表，表示一个设备属于一个船舶
    vessel: Vessel = Relationship(back_populates="equipments")  # 使用正确的类名 Vessel


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
