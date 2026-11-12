---
title: A fonte de tinta do mar branco: quando uma regra de três estrelas não dá para conquistar
description: O mar 14 tem uma fonte que espalha tinta pelas ilhas próximas. Os bots não conseguiram o objetivo de três estrelas "faça a fonte se espalhar por N ilhas", então medimos, tentamos mover ilhas e trocamos a regra por uma contagem de pulsos da fonte. O que tentamos e o que ainda não foi verificado.
slug: the-white-sea-ink-spring
lang: pt-BR
translation_of: en
category: making-of
keywords: Inkisle, design de fases, regra de três estrelas, fonte de tinta, simulação com bots, equilíbrio do jogo, mar 14
image_alt: Um mar pálido com uma pequena ilha-fonte no centro e algumas ilhas ao redor, desenhado em cores vetoriais suaves.
published: 2026-11-10T19:00+09:00
---
O mar 14, o mar branco, acrescenta uma regra: uma **fonte de tinta**. Se você mantém a ilha da fonte, a cada 150 ticks ela pulsa e espalha tinta por uma ilha próxima. O primeiro pulso vem 150 ticks depois de você capturá-la. O objetivo de três estrelas que escrevemos primeiro para ela era "faça a fonte se espalhar por N ilhas". Esse objetivo acabou sendo uma promessa que ninguém conseguia cumprir.

## A medição

O objetivo era usado em sete fases. Em seis delas, escrevemos em script a melhor jogada em que conseguimos pensar: capturar a fonte no tick 0 e depois deixá-la em paz por 900 ticks, com quatro sementes cada. (14-8 não pode ser roteirizada assim, porque o inimigo mantém a fonte desde o início.)

| Fase | Espalhamentos necessários | Espalhamentos obtidos |
|---|---|---|
| 14-1 | 2 | 0 |
| 14-2 | 2 | 0 |
| 14-3 | 3 | 0 |
| 14-5 | 2 | 0 |
| 14-6 | 2 | 0 |
| 14-7 | 3 | 0 |

O inimigo toma as ilhas pequenas ao lado da fonte entre o tick 70 e o tick 250. O primeiro pulso chega no tick 150 ou depois, então muitas vezes não sobra nada para onde espalhar.

## Três coisas que tentamos

1. **Mover as ilhas.** Uma busca sobre as ilhas pequenas ao lado da fonte encontrou disposições que alcançam o número necessário em 14-1 e 14-5, mas só colocando quatro ou cinco ilhas pequenas ao lado da fonte. Isso quebra o nosso próprio limite de três, e 14-5 passa então a não cumprir o piso de que "o bot mais simples precisa vencer pelo menos algumas vezes". Dentro do limite, nenhuma disposição deu mais de um espalhamento.
2. **Antecipar o primeiro pulso.** Com o primeiro pulso em 60 ticks, 14-1 se torna possível e as outras cinco fases ficam em 0 ou 1. Também empurrou 14-8 para baixo do nosso piso para o bot mais simples. Não ficamos com ela.
3. **Mudar a regra.** O objetivo deveria premiar o que o jogador controla: manter a fonte. Então o objetivo de três estrelas virou o **número de pulsos da sua própria fonte**. Os números, escolhidos no nível ou abaixo do que os bots realmente alcançaram em partidas vencidas: 14-1: 4, 14-2: 3, 14-3: 2, 14-5: 3, 14-6: 1, 14-7: 3, 14-8: 1. A fase 14-4 mantém o seu objetivo separado.

Escolhemos a terceira. Ela afeta apenas o mar 14, então os hashes e os arquivos golden dos mares 1 a 13 não mudaram.

## Uma última passada no mar

Junto com isso, alargamos o meio de 14-1 (uma ilha central de 4 para 12) e suavizamos 14-6, onde um bot vencia muito mais que os outros. Agora um novo teste diz que nenhum bot pode levar mais da metade das vitórias em 14-8; hoje são 8, 17, 12 e 24 vitórias para quatro bots e 0 para o quinto.

## O que não verificamos

- Em 14-6 e 14-8 o inimigo mantém a fonte, então um pulso é o máximo com que se pode contar. Os bots raramente chegaram a ela, por isso os números se apoiam em poucos dados. **[não verificado]**
- Ninguém jogou estas fases à mão. Se "faça a fonte pulsar" fica claro no cartão da fase e na tela de resultado, é preciso testar em um celular de verdade. **[não verificado]**
- O jogo está em desenvolvimento e não foi lançado.
