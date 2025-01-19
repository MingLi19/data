from fastapi import Depends
from sqlalchemy import delete
from sqlmodel import Session, select

from app.core.error import NotFoundException
from app.core.mysql import get_mysql_db_session
from app.entity.equipement_fuel import EquipmentFuel
from app.entity.equipment import Equipment
from app.entity.vessel import Vessel
from app.model.vessel import VesselCreate, VesselUpdate


def get_vessel_service(session: Session = Depends(get_mysql_db_session)):
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
            raise NotFoundException(detail="船舶不存在")
        return vessel

    def create_vessel(self, vesselToCreate: VesselCreate) -> Vessel:
        equipment_name_fuel_type_ids_map = {
            equipment.name: equipment.fuel_type_ids for equipment in vesselToCreate.equipments
        }
        vesselToCreate.equipments = [Equipment.model_validate(equipment) for equipment in vesselToCreate.equipments]
        vessel = Vessel.model_validate(vesselToCreate)
        self.session.add(vessel)
        self.session.commit()
        self.session.refresh(vessel)
        for equipment in vessel.equipments:
            fuel_type_ids = equipment_name_fuel_type_ids_map.get(equipment.name)
            for fuel_type_id in fuel_type_ids:
                equipment_fuel = EquipmentFuel(equipment_id=equipment.id, fuel_type_id=fuel_type_id)
                self.session.add(equipment_fuel)
        self.session.commit()
        return vessel

    def update_vessel(self, vessel_id: int, vesselUpdate: VesselUpdate) -> Vessel:
        equipment_name_fuel_type_ids_map = {
            equipment.name: equipment.fuel_type_ids for equipment in vesselUpdate.equipments
        }
        vesselUpdate.equipments = [Equipment.model_validate(equipment) for equipment in vesselUpdate.equipments]
        vessel = self.get_vessel_by_id(vessel_id)
        vessel.sqlmodel_update(vesselUpdate)
        self.session.commit()
        self.session.refresh(vessel)
        for equipment in vessel.equipments:
            delete_statement = delete(EquipmentFuel).where(EquipmentFuel.equipment_id == equipment.id)
            self.session.exec(delete_statement)
            fuel_type_ids = equipment_name_fuel_type_ids_map.get(equipment.name) or []
            for fuel_type_id in fuel_type_ids:
                equipment_fuel = EquipmentFuel(equipment_id=equipment.id, fuel_type_id=fuel_type_id)
                self.session.add(equipment_fuel)
        self.session.commit()
        self.session.refresh(vessel)
        return vessel

    def delete_vessel(self, vessel_id: int) -> Vessel:
        vessel = self.get_vessel_by_id(vessel_id)
        self.session.delete(vessel)
        self.session.commit()
        return vessel
