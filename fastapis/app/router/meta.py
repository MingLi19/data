import logging

from app.models.meta import FuelType
from app.models.response import ResponseModel
from app.services.meta import MetaService, get_meta_service
from fastapi import APIRouter, Depends

logger = logging.getLogger(__name__)

api = APIRouter()


@api.get("/fuel_type", summary="获取燃料类型", response_model=ResponseModel[list[FuelType]])
async def get_fuel_types(service: MetaService = Depends(get_meta_service)) -> ResponseModel[list[FuelType]]:
    """
    “新增船舶”弹窗，选择设备燃料类型
    """
    types = service.get_all_fuel_types()
    return {"code": 200, "data": types, "message": "获取燃料类型成功"}
