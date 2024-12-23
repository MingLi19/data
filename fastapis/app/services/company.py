from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.core.db import get_db_session
from app.models.company import Company, CompanyCreate, CompanyUpdate


def get_company_service(session: Session = Depends(get_db_session)):
    return CompanyService(session)


class CompanyService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_companies(self) -> list[Company]:
        statement = select(Company)
        results = self.session.exec(statement)
        companies = results.all()
        return companies

    def get_company_by_id(self, company_id: int) -> Company:
        company = self.session.get(Company, company_id)
        if not company:
            raise HTTPException(status_code=404, detail="公司不存在")
        return company

    def create_company(self, companyToCreate: CompanyCreate) -> Company:
        company = Company.model_validate(companyToCreate)
        self.session.add(company)
        self.session.commit()
        self.session.refresh(company)
        return company

    def update_company(self, company_id: int, companyUpdate: CompanyUpdate) -> Company:
        companyUpdate = CompanyUpdate.model_validate(companyUpdate).model_dump(
            exclude_unset=True
        )
        db_company = self.get_company_by_id(company_id)
        db_company.sqlmodel_update(companyUpdate)
        self.session.commit()
        self.session.refresh(db_company)
        return db_company

    def delete_company(self, company_id: int) -> Company:
        company = self.get_company_by_id(company_id)
        self.session.delete(company)
        self.session.commit()
        return company
