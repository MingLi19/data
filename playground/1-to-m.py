from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class Vessel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    equipments: list["Equipment"] = Relationship(back_populates="vessel")


class Equipment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    vessel_id: int | None = Field(default=None, foreign_key="vessel.id")
    vessel: Vessel | None = Relationship(back_populates="equipments")


class EquipmentCreate(SQLModel):
    name: str


class VesselCreate(SQLModel):
    name: str
    equipments: list["EquipmentCreate"]  # noqa: F821


sqlite_file_name = "playground/test.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    with Session(engine) as session:
        vesselCreate = VesselCreate(name="Titanic", equipments=[])
        vessel = Vessel.model_validate(vesselCreate)
        meCreate = EquipmentCreate(name="ME")
        dgCreate = EquipmentCreate(name="DG")
        me = Equipment.model_validate(meCreate)
        dg = Equipment.model_validate(dgCreate)
        vessel.equipments = [me, dg]
        session.add(vessel)
        session.commit()


def main():
    create_db_and_tables()
    create_heroes()


if __name__ == "__main__":
    main()
