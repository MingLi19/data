from app.core.db import get_db_session
from app.models.meta import FuelType
from fastapi import Depends, HTTPException
from sqlmodel import Session, select


def get_meta_service(session: Session = Depends(get_db_session)):
    return MetaService(session)


class MetaService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_fuel_types(self) -> list[FuelType]:
        statement = select(FuelType)
        fuel_types = self.session.exec(statement).all()
        return fuel_types
