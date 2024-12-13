import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Path


from app.models.equipment import Equipment, EquipmentCreate, EquipmentUpdate
from models.response import ResponseModel
from app.services.equipment import EquipmentService, get_equipment_service

api = APIRouter()

logger = logging.getLogger(__name__)

@api.get("", summary="获取设备列表")
async def get_equipments(
    service: EquipmentService = Depends(get_equipment_service),
) -> ResponseModel[list[Equipment]]:
    """
    用来显示设备列表
    """
    equipments = service.get_all_equipments()
    return {"code": 200, "data": equipments, "message": "获取设备列表成功"}

@api.get("/{equipment_id}", summary="获取设备详情")
async def get_equipment(
    equipment_id: Annotated[int, Path(description="设备ID")],
    service: EquipmentService = Depends(get_equipment_service),
) -> ResponseModel[Equipment]:
    """
    用来显示设备详情
    """
    equipment = service.get_equipment_by_id(equipment_id)
    return {"code": 200, "data": equipment, "message": "获取设备详情成功"}

@api.post("", summary="创建设备")
async def create_equipment(
    equipment: EquipmentCreate,
    service: EquipmentService = Depends(get_equipment_service),
) -> ResponseModel[Equipment]:
    equipment = service.create_equipment(equipment)
    return {"code": 200, "data": equipment, "message": "创建设备成功"}

@api.put("/{equipment_id}", summary="更新设备信息")
async def update_equipment(
    equipment_id: int,
    equipment: EquipmentUpdate,
    service: EquipmentService = Depends(get_equipment_service),
) -> ResponseModel[Equipment]:
    equipment = service.update_equipment(equipment_id, equipment)
    return {"code": 200, "data": equipment, "message": "更新设备信息成功"}

@api.delete("/{equipment_id}", summary="删除设备")
async def delete_equipment(
    equipment_id: int, service: EquipmentService = Depends(get_equipment_service)
) -> ResponseModel[Equipment]:
    equipment = service.delete_equipment(equipment_id)
    return {"code": 200, "data": equipment, "message": "删除设备成功"}


