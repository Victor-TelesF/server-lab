from domain.satelite import Satelite
from domain.enum_status import Status
from .schemas import SateliteCreate, SateliteRead, SateliteUpdateStatus
from .models import SateliteModel

class SateliteMapper:

    @staticmethod
    def to_domain_schema_create(satelite: SateliteCreate) -> Satelite:
        return Satelite(
            id = None,
            nome= satelite.nome,
            nivel_bateria = satelite.nivel_bateria
        )

    @staticmethod
    def domain_to_schema_read(satelite: Satelite) -> SateliteRead:
        return SateliteRead(
            id = satelite.id,
            nome = satelite.nome,
            nivel_bateria = satelite.nivel_bateria,
            status = satelite.status
        )

    @staticmethod
    def to_domain_model(satelite: SateliteModel) -> Satelite:
        return Satelite.reconstruir(
            id = satelite.id,
            nome = satelite.nome,
            nivel_bateria = satelite.nivel_bateria,
            status= satelite.status
        )

    @staticmethod
    def to_model_create(satelite: Satelite) -> SateliteModel:
        model = SateliteModel()
        model.id = satelite.id
        model.nome = satelite.nome
        model.nivel_bateria = satelite.nivel_bateria
        model.status = satelite.status
        
        return model

    @staticmethod
    def to_model_update(satelite: Satelite, model: SateliteModel) -> SateliteModel:
        model.nome = satelite.nome
        model.nivel_bateria = satelite.nivel_bateria
        model.status = satelite.status
        
        return model