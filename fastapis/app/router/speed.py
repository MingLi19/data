from fastapi import APIRouter

from app.service.speed import generate_speed_histogram, generate_speed_scatter

api = APIRouter()


@api.get("/speed_histogram", summary="航速直方图", tags=["图表"])
async def speed_histogram():
    """处理航速直方图生成请求"""
    return generate_speed_histogram()  # 调用服务层生成图表


@api.get("/speed_scatter", summary="航速散点图", tags=["图表"])
async def speed_scatter():
    """处理航速散点图生成请求"""
    return generate_speed_scatter()  # 调用服务层生成图表
