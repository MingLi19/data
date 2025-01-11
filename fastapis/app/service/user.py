from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.core.db import get_db_session
from app.core.error import IntegrityException
from app.entity.company import Company
from app.entity.user import User
from app.model.user import UserCreate, UserUpdate


def get_user_service(session: Session = Depends(get_db_session)):
    return UserService(session)


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_users(self) -> list[User]:
        statement = select(User)
        users = self.session.exec(statement).all()
        return users

    def get_user_by_id(self, user_id: int) -> User:
        user = self.session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="用户不存在")
        return user

    def create_user(self, userToCreate: UserCreate) -> User:
        user = User.model_validate(userToCreate)
        compnay_id = user.company_id
        company = self.session.get(Company, compnay_id)
        if not company:
            raise IntegrityException(detail="公司不存在")
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update_user(self, user_id: int, userUpdate: UserUpdate) -> User:
        userUpdate = User.model_validate(userUpdate).model_dump(exclude_unset=True)
        db_user = self.get_user_by_id(user_id)
        db_user.sqlmodel_update(userUpdate)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int) -> User:
        user = self.get_user_by_id(user_id)
        self.session.delete(user)
        self.session.commit()
        return user
