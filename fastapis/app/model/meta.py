from pydantic import BaseModel

class AttributeMapping(BaseModel):
    atrribute: str
    description: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "attribute": "speed_water",
                    "description": "对水航速"
                },
                {
                    "attribute": "me_shaft_power",
                    "description": "主机功率"
                }
            ]
        }
    }

class AttributeMappings(BaseModel):
    attribute_left: AttributeMapping
    attribute_right: AttributeMapping

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "attribute_left": {
                        "atrribute": "speed_water",
                        "description": "对水航速"
                    },
                    "attribute_right": {
                        "atrribute": "me_shaft_power",
                        "description": "主机功率"
                    }
                }
            ]
        }
    }

class LabelValue(BaseModel):
    label: str
    value: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "label": "重油",
                    "value": "hfo"
                }
            ]
        }
    }