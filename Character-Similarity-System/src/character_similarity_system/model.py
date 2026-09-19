from .database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer

class ProfileModel(Base):

    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    strength: Mapped[int] = mapped_column(Integer)
    agility: Mapped[int] = mapped_column(Integer)
    magic: Mapped[int] = mapped_column(Integer)
    defense: Mapped[int] = mapped_column(Integer)
    intelligence: Mapped[int] = mapped_column(Integer)