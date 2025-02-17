import logging

from fastapi import APIRouter, Depends

from app.entity.meta import FuelType, ShipType, TimeZone
from app.model.response import ResponseModel
from app.service.meta import MetaService, get_meta_service

from fastapis.app.model.meta import AttributeMapping, AttributeMappings, LabelValue

logger = logging.getLogger(__name__)

api = APIRouter()


@api.get("/fuel_type", summary="获取燃料类型", response_model=ResponseModel[list[FuelType]])
async def get_fuel_types(
    service: MetaService = Depends(get_meta_service),
) -> ResponseModel[list[FuelType]]:
    """
    “新增船舶”弹窗，选择设备燃料类型
    """
    types = service.get_all_fuel_types()
    return {"code": 200, "data": types, "message": "获取燃料类型成功"}


@api.get("/ship_type", summary="获取船舶类型", response_model=ResponseModel[list[ShipType]])
async def get_ship_types(
    service: MetaService = Depends(get_meta_service),
) -> ResponseModel[list[ShipType]]:
    """
    选择船舶类型
    """
    types = service.get_all_ship_types()
    return {"code": 200, "data": types, "message": "获取船舶类型成功"}


@api.get("/time_zone", summary="获取时区", response_model=ResponseModel[list[TimeZone]])
async def get_time_zones(
    service: MetaService = Depends(get_meta_service),
) -> ResponseModel[list[TimeZone]]:
    """
    获取时区
    """
    types = service.get_all_time_zones()
    return {"code": 200, "data": types, "message": "获取时区成功"}

@api.get("/attributes", summary="属性", response_model=ResponseModel[list[AttributeMapping]])
async def get_attributes(
        service: MetaService = Depends(get_meta_service)
) -> ResponseModel[list[AttributeMapping]]:
    """
    获取属性
    """
    types = service.get_attributes()
    return {"code": 200, "data": types, "message": "获取属性成功"}

@api.get("/attribute_mapping", summary="属性组合", response_model=ResponseModel[list[AttributeMappings]])
async def get_attribute_mapping(
        service: MetaService = Depends(get_meta_service)
) -> ResponseModel[list[AttributeMappings]]:
    """
    获取属性组合
    """
    types = service.get_attribute_mapping()
    return {"code": 200, "data": types, "message": "获取属性组合成功"}

@api.get("/fuel_type_category", summary="获取燃料类型分类", response_model=ResponseModel[list[LabelValue]])
async def get_fuel_type_categories(
        service: MetaService = Depends(get_meta_service)
) -> ResponseModel[list[LabelValue]]:
    """
    获取燃料类型分类
    """
    types = service.get_fuel_type_categories()
    return {"code": 200, "data": types, "message": "获取燃料类型分类成功"}