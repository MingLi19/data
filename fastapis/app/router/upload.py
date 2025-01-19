import datetime
from typing import Annotated

import pandas as pd
from fastapi import APIRouter, BackgroundTasks, Depends, File, Path, Query, UploadFile

from app.core.upload import safe_open_w
from app.entity.vessel_data_upload import VesselDataUpload
from app.model.response import ResponseModel
from app.model.vessel_data_upload import VesselDataUploadCreate
from app.service.data import DataService, get_data_service
from app.service.upload import UploadService, get_upload_service
from app.service.vessel import VesselService, get_vessel_service

api = APIRouter()


def read_csv(file_path: str):
    df = pd.read_csv(file_path)
    print("df", df)


@api.get("/vessel/{vessel_id}/history", summary="获取船舶数据上传历史")
async def get_vessel_data_upload_history(
    vessel_id: Annotated[int, Path(description="船舶ID")],
    offset: int = Query(0, description="偏移量"),
    limit: int = Query(10, description="每页数量"),
    service: UploadService = Depends(get_upload_service),
) -> ResponseModel[list[VesselDataUpload]]:
    """
    首页，点击"查看上传历史",显示数据上传历史
    """
    history = service.get_vessel_data_upload_history(vessel_id, offset, limit)
    return {"code": 200, "data": history, "message": "获取成功"}


@api.post("/vessel/{vessel_id}/original", summary="上传原始数据")
async def upload_orginal_file(
    vessel_id: Annotated[int, Path(description="船舶ID")],
    file: Annotated[UploadFile, File(description="建议上传csv或excel文件")],
    background_tasks: BackgroundTasks,
    vessel_service: VesselService = Depends(get_vessel_service),
    upload_service: UploadService = Depends(get_upload_service),
) -> ResponseModel:
    """
    首页，点击“上传数据”按钮，上传原始数据
    第一，将上传的文件保存到服务器
    第二，将上传的文件路径保存到数据库，生成一条数据上传记录
    第三，后台任务读取上传的文件，将数据保存到数据库
    """
    vessel = vessel_service.get_vessel_by_id(vessel_id)
    current_date = datetime.date.today()
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%Y%m%d_%H%M%S")
    file_path = f"upload/{current_date}/{vessel.name}-{current_time}.{file.filename.split('.')[-1]}"
    with safe_open_w(file_path) as f:
        f.write(file.file.read())
    request = VesselDataUploadCreate(file_path=file_path)
    await upload_service.create_vessel_data_upload(vessel_id, request)
    background_tasks.add_task(read_csv, file_path)
    return {"code": 200, "data": None, "message": "上传成功"}


@api.get("/test", summary="获取船舶数据")
async def get_vessel_data(
    service: DataService = Depends(get_data_service),
) -> ResponseModel:
    """
    测试
    """
    data = service.get_all_data()
    return {"code": 200, "data": data, "message": "获取成功"}


@api.post("/test", summary="插入船舶数据")
async def insert_vessel_data(
    service: DataService = Depends(get_data_service),
) -> ResponseModel:
    """
    测试
    """
    data = {"name": "test"}
    service.insert_data(data)
    return {"code": 200, "data": None, "message": "插入成功"}
