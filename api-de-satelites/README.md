# API de Satélites 🛰️

API REST para gerenciamento de satélites, construída com **FastAPI**, **SQLAlchemy** e **Pydantic**, seguindo uma arquitetura em camadas com separação clara entre o domínio (regras de negócio) e a aplicação (infraestrutura e entrega HTTP).

## Tecnologias

- **FastAPI** — framework web e documentação automática (Swagger/OpenAPI)
- **SQLAlchemy 2.0** (ORM, estilo `Mapped`/`mapped_column`) — persistência
- **Pydantic v2** — validação e serialização de dados de entrada/saída
- **SQLite** — banco de dados local (`satelites.db`)
- **Uvicorn** — servidor ASGI
- **Pytest / HTTPX** — dependências para testes

## Estrutura do projeto

```
api-de-satelites/
├── main.py                     # Ponto de entrada: cria o app FastAPI, registra rotas e handlers
├── requirements.txt
├── domain/                     # Camada de domínio (regras de negócio puras)
│   ├── satelite.py             # Entidade Satelite com validações e transições de estado
│   ├── enum_status.py          # Enum Status (desativado, em_orbita, manutencao)
│   └── exceptions.py           # Exceções de domínio
└── app/                        # Camada de aplicação/infraestrutura
    ├── routes.py               # Endpoints HTTP (controllers)
    ├── service.py              # Serviço: orquestra domínio + persistência
    ├── schemas.py              # Schemas Pydantic (DTOs de entrada/saída)
    ├── models.py               # Modelo ORM (tabela `satelite`)
    ├── mappers.py              # Conversão entre schema ↔ domínio ↔ modelo ORM
    ├── database.py             # Engine, sessão e dependency `get_db`
    └── exceptions_handlers.py  # Tradução de exceções para respostas HTTP
```

## Camadas

### 1. Domínio (`domain/`)

Camada pura de regras de negócio, **sem nenhuma dependência de framework, banco ou HTTP**.

- **`satelite.py`** — Entidade `Satelite`. Todos os atributos são protegidos por *properties* com validação nos setters:
  - `id`: deve ser `int` ou `None` (antes de persistir);
  - `nome`: deve ser `str`;
  - `status`: deve ser um membro do enum `Status`;
  - `nivel_bateria`: deve ser `int` entre 0 e 100.

  Também concentra as **regras de transição de estado**:
  - `ativar_satelite()` — só permite ativar (ir para `EM_ORBITA`) com bateria ≥ 20%, caso contrário lança `BateriaInsuficienteError`;
  - `desativar_satelite()` — sempre permitido, vai para `DESATIVADO`;
  - `entrar_manutencao()` — não permitido com bateria em 0%, lança `TransicaoInvalidaError`;
  - `reconstruir()` — *factory method* usado para reidratar a entidade a partir do banco, preservando o status persistido (novos satélites sempre nascem `DESATIVADO`).

- **`enum_status.py`** — Enum `Status` com os três estados possíveis: `DESATIVADO`, `EM_ORBITA` e `MANUTENCAO`.

- **`exceptions.py`** — Hierarquia de exceções de domínio, todas derivadas de `SateliteDomainError`:
  - `BateriaInsuficienteError` — ativação com bateria insuficiente;
  - `TransicaoInvalidaError` — transição de estado inválida;
  - `AtributosError` — atributo com tipo/valor inválido.

### 2. Aplicação / Infraestrutura (`app/`)

Camada que conecta o domínio ao mundo externo (HTTP e banco de dados).

- **`routes.py` (rotas/controllers)** — Define os endpoints REST sob o prefixo `/satelites`. As rotas são finas: apenas recebem a requisição, delegam ao `SateliteService` e devolvem o schema de resposta via mapper. A sessão de banco é injetada com `Depends(get_db)`.

- **`service.py` (serviço)** — `SateliteService` orquestra os casos de uso:
  - `create_satelite` — converte o DTO em entidade de domínio (aplicando as validações), persiste e retorna o domínio atualizado;
  - `get_satelite` — busca por id, lançando `ValueError` (→ 404) quando não existe;
  - `update_satelite_status` — reidrata a entidade do banco, atualiza a bateria (se enviada) e executa a transição de status **através dos métodos do domínio**, garantindo que as regras de negócio sejam respeitadas antes de persistir.

- **`schemas.py` (DTOs)** — Schemas Pydantic que definem o contrato da API:
  - `SateliteCreate` — payload de criação (`nome`, `nivel_bateria`);
  - `SateliteRead` — resposta (inclui `id` e `status`);
  - `SateliteUpdateStatus` — payload de atualização de status (`status` obrigatório, `nivel_bateria` opcional).

- **`models.py` (ORM)** — `SateliteModel`, mapeamento da tabela `satelite` com SQLAlchemy 2.0 (`Mapped`/`mapped_column`), incluindo o `status` como enum nativo do banco.

- **`mappers.py` (mapeadores)** — `SateliteMapper` centraliza as conversões entre as três representações, evitando que uma camada conheça os detalhes da outra:
  - `to_domain_create` — schema de criação → entidade de domínio;
  - `to_domain_model` — modelo ORM → entidade de domínio (via `reconstruir`);
  - `to_model_create` / `to_model_update` — entidade de domínio → modelo ORM;
  - `to_schema_read` — entidade de domínio → schema de resposta.

- **`database.py`** — Configuração do engine SQLite, `SessionLocal` e a dependency `get_db`, que abre uma sessão por request e garante o `close()` ao final.

- **`exceptions_handlers.py`** — Handlers que traduzem exceções em respostas HTTP com o código correto:
  - `BateriaInsuficienteError` → **409 Conflict**;
  - `TransicaoInvalidaError` → **409 Conflict**;
  - `ValueError` (satélite não encontrado) → **404 Not Found**.

### 3. Entrada (`main.py`)

Ponto de composição da aplicação: cria as tabelas (`Base.metadata.create_all`), instancia o `FastAPI`, registra os *exception handlers* e inclui o router de satélites.

## Endpoints

| Método | Rota                      | Descrição                                   |
|--------|---------------------------|---------------------------------------------|
| POST   | `/satelites/`             | Cria um satélite (nasce `desativado`)       |
| GET    | `/satelites/{id}`         | Busca um satélite por id                    |
| PATCH  | `/satelites/{id}/status`  | Atualiza status (e opcionalmente a bateria) |

### Exemplos

Criar um satélite:

```bash
curl -X POST http://localhost:8000/satelites/ \
  -H "Content-Type: application/json" \
  -d '{"nome": "Hubble", "nivel_bateria": 80}'
```

Ativar o satélite (colocar em órbita):

```bash
curl -X PATCH http://localhost:8000/satelites/1/status \
  -H "Content-Type: application/json" \
  -d '{"status": "em_orbita"}'
```

Tentar ativar com bateria abaixo de 20% retorna **409**:

```json
{"detail": "Não é possivel ativar um satélite com a bateria abaixo de 20%, bateria atual: 10%"}
```

## Como rodar

```bash
cd api-de-satelites
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

A documentação interativa fica disponível em `http://localhost:8000/docs`.

## Fluxo de uma requisição

```
HTTP request
   → routes.py   (recebe e valida o payload via schemas.py)
   → service.py  (caso de uso; usa mappers.py para converter)
   → domain/     (regras de negócio: validações e transições de estado)
   → models.py + database.py (persistência)
   → mappers.py  (domínio → schema de resposta)
   → HTTP response (erros de domínio traduzidos por exceptions_handlers.py)
```
