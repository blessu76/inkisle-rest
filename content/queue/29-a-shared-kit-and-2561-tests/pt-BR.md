---
title: O que protegemos ao atualizar um kit compartilhado: um portão de 2.561 testes
description: Toda vez que o Inkisle atualiza o kit compartilhado que nossos apps usam, ele precisa passar por um portão de formato, análise e testes completos. Por que não substituímos um recurso inteiro do kit, como os testes de tempo oscilaram sob carga, quais arquivos mudaram na última atualização e o que não verificamos.
slug: a-shared-kit-and-2561-tests
lang: pt-BR
translation_of: en
category: making-of
keywords: Inkisle, kit compartilhado, testes, Game Center, atualização, jogo mobile
image_alt: Vários blocos pequenos de mesmo formato dentro de uma moldura, com um único ponto verde passando por cima deles.
---

O Inkisle, nosso jogo de estratégia de conquista de ilhas para iOS, usa um kit compartilhado em que vários dos nossos apps se apoiam. Toda vez que subimos a versão do kit, um portão executa formato, análise estática e a suíte completa de testes antes do commit. Em 19 de novembro passamos o kit de 0.15.2 para 0.15.3: o portão passou por 2.561 testes (8 ignorados), e apenas dois arquivos mudaram, `pubspec.yaml` e `pubspec.lock`. Este post trata de como esse número é mantido e do que oscilou pelo caminho. O jogo está em desenvolvimento e não foi lançado.

## O portão tem três etapas

Um script as executa em ordem antes de um commit: a formatação do código não pode mudar, a análise estática deve informar 0 problemas e todos os testes devem passar. Se alguma falhar, não fazemos o commit. Quando outra pessoa diz "passou", executamos de novo nós mesmos antes de fazer o commit.

## 14 de novembro: não substituímos o recurso inteiro do kit

Ao passar o kit de 0.12.0 para 0.13.0, ele passou a poder cuidar do apelido e do ranking do Game Center. A instrução do responsável era que todo jogo deixasse o jogador definir um apelido na primeira abertura e aparecer no ranking do Game Center. **Não trocamos pelo recurso de jogador completo do kit.** Tínhamos quatro razões para achar nossa versão melhor:

1. O apelido fica dentro do registro de configurações, que sincroniza entre dispositivos pelo iCloud. Movê-lo para o armazenamento do kit quebraria essa sincronização.
2. Já temos uma folha de apelido em 16 idiomas e testes congelados para combinações de idioma e tamanho de tela.
3. Os rankings são 24 quadros dinâmicos, com valores derivados do registro de progresso sincronizado. Movê-los deixaria dois lugares guardando uma melhor pontuação.
4. O Play Games no Android ainda precisa da biblioteca que ele usa.

Então só a conexão do Game Center no iOS passou para o kit, e os IDs dos quadros, os apelidos salvos e as melhores pontuações foram mantidos sem mudança. O reenvio de pendências após um login tardio e o preenchimento prévio do apelido com o nome do Game Center entraram ao mesmo tempo. Adicionamos 10 testes, e o portão passou então por 1.990 testes (7 ignorados).

## Testes de tempo oscilaram

Duas vezes neste portão, um teste que mede tempo oscilou sob carga. Um teste de orçamento de quadros que desenha 800 estradas falhou uma vez quando os testes rodavam em paralelo, e durante o trabalho com o iCloud um teste de orçamento de desempenho falhou uma vez. Ambos passaram quando rodados sozinhos ou quando a suíte completa foi executada de novo. Lemos isso como carga, não como nossa mudança [não verificado; não rastreamos a causa]. Não afrouxamos os orçamentos.

## 19 de novembro: dois arquivos mudaram

A versão 0.15.3 deixa a API pública como estava; ela faz uma recontagem na sincronização do iCloud parar após o desmonte e adiciona documentação. Não mudamos nenhum código nem teste no app. O limite de tamanho que o app usa (512 KB) é intencional, então o mantivemos. Os arquivos alterados foram `pubspec.yaml` e `pubspec.lock`, e o portão passou na primeira execução, desta vez sem oscilação de tempo. A contagem de testes cresceu de 1.990 em 14 de novembro para 2.561.

## O que não verificamos

- **Login no Game Center, envio de pontuação, tela de ranking e uma ida e volta do iCloud não foram verificados em um aparelho real [não verificado].** Vamos conferir no TestFlight.
- As telas de 375px e 320px foram cobertas por testes de widget em 320×568, em vez de vistas diretamente [não verificado].
- Não encontramos a causa raiz dos testes que oscilaram sob carga [não verificado].
- Os números aqui são os resultados do portão naquele dia, e a contagem de testes vai mudar depois.

## Perguntas frequentes

### O que é o kit compartilhado?

Um conjunto de código que vários dos nossos apps usam juntos. O Inkisle usa as partes de apelido, Game Center e sincronização do iCloud.

### O que vocês verificam ao atualizar o kit?

Um script verifica que a formatação não muda, que a análise estática informa 0 problemas e que todos os testes passam. Se alguma falhar, não fazemos o commit.

### O jogo foi lançado?

Não. Ele ainda está em desenvolvimento e não foi lançado.
