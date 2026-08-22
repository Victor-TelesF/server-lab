# Simulador de Movimento

Simula a trajetória de um projétil lançado com velocidade inicial, ângulo e gravidade configuráveis — um pequeno motor de física pra lançamento oblíquo.

## Matemática

O motor decompõe a velocidade inicial em componentes horizontal e vertical, e usa essas componentes pra calcular a posição do projétil em qualquer instante:

- Conversão de graus para radianos
- Decomposição de velocidade: `v0x = v0·cos(θ)`, `v0y = v0·sin(θ)`
- Posição horizontal: `x = v0x·t`
- Posição vertical: `y = v0y·t - (g·t²)/2`
- Tempo até o pico: `t = v0y/g`
- Tempo total de voo: `t_total = 2·v0y/g`

## Decisões de design

Ângulos de 0° e 90° são permitidos. Um lançamento a 0° não sobe (o pico da trajetória fica em t=0, altura 0) e a 90° o movimento é puramente vertical — nos dois casos as fórmulas continuam válidas, sem divisão por zero, então não há motivo técnico pra restringir.

## Rodando os testes

Da raiz do projeto:

```bash
pytest
```

## Visualização

O notebook em `notebooks/` importa o domínio diretamente e plota a trajetória com `matplotlib`, útil pra conferir visualmente se a parábola faz sentido antes de confiar só nos testes numéricos.