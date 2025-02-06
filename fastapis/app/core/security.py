# app/core/security.py
from datetime import datetime, timedelta
from typing import Annotated, Optional

import bcrypt
import jwt
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jwt import ExpiredSignatureError, InvalidTokenError
from pydantic import BaseModel, ValidationError
from sqlmodel import Session

from app.core.mysql import get_mysql_db_session
from app.entity.user import User
from app.service.user import UserService

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/users/token", scopes={"me": "普通用户权限", "admin": "管理员操作", "system_admin": "系统管理员操作"}
)


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: list[str] = []


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(
    security_scopes: SecurityScopes,
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_mysql_db_session),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭证",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (ExpiredSignatureError, InvalidTokenError, ValidationError):
        raise credentials_exception

    # 双重验证：数据库权限 + token scopes
    user_service = UserService(session)
    user = user_service.get_user_by_name(username=token_data.username)
    if user is None:
        raise credentials_exception

    # 验证scope与数据库权限的一致性
    if "system_admin" in token_scopes and not user.is_system_admin:
        raise HTTPException(status_code=403, detail="非法权限声明")
    if "admin" in token_scopes and not user.is_admin:
        raise HTTPException(status_code=403, detail="非法权限声明")

    # 验证请求权限
    if security_scopes.scopes:
        for scope in security_scopes.scopes:
            if scope not in token_scopes:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="权限不足",
                )
    return user


async def get_current_active_user(current_user: Annotated[User, Security(get_current_user, scopes=["me"])]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="用户已被禁用")
    return current_user


async def get_admin_user(current_user: Annotated[User, Security(get_current_user, scopes=["admin"])]):
    # 额外验证数据库权限
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="需要管理员权限")
    return current_user


async def get_system_admin_user(current_user: Annotated[User, Security(get_current_user, scopes=["system_admin"])]):
    # 双重验证
    if not current_user.is_system_admin:
        raise HTTPException(status_code=403, detail="需要系统管理员权限")
    return current_user
