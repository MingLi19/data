import datetime
import logging
from datetime import date

import pandas as pd
from fastapi import Depends
from sqlmodel import Session, select

from app.core.error import NotFoundException
from app.core.mysql import get_mysql_db_session
from app.entity.vessel import Vessel
from app.entity.vessel_data_upload import VesselDataUpload
from app.model.vessel_data_upload import VesselDataUploadCreate

from fastapis.app.entity.vessel_data_per_day import VesselDataPerDay
from fastapis.app.entity.vessel_standard_data import VesselStandardData
from fastapis.app.model.vessel_standard_data import VesselStandardDataBase

logger = logging.getLogger(__name__)


def get_upload_service(session: Session = Depends(get_mysql_db_session)):
    return UploadService(session)


class UploadService:
    def __init__(self, session: Session = Depends(get_mysql_db_session)):
        self.session = session

    def get_vessel_by_id(self, vessel_id: int) -> Vessel:
        vessel = self.session.get(Vessel, vessel_id)
        if not vessel:
            raise NotFoundException(detail="船舶不存在")
        return vessel

    def get_vessel_data_upload_history(self, vessel_id: int, offset: int, limit: int) -> list[VesselDataUpload]:
        vessel = self.get_vessel_by_id(vessel_id)
        statement = select(VesselDataUpload).where(VesselDataUpload.vessel_id == vessel.id).offset(offset).limit(limit)
        data = self.session.exec(statement).all()
        return data

    async def create_vessel_data_upload(self, vessel_id: int, request: VesselDataUploadCreate) -> VesselDataUpload:
        vessel = self.get_vessel_by_id(vessel_id)
        vessel_data_upload = VesselDataUpload(vessel_id=vessel.id, **request.model_dump())
        self.session.add(vessel_data_upload)
        self.session.commit()
        return vessel_data_upload

    def get_data_by_vessel_id(self, vessel_id: int) -> list:
        # 获取指定船舶的数据
        statement = select(VesselDataUpload).where(VesselDataUpload.vessel_id == vessel_id)
        data = self.session.exec(statement).all()
        return data

    def insert_data(self, vessel_id: int, file_path: str, date_start: date | None, date_end: date | None):
        # 获取船舶数据
        vessel = self.session.get(Vessel, vessel_id)
        if not vessel:
            raise NotFoundException(detail="船舶不存在")

        # 创建新的 VesselDataUpload 实例
        vessel_data_upload = VesselDataUpload(
            vessel_id=vessel.id,  # 使用传递的 vessel_id
            file_path=file_path,
            date_start=date_start,
            date_end=date_end,
            created_at=datetime.datetime.now(),  # 设置创建时间
        )

        # 插入数据
        self.session.add(vessel_data_upload)
        self.session.commit()
        return vessel_data_upload

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """数据清洗"""
        df = df.dropna()  # 去除缺失值
        df = df[df["value"] > 0]  # 去除异常值（示例）
        return df

    async def insert_standard_data(self, vessel_id: int, standard_data_base: list[VesselStandardDataBase]) -> None:
        for standart_data_row in standard_data_base:
            standart_data = VesselStandardData(
                vessel_id=vessel_id, **standart_data_row.model_dump())
            self.session.add(standart_data)
        self.session.commit()

    async def insert_data_per_day(self, vessel_id: int, standard_data_base: list[VesselStandardDataBase]) -> None:
        """
        pandas groupby date
        """
        df = pd.DataFrame([VesselDataPerDay(**d.model_dump()).model_dump()
                          for d in standard_data_base])
        df = df.groupby('date').agg('mean').reset_index()
        data = df.to_dict(orient='records')
        for d in data:
            data_per_day = VesselDataPerDay(
                vessel_id=vessel_id, **d)
            old_data_per_day = self.session.get(
                VesselDataPerDay, (data_per_day.date, vessel_id))
            if old_data_per_day:
                self.session.delete(old_data_per_day)
                self.session.commit()
            self.session.add(data_per_day)
            self.session.commit()