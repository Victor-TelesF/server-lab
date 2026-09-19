from fastapi import FastAPI
from src.projectile_motion import root
from src.projectile_motion.database import Base, db_engine

app = FastAPI()
Base.metadata.create_all(db_engine)

app.include_router(root.router)