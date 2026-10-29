---
title: Um protótipo jogável em um dia
description: Dezesseis fases, dois mares e um único arquivo HTML de cerca de 95 KB sem requisições externas. Como o protótipo é construído, o que testamos em um navegador sem interface e o que não conseguimos testar.
slug: a-playable-prototype-in-a-day
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, protótipo, protótipo web, motor de jogo determinístico, jogo HTML, jogo para celular, canvas
image_alt: Muitas ilhas pequenas com números de tropas e uma frota atravessando o mar no protótipo do Inkisle.
---
Antes de construir um app, queríamos algo jogável no celular. Em 2026-10-29, construímos um protótipo web em um único dia. Este post descreve o que há nele, como é montado e, igualmente importante, o que não conseguimos verificar.

![Três telas de celular do protótipo: a carta náutica com um cartão de fase, uma batalha com um arrasto em andamento e um resultado de vitória com três estrelas. O texto nas capturas de tela está em coreano.](/assets/posts/img/proto-shots.jpg)
*A carta náutica com um cartão de fase, uma batalha com um arrasto em andamento e a tela de resultado.*

## O que há nele

- **Dezesseis fases:** o mar 1, "Baía Calma" (Calm Bay), tem oito, e o mar 2, "Estreito dos Ventos" (Windy Strait), tem oito. Os mares seguintes aparecem como cartões bloqueados.
- **O ciclo:** carta, cartão de fase, batalha, resultado com uma a três estrelas, próxima fase.
- **Desbloqueio:** vença uma fase e a próxima se abre. Vença o chefe e o próximo mar se abre. As estrelas nunca bloqueiam o progresso; são metas extras.
- **Som:** sintetizado no navegador, com uma escala pentatônica diferente para cada mar e uma nota que sobe a cada captura em sequência.
- **O progresso** é salvo no armazenamento local do navegador, e o jogo continua funcionando na memória se o armazenamento estiver bloqueado.

## Como é construído

- **Um só arquivo.** Cerca de 95 KB, sem requisições externas e sem fontes web, então roda offline e dentro de um frame.
- **Motor e tela são separados.** O motor é um módulo puro, sem DOM, sem relógio e sem chamadas aleatórias. A interface apenas enfileira comandos como "enviar 50% da ilha 0 para a ilha 1", e um laço avança o motor a cada 100 ms.
- **A aceleração funciona avançando mais rápido**, e não mudando as regras, então os limites de tempo das estrelas continuam justos em 2x.
- **A pausa** interrompe os ticks, e o jogo pausa sozinho quando a aba fica oculta.

Manter o motor puro foi uma aposta no futuro: o mesmo código poderá rodar depois turno a turno por uma rede, e uma lista de comandos gravada pode reproduzir uma partida.

## O que testamos

Conduzimos o protótipo com um Chrome sem interface. Em uma tela de 375 por 812, ele começou com o armazenamento vazio, enviou frotas com arrasto do mouse e com arrasto por toque, pausou (o contador de ticks ficou parado), venceu a fase 1-1 em cerca de 12 segundos com três estrelas, salvou o progresso, desbloqueou a 1-2 e manteve o progresso após recarregar. Em 320 por 568, nada transbordou para os lados. O console do navegador não mostrou erros.

Também fizemos uma verificação determinística: o mesmo mapa e os mesmos comandos deram o mesmo resultado em cada execução, e rodar em tempo real e por turnos deu o mesmo desfecho.

## O que não conseguimos testar

- **Dispositivos reais.** iOS Safari e um celular Android intermediário **não foram verificados**. A emulação de toque de um navegador sem interface não é um dedo.
- **Desempenho.** Nossa meta é 22 ilhas e 300 frotas a 60 quadros por segundo. Não foi medida.
- **Recursos que faltam:** um modo de jogo livre, uma forma de exportar registros de jogo, salvamento no meio da fase e várias animações.
- **Arestas conhecidas:** o rótulo do arrasto pode cobrir o número de uma ilha vizinha, e o cartão de fase pode cobrir nós da carta.

Os próximos passos são um teste de 30 minutos com cinco a oito pessoas, com um registro de jogo embutido antes. O próximo post é sobre o trabalho de balanceamento que fizemos sem humanos.
