import logging
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.core.mysql import get_mysql_db_session
from app.entity.user import User
from app.model.response import ResponseModel
from app.model.user import Token, UserCreate, UserPublic, UserUpdate
from app.service.user import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    UserService,
    authenticate_user,
    create_access_token,
    get_current_user,
    get_user_service,
)

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


@api.post("/token", response_model=Token, summary="登录并获取 Token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_mysql_db_session)
):
    """
    用户登录接口，验证用户名和密码，
    若验证成功，返回 JWT Token，用于后续接口访问认证。
    """
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@api.get("/users/me", response_model=UserPublic, summary="获取当前登录用户信息")
async def read_users_me(current_user: User = Depends(get_current_user)):
    """
    受保护接口，只有携带有效 JWT Token 的用户才能访问，
    返回当前用户的公开信息。
    """
    return current_user
