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
    nivel_bateria: int | None = None