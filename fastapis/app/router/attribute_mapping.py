from fastapi import APIRouter
from app.model.attributes import AttributeMapping, AttributeMappings,LabelValue


router = APIRouter()

@router.get("/attributes", response_model=list[AttributeMapping],summary="获取船舶属性")
def get_attributes():
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


@router.get("/attribute_mapping", response_model=list[AttributeMapping],summary="获取船舶属性的映射关系")
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

@router.get("/fuel_types", response_model=list[LabelValue],summary="获取燃油种类")
def get_fuel_type_categories(self) -> list[LabelValue]:
    category_list = [
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
    return category_list