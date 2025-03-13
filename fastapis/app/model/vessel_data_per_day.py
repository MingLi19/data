from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
from bson import ObjectId

# 定义 VesselDataPerDay 的基础数据模型
class VesselDataPerDayBase(BaseModel):
    speed_ground: float
    speed_water: float
    draft: float
    heel: float
    trim: float
    draught_astern: float
    draught_bow: float
    draught_mid_left: float
    draught_mid_right: float
    me_rpm: float
    wind_speed: float
    wind_direction: float
    slip_ratio: float
    me_fuel_consumption_nmile: float
    me_fuel_consumption_kwh: float
    me_shaft_power: float
    me_torque: float
    me_hfo_act_cons: float
    me_mgo_act_cons: float
    me_hfo_acc_cons: float
    blr_hfo_act_cons: float
    blr_mgo_act_cons: float
    dg_hfo_act_cons: float
    dg_mgo_act_cons: float
    dg_hfo_acc_cons: float
    dg_mgo_acc_cons: float
    fcm_fo_density: float
    blr_fo_density: float
    blr_mgo_density: float
    dg_fo_density: float
    dg_mgo_density: float
    me_fo_in_temp: float
    blr_fo_in_temp: float
    blr_mgo_in_temp: float
    dg_fo_in_temp: float
    dg_mgo_in_temp: float
    dg1_power: float
    dg2_power: float
    dg3_power: float
    CII: float
    CII_temp: float
    created_at: Optional[datetime] = None  # 创建时间戳
    date: date  # 日期
    vessel_id: int  # 船舶 ID

    class Config:
        json_encoders = {
            ObjectId: str
        }

class VesselDataPerDay(VesselDataPerDayBase):
    id: Optional[str] = None

    class Config:
        json_encoders = {
            ObjectId: str
        }
