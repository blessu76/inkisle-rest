---
title: As regras numa página: ilhas, tropas, conquista
description: Todas as regras do Inkisle numa página: como as ilhas produzem tropas, como as frotas voam, como a conquista é calculada e como uma partida termina. Valores iniciais, antes dos testes.
slug: the-rules-on-one-page
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, regras do jogo, conquista de ilhas, motor determinístico, design de jogos, regras de conquista
image_alt: Ilhas com números de tropas e rotas pontilhadas por onde as frotas viajam entre elas.
---
Bons jogos de estratégia podem ser explicados em um minuto. Esta é a nossa tentativa de explicar as regras do Inkisle numa página. **Todos os números aqui são valores iniciais do documento de design.** Esperamos mudar alguns depois dos testes, e os próximos posts desta série mostrarão quais já mudaram.

## As ilhas produzem tropas

- Cada ilha que você possui acrescenta **1 tropa por segundo** (um "tick" são 100 ms, ou seja, uma tropa a cada 10 ticks).
- Há um **limite** de 45. Passado o limite, a ilha para de produzir, e as tropas extras vindas de reforços voltam ao limite a 1 por segundo. Isso impede que você empilhe tudo numa ilha só e fique esperando.
- **Ilhas neutras não produzem.** O número delas é fixo, então funciona como uma etiqueta de preço.
- Você começa com uma ilha-base de 20 tropas. O inimigo normalmente também, e quando não é assim, o cartão da fase avisa.

## Enviando frotas

Arraste de uma das suas ilhas até outra ilha e solte. Uma barra na parte de baixo escolhe a proporção: **25, 50, 75 ou 100%**. Você envia o arredondamento para baixo das tropas vezes a proporção, no mínimo 1. Com 100% você envia "tudo menos um", então a ilha nunca fica vazia e continua sua.

Uma frota voa em linha reta a **2,5 unidades de mapa por segundo**. Uma ilha vizinha a 4 a 8 unidades leva cerca de 1,6 a 3,2 segundos, e atravessar o mapa inteiro leva cerca de 11 segundos. As frotas não lutam no mar; elas se cruzam. Isso mantém honesta a prévia de chegada, e a tensão do gênero permanece: uma viagem longa é um risco, porque o alvo continua crescendo enquanto você viaja.

## Conquista, calculada na chegada

- Chegar a uma ilha sua soma as tropas.
- Chegando a uma ilha inimiga ou neutra, você precisa de mais que **a defesa vezes o multiplicador**. O multiplicador é 1,0 normalmente e **1,5 para uma fortaleza**.
- Ataque acima do exigido: você conquista, e a nova defesa é o que sobrou. Igual: o defensor resiste com 0 (empates favorecem o defensor). Abaixo: o defensor perde uma parte.

Dois exemplos. Uma frota de 18 chega a uma fortaleza de 10. A exigência é ceil(10 × 1,5) = 15, então você a conquista com 3 sobrando. Uma frota de 12 chegando à mesma fortaleza a deixa com 2.

Se várias frotas chegarem no mesmo tick, elas são resolvidas uma a uma, na ordem em que partiram.

## Como uma partida termina

- **Vitória:** o inimigo não tem ilhas nem frotas.
- **Vitória decisiva:** se você tem o triplo do total de tropas do inimigo e pelo menos 60% das ilhas por 5 segundos, o inimigo desiste. Isso evita a limpeza chata de uma partida já ganha.
- **Derrota:** você não tem ilhas nem frotas, ou perde uma ilha que devia proteger.
- **Limite de tempo:** aos 8 minutos simulados, vence o jogador com mais ilhas. Isso quase nunca deve acontecer.

## Um motor para tempo real e por turnos

O estado do jogo depende apenas do mapa inicial, de uma semente e de uma lista de comandos, sem relógio nem aleatoriedade dentro do motor. A mesma entrada dá o mesmo resultado em todos os dispositivos. É isso que permite ao mesmo motor rodar em tempo real agora e em turnos em rede depois, e faz com que replays e relatos de bugs se resumam a salvar uma lista de comandos.
