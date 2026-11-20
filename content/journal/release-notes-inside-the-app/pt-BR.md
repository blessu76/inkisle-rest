---
title: Notas de versão dentro do app: uma folha em 12 idiomas e uma verificação de tamanho
description: As notas de versão do Inkisle são uma folha dentro de Configurações, não uma página da web. Como as notas de cada build são escritas em 12 idiomas, as verificações de quantidade de itens e tamanho, e o bug de teste que mostrou uma folha vazia.
slug: release-notes-inside-the-app
lang: pt-BR
translation_of: en
category: making-of
keywords: Inkisle, notas de versão, localização, multilíngue, testes, jogo mobile
image_alt: Uma folha de papel subindo da parte inferior de uma tela, com doze pequenas abas de idioma em fileira acima dela.
published: 2026-11-20T17:45+09:00
---

As notas de versão do Inkisle, nosso jogo de estratégia de conquista de ilhas para iOS, são uma folha dentro do app, aberta a partir de Configurações, e não uma página da web. As notas de cada build são escritas em 12 idiomas, e um script de verificação confere a quantidade de itens e o tamanho. A verificação do build 34 resultou em 0 erros e 0 avisos. O jogo ainda está em desenvolvimento e não foi lançado.

## Removemos a página da web

No início, a tela principal tinha um link "Notas de versão" e um botão de informações (ⓘ). No build 32, removemos os dois. O que a janela de informações tinha (política de privacidade, termos, versão, licenças de código aberto, operador, contato e o aviso de 16+) foi para Configurações, e as notas de versão passaram a ser uma folha aberta por uma linha "Notas de versão" ali. A página de notas de versão do site também foi retirada em 15 de novembro. Sem um site separado, o texto dentro do app é a única fonte.

A folha usa a mesma moldura dos nossos outros pop-ups (InkSheet). Ela ocupa no máximo 60% da altura da tela, a linha do título e o X de fechar (48×48) ficam fixos, e só o conteúdo rola dentro da folha.

## Um build, um arquivo, 12 idiomas

Para cada build, `release_notes/<build>.json` guarda um título, uma introdução e os itens em 12 idiomas (ko, en, ja, zh-Hant, es, pt-BR, fr, de, id, th, vi, tr). Os arquivos são empacotados em `assets/release_notes.json`, que vai dentro do app, e a folha lê esse arquivo.

## Verificações de tamanho e quantidade

Um script de verificação lê os arquivos e informa as quebras de regra.

- **RN06:** um item deve ter 200 caracteres ou menos. O texto em alemão ficou longo, então o item de fim de temporada do build 34 foi reduzido para 183 caracteres. No build 31, dividimos um item de compra em dois para caber no limite.
- **RN05:** são recomendados de 3 a 6 itens. É apenas um aviso e não bloqueia uma publicação. Os avisos restantes são de builds antigos com 1 ou 2 itens; são um registro honesto do que foi escrito, então os deixamos como estão.
- Um teste falha se não houver entrada para a versão e o número de build atuais, então cada aumento de build exige que a nota em 12 idiomas seja escrita antes.
- O script de envio para iOS roda a verificação de notas de versão antes do portão verde (formato, análise, testes).

## O teste que viu uma folha vazia

Dois testes da folha de notas de versão passaram a ver uma folha vazia. A causa estava no teste, não no app. O pacote é um arquivo de asset real e, conforme ele cresceu, o `pumpAndSettle`, que espera a tela estabilizar, terminava antes de a leitura do arquivo ser concluída. Mudamos os testes para abrir a folha, esperar 300 ms com `runAsync` e desenhar de novo. O código do app não mudou.

## O que não verificamos

- As traduções que não são coreano nem inglês são feitas por máquina e não passaram por revisão de falantes nativos [não verificado].
- Não vimos a folha abrir a 60% em um aparelho real. Testes de widget em 375×667 e 320×568 fazem esse papel [não verificado].

## Perguntas frequentes

### Onde encontro as notas de versão do Inkisle?

No app, toque na linha "Notas de versão" em Configurações e uma folha se abre. Não há página da web separada. O jogo ainda não foi lançado.

### Em quantos idiomas elas estão escritas?

Em 12 idiomas. Exceto o coreano e o inglês, são traduções automáticas e ainda não foram revisadas.

### O que acontece se um item for longo demais?

Se um item passar de 200 caracteres, o script de verificação informa um erro, e então o encurtamos ou o dividimos em dois.
