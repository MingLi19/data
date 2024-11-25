from core.db import get_db_session
from fastapi import Depends, HTTPException
from models.master import ShipType
from sqlmodel import Session, select
from sqlalchemy import and_


def get_master_service(session: Session = Depends(get_db_session)):
    return MasterService(session)


class MasterService:
    def __init__(self, session: Session):
        self.session = session

    def get_ship_types(self, name_cn=None, name_en=None, code=None) -> list[ShipType]:
        statement = select(ShipType).filter(
            and_(
                ShipType.name_cn == name_cn if name_cn else True,
                ShipType.name_en == name_en if name_en else True,
                ShipType.code == code if code else True,
            )
        )
        ship_types = self.session.exec(statement).all()
        return ship_types

    def insert_ship_type(self, name_cn, name_en, code):
        if self.get_ship_types(name_cn=name_cn):
            raise HTTPException(
                status_code=500,
                detail=f"{name_cn}对应数据已经存在")
        self.session.add(ShipType(
            name_cn=name_cn,
            name_en=name_en,
            code=code))
        self.session.commit()
        return 'ok'


