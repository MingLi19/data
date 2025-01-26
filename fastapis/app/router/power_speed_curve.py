import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Path

from app.entity.power_speed_curve import PowerSpeedCurve
from app.model.response import ResponseModel
from app.model.power_speed_curve import PowerSpeedCurveCreate, PowerSpeedCurvePublic
from app.service.power_speed_curve import PowerSpeedCurveService, get_power_speed_curve_service

api = APIRouter()

logger = logging.getLogger(__name__)


@api.get("", summary="获取所有功率-速度曲线")
async def get_power_speed_curves(
    service: PowerSpeedCurveService = Depends(get_power_speed_curve_service),
) -> ResponseModel[list[PowerSpeedCurve]]:
    curves = service.get_all_curves()
    return {"code": 200, "data": curves, "message": "获取功率-速度曲线成功"}


@api.post("", summary="创建功率-速度曲线")
async def create_power_speed_curve(
    curve: PowerSpeedCurveCreate, 
    service: PowerSpeedCurveService = Depends(get_power_speed_curve_service)
) -> ResponseModel[PowerSpeedCurve]:
    curve = service.create_curve(curve)
    return {"code": 200, "data": curve, "message": "功率-速度曲线创建成功"}


@api.get("/{curve_id}", summary="获取单个功率-速度曲线")
async def get_power_speed_curve(
    curve_id: Annotated[int, Path(description="曲线ID")],
    service: PowerSpeedCurveService = Depends(get_power_speed_curve_service),
) -> ResponseModel[PowerSpeedCurvePublic]:
    curve = service.get_curve_by_id(curve_id)
    return {"code": 200, "data": curve, "message": "获取功率-速度曲线成功"}


@api.put("/{curve_id}", summary="更新功率-速度曲线")
async def update_power_speed_curve(
    curve_id: int,
    curve: PowerSpeedCurveCreate,
    service: PowerSpeedCurveService = Depends(get_power_speed_curve_service),
) -> ResponseModel[PowerSpeedCurve]:
    curve = service.update_curve(curve_id, curve)
    return {"code": 200, "data": curve, "message": "功率-速度曲线更新成功"}


@api.delete("/{curve_id}", summary="删除功率-速度曲线")
async def delete_power_speed_curve(
    curve_id: int, 
    service: PowerSpeedCurveService = Depends(get_power_speed_curve_service)
) -> ResponseModel[PowerSpeedCurve]:
    curve = service.delete_curve(curve_id)
    return {"code": 200, "data": curve, "message": "功率-速度曲线删除成功"}
