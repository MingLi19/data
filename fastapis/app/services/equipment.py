from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.core.db import get_db_session
from app.models.equipment import Equipment, EquipmentCreate, EquipmentUpdate


def get_equipment_service(session: Session = Depends(get_db_session)):
    return EquipmentService(session)

class EquipmentService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_equipments(self) -> list[Equipment]:
        statement = select(Equipment)
        equipments = self.session.exec(statement).all()
        return equipments

    def get_equipment_by_id(self, equipment_id: int) -> Equipment:
        equipment = self.session.get(Equipment, equipment_id)
        if not equipment:
            raise HTTPException(status_code=404, detail="Equipment not found")
        return equipment

    def create_equipment(self, equipmentToCreate: EquipmentCreate) -> Equipment:
        equipment = Equipment.model_validate(equipmentToCreate)
        self.session.add(equipment)
        self.session.commit()
        self.session.refresh(equipment)
        return equipment

    def update_equipment(self, equipment_id: int, equipmentUpdate: EquipmentUpdate) -> Equipment:
        equipmentUpdate = EquipmentUpdate.model_validate(equipmentUpdate).model_dump(
            exclude_unset=True
        )
        db_equipment = self.get_equipment_by_id(equipment_id)
        db_equipment.sqlmodel_update(equipmentUpdate)
        self.session.commit()
        self.session.refresh(db_equipment)
        return db_equipment

    def delete_equipment(self, equipment_id: int) -> Equipment:
        equipment = self.get_equipment_by_id(equipment_id)
        self.session.delete(equipment)
        self.session.commit()
        return equipment

