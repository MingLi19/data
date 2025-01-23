from datetime import datetime, timedelta
from typing import Dict, Optional, Union

import bcrypt
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

SECRET_KEY = "123456"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# 密码加密
def hash_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed_password.decode("utf-8")


# 密码验证
def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except ValueError:
        return False


# 生成 JWT Token
def create_access_token(data: Dict[str, Union[str, int]], expires_delta: Optional[timedelta] = None) -> str:
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# 验证 token 的函数
def verify_token(token: str) -> Optional[Dict[str, Union[str, int]]]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise ValueError("Token 已过期")
    except InvalidTokenError:
        raise ValueError("无效的 Token")


# 权限验证函数
def check_permission(token: str, required_role: str) -> bool:
    try:
        payload = verify_token(token)
        user_role = payload.get("role")
        if user_role == required_role:
            return True
        return False
    except ValueError as e:
        raise ValueError(f"Permission check failed: {e}")
