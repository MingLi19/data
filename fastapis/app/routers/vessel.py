import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Path

# from models.equipment import Equipment
from models.response import ResponseModel
from models.vessel import Vessel, VesselCreate, VesselUpdate
from services.vessel import VesselService, get_vessel_service

api = APIRouter()

logger = logging.getLogger(__name__)


@api.get("", summary="获取所有船舶")
async def get_vessels(
    service: VesselService = Depends(get_vessel_service),
) -> ResponseModel[list[Vessel]]:
    """
    用来显示船舶列表
    """
    vessels = service.get_all_vessels()
    return {"code": 200, "data": vessels, "message": "获取船舶列表成功"}


@api.post("", summary="创建船舶")
async def create_vessel(
    vessel: VesselCreate, service: VesselService = Depends(get_vessel_service)
) -> ResponseModel[Vessel]:
    vessel = service.create_vessel(vessel)
    return {"code": 200, "data": vessel, "message": "船舶创建成功"}


@api.get("/{vessel_id}", summary="获取单个船舶详情")
async def get_vessel(
    vessel_id: Annotated[int, Path(description="船舶ID")],
    service: VesselService = Depends(get_vessel_service),
) -> ResponseModel[Vessel]:
    """
    首页，显示船舶信息
    """
    vessel = service.get_vessel_by_id(vessel_id)
    return {"code": 200, "data": vessel, "message": "获取船舶信息成功"}


@api.put("/{vessel_id}", summary="更新船舶信息")
async def update_vessel(
    vessel_id: int,
    vessel: VesselUpdate,
    service: VesselService = Depends(get_vessel_service),
) -> ResponseModel[Vessel]:
    vessel = service.update_vessel(vessel_id, vessel)
    return {"code": 200, "data": vessel, "message": "船舶信息更新成功"}


@api.delete("/{vessel_id}", summary="删除船舶")
async def delete_vessel(
    vessel_id: int, service: VesselService = Depends(get_vessel_service)
) -> ResponseModel[Vessel]:
    vessel = service.delete_vessel(vessel_id)
    return {"code": 200, "data": vessel, "message": "船舶删除成功"}


@api.get("/{vessel_id}/equipments", summary="获取船舶设备")
async def get_equipments_by_vessel_id(
    vessel_id: Annotated[int, Path(description="船舶ID")],
    service: VesselService = Depends(get_vessel_service),
) -> ResponseModel[Vessel]:
    """
    用来显示船舶设备列表
    """
    equioments = service.get_equipments_by_vessel_id(vessel_id)
    return {"code": 200, "data": equioments, "message": "获取船舶设备成功"}
