from pydantic import BaseModel

class AttributeMapping(BaseModel):
    attribute: str
    description: str | None = None

class AttributeMappings(BaseModel):
    attribute_left: AttributeMapping
    attribute_right: AttributeMapping

class LabelValue(BaseModel):
    value: str
    label: str

class AttributeMapping(AttributeMapping):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "attribute": "speed_ground",
                    "description": "对地航速"
                },
                {
                    "attribute": "speed_water",
                    "description": "对水航速"
                },
                {
                    "attribute": "draft",
                    "description": "船艏船尾平均吃水"
                },
                {
                    "attribute": "trim",
                    "description": "船舶纵倾"
                },
                {
                    "attribute": "me_rpm",
                    "description": "主机转速"
                },
                {
                    "attribute": "wind_speed",
                    "description": "风速"
                },
                {
                    "attribute": "wind_direction",
                    "description": "风向"
                },
                {
                    "attribute": "slip_ratio",
                    "description": "滑失比"
                },
                {
                    "attribute": "me_fuel_consumption_nmile",
                    "description": "主机每海里油耗（Kg/NM）"
                },
                {
                    "attribute": "me_fuel_consumption_power",
                    "description": "主机油耗（g/kWh）"
                },
                {
                    "attribute": "me_shaft_power",
                    "description": "主机功率"
                }
            ]
        }
    }

class AttributeMappingUpdate(AttributeMapping):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "attribute": "speed_ground",
                    "description": "更新后的对地航速"
                }
            ]
        }
    }