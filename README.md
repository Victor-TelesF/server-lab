# server-lab

Repositório de estudo com exercícios de backend aplicando matemática e física a problemas de domínio. Cada pasta é um exercício independente, com seu próprio README, testes e (quando aplicável) notebook de visualização.

## Exercícios

- [`api-de-satelites/`](./api-de-satelites/README.md) — API REST (FastAPI + SQLAlchemy) para gerenciar satélites: criação, consulta e transição de status (desativado, em órbita, manutenção), com regras de negócio isoladas na camada de domínio.
- [`projectile-motion/`](./projectile-motion/README.md) — Simulador de lançamento oblíquo (movimento de projétil), com trajetória, altura máxima e tempo de voo calculados a partir de velocidade, ângulo e gravidade.
- [`Character-Similarity-System/`](./Character-Similarity-System/README.md) — Sistema de similaridade entre personagens de jogo, usando produto escalar e similaridade do cosseno sobre atributos numéricos.
- [`Route-optimization/`](./Route-optimization/README.md) — Otimizador de rotas entre pontos em um plano cartesiano, usando distância euclidiana e a heurística do vizinho mais próximo.

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