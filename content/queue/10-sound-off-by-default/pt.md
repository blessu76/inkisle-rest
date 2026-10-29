---
title: Som desligado por padrão: uma escala para cada mar
description: O Inkisle começa em silêncio e o jogador liga o som. Como os sons são criados em código sem arquivos de áudio, como cada mar ganha sua própria escala de cinco notas e por que uma sequência de capturas sobe pela escala.
slug: sound-off-by-default
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, áudio de jogo, som procedural, escala pentatônica, jogo para celular, acessibilidade, configurações
image_alt: Cinco notas ascendentes desenhadas como pequenos pontos de tinta acima de uma fileira de ilhas.
---
Muita gente joga no celular em público ou na cama. Um jogo que começa alto é um jogo que se fecha. Por isso, no Inkisle, **o som fica desligado até o jogador ligá-lo**, e essa configuração é salva.

## Desligado é desligado de verdade

Quando o som está desligado, o código de áudio nem é iniciado: o reprodutor de som é criado na primeira vez em que um som é realmente necessário. Um jogo no mudo nunca toca o sistema de áudio do celular. Se a configuração salva estiver danificada ou o armazenamento falhar, a resposta volta a ser "desligado". O app também respeita a chave de silencioso do celular. Erros dentro do código de áudio são capturados em vez de escaparem, o que foi uma correção depois que uma revisão de código descobriu que um tipo de erro de áudio podia atravessar a rede de segurança.

## Sem arquivos de som

Cada som é **criado em código**. O app constrói, para cada tom, um WAV curto de 16 bits mono a 22.050 amostras por segundo: uma onda (senoidal, triangular ou dente de serra), um ataque de 12 ms e um decaimento exponencial. Não há arquivos gravados para licenciar. Os parâmetros dos tons vêm do protótipo web, então o app soa como o protótipo soava.

## Uma escala para cada mar

Cada mar tem sua própria **escala pentatônica**, cinco notas que soam bem em qualquer ordem:

| Mar | Passos acima da nota base (semitons) |
|---|---|
| Baía Calma (Calm Bay) | 0, 2, 4, 7, 9 |
| Estreito dos Ventos (Windy Strait) | 0, 2, 5, 7, 9 |

A nota base é 523,25 Hz. O segundo mar difere em uma nota, o terceiro passo (5 em vez de 4).

## As sequências sobem

Quando você captura várias ilhas seguidas, **cada captura soa um passo mais alta** na escala do mar. Depois de cinco passos a escala sobe uma oitava, e acima do décimo passo ela permanece na nota mais alta. Uma boa sequência, portanto, é audível como uma linha ascendente e, como a escala só tem notas que combinam entre si, uma sequência rápida se mantém afinada.

## O que não verificamos

- Os testes verificam as notas e que mudo significa silêncio. Eles não conseguem nos dizer se **soa agradável**. Ninguém fora da equipe ouviu no alto-falante de um celular real ou com fones de ouvido.
- Esses tons são bipes simples. Se permanecerão como som final ou serão substituídos não está decidido.
