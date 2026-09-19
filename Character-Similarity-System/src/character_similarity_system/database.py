from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase, sessionmaker
from typing import Annotated

from fastapi import Depends

DATABASE_URL = "sqlite:///./projectile_motion.db"

db_engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=db_engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionDep = Annotated[Session, Depends(get_db)]
