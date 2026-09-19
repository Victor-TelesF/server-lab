from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./projectile_motion.db"

db_engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(db_engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()