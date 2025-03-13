import logging

from motor.motor_asyncio import AsyncIOMotorClient
import pandas as pd
from fastapi import Depends


from app.core.mongo import get_mondo_db_client

from fastapis.app.model.vessel_data_per_day import VesselDataPerDay
from fastapis.app.model.vessel_standard_data import VesselStandardDataBase

logger = logging.getLogger(__name__)


def get_dataUpload_service(db: AsyncIOMotorClient = Depends(get_mondo_db_client)):
    return dataUploadService(db)


class dataUploadService:
    def __init__(self, db: AsyncIOMotorClient = Depends(get_mondo_db_client)):
        self.db = db
        self.standard_data_collection = self.db.vesselStandardData.vessel_standard_data
        self.data_per_day_collection = self.db.vesselDataPerDay.vessel_data_per_day


    def clean_data(self, data: list[VesselStandardDataBase]) -> list[VesselStandardDataBase]:
        """
        数据清洗，去除缺失值和异常值
        """
        df = pd.DataFrame([d.dict() for d in data])
        df = df.dropna()
        df = df[df["value"] > 0]
        cleaned_data = [VesselStandardDataBase(**row) for row in df.to_dict(orient="records")]
        return cleaned_data

    async def insert_standard_data(self, vessel_id: int, standard_data_base: list[VesselStandardDataBase]) -> None:
        """
        插入标准数据到 MongoDB
        """
        for standard_data_row in standard_data_base:
            data_dict = standard_data_row.dict()
            data_dict["vessel_id"] = vessel_id
            await self.standard_data_collection.insert_one(data_dict)

    async def insert_data_per_day(self, vessel_id: int, standard_data_base: list[VesselStandardDataBase]) -> None:
        """
        按天分组数据并插入 MongoDB
        """
        # 将标准数据转换为 DataFrame
        df = pd.DataFrame([VesselDataPerDay(**d.dict()).dict() for d in standard_data_base])
        df["date"] = pd.to_datetime(df["date"])
        df = df.groupby(df["date"].dt.date).agg("mean").reset_index()
        data = df.to_dict(orient="records")

        # 插入/更新数据
        for d in data:
            # 检查是否已有该日期的数据
            existing_data = await self.data_per_day_collection.find_one({"vessel_id": vessel_id, "date": d["date"]})
            if existing_data:
                await self.data_per_day_collection.replace_one({"_id": existing_data["_id"]}, d)
            else:
                d["vessel_id"] = vessel_id
                await self.data_per_day_collection.insert_one(d)