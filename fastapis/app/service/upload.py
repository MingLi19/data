import datetime
import logging
from datetime import date

from fastapi import Depends
from sqlmodel import Session, select

from app.core.error import NotFoundException
from app.core.mysql import get_mysql_db_session
from app.entity.vessel import Vessel
from app.entity.vessel_data_upload import VesselDataUpload
from app.model.vessel_data_upload import VesselDataUploadCreate

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
