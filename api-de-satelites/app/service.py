# TODO: implemente aqui a orquestração (busca no banco, chama o domínio,
# persiste, devolve).
#
# Funções que você provavelmente vai precisar:
# - criar_satelite(db, dados: SateliteCreate) -> Satelite
# - buscar_satelite(db, satelite_id) -> Satelite
# - atualizar_status(db, satelite_id, nova_transicao) -> Satelite
#
# Pense em: o service deve devolver o objeto de domínio puro, ou já
# o schema de resposta? Onde entra o mapper nesse fluxo? O service
# deixa a exceção de domínio "vazar" pra fora, ou já traduz pra algo
# HTTP aqui? (dica: pense de novo no exceptions_handlers.py)
from sqlalchemy.orm import Session
from .schemas import SateliteCreate, SateliteRead, SateliteUpdateStatus
from domain.satelite import Satelite
from domain.enum_status import Status


