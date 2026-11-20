---
title: O engasgo na fase 5-8: era a tela, não o motor do jogo
description: A fase 5-8 do Inkisle estava engasgando. Medimos antes de mexer em qualquer coisa, vimos que o custo estava em desenhar a tela e não nas regras do jogo, e reduzimos o custo de um quadro de 3,4 para 1,3 ms em um computador. O que mudamos, o que deixamos como estava e o que ainda não verificamos em um celular.
slug: the-stutter-on-stage-5-8
lang: pt-BR
translation_of: en
category: making-of
keywords: Inkisle, desempenho, engasgo, tempo de quadro, design de jogos, jogo mobile, otimização
image_alt: Quatro barras roxas altas à esquerda e quatro barras coral baixas à direita, com uma seta no meio e uma linha tracejada marcando o orçamento.
---

O Inkisle, nosso jogo de estratégia de conquista de ilhas para iOS, engasgava na fase 5-8 durante os testes. O palpite fácil era que o motor do jogo, a parte que move as frotas e decide as capturas, tinha ficado pesado demais. Medimos primeiro. O problema não era o motor, e sim a tela ao redor dele. Depois da mudança, o custo de um quadro na fase 5-8 caiu de 3,4 ms para 1,3 ms no nosso computador. O jogo está em desenvolvimento e não foi lançado, e esses números não vêm de um celular.

## O que medimos

Um quadro tem dois tipos de trabalho: avançar um tick das regras do jogo e montar e desenhar a tela. Na fase 5-8, um tick das regras custava em média apenas de 3 a 5 microssegundos. A tela custava cerca de mil vezes mais.

A maior parte desse custo de tela vinha de três coisas:

1. **Todo o HUD era reconstruído a cada quadro.** O controlador do jogo anunciava uma mudança a cada quadro, então as barras de poder, o texto do objetivo, a folha de resultado, a barra de proporção, os emblemas, a barra de escolha, a sobreposição de crise e o botão de maré eram reconstruídos mesmo sem nada ter mudado. Cerca de 2,5 ms dos 3,4 ms iam para construir widgets.
2. **Os rótulos numéricos erravam o cache.** A chave do cache incluía a transparência e o tamanho exatos de cada número, e eles mudam continuamente durante a expansão de uma captura ou um esmaecimento. Assim, cada quadro gerava layouts novos, e quando o cache passava de 600 entradas era limpo por inteiro, então um quadro tinha de refazer o layout de tudo. O tempo de desenho no 1% de quadros mais lentos era de 5 a 10 vezes a média.
3. **Pequeno trabalho repetido.** Cada frota consultava duas vezes a sua cor de tinta, a posição e o raio de cada ilha eram recalculados para cada frota, e um cache de shader usava uma chave de texto.

## O que mudamos

- O HUD agora escuta um pequeno sinal que dispara só quando algo que ele mostra muda, como o tick, a pausa, a velocidade, o estado de crise, os objetivos ou as dicas. A pintura continua acontecendo a cada quadro, como antes.
- Os rótulos numéricos são arredondados em degraus grosseiros (transparência em 32 degraus, tamanho em quartos de pixel) para que o cache acerte, e quando ele enche só a metade mais antiga é removida.
- As consultas repetidas são calculadas uma vez por quadro, e a chave do shader passou de uma string para um registro.

O arredondamento de tamanho e transparência não é visível a olho nu.

## Os números

Foram medidos em um computador, com uma tela de 375 × 667, em um modo que só serve para comparar antes e depois.

| | antes | depois |
|---|---|---|
| Fase 5-8, quadro inteiro, média | 3.433 µs | 1.267 µs |
| Fase 5-8, quadro inteiro, 1% mais lento | 10.803 µs | 5.182 µs |
| Fase 5-8, desenho, média | 818 µs | 201 µs |
| Fase 5-8, desenho, 1% mais lento | 4.540 µs | 1.284 µs |

Um jogo a 60 quadros por segundo tem cerca de 16,6 ms por quadro, então, mesmo antes da mudança, o trabalho cabia nesse orçamento em um computador. Por isso o engasgo que sentimos pode ter também outra causa (veja abaixo).

## O que deixamos como estava

Não mudamos uma linha sequer das regras nem do código de balanceamento. Só a camada de tela mudou: como o controlador anuncia as atualizações, quais widgets escutam e os caches de desenho. A mesma semente continua produzindo o mesmo resultado de 600 ticks, e as verificações existentes de imagens de referência, jogo determinístico e simulações de bots continuaram verdes.

Também deixamos um custo real para depois. A previsão de crise roda na thread da tela: na fase mais pesada que medimos, a 17-3, ela levou em média 3,4 ms e seu 1% mais lento chegou a 11,8 ms, o que pode causar um pequeno engasgo a cada meio segundo. Espalhar esse trabalho por vários quadros daria o mesmo resultado, mas arrisca mudar decisões, então não o fizemos agora. Na fase 5-8 ela custa 0,17 ms e não importa.

## O que adicionamos

Um benchmark do motor sem tela e um teste de desempenho com limites superiores folgados. Ele pega o tipo de regressão em que o custo explode com o número de frotas ou em que cada quadro aloca memória demais. Mantivemos os limites folgados de propósito, porque limites apertados falhariam sempre que a máquina de testes estivesse ocupada. Por padrão, os mais pesados desses testes são pulados e só rodam quando pedidos.

## O que não verificamos

- **A taxa de quadros em um celular de verdade, a 60 ou 120 quadros por segundo, não foi verificada.** Nossos números são custo da thread da tela em um computador, não custo gráfico em um dispositivo.
- **O véu de névoa e as camadas de faixa não foram medidos nem alterados.** Elas são desenhadas com um desfoque em tela cheia, que custa ao chip gráfico e não ao processador. Se a fase 5-8 ainda engasgar em um celular, é o nosso primeiro suspeito.
- Não olhamos a renderização no navegador em 320, 375, 768 e 1280 px, porque nenhum layout mudou.
- Que a entrada fique mais responsiva é apenas uma expectativa nossa.

## FAQ

### Por que a fase 5-8 do Inkisle engasgava?

Nossa medição apontou para a tela sendo reconstruída e os rótulos numéricos sendo refeitos a cada quadro, não para as regras do jogo. Corrigimos isso; a taxa de quadros em um celular de verdade ainda não foi verificada.

### A otimização mudou a forma de jogar?

Não. Não tocamos nas regras nem no código de balanceamento, e a mesma semente dá o mesmo resultado de antes.

### Ainda engasga em um celular?

Ainda não sabemos. Nossos números vêm de um computador. Vamos verificar em um dispositivo real no TestFlight.
