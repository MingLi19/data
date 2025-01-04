import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Path

from app.model.response import ResponseModel
from app.model.user import User, UserCreate, UserUpdate, UserWithCompany
from app.service.user import UserService, get_user_service

api = APIRouter()

logger = logging.getLogger(__name__)


@api.get("", summary="获取所有用户")
async def get_users(
    service: UserService = Depends(get_user_service),
) -> ResponseModel[list[User]]:
    """
    用来显示用户列表
    """
    users = service.get_all_users()
    return {"code": 200, "data": users, "message": "获取用户列表成功"}


@api.post("", summary="创建用户")
async def create_user(
    user: UserCreate, service: UserService = Depends(get_user_service)
) -> ResponseModel[User]:
    user = service.create_user(user)
    return {"code": 200, "data": user, "message": "用户创建成功"}


@api.get("/{user_id}", summary="获取单个用户详情")
async def get_user(
    user_id: Annotated[int, Path(description="用户ID")],
    service: UserService = Depends(get_user_service),
) -> ResponseModel[UserWithCompany]:
    """
    首页，显示用户信息
    """
    user = service.get_user_with_company(user_id)
    return {"code": 200, "data": user, "message": "获取用户信息成功"}


@api.put("/{user_id}", summary="更新用户信息")
async def update_user(
    user_id: int,
    user: UserUpdate,
    service: UserService = Depends(get_user_service),
) -> ResponseModel[User]:
    user = service.update_user(user_id, user)
    return {"code": 200, "data": user, "message": "用户信息更新成功"}


@api.delete("/{user_id}", summary="删除用户")
async def delete_user(
    user_id: int, service: UserService = Depends(get_user_service)
) -> ResponseModel[User]:
    user = service.delete_user(user_id)
    return {"code": 200, "data": user, "message": "用户删除成功"}
