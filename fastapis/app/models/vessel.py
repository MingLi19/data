from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

# 导入 Equipment 类，如果使用相对导入，可以根据你的项目结构调整路径
from .equipment import Equipment  # 或者直接使用 "equipment" 作为字符串


# Vessel 基础类，定义字段
class VesselBase(SQLModel):
    name: str = Field(unique=True, nullable=False)  # 船名，必填且唯一
    mmsi: str = Field(unique=True, nullable=False)  # 海事识别号，必填且唯一
    build_date: str  # 建造日期，格式为 'YYYY-MM-DD'
    gross_tone: float  # 总吨位
    dead_weight: float  # 装载吨位
    new_vessel: bool  # 是否为新船
    hull_clean_date: str | None  # 船体清洁日期
    engine_overhaul_date: str | None  # 发动机检修日期
    newly_paint_date: str | None  # 新涂装日期
    propeller_polish_date: str | None  # 螺旋桨抛光日期
    company_id: int  # 公司ID
    ship_type: int  # 船舶类型
    time_zone: int  # 时区

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "船名",
                    "mmsi": "海事识别号",
                    "build_date": "2024-12-06",
                    "gross_tone": 1.0,
                    "dead_weight": 2.0,
                    "new_vessel": True,
                    "hull_clean_date": None,
                    "engine_overhaul_date": None,
                    "newly_paint_date": None,
                    "propeller_polish_date": None,
                    "company_id": 1,
                    "ship_type": 3,
                    "time_zone": 4,
                }
            ]
        }
    }


# Vessel 模型，表结构定义
class Vessel(VesselBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # 反向关系，表示一个船舶可以有多个设备
    # 使用字符串注释来避免循环引用问题
    equipments: list["Equipment"] = Relationship(back_populates="vessel")


# 创建 Vessel 时使用的模型
class VesselCreate(VesselBase):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "船名",
                    "mmsi": "海事识别号",
                    "build_date": "2024-12-06",
                    "gross_tone": 1.0,
                    "dead_weight": 2.0,
                    "new_vessel": True,
                    "hull_clean_date": "2024-12-06",
                    "engine_overhaul_date": "2024-12-06",
                    "newly_paint_date": "2024-12-06",
                    "propeller_polish_date": "2024-12-06",
                    "company_id": 1,
                    "ship_type": 3,
                    "time_zone": 4,
                }
            ]
        }
    }


# 更新 Vessel 时使用的模型，继承 VesselBase 来避免重复字段定义
class VesselUpdate(VesselBase):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "船名",
                    "mmsi": "海事识别号",
                    "build_date": "2024-12-06",
                    "gross_tone": 1.0,
                    "dead_weight": 2.0,
                    "new_vessel": True,
                    "hull_clean_date": "2024-12-06",
                    "engine_overhaul_date": "2024-12-06",
                    "newly_paint_date": "2024-12-06",
                    "propeller_polish_date": "2024-12-06",
                    "company_id": 1,
                    "ship_type": 3,
                    "time_zone": 4,
                }
            ]
        }
    }
