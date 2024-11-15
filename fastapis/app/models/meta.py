from sqlmodel import Field, SQLModel


class FuelType(SQLModel, table=True):
    __tablename__ = "fuel_type"
    id: int = Field(primary_key=True)
    name_cn: str
    name_en: str
    name_abbr: str
    cf: float

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name_cn": "液化天然气",
                    "name_en": "Liquefied Natural Gas",
                    "name_abbr": "LNG",
                    "cf": 2.75,
                }
            ]
        }
    }
