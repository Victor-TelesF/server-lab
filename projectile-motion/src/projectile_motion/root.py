from .database import get_db

from fastapi import APIRouter, Depends
from fastapi.responses import Response

from .schema import CreateLaunchConfigSchema, LaunchConfigResponse

from .model import TrajectoryEngineModel
from sqlalchemy.orm import Session
from io import BytesIO

from matplotlib.figure import Figure

from .service import registro_trajetoria


router = APIRouter(prefix="/funcao")

@router.post("/criar_dados", response_model=LaunchConfigResponse, status_code=201)
def criar_engine(dados: CreateLaunchConfigSchema, db: Session = Depends(get_db)):
    banco = TrajectoryEngineModel(**dados.model_dump())
    db.add(banco)
    db.commit()
    db.refresh(banco)
    return banco

@router.get("/posicao/{id}", response_model=tuple[float, float])
def posicao(id: int,time: float, db: Session = Depends(get_db)):
    return registro_trajetoria(db, id).position_at(time)

@router.get("/altura_maxima/{id}", response_model=tuple[float, float])
def altura(id: int, db: Session = Depends(get_db)):
    return registro_trajetoria(db, id).max_height()

@router.get("/tempo_de_voo/{id}", response_model=float)
def tempo_de_voo(id: int, db: Session = Depends(get_db)):
    return registro_trajetoria(db, id).time_of_flight()


class PNGResponse(Response):
    media_type = "image/png"


@router.get(
    "/grafico/{config_id}",
    response_class=PNGResponse,
)
def grafico(
    config_id: int,
    db: Session = Depends(get_db),
):

    engine = registro_trajetoria(db, config_id)
    pontos = engine.trajectory_points(num_points=100)

    valores_x = [ponto["x"] for ponto in pontos]
    valores_y = [ponto["y"] for ponto in pontos]

    figura = Figure(figsize=(12, 4))
    eixos = figura.subplots()

    eixos.plot(valores_x, valores_y)

    eixos.set_xlim(0, 450)
    eixos.set_ylim(0, 120)
    eixos.set_aspect("equal", adjustable="box")

    eixos.set_title("Trajetória do projétil")
    eixos.set_xlabel("Distância horizontal (m)")
    eixos.set_ylabel("Altura (m)")
    eixos.grid()

    arquivo = BytesIO()
    figura.savefig(arquivo, format="png", bbox_inches="tight")

    return PNGResponse(content=arquivo.getvalue())