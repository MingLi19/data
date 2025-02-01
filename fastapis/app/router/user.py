# app/router/user.py
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi.security import OAuth2PasswordRequestForm

from app.core.security import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_current_active_user,
    hash_password,
    verify_password,
)
from app.entity.user import User
from app.model.response import ResponseModel
from app.model.user import UserCreate, UserPublic, UserUpdate  # 添加 UserLogin
from app.service.user import UserService, get_user_service

api = APIRouter()


@api.get("/me", summary="当前用户信息")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user


@api.get("", summary="获取所有用户")
async def get_users(service: UserService = Depends(get_user_service)) -> ResponseModel[list[User]]:
    """获取所有用户列表"""
    users = service.get_all_users()
    return {"code": 200, "data": users, "message": "获取用户列表成功"}


@api.post("", summary="创建用户")
async def create_user(user: UserCreate, service: UserService = Depends(get_user_service)) -> ResponseModel[User]:
    """创建新用户"""
    user = service.create_user(user)
    return {"code": 200, "data": user, "message": "用户创建成功"}


@api.get("/{user_id}", summary="获取单个用户详情")
async def get_user(
    user_id: Annotated[int, Path(description="用户ID")], service: UserService = Depends(get_user_service)
) -> ResponseModel[UserPublic]:
    """获取单个用户信息"""
    user = service.get_user_by_id(user_id)
    return {"code": 200, "data": user, "message": "获取用户信息成功"}


@api.put("/{user_id}", summary="更新用户信息")
async def update_user(
    user_id: int, user: UserUpdate, service: UserService = Depends(get_user_service)
) -> ResponseModel[User]:
    """更新用户信息"""
    user = service.update_user(user_id, user)
    return {"code": 200, "data": user, "message": "用户信息更新成功"}


@api.delete("/{user_id}", summary="删除用户")
async def delete_user(user_id: int, service: UserService = Depends(get_user_service)) -> ResponseModel[User]:
    """删除用户"""
    user = service.delete_user(user_id)
    return {"code": 200, "data": user, "message": "用户删除成功"}


@api.post("/signup", summary="用户注册")
async def signup(user: UserCreate, service: UserService = Depends(get_user_service)):
    """用户注册"""
    if service.get_user_by_name(user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名已被注册",
        )
    user.hashed_password = hash_password(user.hashed_password)  # 加密存储密码
    created_user = service.create_user(user)
    return {"code": 200, "message": "用户注册成功", "data": created_user}


# app/router/user.py
@api.post("/token", summary="用户登录")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), service: UserService = Depends(get_user_service)
):
    db_user = service.get_user_by_name(form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
        )

    # 严格根据数据库权限生成scopes
    scopes = []
    if db_user.is_system_admin:
        scopes = ["system_admin"]
    if db_user.is_admin:
        scopes.append("admin")
    scopes.append("me")  # 所有用户都有me权限

    access_token = create_access_token(
        data={"sub": db_user.username, "scopes": scopes}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}
