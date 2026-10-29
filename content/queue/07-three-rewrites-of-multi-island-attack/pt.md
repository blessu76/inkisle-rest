---
title: Enviar de várias ilhas ao mesmo tempo: três reescritas de um único controle
description: Atacar uma ilha a partir de várias das suas era o controle mais difícil do Inkisle. A primeira versão baseada em arrastar, a correção de tocar para selecionar e a versão de deslizar para selecionar, e o que cada uma nos ensinou.
slug: three-rewrites-of-multi-island-attack
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, controles por toque, UX de jogos mobile, seleção múltipla, arrastar e soltar, design de jogos, iteração
image_alt: Uma batalha em que várias ilhas enviam frotas para uma ilha inimiga.
---
Enviar uma frota é fácil: arraste da sua ilha até o alvo. O difícil nos controles do Inkisle é **enviar de várias ilhas ao mesmo tempo**, porque as fases finais são vencidas chegando juntos. Reescrevemos esse controle três vezes em poucas horas, e a história mostra o porquê.

## v0.1: tudo de uma vez

O primeiro protótipo aceitava várias formas de fazer isso:

- Arrastar de uma ilha até um alvo e **passar por cima das suas outras ilhas no caminho** para adicioná-las como origens.
- **Pressionar e segurar** (0,4 segundo) uma ilha para selecionar todas as suas e depois arrastar para um ataque total.
- Tocar em uma origem e depois tocar no alvo, como alternativa ao arrastar.

No papel, cobria tudo. Na prática, o polegar cobre justamente a ilha por onde está passando, e uma fase que ensinava "passe por cima das ilhas enquanto arrasta" pedia um gesto difícil de ver e difícil de mirar.

## v0.1.1: selecionar primeiro, depois ir

A solução foi dividir o gesto em dois. **Toque nas suas ilhas uma a uma para selecioná-las**, depois toque no alvo e todas partem. Arrastar uma ilha selecionada ainda envia o grupo inteiro. Acrescentamos:

- um pequeno emblema acima da seleção que mostra quantas ilhas estão escolhidas,
- um toque no mar vazio para limpar a seleção,
- uma área de seleção maior ao juntar ilhas durante o arrasto (raio da ilha mais 12 px), já que um dedo é maior que uma ilha,
- uma dica mostrada nas primeiras vezes, e os cartões de fase que ensinam o controle agora descrevem o toque.

Tocar é preciso e tranquilo, mas com muitas ilhas são **muitos toques** antes de cada ataque. Em um jogo em tempo real, isso é tempo.

## v0.1.2: deslizar para escolher

A versão mais recente permite **deslizar o dedo sobre as suas ilhas para escolhê-las em um só traço**, e depois escolher o alvo. Selecionar quatro ilhas agora é um único movimento em vez de quatro toques. Se os métodos anteriores continuarão como alternativa, e como o deslize se sente em detalhe, ainda não está definido **[não verificado no momento da escrita]**.

## O que aprendemos e o que não sabemos

- **Um gesto que exige que o dedo pouse em um alvo pequeno enquanto se move é frágil em um celular.** A primeira correção eliminou a mira; a segunda eliminou a repetição.
- Cada versão resolveu um problema e expôs o seguinte, o que é normal, mas também significa que o controle ainda não está assentado.
- **Não temos dados de jogadores externos** sobre nenhuma das três versões. A sensação exata da v0.1.2 é **[não verificada]** até que outras pessoas a experimentem.

O teste com cinco a oito pessoas é onde esse controle será realmente julgado. Se elas ainda hesitarem antes de atacar, vamos mudá-lo pela quarta vez.
