---
title: Dois mares grátis e uma só liberação: como simplificamos o pagamento
description: O Inkisle mantém os mares 1 e 2 grátis e libera o resto com uma única compra, Liberar todos os mares. Como a tinta consumível está configurada, como o bloqueio é calculado no código, as linhas que traçamos na restauração e nos reembolsos, e o que ainda não testamos.
slug: two-free-seas-and-one-unlock
lang: pt-BR
translation_of: en
category: making-of
keywords: Inkisle, compra no aplicativo, não consumível, mares grátis, restaurar compras, jogo mobile
image_alt: Duas ilhas abertas, depois uma fileira de ilhas com cadeados atrás, e uma chave atravessada sobre a fileira.
published: 2026-11-19T19:17+09:00
---

O Inkisle, nosso jogo de estratégia de conquista de ilhas para iOS, mantém os mares 1 e 2 grátis e libera os mares 3 a 30 (28 mares) com uma única compra, Liberar todos os mares. A tinta consumível está na configuração de venda, mas não foi lançada nem testada em aparelho. Os seis itens de gorjeta continuam como estão. Os produtos da loja estão na etapa de cadastro, mas ainda não foram enviados para análise nem testados em aparelho, então a compra ainda não está confirmada. O jogo está em desenvolvimento e não foi lançado, e esta publicação não informa preço nem data.

## O que mudou

O primeiro design tornava gratuitas todas as fases, e a tinta que reduz a dificuldade era vendida em pequenos itens consumíveis. Em 15 de novembro, o responsável mudou isso. **Os mares 1 e 2 são grátis, e Liberar todos os mares é uma compra única não consumível.** A tinta consumível (pacotes de 5 e de 15) está na configuração de venda, mas não foi lançada nem testada em aparelho. Também se obtém tinta com estrelas: uma a cada 5 estrelas, e 2 por vencer um chefe. A tinta comprada antes continua funcionando.

## O bloqueio é calculado

O número de mares bloqueados não é digitado no código. É o total de mares menos a quantidade de mares gratuitos. Hoje isso dá 30 − 2 = 28, e quando forem adicionados mares, o texto da folha de compra "libera N mares" acompanha. O texto de venda que preparamos promete que os novos mares estão incluídos.

- No mapa, as fases a partir do mar 3 têm um cadeado vermelho, e tocar em uma abre a loja em vez da fase.
- Comprar ou restaurar libera todos.
- Depois de uma vitória, se a próxima fase estiver em um mar bloqueado, o jogo volta ao mapa.

## O app precisa funcionar sem o produto

Se a loja ainda não tiver o produto, ou se a consulta de preço falhar, só o botão de compra é desativado e aparece uma nota de "em breve". O app não quebra. O preço é consultado de novo sempre que a folha abre, então, quando o produto existir, funciona sem nenhuma mudança de código. É exatamente onde estamos agora. A configuração do produto está travada do lado da loja, por isso nunca executamos o fluxo de compra real.

## Linhas que traçamos de propósito

| Caso | Comportamento |
|---|---|
| Um jogador que já passou do mar 2 | Fica bloqueado. Registros e estrelas permanecem, e uma compra ou restauração os libera de novo |
| Outro dispositivo | O progresso chega pelo iCloud, mas a liberação não. Toque em "Restaurar compras" ali |
| Reembolsos | Não retiramos o acesso |
| "Liberar tudo" no TestFlight | Remove o bloqueio de progresso, mas não o bloqueio de pagamento, para que o fluxo de compra possa ser testado no sandbox |

Não retirar o acesso após um reembolso é ao mesmo tempo uma escolha e um limite. O pacote `in_app_purchase` do Flutter não tem um estado que informe reembolsos, e, nesta escala, decidimos não verificar recibos em um servidor. Esse julgamento é uma estimativa [não verificado].

## O que não verificamos

- Não compramos nem restauramos em um aparelho real [não verificado]. Até agora há testes de widget (cadeado, loja, compra, liberação) e uma verificação da configuração do StoreKit.
- As telas de 375 px e 320 px foram cobertas por testes de widget, não por um simulador [não verificado].
- O Android usa o mesmo caminho de código, mas, sem um produto registrado, não conseguimos testar o pagamento ali [não verificado].
- O texto de compra nos 11 idiomas que não são coreano é traduzido por máquina [não verificado].

## Perguntas frequentes

### Quanto do Inkisle é grátis?

Os mares 1 e 2. Os outros 28 mares são liberados juntos quando se compra Liberar todos os mares. O jogo ainda não foi lançado.

### Quantas vezes preciso comprar?

Uma vez. É uma compra não consumível, pensada para incluir também os novos mares.

### As gorjetas afetam o jogo?

Não. Os seis itens de gorjeta não dão vantagem no jogo e permanecem como estão.
