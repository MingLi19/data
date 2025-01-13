from pydantic import BaseModel
from sqlmodel import Field

from app.entity.company import Company


class UserBase(BaseModel):
    name: str = Field(nullable=False)
    username: str = Field(unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    phone: str = Field(nullable=False)
    is_admin: bool = False
    is_system_admin: bool = False
    disabled: bool = False


class UserCreate(UserBase):
    company_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Jayzhu",
                    "username": "jayzhu",
                    "hashed_password": "123456789",
                    "phone": "12345678999",
                    "is_admin": True,
                    "is_system_admin": False,
                    "disabled": False,
                    "company_id": 1,
                }
            ]
        }
    }


class UserUpdate(UserBase):
    company_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Jayzhu Updated",
                    "username": "jayzhu",
                    "hashed_password": "123456789",
                    "phone": "12345678999",
                    "is_admin": True,
                    "is_system_admin": False,
                    "disabled": False,
                    "company_id": 1,
                }
            ]
        }
    }


class UserPublic(UserBase):
    id: int
    company: Company
