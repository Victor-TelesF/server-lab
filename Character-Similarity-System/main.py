from fastapi import FastAPI
from src.character_similarity_system import root

from src.character_similarity_system.database import Base, db_engine

Base.metadata.create_all(db_engine)

app = FastAPI()

app.include_router(root.router)