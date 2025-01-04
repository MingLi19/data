import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Path

from app.entity.company import Company
from app.model.company import CompanyCreate, CompanyUpdate
from app.model.response import ResponseModel
from app.service.company import CompanyService, get_company_service

api = APIRouter()

logger = logging.getLogger(__name__)


@api.get("", summary="获取所有公司")
async def get_companies(
    service: CompanyService = Depends(get_company_service),
) -> ResponseModel[list[Company]]:
    """
    用来显示公司列表
    """
    companies = service.get_all_companies()
    return {"code": 200, "data": companies, "message": "获取公司列表成功"}


@api.post("", summary="创建公司")
async def create_company(
    company: CompanyCreate, service: CompanyService = Depends(get_company_service)
) -> ResponseModel[Company]:
    company = service.create_company(company)
    return {"code": 200, "data": company, "message": "公司创建成功"}


@api.get("/{company_id}", summary="获取单个公司详情")
async def get_company(
    company_id: Annotated[int, Path(description="公司ID")],
    service: CompanyService = Depends(get_company_service),
) -> ResponseModel[Company]:
    """
    首页，显示公司信息
    """
    company = service.get_company_by_id(company_id)
    return {"code": 200, "data": company, "message": "获取公司信息成功"}


@api.put("/{company_id}", summary="更新公司信息")
async def update_company(
    company_id: int,
    company: CompanyUpdate,
    service: CompanyService = Depends(get_company_service),
) -> ResponseModel[Company]:
    company = service.update_company(company_id, company)
    return {"code": 200, "data": company, "message": "公司信息更新成功"}


@api.delete("/{company_id}", summary="删除公司")
async def delete_company(
    company_id: int, service: CompanyService = Depends(get_company_service)
) -> ResponseModel[Company]:
    company = service.delete_company(company_id)
    return {"code": 200, "data": company, "message": "公司删除成功"}
