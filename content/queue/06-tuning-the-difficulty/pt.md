---
title: Ajustando a dificuldade com bots: cinco fases que estavam erradas
description: Jogamos todas as fases com bots simples, 40 sementes por fase, e encontramos fases impossíveis, curtas demais ou difíceis demais. As cinco mudanças, as taxas de vitória antes e depois, e por que bots não são pessoas.
slug: tuning-the-difficulty
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, equilíbrio de jogo, ajuste de dificuldade, simulação com bots, taxa de vitória, design de fases
image_alt: Uma batalha movimentada entre vários lados coloridos no protótipo do Inkisle.
---
Ainda não temos testadores, então fizemos outra pergunta: quais fases estão *obviamente* erradas? Dois bots simples jogaram cada fase 40 vezes, com 40 sementes diferentes, e lemos as taxas de vitória.

## Os dois bots

- **Bot simples:** a cada 10 ticks, ataca a ilha mais barata que consegue vencer. Representa um jogador casual.
- **Bot habilidoso:** a cada 5 ticks, reúne até três ilhas e ataca em conjunto.

Nenhum dos dois é uma pessoa. Eles nos dão uma direção, não a dificuldade como um humano a sente.

## Cinco fases que estavam erradas

| Fase | Problema | Mudança | Bot simples antes → depois |
|---|---|---|---|
| 1-1 | A meta de três estrelas "perder no máximo 5" era impossível: só as ilhas neutras custavam 13 | Meta alterada para "no máximo 14" | Três estrelas 0% → 100% |
| 1-5 | Acabava em 18 segundos | Base inimiga 20 → 26, uma ilha neutra entregue ao inimigo | 100%, agora 30 s |
| 1-8 chefe | Praticamente impossível de vencer | Segunda ilha do inimigo reduzida, ilha da bandeira 24 → 26, uma ilha pequena entregue ao jogador | **0% → 53%** |
| 2-2 | Acabava em 23 segundos | Base do jogador 15 → 20, uma ilha entregue ao inimigo | 100%, agora 38 s |
| 2-8 chefe | Difícil demais | Ilha da bandeira 24 → 28, uma fortaleza inimiga transformada em fortaleza neutra de 14 | **10% → 38%** |

Deixamos as outras 11 fases como estavam. A meta era uma fase de chefe que um jogador casual vence depois de cerca de uma nova tentativa, ou seja, de 40 a 60% para o bot simples.

## Efeitos colaterais que notamos

- Em um conjunto de 20 sementes, a taxa de vitória geral do bot simples foi de 84% para 91%, e a do bot habilidoso de 78% para 82%.
- A fase 2-2 ficou *mais difícil* para o bot habilidoso, de 100% para 65%. Achamos que o bot tem o hábito de esvaziar fortalezas, mas isso é **[não verificado]**.
- As fases 2-4 e 2-7 mostram taxas de vitória baixas para o bot habilidoso, 40% e 38%. Em uma luta cheia, reunir as tropas pode atrapalhar. Também **[não verificado]**.
- Os limites de tempo de duas estrelas parecem generosos demais, já que os bots quase sempre os cumprem. Vamos apertá-los depois de ver tempos de pessoas.

![Três telas de celular com batalhas movimentadas no protótipo. O texto nas capturas está em coreano.](/assets/posts/img/tuning-boss.jpg)
*Fases movimentadas no protótipo: uma confusão no meio do mar, uma fase de chefe com a ilha da bandeira cercada e uma tela de 320 px de largura.*

## Por que bots não são pessoas

Um bot nunca lê um número errado, nunca se entedia e nunca arrasta errado. Os primeiros 30 minutos de uma pessoa são o teste de verdade: onde ela tenta de novo, onde desiste, quanto tempo leva para chegar a "próxima". O plano é adicionar primeiro um registro de jogo e depois observar de cinco a oito pessoas. Até lá, esses números dizem apenas que nenhuma fase está claramente quebrada, e isso é uma afirmação mais fraca do que "a dificuldade está certa".
