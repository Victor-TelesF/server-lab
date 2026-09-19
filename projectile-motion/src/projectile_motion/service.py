from fastapi import HTTPException
from sqlalchemy.orm import Session

from domain.launch_config import LaunchConfig
from domain.trajectory_engine import TrajectoryEngine

from .model import TrajectoryEngineModel

def registro_trajetoria(db: Session, id: int) -> TrajectoryEngine:
    registro = db.get(TrajectoryEngineModel, id)
    
    if registro is None:
        raise HTTPException(
            status_code=404,
            detail="Configuração de lançamento não encontrada"
        )
    
    config = LaunchConfig(registro.v0, registro.angle_deg, registro.gravity)
    return TrajectoryEngine(config)