from datetime import datetime
from sqlmodel import Field, SQLModel
from pydantic import BaseModel

class EquipmentBase(SQLModel):
    """
    船舶设备的基础模型
    """
    name: str = Field(nullable=False, description="设备名称")
    type: str = Field(nullable=False, description="设备类型")
    vessel_id: int = Field(nullable=False, description="所属船舶ID")

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


class EquipmentCreate(EquipmentBase):
    """
    用于创建船舶设备的模型
    """
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

    name: str | None = Field(default=None, description="设备名称")
    type: str | None 
    vessel_id: int | None 


class EquipmentUpdate(BaseModel):
    name: str | None 
    type: str | None 
    vessel_id: int | None 

