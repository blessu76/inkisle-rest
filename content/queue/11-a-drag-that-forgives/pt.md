---
title: Um arrastar que perdoa: as pequenas regras por trás de um gesto
description: Enviar uma frota no Inkisle é um único arrastar. As pequenas regras que o fazem funcionar com um dedo de verdade: uma área de seleção maior, um arrastar que amostra o caminho inteiro, um dedo de cada vez e mensagens claras quando um envio não é possível.
slug: a-drag-that-forgives
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, controles por toque, UX de jogos mobile, arrastar e soltar, multitoque, design de jogos
image_alt: Um polegar arrastando de uma ilha coral através do mar até uma ilha vizinha, com uma linha pontilhada atrás.
---
A primeira fase ensina o controle inteiro em uma linha: **arraste uma ilha até outra ilha e um navio parte**. Essa frase esconde muitas decisões pequenas, porque um polegar é bem mais desajeitado que um mouse. Este post reúne as que temos mais certeza.

## O dedo é maior que a ilha

Uma ilha na tela pode ser menor que a ponta de um dedo, e o dedo a cobre enquanto você mira. Por isso, quando você passa por ilhas durante um arrastar, a área que conta como "sobre esta ilha" é **o raio da ilha mais 12 pixels**. Sem essa margem extra, um arrastar que visivelmente terminava numa ilha muitas vezes errava.

## Um deslize rápido não pode pular uma ilha

Quando você desliza por várias ilhas para escolhê-las, a tela só informa a posição do seu dedo de tempos em tempos. Um deslize rápido podia saltar de um lado de uma ilha para o outro sem nunca ser informado dentro dela. Por isso o jogo **amostra ao longo da linha** entre dois relatos, de modo que toda ilha que o dedo cruzou é contada.

## Um dedo de cada vez

Nossa primeira revisão de código encontrou um caso em que não tínhamos pensado: se um **segundo dedo** toca a tela no meio de um arrastar, o segundo toque substituía o primeiro, e os movimentos dos dois dedos se misturavam. Isso podia deixar a seleção num estado estranho ou enviar uma frota que ninguém queria enviar. A correção é simples: o jogo segue **apenas o primeiro dedo** e ignora os outros até ele ser levantado. Um teste cobre o segundo dedo sendo ignorado.

## Dizer por que nada aconteceu

Se você tenta enviar de uma ilha com poucas tropas, o envio não acontece. O silêncio parece um bug, então o jogo mostra uma mensagem curta: uma ilha precisa de **pelo menos 2 tropas** para enviar. Manter uma ilha pressionada por **0,4 segundo** seleciona todas as suas ilhas, e uma mensagem diz para tocar ou arrastar até um alvo para um ataque total.

## A quantidade a enviar

Quanto sai de uma ilha é definido por uma barra de proporção. O padrão é **50%**. A fase 1-2 ensina a escolher a proporção, e sua meta de três estrelas é vencer **sem nunca enviar 100%**, o que o incentiva a experimentar as outras configurações.

## O que não verificamos

- Tudo aqui foi verificado com toques simulados em testes. **Não vimos pessoas reais** usando em celulares reais, e gestos que parecem bons num teste ainda podem parecer errados.
- Os tamanhos (12 px, 0,4 s) são primeiros palpites. Eles vão mudar se os jogadores errarem as ilhas ou selecionarem tudo por acidente.
