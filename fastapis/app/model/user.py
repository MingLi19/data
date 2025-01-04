from sqlmodel import Field, SQLModel

from app.entity.company import Company


class UserBase(SQLModel):
    name: str
    username: str = Field(unique=True, nullable=False)
    hashed_password: str
    phone: str
    is_admin: bool
    is_system_admin: bool
    disabled: bool


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


class UserWithCompany(UserBase):
    company: Company
