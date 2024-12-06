from sqlmodel import Field, SQLModel


## Data Modal -> Meta Data -> Fuel Type
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


## Data Modal -> Meta Data -> Ship Type
class ShipType(SQLModel, table=True):
    __tablename__ = "ship_type"
    id: int = Field(primary_key=True)
    name_cn: str
    name_en: str
    code: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name_cn": "散货船",
                    "name_en": "Bulk carrier",
                    "code": "I001",
                }
            ]
        }
    }


class TimeZone(SQLModel, table=True):
    __tablename__ = "time_zone"
    id: int = Field(primary_key=True)
    name_cn: str
    name_en: str
    explaination: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name_cn": "中国标准时间",
                    "name_en": "China Standard Time",
                    "explaination": "UTC+8",
                }
            ]
        }
    }


class User(SQLModel, table=True):
    __tablename__ = "user"
    id: int = Field(primary_key=True)
    username: str
    hashed_password: str
    phone: str
    is_admin: bool
    is_system_admin: bool
    disabled: bool
    created_at: int
    company_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "username": "Jayzhu",
                    "hashed_password": "123456789",
                    "phone": "12345678999",
                    "is_admin": True,
                    "is_system_admin": False,
                    "disabled": False,
                    "created_at": "2024-12-01",
                    "company_id": 101,
                }
            ]
        }
    }
