# Exercícios com Pandas e NumPy

Use estes arquivos para praticar o caminho completo:

```text
CSV -> DataFrame do Pandas -> array do NumPy -> cálculo
```

Comece cada exercício carregando o arquivo correspondente:

```python
import numpy as np
import pandas as pd

df = pd.read_csv("exercicios_csv/notas_alunos.csv")
print(df.head())
print(df.shape)
print(df.dtypes)
```

Se o notebook estiver em outro diretório, ajuste o caminho do arquivo.

## 1. Notas ponderadas — `notas_alunos.csv`

1. Carregue o CSV e mostre as cinco primeiras linhas.
2. Selecione `prova1`, `prova2` e `trabalho` e converta essas para uma matriz NumPy chamada `X`.
3. Crie o vetor de pesos `pesos = np.array([0.30, 0.40, 0.30])`.
4. Calcule a nota final de todos os alunos com uma única multiplicação `X @ pesos`.
5. Acrescente a nota final ao DataFrame.
6. Mostre somente os alunos com nota final maior ou igual a 7 e frequência maior ou igual a 75.

Perguntas: qual é o formato de `X`? Por que o resultado tem um valor por aluno?

## 2. Receita de vendas — `vendas_produtos.csv`

Os valores nas colunas de produtos representam quantidades vendidas.

1. Transforme as quatro colunas de produtos em uma matriz `quantidades`.
2. Crie o vetor de preços `precos = np.array([3500, 900, 180, 120])`.
3. Use `quantidades @ precos` para encontrar a receita total de cada mês.
4. Adicione a receita ao DataFrame e descubra o mês de maior receita.
5. Calcule a quantidade total vendida de cada produto.

Desafio: aumente todos os preços em 8% e recalcule as receitas sem alterar o CSV.

## 3. Previsão de preços — `casas.csv`

1. Crie `X` usando `area_m2`, `quartos`, `idade_anos` e `distancia_centro_km`.
2. Crie o vetor `y` usando a coluna `preco_real`.
3. Use inicialmente os pesos `np.array([2800, 18000, -900, -2500])`.
4. Calcule `previsoes = X @ pesos`.
5. Calcule o erro de cada previsão com `y - previsoes`.
6. Calcule o erro absoluto médio com `np.mean(np.abs(erros))`.

Pergunta: quais pesos valorizam a casa e quais reduzem seu preço previsto?

## 4. Recomendação de filmes — `filmes.csv`

Cada filme possui uma intensidade de 0 a 5 para cada gênero.

1. Crie uma matriz com `acao`, `comedia`, `drama` e `ficcao`.
2. Represente um usuário com `preferencias = np.array([5, 1, 2, 4])`.
3. Calcule a pontuação de todos os filmes usando matriz × vetor.
4. Adicione as pontuações ao DataFrame e ordene do maior para o menor.
5. Experimente outro vetor de preferências e observe como o ranking muda.

Desafio: divida a pontuação por `np.linalg.norm(preferencias)` e pesquise depois por que normalizações ajudam em sistemas de recomendação.

## 5. Limpeza de sensores — `leituras_sensores.csv`

Este arquivo tem valores ausentes de propósito.

1. Use `df.isna().sum()` para localizar os valores ausentes.
2. Preencha cada valor ausente com a média de sua respectiva coluna.
3. Converta as três colunas numéricas para uma matriz NumPy.
4. Calcule a média e o desvio-padrão de cada coluna usando `axis=0`.
5. Padronize os dados com `(X - media) / desvio`.
6. Confirme se as colunas padronizadas ficaram com média próxima de zero.

Desafio: encontre as linhas nas quais alguma medição padronizada tem valor absoluto maior que 1.5.

## Dicas

Selecionar colunas e converter para NumPy:

```python
colunas = ["prova1", "prova2", "trabalho"]
X = df[colunas].to_numpy()
```

Verificar dimensões antes de multiplicar:

```python
print(X.shape)
print(pesos.shape)
```

Lembrete:

```text
(número de linhas, número de colunas) @ (número de pesos,)
```

O número de colunas da matriz deve ser igual ao número de valores do vetor.
