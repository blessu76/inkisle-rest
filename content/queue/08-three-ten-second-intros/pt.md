---
title: Uma introdução de dez segundos em três versões: céu, mar e terra
description: O Inkisle abre com uma introdução de dez segundos que tem três versões. Como as três compartilham o mesmo final, por que um saco embaralhado decide qual você vê, quando ela encurta para três segundos e o que acontece com a opção de reduzir movimento ativada.
slug: three-ten-second-intros
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, introdução do jogo, abertura do app, botão de pular, reduzir movimento, acessibilidade, jogo para celular
image_alt: Ilhas em um mar verde-menta, com tinta cor de coral se espalhando por uma delas, a imagem de abertura da introdução do Inkisle.
---
A primeira coisa que você vê ao abrir o Inkisle é uma introdução. Queríamos que ela parecesse um pequeno acontecimento nas primeiras vezes e que depois **saísse do caminho**. Este post descreve como a introdução é construída e as regras que decidem o que você vê.

## Um final, três começos

A introdução completa dura **10 segundos**. Os primeiros 7 segundos vêm em três versões: **céu**, **mar** e **terra**. Os últimos 3 segundos são iguais em todas: o final que leva ao menu. Compartilhar o final significa que o desenhamos uma só vez e que todas as versões chegam ao mesmo lugar.

## Qual você recebe?

Escolher ao acaso pode mostrar a mesma introdução três vezes seguidas, o que parece um defeito. Por isso o app usa um **saco embaralhado**: coloca as três versões em um saco em ordem aleatória e tira uma a cada abertura. Quando o saco esvazia, é reabastecido. Duas consequências:

- Dentro de uma mesma rodada, **três aberturas seguidas mostram as três versões**.
- A primeira versão de uma nova rodada nunca é igual à última que você viu.

O saco é salvo no celular, então continua funcionando entre as aberturas.

## Longa no início, curta depois

Nas **três primeiras aberturas** você vê os 10 segundos completos. A partir da quarta abertura, o app reproduz apenas o final compartilhado, de **3 segundos**. Um botão de pular aparece **0,6 segundo** depois que a introdução começa, para que quem a vê pela primeira vez não seja convidado a pular antes de ver qualquer coisa. Pular chama a mesma etapa de "concluído" que o fim da introdução, e um teste verifica que ela roda apenas uma vez.

## Reduzir movimento

Se a configuração de reduzir movimento do celular estiver ativada (no iOS, "Reduzir Movimento"; no Android, animações desativadas), a introdução **não se move**. Ela mostra o quadro final já pronto por **1,2 segundo** e vai para o menu. O botão de pular está presente desde o início.

## Quando o saco salvo está corrompido

Nossa revisão de código descobriu que um saco salvo danificado nunca era reparado: o app não conseguia lê-lo, recomeçava a cada abertura e continuava mostrando a versão completa de 10 segundos. A correção é tratar dados ilegíveis como "sem dados" e gravar um novo imediatamente. Se o armazenamento não estiver disponível de forma alguma, o app escolhe uma versão ao acaso e reproduz a introdução completa, e nunca bloqueia o início do jogo. Há testes para esses casos.

## O que não verificamos

- Não medimos como a introdução funciona em um **celular real**. Os testes cobrem as regras acima, não a fluidez da animação.
- Se dez segundos é a duração certa para a primeira abertura é um palpite até que outras pessoas a vejam.
