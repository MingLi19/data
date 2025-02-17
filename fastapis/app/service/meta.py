from fastapi import Depends
from sqlmodel import Session, select

from app.core.mysql import get_mysql_db_session
from app.entity.meta import FuelType, ShipType, TimeZone

from app.model.meta import AttributeMapping, AttributeMappings, LabelValue




def get_meta_service(session: Session = Depends(get_mysql_db_session)):
    return MetaService(session)


class MetaService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_fuel_types(self) -> list[FuelType]:
        statement = select(FuelType)
        fuel_types = self.session.exec(statement).all()
        return fuel_types

    def get_all_ship_types(self) -> list[ShipType]:
        statement = select(ShipType)
        ship_types = self.session.exec(statement).all()
        return ship_types

    def get_all_time_zones(self) -> list[TimeZone]:
        statement = select(TimeZone)
        time_zones = self.session.exec(statement).all()
        return time_zones

    def get_attributes(self) -> list[AttributeMapping]:
        attributes = [
            AttributeMapping(attribute="speed_ground", description="对地航速"),
            AttributeMapping(attribute="speed_water", description="对水航速"),
            AttributeMapping(attribute="draft", description="船艏船尾平均吃水"),
            AttributeMapping(attribute="trim", description="船舶纵倾"),
            AttributeMapping(attribute="me_rpm", description="主机转速"),
            AttributeMapping(attribute="wind_speed", description="风速"),
            AttributeMapping(attribute="wind_direction", description="风向"),
            AttributeMapping(attribute="slip_ratio", description="滑失比"),
            AttributeMapping(
                attribute="me_fuel_consumption_nmile", description="主机每海里油耗（Kg/NM）"
            ),
            AttributeMapping(
                attribute="me_fuel_consumption_power", description="主机油耗（g/kWh）"
            ),
            AttributeMapping(attribute="me_shaft_power", description="主机功率"),
        ]
        return attributes

    def get_attribute_mapping(self) -> list[AttributeMappings]:
        mappings = [
            AttributeMappings(
                attribute_left=AttributeMapping(attribute="speed_water", description="对水航速"),
                attribute_right=AttributeMapping(
                    attribute="me_shaft_power", description="主机功率"
                ),
            ),
            AttributeMappings(
                attribute_left=AttributeMapping(attribute="speed_water", description="对水航速"),
                attribute_right=AttributeMapping(
                    attribute="me_fuel_consumption_nmile", description="主机每海里油耗（Kg/NM）"
                ),
            ),
            AttributeMappings(
                attribute_left=AttributeMapping(attribute="me_rpm", description="主机转速"),
                attribute_right=AttributeMapping(
                    attribute="me_shaft_power", description="主机功率"
                ),
            ),
            AttributeMappings(
                attribute_left=AttributeMapping(attribute="me_rpm", description="主机转速"),
                attribute_right=AttributeMapping(
                    attribute="me_fuel_consumption_power", description="主机功率油耗（g/kWh）"
                ),
            ),
            AttributeMappings(
                attribute_left=AttributeMapping(
                    attribute="me_fuel_consumption_power", description="主机功率油耗（g/kWh）"
                ),
                attribute_right=AttributeMapping(
                    attribute="me_shaft_power", description="主机功率"
                ),
            ),
        ]
        return mappings

    def get_fuel_type_categories(self) -> list[LabelValue]:
        catecory_list = [
            LabelValue(value="hfo", label="重油"),
            LabelValue(value="lfo", label="轻油"),
            LabelValue(value="mgo", label="船舶柴油"),
            LabelValue(value="mdo", label="船舶柴油"),
            LabelValue(value="lng", label="液化天然气"),
            LabelValue(value="lpg_p", label="液化石油气(丙烷)"),
            LabelValue(value="lpg_b", label="液化石油气(丁烷)"),
            LabelValue(value="methanol", label="甲醇"),
            LabelValue(value="ethanol", label="乙醇"),
            LabelValue(value="ethane", label="乙烷"),
            LabelValue(value="ammonia", label="氨"),
            LabelValue(value="hydrogen", label="氢"),
        ]
        return catecory_list