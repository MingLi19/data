import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status

from app.core.security import create_access_token, hash_password, verify_password
from app.entity.user import User
from app.model.response import ResponseModel
from app.model.user import UserCreate, UserLogin, UserPublic, UserUpdate
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
async def create_user(user: UserCreate, service: UserService = Depends(get_user_service)) -> ResponseModel[User]:
    user = service.create_user(user)
    return {"code": 200, "data": user, "message": "用户创建成功"}


@api.get("/{user_id}", summary="获取单个用户详情")
async def get_user(
    user_id: Annotated[int, Path(description="用户ID")],
    service: UserService = Depends(get_user_service),
) -> ResponseModel[UserPublic]:
    """
    首页，显示用户信息
    """
    user = service.get_user_by_id(user_id)
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
async def delete_user(user_id: int, service: UserService = Depends(get_user_service)) -> ResponseModel[User]:
    user = service.delete_user(user_id)
    return {"code": 200, "data": user, "message": "用户删除成功"}


@api.post("/signup", summary="用户注册")
async def signup(user: UserCreate, service: UserService = Depends(get_user_service)):
    # 检查用户名是否已注册
    if service.get_user_by_name(user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名已被注册",
        )
    user.hashed_password = hash_password(user.hashed_password)  # 加密存储密码
    created_user = service.create_user(user)
    return {"code": 200, "message": "用户注册成功", "data": created_user}


@api.post("/signin", summary="用户登录")
async def signin(user: UserLogin, service: UserService = Depends(get_user_service)):
    db_user = service.get_user_by_name(user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
        )
    # 创建 JWT Token，包含用户角色信息
    access_token = create_access_token(data={"sub": db_user.username, "role": "admin" if db_user.is_admin else "user"})
    return {"code": 200, "message": "登录成功", "access_token": access_token, "token_type": "bearer"}
