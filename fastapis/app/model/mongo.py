from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

from app.core.config import COLLECTION_NAME, DATABASE_NAME, MONGO_DETAILS

# 创建MongoDB客户端和数据库
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]


class ItemBase(BaseModel):
    name: str
    description: str


class ItemCreate(ItemBase):
    pass


class ItemInDB(ItemBase):
    id: str

    class Config:
        orm_mode = True
