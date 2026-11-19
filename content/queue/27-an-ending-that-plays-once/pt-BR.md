---
title: Um final que toca uma só vez, e um farol para vê-lo de novo
description: O final da temporada 1 de Inkisle toca sozinho exatamente uma vez, na primeira vez que a última fase do ato 30 é concluída. Como definimos as regras de repetição, como tratamos quem já concluiu e o final do ato 10, e o que ainda não verificamos nas traduções nem em um aparelho real.
slug: an-ending-that-plays-once
lang: pt-BR
translation_of: en
category: making-of
keywords: Inkisle, temporada 1, final, final aberto, farol, design de jogos, jogo mobile
image_alt: Uma ilha solitária em um mar calmo com um farol aceso, e a rota da carta náutica parando diante dele.
---

O final da temporada 1 de Inkisle, nosso jogo de estratégia de conquista de ilhas para iOS, toca sozinho uma vez, na primeira vez que a fase 8 do ato 30 é concluída. Para assisti-lo de novo, o jogador toca o farol no topo do ato 30. O final não tem palavra de encerramento; a única marca é "Inkisle · Season 1". Este texto fala menos do que o final mostra e mais de quando ele toca e quando não toca, e de como definimos essas regras. O jogo está em desenvolvimento e não foi lançado.

## Quatro regras

Estas são as regras de repetição que definimos quando o final entrou.

- **Uma vez, na primeira conclusão.** Toca sozinho no momento em que a fase 8 do ato 30 é vencida pela primeira vez.
- **Nunca mais sozinho.** Vencer a mesma fase de novo, ou reiniciar o app, não o toca automaticamente.
- **Pode ser pulado a qualquer momento.** Um toque vai para o último quadro parado, e um aparelho com reduzir movimento ativado começa no quadro parado.
- **A repetição é o farol.** Há um farol no topo do ato 30, e tocá-lo reproduz o mesmo final outra vez.

Mesmo quando um final dura menos de 30 segundos, decidimos que "uma vez, logo depois da vitória" é um presente e "toda vez que você vence" é uma interrupção.

## Onde "já visto" é registrado

Se ele já tocou fica guardado como uma chave de história nos dados de save. A chave do final da temporada é **deliberadamente separada** da chave do final do ato 10. Se ambos usassem uma só chave, um jogador que tivesse visto o final do ato 10 poderia ter o final da temporada contado como já visto. Um teste verifica isso: assistir ao final do ato 10 deixa a chave da temporada intacta.

## Quem já concluiu

Alguém pode ter concluído a fase 8 do ato 30 antes de o final existir. Para esse save o momento da primeira conclusão já passou, então nada toca sozinho e só o farol aparece. Escolhemos não forçar um momento que já se foi, e deixar o jogador apertá-lo quando quiser.

Na mesma mudança, o farol do ato 10 foi movido para o topo do ato 10, onde ele deve ficar.

## O que os testes fixam

O final tem 18 testes. Os ligados a estas regras:

- Toca exatamente uma vez na primeira vitória da fase 8 do ato 30, e não quando o jogador entra de novo.
- Nada toca na fase 7 do ato 30 nem na fase 8 do ato 29.
- Um save que já concluiu a fase 8 do ato 30 não recebe reprodução automática, só o farol.
- Em 375px e 320px, em testes de widget, reproduzir, pular e sair no meio funcionam.
- O texto de todos os 12 idiomas cabe sem estourar.

## Sem palavra de encerramento

A última linha, em coreano, é "A água profunda reflete." (「깊은 물이 비친다.」). Nenhuma versão de idioma traz uma palavra como "Fim", e a marca na parte de baixo é "Inkisle · Season 1". As regras de repetição vêm do mesmo pensamento: a história se fecha, mas o app não. Depois do ato 30, os jogadores ainda podem rejogar atos, juntar três estrelas e olhar os placares.

## O que não verificamos

- **O texto do final nos 10 idiomas além do coreano e do inglês é traduzido por máquina e não foi revisado [não verificado].** Com apenas algumas linhas na tela, a qualidade de uma tradução aparece de imediato.
- O desvanecimento lento, as letras douradas e o volume do sino não foram vistos em um aparelho real [não verificado].
- As telas de 375px e 320px foram verificadas apenas em testes de widget, cuja fonte de teste é muito mais larga que a real [não verificado].
- Se haverá uma temporada 2 está indefinido, e nenhuma data de lançamento foi marcada.

## FAQ

### Quantas vezes o final toca sozinho?

Uma vez, na primeira vez que a fase 8 do ato 30 é concluída. Depois disso, o jogador toca o farol no topo do ato 30 para vê-lo de novo.

### É possível pular o final?

Sim. Um toque salta para o último quadro parado, e com reduzir movimento ativado ele começa no quadro parado.

### O texto do final está revisado em todos os idiomas?

Não. As traduções além do coreano e do inglês são feitas por máquina e ainda não foram revisadas.
