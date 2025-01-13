from sqlmodel import Field, SQLModel


class EquipmentFuel(SQLModel, table=True):
    __tablename__ = "equipment_fuel"

    equipment_id: int | None = Field(default=None, primary_key=True, foreign_key="equipment.id", ondelete="CASCADE")
    fuel_type_id: int | None = Field(default=None, primary_key=True, foreign_key="fuel_type.id")
