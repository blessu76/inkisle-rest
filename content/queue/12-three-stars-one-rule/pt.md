---
title: Três estrelas, uma regra: como uma fase é avaliada
description: Cada fase do Inkisle pode render até três estrelas. O que cada estrela significa, por que as estrelas nunca bloqueiam o progresso nem diminuem, os 13 tipos de metas de três estrelas e o rótulo errado que encontramos e corrigimos.
slug: three-stars-one-rule
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, avaliação por estrelas, progressão do jogo, design de jogos, jogo mobile, rejogabilidade
image_alt: Uma fileira de três estrelas, as duas primeiras preenchidas em coral e a terceira apenas um contorno.
---
Cada uma das 16 fases do Inkisle dá de uma a três estrelas. As estrelas são o jeito do jogo dizer "você pode fazer melhor" sem obrigar você. Aqui está a regra, e um erro que cometemos ao explicá-la.

## O que cada estrela significa

1. **★1: vencer.** Você vence a fase.
2. **★2: vencer dentro do limite de tempo da fase.** Cada fase tem seu próprio limite.
3. **★3: a meta própria da fase.** Uma meta diferente para cada fase, mostrada no seu cartão.

O jogo decide essas três condições em um só lugar, e as telas apenas pedem o resultado a ele. Parece óbvio, mas quando escrevemos o gráfico e a folha de resultados pela primeira vez, pedaços da regra tinham vazado para os dois. Uma revisão encontrou, e movemos as verificações para pequenas funções auxiliares ao lado da regra; assim, se a regra mudar, há um só lugar para alterar.

## As estrelas nunca atrapalham

- **As estrelas não desbloqueiam nada.** Vencer uma fase abre a próxima. Derrotar o chefe abre o próximo mar.
- **As estrelas nunca diminuem.** Rejogue uma fase e perca, e nada é registrado. Rejogue e vença, e o jogo guarda o melhor de tudo: uma estrela conquistada permanece, e o melhor tempo é mantido.

Então rejogar só pode ajudar você.

## Treze tipos de metas de três estrelas

A meta de ★3 é diferente em quase todas as fases. Há 13 tipos até agora, por exemplo:

- perder no máximo um número de tropas,
- vencer sem nunca enviar 100%,
- tomar todas as ilhas vazias,
- nunca perder uma única ilha,
- capturar uma fortaleza em um só ataque,
- resistir uma vez a um ataque inimigo simultâneo,
- não atacar a ilha-base do inimigo antes de um tempo determinado.

Cada meta é escrita em palavras simples no app, por exemplo "Vença sem enviar 100%."

## O rótulo errado

O rótulo de ★1 dizia primeiro "**vença mantendo suas ilhas**". Mas a condição era apenas "vencer": você podia perder ilhas e mesmo assim ganhar a estrela. O rótulo prometia algo que o jogo não verificava. Uma revisão pegou isso, e agora o rótulo é simplesmente "**vencer**".

## O que não verificamos

- Os limites de tempo de ★2 foram definidos pelo protótipo e, como o teste com bots de um post anterior mostrou, parecem **generosos demais** para bots. Ainda não sabemos como são os tempos humanos.
- Não sabemos se os jogadores vão achar que 13 metas diferentes são interessantes ou apenas confusas.
