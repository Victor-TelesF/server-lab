# TODO: implemente aqui os schemas Pydantic (v2).
#
# Sugestão de schemas pra esse exercício:
# - SateliteCreate       -> dados recebidos no POST (nome, nivel_bateria inicial)
# - SateliteRead         -> dados devolvidos nas respostas (inclui id, status)
# - SateliteUpdateStatus -> dados recebidos no PATCH /status (qual transição pedir?)
#
# Pense em: o schema de entrada precisa de validação de nivel_bateria
# (ex: 0-100)? Onde isso deveria morar -- no schema (Pydantic) ou no domínio?

from pydantic import BaseModel, ConfigDict
from domain.enum_status import Status

class SateliteCreate(BaseModel):
    nome: str
    nivel_bateria: int

class SateliteRead(SateliteCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: Status

class SateliteUpdateStatus(BaseModel):
    status: Status





