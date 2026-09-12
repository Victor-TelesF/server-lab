# Experimentos

Esta pasta é meu espaço de estudo para testar ideias e resolver exercícios em Python. Os notebooks são independentes: alguns são rascunhos, outros acompanham dados e um roteiro de prática. O pacote `experiments` guarda funções que podem ser reutilizadas entre notebooks; o repositório não é uma aplicação pronta.

No momento, o foco é álgebra linear aplicada a dados com NumPy e Pandas. A pasta pode crescer com novos exercícios sem precisar mudar a estrutura dos que já existem.

## Por onde começar

Os exercícios mais completos estão em [`src/linear_algebra/`](src/linear_algebra/). Para praticar a sequência de CSV → Pandas → NumPy, siga o [roteiro dos cinco exercícios](src/linear_algebra/exercicios_csv/README.md) e abra os notebooks nesta ordem:

1. [Notas ponderadas](src/linear_algebra/notas_ponderadas.ipynb) — multiplicação matriz × vetor e filtro de alunos.
2. [Receita de vendas](src/linear_algebra/receita_de_vendas.ipynb) — quantidades × preços e agregações.
3. [Previsão de preços](src/linear_algebra/previsao_de_precos.ipynb) — pesos, previsões e erro absoluto médio.
4. [Recomendação de filmes](src/linear_algebra/recomendacao_de_filmes.ipynb) — pontuação e ordenação por preferência.
5. [Limpeza de sensores](src/linear_algebra/limpeza_de_sensores.ipynb) — valores ausentes, padronização e identificação de leituras atípicas.

O [notebook de exercícios de álgebra linear](src/linear_algebra/exercicios.ipynb) contém contas mais diretas com vetores e matrizes. Os CSVs ficam junto do roteiro, em `src/linear_algebra/exercicios_csv/`.

## Estrutura

```text
experiments/
├── src/
│   ├── experiments/             # código Python reutilizável e importável
│   ├── linear_algebra/          # exercícios de vetores, matrizes e dados
│   │   └── exercicios_csv/      # enunciados e arquivos CSV usados nos notebooks
│   ├── leetcode/                # exercícios de algoritmos
│   └── notebooks/               # testes e rascunhos gerais
├── pyproject.toml               # versão do Python e dependências
└── README.md
```

Os notebooks e CSVs continuam organizados por tema. As funções que crescerem demais para uma célula podem ir em `src/experiments/`. Novos exercícios de álgebra linear podem entrar em `src/linear_algebra/`, com seus dados próximos do notebook ou em uma subpasta própria.

## Como executar

Requisitos: Python 3.14 ou superior e [uv](https://docs.astral.sh/uv/).

Na pasta `experiments/`, prepare o ambiente e abra o Jupyter a partir da pasta dos exercícios:

```bash
uv sync
cd src/linear_algebra
uv run python -m jupyter lab .
```

Abra um notebook pelo navegador e escolha o ambiente criado pelo projeto. Os notebooks de Pandas leem caminhos como `exercicios_csv/casas.csv`, portanto devem ser executados com o diretório de trabalho em `src/linear_algebra/`. Se um arquivo não for encontrado, confira `Path.cwd()` no notebook e ajuste o diretório de trabalho ou o caminho do CSV.

Os arquivos em `src/leetcode/` e `src/notebooks/` são explorações separadas; não dependem dos CSVs de álgebra linear.

## Reutilizar funções nos notebooks

Depois de `uv sync`, o pacote `experiments` fica instalado em modo editável na `.venv`. Para criar uma função reutilizável, adicione, por exemplo, `src/experiments/calculos.py`:

```python
def dobro(valor):
    return valor * 2
```

Em qualquer notebook que use o kernel da `.venv` deste projeto:

```python
from experiments.calculos import dobro

dobro(3)  # 6
```

O arquivo `calculos.py` acima é apenas um exemplo; você pode organizar os módulos por assunto. Não é preciso alterar `sys.path` ou repetir `uv sync` a cada edição de um `.py`. Se editar um módulo que já foi importado em um notebook aberto, reinicie o kernel para carregar a versão nova.
