from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.core.db import get_db_session
from app.core.error import IntegrityException
from app.entity.power_speed_curve import PowerSpeedCurve
from app.model.power_speed_curve import PowerSpeedCurveCreate


def get_power_speed_curve_service(session: Session = Depends(get_db_session)):
    return PowerSpeedCurveService(session)


class PowerSpeedCurveService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_curves(self) -> list[PowerSpeedCurve]:
        statement = select(PowerSpeedCurve)
        curves = self.session.exec(statement).all()
        return curves

    def get_curve_by_id(self, curve_id: int) -> PowerSpeedCurve:
        curve = self.session.get(PowerSpeedCurve, curve_id)
        if not curve:
            raise HTTPException(status_code=404, detail="功率-速度曲线不存在")
        return curve

    def create_curve(self, curve: PowerSpeedCurveCreate) -> PowerSpeedCurve:
        db_curve = PowerSpeedCurve.model_validate(curve)
        self.session.add(db_curve)
        self.session.commit()
        self.session.refresh(db_curve)
        return db_curve

    def update_curve(self, curve_id: int, curve: PowerSpeedCurveCreate) -> PowerSpeedCurve:
        curve_data = curve.model_dump(exclude_unset=True)
        db_curve = self.get_curve_by_id(curve_id)
        db_curve.sqlmodel_update(curve_data)
        self.session.commit()
        self.session.refresh(db_curve)
        return db_curve

    def delete_curve(self, curve_id: int) -> PowerSpeedCurve:
        curve = self.get_curve_by_id(curve_id)
        self.session.delete(curve)
        self.session.commit()
        return curve
