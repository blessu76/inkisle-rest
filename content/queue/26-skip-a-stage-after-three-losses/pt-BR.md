---
title: Pular uma fase após três derrotas: uma oferta gentil com um custo
description: No Inkisle, perder três vezes a mesma fase oferece pulá-la por 3 Ink. Quando a oferta aparece, quais fases ficam de fora, como uma fase pulada aparece na carta e como tudo é salvo.
slug: skip-a-stage-after-three-losses
lang: pt-BR
translation_of: en
category: making-of
keywords: Inkisle, pular fase, dificuldade, design de jogos, dados salvos, jogo mobile
image_alt: Uma carta náutica com uma ilha marcada por uma pequena bandeira de coral e um caminho pontilhado que passa por ela até a próxima ilha.
---

No Inkisle, nosso jogo de estratégia de conquista de ilhas para iOS, perder três vezes a mesma fase faz aparecer uma pergunta: "Pular esta fase e tentar mais tarde?" Pular custa 3 Ink. A fase pulada ganha uma bandeira na carta e pode ser jogada quando você quiser. O jogo ainda está em desenvolvimento e não foi lançado, e ainda não vimos este aviso em um aparelho real.

## Por que oferecer um pulo

Algumas fases continuam difíceis mesmo depois do ajuste de dificuldade. Não queríamos que o jogador parasse em uma ilha. A oferta permite seguir adiante e voltar depois, em vez de abandonar o jogo.

## Quando ele pergunta

- O aviso aparece após a **terceira derrota** na mesma fase, depois que a folha de resultado se acomoda (1,1 segundo).
- Se o jogador recusa, ele não pergunta na 4ª e na 5ª derrota. Pergunta de novo na **6ª, na 9ª** e assim por diante. Perguntar sempre seria insistência; perguntar só uma vez deixaria de fora quem continua preso.
- As derrotas são contadas por fase. Vencer a fase zera a contagem. Derrotas em uma fase já concluída ou pulada não contam.

## Quanto custa

Pular custa **3 Ink**, o mesmo Ink que o jogador já ganha no jogo ou compra. Nenhuma moeda nem produto novo foi criado. O valor é uma única constante no código, e o texto do aviso, o botão e o link para a loja a acompanham.

Primeiro definimos 1 Ink e depois subimos para 3, quando o dono pediu entre 2 e 3. Se o jogador tem menos de 3 Ink, o botão de pular vira "Sem Ink, abrir a loja" e abre a folha da loja que já existe. Com 3 ou mais, o botão de pular volta.

## Quais fases ficam de fora

- As fases 1-1 a 1-4, o trecho de tutorial sem Ink. Pulá-las significaria nunca aprender os controles.
- A fase 1-5, em que o jogo dá de presente o primeiro Ink.
- A última fase, porque não há próxima fase para abrir.
- As fases de chefe estão incluídas.

## O que significa uma fase pulada

- A próxima fase abre, e a fase pulada fica com **0 estrelas**. Pular não é concluir, então estrelas não podem ser compradas.
- Na carta, o nó ganha uma bandeira de coral. Leitores de tela acrescentam "pulada". O cartão da fase diz: "Esta fase foi pulada. Desafie-a de novo quando quiser."
- Ao vencê-la depois, a bandeira some e as estrelas são registradas normalmente.
- Um mar só fica completo quando suas fases são concluídas, então uma fase com bandeira ainda precisa ser vencida para completar o mar.
- O final só abre com uma vitória de verdade, então pular a fase 10-8 não o abre.

## Como é salvo

O registro de progresso existente ganha duas chaves opcionais: a contagem de derrotas por fase e a lista de fases puladas. Se ambas estão vazias, as chaves não são gravadas, e um save antigo continua idêntico byte a byte. Na leitura, ids desconhecidos e valores negativos ou de texto são descartados, e uma fase já concluída perde a marca de pulo, porque a conclusão prevalece.

Na mesclagem com o iCloud, mantém-se a maior contagem de derrotas, as listas de puladas são unidas e uma conclusão em outro aparelho prevalece. Mesclar de novo o mesmo snapshot não muda nada, e um teste verifica isso.

## O que não verificamos

- O aviso e a bandeira em um aparelho real ou simulador. Testes de widget com largura de 375 e 320 px não encontraram estouro em 16 colunas de idioma, mas não olhamos capturas de tela.
- Se uma versão antiga do app que sobrescreva o snapshot do iCloud perde as duas chaves novas. Se perder, as fases concluídas e as estrelas permanecem e acreditamos que só as marcas de pulo se perderiam.
- As traduções além do coreano e do inglês não passaram por revisão de falantes nativos.

## FAQ

### Quando o Inkisle oferece pular uma fase?

Depois de perder três vezes a mesma fase, e de novo após a 6ª, a 9ª derrota e assim por diante, se você continuar tentando. As primeiras fases, a fase-presente 1-5 e a última fase ficam de fora.

### Quanto custa pular e eu ganho estrelas?

Custa 3 Ink. Uma fase pulada dá 0 estrelas. Se você vencê-la depois, ganha as estrelas normalmente.

### Pular completa um mar ou abre o final?

Não. Um mar só fica completo quando suas fases são concluídas, e o final só abre com uma vitória de verdade.
