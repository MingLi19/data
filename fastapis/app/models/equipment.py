from datetime import datetime

from sqlmodel import Field, SQLModel

# from models.vessel import Vessel


class EquipmentBase(SQLModel):
    name: str = Field(nullable=False)  # 设备名称，必填
    type: str = Field(nullable=False)  # 设备类型，必填
    vessel_id: int = Field(nullable=False, foreign_key="vessel.id")  # 所属船舶，必填

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "设备名称",
                    "type": "设备类型",
                    "vessel_id": 1,
                }
            ]
        }
    }


class Equipment(EquipmentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # vessel: Vessel = Relationship(back_populates="equipments")
