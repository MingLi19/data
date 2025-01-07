import logging

from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.core.db import get_db_session
from app.core.error import IntegrityException, NotFoundException, UnknownException
from app.entity.company import Company
from app.model.company import CompanyCreate, CompanyUpdate

logger = logging.getLogger(__name__)


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
            raise NotFoundException(detail="公司不存在")
        return company

    def create_company(self, companyToCreate: CompanyCreate) -> Company:
        company = Company.model_validate(companyToCreate)
        try:
            self.session.add(company)
            self.session.commit()
            self.session.refresh(company)
        except IntegrityError as e:
            logger.error("--IntegrityError: %s", e.__str__())
            self.session.rollback()
            raise IntegrityException(e.args)
        except Exception as e:
            logger.error("--Exception: %s", e.__str__())
            self.session.rollback()
            raise UnknownException(e.args)
        return company

    def update_company(self, company_id: int, companyUpdate: CompanyUpdate) -> Company:
        companyUpdate = CompanyUpdate.model_validate(companyUpdate).model_dump(exclude_unset=True)
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
