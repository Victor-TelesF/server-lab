# Desafio 4 — Otimizador de Rotas

**Tier 1 — Domínio puro**

Recebe pontos em um plano cartesiano e calcula uma rota para visitá-los usando a heurística do vizinho mais próximo.

## Objetivo

Calcular a distância entre dois pontos, a distância total de uma rota (soma dos trechos) e uma ordem de visita otimizada por heurística gulosa. A distância usa a fórmula euclidiana padrão: `d = √((x₂−x₁)² + (y₂−y₁)²)`.

## Estrutura

```
domain/
  location.py           # Point
  route_calculator.py    # RouteCalculator
tests/
  unit/
    test_point.py
    test_route_calculator.py
notebooks/
  experiments.ipynb      # visualização da rota otimizada
pyproject.toml           # dependências + pacote instalável (domain/)
```

## Instalação

```bash
pip install -e .
```

Instala as dependências (numpy, matplotlib, jupyter, pytest, etc.) e registra `domain/` como pacote importável, permitindo `from domain.location import Point` direto no notebook.

## Decisões de modelagem

- `Point` guarda só o dado (imutável); todo o cálculo fica em `RouteCalculator`
- Coordenadas em metros abstratos, sem curvatura — plano cartesiano simples
- `Point` rejeita `NaN` e `±infinito`, mas aceita negativos; não há validação de tipo
- `distance_between` é `staticmethod`, já que não depende de estado da instância
- `total_distance` soma os trechos na ordem recebida; rota vazia ou com um ponto retorna `0`
- `nearest_neighbor` é uma heurística gulosa, não a rota ótima; sempre parte do primeiro ponto da lista
- `nearest_neighbor` levanta `ValueError` para lista vazia, em vez de devolver algo silenciosamente
- `RouteCalculator` nunca altera a lista recebida — guarda e opera sobre cópias

## Testes

19 testes no total: criação e validação de `Point` (coordenadas, rejeição de valores não finitos), `distance_between` (valor conhecido, simetria), `total_distance` (lista vazia, ponto único, múltiplos pontos, ordem) e `nearest_neighbor` (lista vazia, ponto único, visita única por ponto, imutabilidade da lista original).

```bash
pytest tests/unit/
```

## Visualização

`notebooks/experiments.ipynb` gera pontos aleatórios com seed fixa, calcula a rota pelo vizinho mais próximo e plota com `matplotlib`. Em um teste com 40 pontos, a distância total caiu de ~1883 para ~518 — redução de cerca de 3.6x em relação à ordem de entrada.

## Limitações conhecidas

- A heurística não garante a rota mais curta possível, só uma rota razoável e rápida de calcular
- O ponto de partida é sempre o primeiro da lista, sem otimização sobre qual deveria ser