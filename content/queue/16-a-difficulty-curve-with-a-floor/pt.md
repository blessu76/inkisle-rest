---
title: Uma curva de dificuldade com piso: nenhuma fase que o bot mais simples nunca consiga vencer
description: Com centenas de fases, algumas fases difíceis não são apenas algumas fases difíceis, são um muro. Reajustamos os 14 mares para uma curva com uma fase de descanso em cada mar, limitamos a força da IA inimiga e adicionamos um teste que falha se o bot mais simples vencer 0 de 40. O antes e o depois.
slug: a-difficulty-curve-with-a-floor
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, curva de dificuldade, equilíbrio de jogo, simulação com bots, design de fases, taxa de vitória, nível da IA
image_alt: Uma fileira sinuosa de ilhas que sobe e desce como uma onda, desenhada em cores vetoriais suaves.
---
Um comentário do dono mudou este trabalho: se apenas 40 de 800 fases podem ser vencidas, o jogo é difícil demais, mesmo que cada fase pareça boa isoladamente. Então paramos de ajustar as fases uma a uma e escrevemos uma **curva**.

## A curva

- Cada mar tem oito fases com um **papel**: abertura, preparação, uma fase de descanso, subida e chefe. A fase de descanso deve ser fácil: o bot mais simples vence pelo menos 80% das vezes.
- A taxa de vitória alvo também segue uma **onda ao longo dos volumes**: um mar é um pouco mais difícil que o anterior, e depois vem de novo um mar mais suave.
- Os mares 1 a 3 já estão em versões do TestFlight, então deixamos seus valores fáceis como estavam.

## Um limite para o inimigo

Algumas fases eram difíceis porque a IA inimiga era esperta demais, não porque o mapa fosse duro. Adicionamos um **teto de IA**: nível 5 apenas para fases com vários inimigos, nível 4 para os mares 11 em diante, para os chefes e para a sétima fase a partir do mar 6, e nível 3 em todos os outros lugares. Qualquer IA acima do seu teto é reduzida quando a fase é carregada. Um exemplo: em 10-8, o almirante passou do nível 5 para o 3, e a defesa do farol neutro de 10 para 5.

## A medição

Todos os 14 mares, cinco bots, 40 sementes cada. O "bot simples" é o mais fraco dos cinco e representa uma pessoa.

| | Antes | Depois |
|---|---|---|
| Fases que o bot simples nunca vence | **9** (3-8, 4-3, 4-6, 5-5, 6-8, 7-6, 10-3, 10-8, 14-2) | **0** |
| Fase mais fraca | 0 vitórias em 40 | 4 vitórias em 40 (8-8), depois 5 em 40 (10-8) |
| Fases de descanso, bot simples | não acompanhado | pelo menos 80% |

Alguns exemplos de vitórias do bot simples em 40: 3-8: 0 → 30. 4-3: 0 → 18. 6-1: 2 → 39. 7-6: 0 → 17.

## Um teste que segura o piso

O `curve_floor_test` falha se o bot simples vencer 0 de 40 em qualquer lugar, se uma fase de descanso ficar abaixo de 80% ou se a média dos cinco bots se afastar demais do alvo da curva. Os alvos ficam em um único arquivo, então mudar a curva é mudar uma tabela.

## O que ficou mais fácil de propósito, e o custo

Facilitar as fases fez os itens de **Tinta** valerem mais, porque uma fase mais fácil de vencer também ganha mais com um bônus. Para manter as fases que queríamos, afrouxamos duas travas da Tinta: o limite da taxa de vitória de um chefe com Tinta passou de 55% para 75% em cinco fases de chefe, e o ganho de um uso de Tinta passou de 25 para 35 pontos percentuais em quatro fases. São exceções que registramos, e ainda falta decidir quanto a Tinta deve valer. **[não verificado como política]**

## O que não verificamos

- As taxas de vitória vêm de bots. Algumas fases (4-6, 5-7, 9-5, 10-2, 10-3, 11-6) ficam cerca de dez pontos fora do alvo, e 10-8 tem uma média dos bots de 62% contra um alvo de 33%, porque o almirante é muito difícil para o bot mais simples, mas fácil para os outros.
- Ninguém jogou a nova curva à mão, então "40 de 800 é difícil demais" só foi resolvido nos números dos bots. **[não verificado]**
- O jogo está em desenvolvimento e não foi lançado.
