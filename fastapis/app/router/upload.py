import datetime
from typing import Annotated

import pandas as pd
from fastapi import APIRouter, BackgroundTasks, Depends, File, Path, Query, UploadFile

from app.core.upload import safe_open_w
from app.entity.vessel_data_upload import VesselDataUpload
from app.model.response import ResponseModel
from app.model.vessel_data_upload import VesselDataUploadCreate
from app.service.data import DataService
from app.service.upload import UploadService, get_upload_service
from app.service.vessel import VesselService, get_vessel_service

api = APIRouter()


def read_csv(file_path: str):
    df = pd.read_csv(file_path)  # 读取csv文件, 生成DataFrame
    print("df", df)
    # TODO: 生成两套数据，一套是标准化数据 StandardData，一套是日平均标准化数据StandardDataPerDay
    # StandardData的生成是对原始数据进行标准化处理, 用几个clean function来处理，比如去除异常值，填充缺失值等（data_nulls, data_abnormal, data_filtering） -> 存入MongoDB Collection StandardData
    # StandardDataPerDay的生成是对StandardData进行按天求平均, groupby('date').mean(), 每天只存一个数据，对历史数据也会进行Overwrite -> 存入MongoDB Collection StandardDataPerDay


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
    background_tasks.add_task(read_csv, file_path)  ## 后台任务读取上传的文件，将数据保存到数据库, 不会阻塞主线程
    return {"code": 200, "data": None, "message": "上传成功"}


@api.get("/vessel/{vessel_id}/data", summary="获取船舶数据")
async def get_vessel_data(
    vessel_id: Annotated[int, Path(description="船舶ID")],
    service: DataService = Depends(get_upload_service),
) -> ResponseModel:
    """
    获取指定船舶的数据
    """
    vessel_data = service.get_vessel_by_id(vessel_id)
    if not vessel_data:
        return {"code": 404, "data": None, "message": "未找到数据"}
    return {"code": 200, "data": vessel_data, "message": "获取成功"}


@api.post("/vessel/{vessel_id}/data", summary="插入船舶数据")
async def insert_vessel_data(
    vessel_id: Annotated[int, Path(description="船舶ID")],
    vessel_data: VesselDataUploadCreate,
    service: DataService = Depends(get_upload_service),
) -> ResponseModel:
    """
    插入船舶数据
    """
    file_path = vessel_data.file_path  # 从请求体中获取文件路径
    date_start = vessel_data.date_start
    date_end = vessel_data.date_end

    service.insert_data(vessel_id=vessel_id, file_path=file_path, date_start=date_start, date_end=date_end)
    return {"code": 200, "data": None, "message": "插入成功"}
