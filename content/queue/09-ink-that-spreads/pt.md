---
title: Tinta que se espalha: os pequenos efeitos que dizem o que acabou de acontecer
description: No Inkisle, uma ilha capturada deixa uma mancha de tinta, uma virada mostra um banner e a última ilha inimiga se ilumina. Para que serve cada efeito, quanto tempo dura e como funciona a dica do dedo na primeira partida.
slug: ink-that-spreads
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, sensação de jogo, feedback visual, jogo para celular, dica de introdução, animação
image_alt: Uma mancha de tinta cor de coral se espalhando sobre uma ilha capturada enquanto frotas se movem entre outras ilhas.
---
Em um jogo sobre pintar o mapa da sua cor, o momento mais importante é **quando uma ilha muda de mãos**. Se for apenas uma troca de cor, é fácil não notar em uma tela pequena. Por isso acrescentamos alguns efeitos pequenos cuja função é dizer "isso acabou de acontecer".

## A mancha de captura

Quando uma ilha muda de dono, uma **mancha de tinta** se espalha a partir dela na cor do novo dono e depois desaparece. Dura cerca de **0,75 segundo**. A forma é uma mancha irregular desenhada do mesmo modo que as manchas da introdução, então o jogo e sua abertura parecem aparentados. Um teste verifica que uma captura deixa uma mancha e que ela desaparece depois.

## Três momentos que recebem uma mensagem

- **Uma virada.** Quando você estava atrás e assume a liderança, um banner aparece **uma única vez**. Ele fica visível por cerca de 1,6 segundo. "Uma vez" importa: um banner que dispara toda vez que a liderança alterna vira ruído.
- **A última ilha.** Quando o inimigo fica com **sua última ilha**, essa ilha é destacada para você saber onde mirar.
- **Concluir um mar.** Limpar um mar inteiro tem seu próprio momento curto, separado da tela de resultado de uma única fase.

## A dica do dedo na primeira partida

Um jogador novo não sabe que se arrasta de uma ilha para outra. Na primeira vez em uma fase, um pequeno **dedo desliza da sua ilha até a outra ilha mais próxima**. Ele some assim que você envia qualquer coisa, e um teste verifica isso. Mantivemos o efeito pequeno e curto para não atrasar quem já conhece o controle.

## O que não verificamos

- Tudo isso é coberto por testes sobre **quando** um efeito aparece, não sobre **como ele é sentido**. Tempo, tamanho e cor são primeiros palpites e ninguém fora da equipe os experimentou em um celular real.
- Ainda não sabemos se o banner de virada anima ou apenas distrai.
