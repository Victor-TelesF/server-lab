from fastapi import FastAPI

from app.database import Base, engine
from app.routes import router as satelites_router
from app.exceptions_handlers import (
    bateria_insuficiente_handler,
    transicao_invalida_handler,
    value_error_handler,
)
from domain.exceptions import BateriaInsuficienteError, TransicaoInvalidaError
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Satélites API")

app.add_exception_handler(BateriaInsuficienteError, bateria_insuficiente_handler)
app.add_exception_handler(TransicaoInvalidaError, transicao_invalida_handler)
app.add_exception_handler(ValueError, value_error_handler)

app.include_router(satelites_router)