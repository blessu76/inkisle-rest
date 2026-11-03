---
title: Uma carta náutica que muda de caminho: um estilo de linha por mar
description: Com 14 mares numa única carta com rolagem, o caminho entre as fases parecia igual em todo lugar. Demos a cada mar seu próprio estilo de linha, cor e ondulação, fizemos o ângulo continuar nas fronteiras entre mares e só desenhamos o que está na tela. Os valores, os testes e o que ainda não vimos num celular.
slug: a-chart-that-changes-its-road
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, carta náutica, mapa de fases, estilo de rota, UI mobile, Flutter, desempenho de renderização
image_alt: Um caminho tracejado e sinuoso entre ilhas que muda de uma linha de corda para uma linha de onda, desenhado em cores vetoriais suaves.
---
A carta é a tela onde você passa o tempo tranquilo entre batalhas: um longo caminho de fases. Com 14 mares, o caminho parecia o mesmo do começo ao fim. Uma rolagem longa sem mudança dá a sensação de um único mar repetido. Por isso cada mar ganhou seu próprio caminho.

## O que muda por mar

| Mar | Linha | Cor de um caminho concluído |
|---|---|---|
| 1 | contínua (como antes) | coral |
| 2 | corda | bege de vela |
| 3 | traços longos, tênue | branco de farol |
| 4 | onda | azul-petróleo |
| 5 | contas | rosa coral |
| 6 | traços longos | ouro de areia |
| 7 | contínua grossa | azul-marinho |
| 8 | contínua fina | cobalto |
| 9 | contas | ouro de lanterna |
| 10 | contínua grossa | ouro |
| 11 | pincel | tinta |
| 12 | linha dupla | prata |
| 13 | onda | vela branca |
| 14 | contas | tinta profunda |

Cada mar também tem seu próprio balanço (o quanto o caminho oscila para os lados e com que frequência). Sete tipos de linha são compartilhados entre os 14 mares, e as cores são todas diferentes. O caminho que leva a uma fase é desenhado no estilo do mar ao qual essa fase pertence. Depois do mar 14 os estilos se repetem, como solução provisória.

## Duas coisas que não eram sobre aparência

- **Sem saltos nas fronteiras entre mares.** O balanço é uma única função contínua, então o ângulo continua onde um mar termina e o próximo começa, e as ilhas não saltam para o lado.
- **Desenhar só o que está visível.** A carta terá centenas de fases, então ilhas e caminhos fora da área visível são ignorados. Num teste de widget, desenhar dez caminhos visíveis levou menos de 16 ms.

## As decorações vieram depois

Uma segunda etapa acrescentou pequenas marcas ao longo do caminho em cada mar: nós, colchetes, pegadas, estrelas, gotas de tinta. Depois, nos mares 7, 10 e 11, trocamos essas marcas por um redemoinho, um farol e uma dispersão, e a gota do mar 14 por uma pontiaguda.

## Testes

Sete testes verificam que todo mar tem um estilo, que o balanço fica abaixo de .32, que as 14 cores são todas diferentes, que todo tipo de linha é usado, que um caminho concluído tem contraste de pelo menos 3:1 com a sua borda, que as ilhas ficam dentro de 18% a 82% da largura a 320 px, e que cada mar desenha pixels diferentes. O layout do primeiro mar não se move.

## O que não verificamos

- Todas as renderizações até agora são capturas de teste, em que a fonte é um bloco. Não olhamos num iPhone ou celular Android de verdade. **[não verificado]**
- Não medimos o tempo de quadro com as 800 fases, apenas a verificação de dez caminhos. **[não verificado]**
- Nos mares noturnos escuros (11 e 14), o caminho cor de tinta é sustentado por uma borda branca. Se isso fica bom é uma revisão de design que ainda devemos.
- O jogo está em desenvolvimento e não foi lançado.
