# server-lab

Repositório de estudo com exercícios de backend aplicando matemática e física a problemas de domínio. Cada pasta é um exercício independente, com seu próprio README, testes e (quando aplicável) notebook de visualização.

## Exercícios

- [`api-de-satelites/`](./api-de-satelites/README.md) — API REST (FastAPI + SQLAlchemy) para gerenciar satélites: criação, consulta e transição de status (desativado, em órbita, manutenção), com regras de negócio isoladas na camada de domínio.
- [`projectile-motion/`](./projectile-motion/README.md) — Simulador de lançamento oblíquo (movimento de projétil), com trajetória, altura máxima e tempo de voo calculados a partir de velocidade, ângulo e gravidade.

## Estrutura geral

Cada exercício segue (quando aplicável) uma separação entre domínio puro e infraestrutura:

```
exercicio/
├── domain/      # regras de negócio e matemática, sem dependências externas
├── tests/       # testes unitários e de integração
├── notebooks/   # visualização exploratória (Jupyter), quando aplicável
├── app/         # camada de aplicação/API, quando aplicável
└── README.md    # detalhes específicos do exercício
```