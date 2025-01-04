from fastapi import Depends
from sqlmodel import Session, select

from app.core.db import get_db_session
from app.entity.meta import FuelType, ShipType, TimeZone


def get_meta_service(session: Session = Depends(get_db_session)):
    return MetaService(session)


class MetaService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_fuel_types(self) -> list[FuelType]:
        statement = select(FuelType)
        fuel_types = self.session.exec(statement).all()
        return fuel_types

    def get_all_ship_types(self) -> list[ShipType]:
        statement = select(ShipType)
        ship_types = self.session.exec(statement).all()
        return ship_types

    def get_all_time_zones(self) -> list[TimeZone]:
        statement = select(TimeZone)
        time_zones = self.session.exec(statement).all()
        return time_zones
