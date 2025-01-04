from sqlmodel import Field, SQLModel


class CompanyBase(SQLModel):
    name: str = Field(unique=True, nullable=False)
    address: str | None = None
    contact_person: str | None = None
    contact_phone: str | None = None
    contact_email: str | None = None


class CompanyCreate(CompanyBase):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Company A",
                    "address": "123 Main St, New York, NY",
                    "contact_person": "John Doe",
                    "contact_phone": "12345678",
                    "contact_email": "test@163.com",
                }
            ]
        }
    }


class CompanyUpdate(CompanyBase):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Company A Updated",
                    "address": "123 Main St, New York, NY",
                    "contact_person": "John Doe",
                    "contact_phone": "12345678",
                    "contact_email": "test@163.com",
                }
            ]
        }
    }
