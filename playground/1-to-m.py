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


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    with Session(engine) as session:
        vessel = Vessel(name="Titanic")
        me = Equipment(name="ME")
        dg = Equipment(name="DG")
        me.vessel = vessel
        dg.vessel = vessel
        session.add(vessel)
        session.commit()


def main():
    create_db_and_tables()
    create_heroes()


if __name__ == "__main__":
    main()
