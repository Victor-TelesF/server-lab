from fastapi import Request
from fastapi.responses import JSONResponse
from domain.exceptions import BateriaInsuficienteError, TransicaoInvalidaError


async def bateria_insuficiente_handler(request: Request, exc: BateriaInsuficienteError):
    status_code = 409
    return JSONResponse(
        status_code=status_code,
        content={"detail": str(exc)},
    )

async def transicao_invalida_handler(request: Request, exc: TransicaoInvalidaError):
    status_code = 409
    return JSONResponse(
        status_code=status_code,
        content={"detail": str(exc)},
    )

async def value_error_handler(request: Request, exc: ValueError):
    status_code = 404
    return JSONResponse(
        status_code=status_code,
        content={"detail": str(exc)},
    )
