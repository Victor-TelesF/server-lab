from email.policy import default

from sqlalchemy.orm import Session
from sqlalchemy import select

from .schemas import SateliteCreate
from .models import SateliteModel
from domain.satelite import Satelite
from domain.enum_status import Status
from .mappers import SateliteMapper


class SateliteService:
    def __init__(self, db: Session):
        self.db = db

    def create_satelite(self, satelite_data: SateliteCreate) -> Satelite:
        satelite = SateliteMapper.to_domain_create(satelite_data)
        data = SateliteMapper.to_model_create(satelite)
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return SateliteMapper.to_domain_model(data)

    def get_satelite(self, satelite_id: int) -> Satelite:
        stmt = select(SateliteModel).where(SateliteModel.id == satelite_id)
        satelite = self.db.execute(stmt).scalar_one_or_none()
        if not satelite:
            raise ValueError("Satélite não encontrado")
        return SateliteMapper.to_domain_model(satelite)

    def update_satelite_status(self, satelite_id: int,bateria: int | None,status: Status) -> Satelite:

        stmt = select(SateliteModel).where(SateliteModel.id == satelite_id)
        satelite_data = self.db.execute(stmt).scalar_one_or_none()
        
        if not satelite_data:
            raise ValueError("Satélite não encontrado")
        
        satelite = SateliteMapper.to_domain_model(satelite_data)

        if bateria is not None:
            satelite.nivel_bateria = bateria
                     
        match status:
            case Status.EM_ORBITA:
                satelite.ativar_satelite()
            case Status.DESATIVADO:
                satelite.desativar_satelite()
            case Status.MANUTENCAO:
                satelite.entrar_manutencao()
            case _:
                raise ValueError("Status inválido")

        updated_model = SateliteMapper.to_model_update(satelite, satelite_data)
        self.db.commit()
        self.db.refresh(updated_model)
        return SateliteMapper.to_domain_model(updated_model)