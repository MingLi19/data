
from pydantic import BaseModel


class VesselDataPerDayBase(BaseModel):
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

class VesselDataPerDayCreate(VesselDataPerDayBase):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                     "date": "2025-01-01",
                    "vessel_id": 1,
                    "speed_ground": 12.5,
                    "speed_water": 10.2,
                    "draft": 5.0,
                    "heel": 0.3,
                    "trim": 0.1,
                    "draught_astern": 4.8,
                    "draught_bow": 5.2,
                    "draught_mid_left": 5.0,
                    "draught_mid_right": 5.0,
                    "me_rpm": 1500,
                    "wind_speed": 8.0,
                    "wind_direction": 45,
                    "slip_ratio": 0.05,
                    "me_fuel_consumption_nmile": 10.0,
                    "me_fuel_consumption_kwh": 200.0,
                    "me_shaft_power": 1000.0,
                    "me_torque": 2000.0,
                    "me_hfo_act_cons": 50.0,
                    "me_mgo_act_cons": 20.0,
                    "me_hfo_acc_cons": 100.0,
                    "blr_hfo_act_cons": 30.0,
                    "blr_mgo_act_cons": 10.0,
                    "dg_hfo_act_cons": 20.0,
                    "dg_mgo_act_cons": 5.0,
                    "dg_hfo_acc_cons": 50.0,
                    "dg_mgo_acc_cons": 10.0,
                    "fcm_fo_density": 0.85,
                    "blr_fo_density": 0.85,
                    "blr_mgo_density": 0.88,
                    "dg_fo_density": 0.85,
                    "dg_mgo_density": 0.88,
                    "me_fo_in_temp": 40.0,
                    "blr_fo_in_temp": 30.0,
                    "blr_mgo_in_temp": 35.0,
                    "dg_fo_in_temp": 45.0,
                    "dg_mgo_in_temp": 40.0,
                    "dg1_power": 500.0,
                    "dg2_power": 400.0,
                    "dg3_power": 300.0,
                    "CII": 1.5,
                    "CII_temp": 20.0,
                    "created_at": "2025-01-01T12:00:00",
                }
            ]
        }
    }

