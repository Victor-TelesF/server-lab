from .database import Base

from sqlalchemy import String, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column
from domain.enum_status import Status

class SateliteModel(Base):
    __tablename__ = "satelite"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(100))
    status: Mapped[Status] = mapped_column(Enum(Status, name="status_enum", native_enum=True))
    nivel_bateria: Mapped[int] = mapped_column(Integer)
