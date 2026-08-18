
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.service import SateliteService
from app.schemas import SateliteCreate, SateliteRead, SateliteUpdateStatus
from .mappers import SateliteMapper


router = APIRouter(prefix="/satelites", tags=["satelites"])

@router.post("/", response_model=SateliteRead)
def create_satelite(satelite_data: SateliteCreate, db: Session = Depends(get_db)):
    service = SateliteService(db)
    satelite = service.create_satelite(satelite_data)
    return SateliteMapper.to_schema_read(satelite)

@router.get("/{satelite_id}", response_model=SateliteRead)
def get_satelite(satelite_id: int, db: Session = Depends(get_db)):
    service = SateliteService(db)
    satelite = service.get_satelite(satelite_id)
    return SateliteMapper.to_schema_read(satelite)

@router.patch("/{satelite_id}/status", response_model=SateliteRead)
def update_satelite_status(satelite_id: int, status: SateliteUpdateStatus, db: Session = Depends(get_db)):
    service = SateliteService(db)
    satelite = service.update_satelite_status(satelite_id, status.nivel_bateria, status.status)
    return SateliteMapper.to_schema_read(satelite)