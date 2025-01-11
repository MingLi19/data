from sqlmodel import Field, SQLModel


class EquipmentFuel(SQLModel, table=True):
    __tablename__ = "equipment_fuel"

    id: int | None = Field(default=None, primary_key=True)
    equipment_id: int = Field(foreign_key="equipment.id", ondelete="CASCADE")
    fuel_type_id: int = Field(foreign_key="fuel_type.id")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "equipment_id": 1,
                    "fuel_type_id": 1,
                    "created_at": "2021-01-01T00:00:00",
                    "updated_at": "2021-01-01T00:00:00",
                }
            ]
        }
    }
