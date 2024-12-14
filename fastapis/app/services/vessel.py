from core.db import get_db_session
from fastapi import Depends, HTTPException

# from models.equipment import Equipment
from models.vessel import Vessel, VesselCreate, VesselUpdate
from sqlmodel import Session, select


def get_vessel_service(session: Session = Depends(get_db_session)):
    return VesselService(session)


class VesselService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_vessels(self) -> list[Vessel]:
        statement = select(Vessel)
        vessels = self.session.exec(statement).all()
        return vessels

    def get_vessel_by_id(self, vessel_id: int) -> Vessel:
        vessel = self.session.get(Vessel, vessel_id)
        if not vessel:
            raise HTTPException(status_code=404, detail="船舶不存在")
        return vessel

    def create_vessel(self, vesselToCreate: VesselCreate) -> Vessel:
        vessel = Vessel.model_validate(vesselToCreate)
        self.session.add(vessel)
        self.session.commit()
        self.session.refresh(vessel)
        return vessel

    def update_vessel(self, vessel_id: int, vesselUpdate: VesselUpdate) -> Vessel:
        vesselUpdate = VesselUpdate.model_validate(vesselUpdate).model_dump(
            exclude_unset=True
        )
        db_vessel = self.get_vessel_by_id(vessel_id)
        db_vessel.sqlmodel_update(vesselUpdate)
        self.session.commit()
        self.session.refresh(db_vessel)
        return db_vessel

    def delete_vessel(self, vessel_id: int) -> Vessel:
        vessel = self.get_vessel_by_id(vessel_id)
        self.session.delete(vessel)
        self.session.commit()
        return vessel

    def get_equipments_by_vessel_id(self, vessel_id: int) -> Vessel:
        statement = select(Vessel).where(Vessel.id == vessel_id)
        equipment = self.session.exec(statement).all()
        return equipment.equipments
