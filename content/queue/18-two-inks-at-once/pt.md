---
title: Dois itens de tinta ao mesmo tempo: vagas, intervalos e o que os bots nos mostraram
description: Nos primeiros mares, você só podia usar um item de tinta por vez. A partir do mar 5 pode usar dois, e depois três, com um intervalo entre os inícios. A tabela de regras, como o botão mostra isso e uma simulação que encontrou um efeito muito menor do que esperávamos.
slug: two-inks-at-once
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, itens de tinta, design de jogos, equilíbrio do jogo, simulação com bots, interface móvel, acessibilidade
image_alt: Duas pequenas gotas de tinta lado a lado acima de uma fileira de ilhas, desenhadas em cores vetoriais suaves.
---
Os itens de tinta (surto, âncora, névoa, lanterna, inversão da maré) funcionavam um de cada vez. Isso é fácil de entender, mas também significa que uma fase mais avançada nunca dá a sensação de que você tem mais ferramentas. Por isso demos ao botão de tinta **vagas**.

## A regra

| Mar | Vagas ao mesmo tempo | Intervalo entre inícios |
|---|---|---|
| 1 a 4 | 1 | nenhum (como antes) |
| 5 a 10 | 2 | 10 segundos |
| Volume 2, mares 11 a 20 | 2 | 5 segundos |
| Volume 3, a partir do mar 21 | 3 | 5 segundos |

O que continua igual: um chefe soma 5 segundos ao intervalo; o limite de usos por fase (5 ou 6) é compartilhado por todas as vagas; não é possível usar dois itens do mesmo tipo; a vaga de uma âncora ou de névoa é liberada quando sua ilha é capturada; e os primeiros 20 segundos de uma fase ainda bloqueiam toda a tinta.

## Como o botão mostra isso

O botão de tinta tem um ponto por vaga, preenchido enquanto a vaga está em uso. Um anel fino dentro do botão conta o intervalo antes de você poder iniciar o próximo. Na folha do porto, um cartão bloqueado diz "próxima tinta em N segundos" durante o intervalo, ou "espalhando" quando as vagas estão cheias. O rótulo de acessibilidade é lido como "1 de 2 vagas". Tudo isso está em 12 idiomas.

## Por que o motor não precisou de um novo hash

O estado do jogo já guarda uma lista dos horários de término da tinta em uso e a contagem de usos, então os mares 1 a 4 se comportam e geram o hash exatamente como antes. Os testes cobrem cada linha da tabela, o comportamento do primeiro mar, a recusa do mesmo tipo, vagas cheias, três vagas, o limite compartilhado e a liberação na captura, além do botão em 320 e 375 px.

## O que os bots disseram

Simulamos 80 fases do mar 5 ao 14, com cinco bots e 24 sementes cada, para quatro planos de dois ou três itens começando aos 20 segundos, e comparamos o melhor plano na regra antiga (uma vaga, sem intervalo) com a nova regra.

- O ganho médio foi de **+1,1 ponto percentual** (+0,9 nos mares 5 a 10, +1,5 nos mares 11 a 14). Esperávamos de 3 a 8.
- Nos chefes foi de +0,9. A melhor taxa de vitórias com tinta em relação a sem tinta foi de +36 pontos, dentro do nosso limite de 40.
- Fase por fase, a mudança variou entre −7 e +10, que é mais ou menos o ruído de 24 sementes.

Os bots raramente usam bem a segunda vaga, então o número pequeno pode dizer mais sobre os bots do que sobre a regra. **[não verificado]** Uma pessoa poderia ganhar mais.

## O que não verificamos

- Se uma pessoa acha as duas vagas e o intervalo claros, ou se parece um bloqueio. Não testamos em um celular de verdade. **[não verificado]**
- Um aviso de uma linha na primeira vez que o jogador chega a um mar de duas vagas (5-1) ainda não foi feito.
- O jogo está em desenvolvimento e não foi lançado.
