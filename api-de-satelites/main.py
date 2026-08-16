from fastapi import FastAPI

from app.database import Base, engine
from app.routes import router as satelites_router

# TODO: registre aqui os exception_handlers definidos em app/exceptions_handlers.py
# (@app.exception_handler(...)) antes de subir a API pra valer.

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Satélites API")

app.include_router(satelites_router)
