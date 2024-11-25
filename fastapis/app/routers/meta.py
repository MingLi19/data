import logging

from fastapi import APIRouter, Depends
from models.meta import FuelType, FuelTypeInsert
from models.response import ResponseModel
from services.meta import MetaService, get_meta_service

logger = logging.getLogger(__name__)

api = APIRouter()


@api.get(
    "/fuel_type", summary="获取燃料类型", response_model=ResponseModel[list[FuelType]]
)
async def get_fuel_types(
    service: MetaService = Depends(get_meta_service),
) -> ResponseModel[list[FuelType]]:
    """
    “新增船舶”弹窗，选择设备燃料类型
    """
    types = service.get_all_fuel_types()
    return {"code": 200, "data": types, "message": "获取燃料类型成功"}


@api.post("/fuel_type", summary='添加燃料类型数据')
async def insert_fuel_type(
        fuel_type: FuelTypeInsert,
        service: MetaService = Depends(get_meta_service)
):
    """
    新增一条燃料类型数据
    """
    res = service.insert_fuel_type(**fuel_type)
    return {"code": 200, "data": res, "message": "添加燃料类型数据成功"}


@api.post("/new_table", summary='创建未创建数据表')
async def create_fuel_type(
        service: MetaService = Depends(get_meta_service),
):
    """
    创建未创建数据表
    """
    res = service.create_new_tale()
    return {"code": 200, "data": res, "message": "创建未创建数据表成功"}
