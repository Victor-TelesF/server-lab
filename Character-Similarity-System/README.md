# Character Similarity System

Sistema de similaridade de personagens usando similaridade de cosseno. Projeto Python puro para comparar perfis de personagens baseados em atributos numéricos.

## Propósito

Exercício de backend (Tier 1) focado em:
- Classes imutáveis com validação
- Cálculo de similaridade usando álgebra linear
- Testes unitários
- Visualizações de dados

## Matemática

Usa a fórmula de similaridade de cosseno: `cosine_similarity(A, B) = (A · B) / (||A|| × ||B||)`

Retorna valores entre -1 (opostos) e 1 (idênticos), focando na proporção dos atributos em vez da magnitude absoluta.

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -e .
```

## Rodar Testes

```bash
pytest
```

## Como Usar

Crie perfis de personagens com atributos (1-100) e use a engine para calcular similaridade:

```python
from domain.character_profile import CharacterProfile
from domain.similarity_engine import SimilarityEngine

warrior = CharacterProfile(strength=90, agility=60, magic=20, defense=85, intelligence=40)
mage = CharacterProfile(strength=30, agility=50, magic=95, defense=30, intelligence=90)

engine = SimilarityEngine([warrior, mage])
similarity = engine.similarity(warrior, mage)
print(f"Similarity: {similarity:.3f}")
```

## Notebook de Visualizações

O notebook `notebooks/similarity.ipynb` importa o `domain/` diretamente (via editable install) e traz exemplos visuais do cálculo de similaridade aplicado a um conjunto maior de perfis:

- **Heatmap** de similaridade entre todos os perfis
- **Radar chart** comparando o "formato" de atributos de 2-3 perfis
- **Ranking** (gráfico de barras) dos perfis mais similares a um perfil de referência
- **Grafo de rede** conectando perfis com similaridade acima de um limiar

```bash
jupyter notebook notebooks/similarity.ipynb
```