# TODO: implemente aqui a tradução das exceções de domínio para respostas HTTP.
#
# Ideia: usar @app.exception_handler(SuaExcecao) no main.py, registrando
# funções definidas aqui, ao invés de try/except espalhado nas rotas.
#
# Pense em: qual status HTTP faz sentido pra cada exceção de domínio?
# - BateriaInsuficienteError -> ?
# - TransicaoInvalidaError   -> ?
#
# def bateria_insuficiente_handler(request, exc): ...
# def transicao_invalida_handler(request, exc): ...
