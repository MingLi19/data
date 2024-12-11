from datetime import datetime

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: str = Field(unique=True, nullable=False)
    username: str
    hashed_password: str
    phone: str
    is_admin: bool
    is_system_admin: bool
    disabled: bool
    created_at: datetime
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


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(UserBase):
    pass

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


class UserUpdate(BaseModel):
    name: str = Field(unique=True, nullable=False)
    username: str
    hashed_password: str
    phone: str
    is_admin: bool
    is_system_admin: bool
    disabled: bool
    created_at: datetime
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
