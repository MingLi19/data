import logging

from fastapi import APIRouter, Depends
from models.meta import FuelType
from models.meta import ShipType
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


@api.get(
    "/ship_type", summary="获取船舶类型", response_model=ResponseModel[list[ShipType]]
)
async def get_ship_types(
    service: MetaService = Depends(get_meta_service),
) -> ResponseModel[list[ShipType]]:
    """
    “新增船舶”弹窗，选择设备船舶类型
    """
    types = service.get_all_ship_types()
    return {"code": 200, "data": types, "message": "获取船舶类型成功"}
