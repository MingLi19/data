import logging

from fastapi import APIRouter, Depends, Query
from models.master import ShipType, ShipTypeInsert
from models.response import ResponseModel
from services.master import MasterService, get_master_service

logger = logging.getLogger(__name__)

api = APIRouter()


@api.get("/ship_type", summary="获取船舶类型", response_model=ResponseModel[list[ShipType]])
async def get_fuel_types(
        name_cn: str = Query(None, description='船舶类型中文名称'),
        name_en: str = Query(None, description='船舶类型英文名称'),
        code: str = Query(None, description='船舶类型代码'),
        service: MasterService = Depends(get_master_service)
):
    """
    输出符合条件船舶类型
    """
    types = service.get_ship_types(name_cn, name_en, code)
    return {"code": 200, "data": types, "message": "获取船舶类型成功"}


@api.post("/ship_type", summary='添加船舶类型数据')
async def insert_fuel_type(
        ship_type: ShipTypeInsert,
        service: MasterService = Depends(get_master_service)
):
    """
    插入一条船舶类型数据
    """
    res = service.insert_ship_type(**ship_type)
    return {"code": 200, "data": res, "message": "擦汗如船舶类型数据成功"}



