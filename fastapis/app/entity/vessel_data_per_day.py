from datetime import datetime

from sqlmodel import Field, SQLModel


class VesselDataPerDayBase(SQLModel):
    speed_ground: float = 0
    speed_water: float = 0
    draft: float = 0
    heel: float = 0
    trim: float = 0
    draught_astern: float = 0
    draught_bow: float = 0
    draught_mid_left: float = 0
    draught_mid_right: float = 0
    me_rpm: float = 0
    wind_speed: float = 0
    wind_direction: float = 0
    slip_ratio: float = 0
    me_fuel_consumption_nmile: float = 0
    me_fuel_consumption_kwh: float = 0
    me_shaft_power: float = 0
    me_torque: float = 0
    me_hfo_act_cons: float = 0
    me_mgo_act_cons: float = 0
    me_hfo_acc_cons: float = 0
    blr_hfo_act_cons: float = 0
    blr_mgo_act_cons: float = 0
    dg_hfo_act_cons: float = 0
    dg_mgo_act_cons: float = 0
    dg_hfo_acc_cons: float = 0
    dg_mgo_acc_cons: float = 0
    fcm_fo_density: float = 0
    blr_fo_density: float = 0
    blr_mgo_density: float = 0
    dg_fo_density: float = 0
    dg_mgo_density: float = 0
    me_fo_in_temp: float = 0
    blr_fo_in_temp: float = 0
    blr_mgo_in_temp: float = 0
    dg_fo_in_temp: float = 0
    dg_mgo_in_temp: float = 0
    dg1_power: float = 0
    dg2_power: float = 0
    dg3_power: float = 0
    CII: float = 0
    CII_temp: float = 0


class VesselDataPerDay(VesselDataPerDayBase, table=True):
    __tablename__ = "vessel_data_per_day"
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow)
    date: datetime.date = Field(primary_key=True)
    vessel_id: int = Field(foreign_key="vessel.id", primary_key=True)
