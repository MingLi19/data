from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel
from pydantic import BaseModel

from app.models.equipment_fuel import EquipmentFuel
from app.models.vessel import Vessel

class EquipmentBase(SQLModel):
    name: str = Field(nullable=False, description="设备名称")
    type: str = Field(nullable=False, description="设备类型")
    vessel_id: int = Field(foreign_key="vessel.id")

class Equipment(EquipmentBase, table=True):
    __tablename__ = "equipment"

    id: int | None = Field(default=None, primary_key=True)
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

# 创建模型
class EquipmentCreate(EquipmentBase):
    """
    用于创建设备的数据模型
    """
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Equipment A",
                    "type": "Main Engine",
                    "vessel_id": 1
                }
            ]
        }
    }


# 更新模型
class EquipmentUpdate(BaseModel):
    """
    用于更新设备的数据模型
    """
    name: str | None = Field(description="设备名称")
    type: str | None = Field(description="设备类型")
    vessel_id: int | None = Field(foreign_key="vessel.id", description="所属船")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Updated Equipment Name",
                    "type": "Updated Equipment Type",
                    "vessel_id": 2
                }
            ]
        }
    }