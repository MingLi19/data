from core.db import get_db_session
from fastapi import Depends, HTTPException
from models.meta import FuelType
from sqlmodel import Session, select
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base


def get_meta_service(session: Session = Depends(get_db_session)):
    return MetaService(session)


class MetaService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_fuel_types(self) -> list[FuelType]:
        statement = select(FuelType)
        fuel_types = self.session.exec(statement).all()
        return fuel_types

    def insert_fuel_type(self, name_cn, name_en, name_abbr, cf):
        statement = select(FuelType).filter(FuelType.name_cn == name_cn)
        check_existence = self.session.exec(statement).all()
        if check_existence:
            raise HTTPException(
                status_code=500,
                detail=f"{name_cn}对应数据已存在"
            )
        self.session.add(FuelType(
            name_cn=name_cn,
            name_en=name_en,
            name_abbr=name_abbr,
            cf=cf))
        self.session.commit()
        return 'ok'

    def create_new_tale(self):
        metadata = MetaData()
        metadata.reflect(bind=self.session)
        Base = declarative_base()
        Base.metadata.create_all(self.session)
        return 'ok'

