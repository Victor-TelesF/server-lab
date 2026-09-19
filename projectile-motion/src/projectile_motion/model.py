from .database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import FLOAT

class TrajectoryEngineModel(Base):
    __tablename__ = "trajectory_engine"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    v0: Mapped[float] = mapped_column(FLOAT)
    angle_deg : Mapped[float] = mapped_column(FLOAT)
    gravity: Mapped[float] = mapped_column(FLOAT)