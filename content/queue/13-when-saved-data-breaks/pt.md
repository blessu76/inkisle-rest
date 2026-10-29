---
title: Quando os dados salvos quebram: como o app se recupera
description: Um celular pode perder, truncar ou bloquear os dados salvos de um app. Como o Inkisle lida com armazenamento ausente, danificado, desatualizado ou indisponível para o progresso, a introdução e a configuração de som, e onde nossa recuperação ainda é grosseira.
slug: when-saved-data-breaks
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, dados salvos, tratamento de erros, robustez, armazenamento local, jogo para celular, save com versão
image_alt: Um pequeno caderno com uma página rasgada ao lado de uma fileira de ilhas, uma forma tranquila de mostrar um save danificado.
---
O Inkisle não tem contas nem servidor, então todo o progresso fica **apenas no celular**. Isso deixa os dados salvos simples, e também significa que ninguém pode restaurá-los por você. A pergunta que fizemos: o que o app deve fazer quando o que ele lê de volta está errado?

## Quatro coisas que podem dar errado

| Situação | O que o app faz |
|---|---|
| Ainda não há nada salvo | Começar na fase 1-1 |
| O texto salvo está danificado (não pode ser lido) | Tratar como vazio e começar do zero |
| Salvo por outra versão do formato | Ignorar e começar do zero |
| O armazenamento do celular não pode ser aberto de jeito nenhum | Jogar na memória; nada quebra, mas nada é mantido depois de fechar |

Os dados salvos levam um número de versão no nome e no conteúdo, de modo que uma mudança futura no formato possa ser reconhecida em vez de lida de forma errada.

## O dano em uma parte não apaga o resto

O registro de progresso tem uma entrada por fase. Nossa revisão apontou que uma única entrada danificada antes reiniciava tudo. Agora cada fase é lida separadamente: uma entrada ilegível é ignorada e as outras fases são mantidas. Só um arquivo totalmente ilegível, ou uma versão diferente, significa começar do zero. As entradas também precisam indicar que a fase foi **vencida**, porque só as vitórias são gravadas.

## Um reparo que repara de verdade

A introdução guarda seu próprio pequeno save (o saco embaralhado de um post anterior). Quando ele estava danificado, a leitura falhava antes de o app gravar qualquer coisa nova, então o texto quebrado continuava lá e o problema se repetia a cada abertura. A correção: se a leitura falhar, começa-se pelo padrão e **grava-se o padrão por cima**. O código da introdução tem testes para saves quebrados.

## As configurações voltam para a escolha silenciosa

A única configuração é o som. Se os dados salvos dela estiverem quebrados, a resposta é **desligado**, não ligado. Um arquivo quebrado nunca deveria deixar o jogo mais alto.

## O progresso só pode crescer

Estrelas e melhores tempos só são melhorados, e uma repetição perdida não muda nada. A regra de desbloqueio olha apenas se a fase anterior foi vencida.

## O que não verificamos

- Testamos no código texto danificado, versões erradas e armazenamento ausente. **Não** testamos um celular sem espaço nem um backup e restauração do sistema operacional.
- Quando o arquivo inteiro é ilegível, o jogador recomeça da fase 1-1. Para um jogador com muitas estrelas isso seria ruim, e não decidimos se vamos acrescentar algo mais gentil.
