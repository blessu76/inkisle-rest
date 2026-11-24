---
title: Um botão que o leitor de tela pode acionar
description: O ícone de fechar e o farol de Inkisle tinham rótulos para leitura, mas faltavam as ações de acessibilidade. Verificamos as palavras e o que acontece quando a pessoa aciona o controle.
slug: a-button-the-screen-reader-can-press
lang: pt-BR
translation_of: en
category: making-of
keywords: Inkisle, acessibilidade, leitor de tela, interface, testes de widgets
image_alt: Um X e um ícone de farol em dois cartões pequenos, com um contorno de foco ao redor de cada controle.
---

Inkisle é um jogo de estratégia e conquista de ilhas em desenvolvimento. Em uma revisão de acessibilidade, examinamos como o jogo descreve seus controles para um leitor de tela. Dois chamaram a atenção: o X que fecha um painel e o farol do mapa que permite rever um final. Estamos desenvolvendo o jogo para iOS.

## Do nome à ação

Os dois controles já tinham nomes. Na árvore de acessibilidade do Flutter, o nó com o nome perdeu a ação de toque quando substituímos a descrição padrão do ícone. Ligamos a ação ao mesmo nó que contém o rótulo. Nos testes, acionar Fechar fecha o painel, e acionar o farol abre o final.

## Ouvir uma vez

Também verificamos o que era lido duas vezes. Um botão que define a proporção da frota expunha a mesma porcentagem no rótulo e no texto visível. O controle de pular a introdução e os marcadores numerados do mapa tinham repetições parecidas. Mantivemos um único rótulo para leitura em cada caso, com a informação necessária para identificar o controle.

## Perguntas frequentes (FAQ)

### Isso foi testado em um celular com leitor de tela?

Os testes de widgets verificaram os rótulos e as ações de acessibilidade. Ainda não verificamos as mudanças com o VoiceOver em um iPhone.

### Para que serve o farol no mapa?

Acione o farol para rever um final.
