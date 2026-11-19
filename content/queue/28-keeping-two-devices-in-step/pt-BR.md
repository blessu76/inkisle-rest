---
title: Mantendo dois aparelhos em sintonia: levando a sincronização do iCloud para um kit de app compartilhado
description: O progresso, a tinta e as configurações do Inkisle já eram igualados entre aparelhos pelo iCloud. Em 16 de novembro, movemos essa ponte para um kit de app compartilhado. Como mantivemos os dados salvos intactos, as regras de mesclagem que nunca encolhem, como a marca de compra é tratada e o que ainda não verificamos em aparelhos reais.
slug: keeping-two-devices-in-step
lang: pt-BR
translation_of: en
category: making-of
keywords: Inkisle, iCloud, sincronização entre aparelhos, dados salvos, mesclagem, jogo mobile
image_alt: Duas telas de tamanhos diferentes unidas por um fio fino, com as ilhas dos dois mapas pintadas das mesmas cores.
---

No Inkisle, nosso jogo de estratégia de conquista de ilhas para iOS, o progresso, a tinta e as configurações principais (idioma e apelido) são igualados entre aparelhos com o mesmo Apple ID por meio do armazenamento chave-valor do iCloud do próprio jogador. Essa sincronização já existia. O que fizemos em 16 de novembro não foi criá-la, mas mover para um kit de app compartilhado uma ponte que nós mesmos tínhamos escrito, e a maior preocupação era não perder nenhum valor salvo. Ainda não verificamos uma ida e volta entre um iPhone e um iPad reais [não verificado]. O jogo está em desenvolvimento e não foi lançado.

## O que movemos

A instrução do responsável naquele dia foi que sincronizar os dados do jogo entre aparelhos Apple deveria ser obrigatório e deveria ir para o kit de app compartilhado. Encontramos a permissão chave-valor do iCloud já ativada, e uma ponte em Swift e um invólucro de armazenamento nossos rodando dentro do app. Então:

| Parte | O que mudou |
|---|---|
| Ponte | Apagamos nossa ponte em Swift e o invólucro, e passamos para o armazenamento de plataforma do kit: iCloud no iOS, somente local nos outros |
| Chaves e codificação | Mantivemos como estavam as chaves de armazenamento, a codificação de strings e o identificador de armazenamento |
| Antes de ler | No iOS, acordar a sincronização uma vez logo antes de uma leitura (a sincronização continua se isso falhar) |
| Configurações do projeto | Adicionamos também a capacidade do iCloud ao arquivo do projeto |

## Não perder dados

Como as chaves e os formatos continuaram os mesmos, a build nova lê o que a antiga escreveu, e a antiga lê o que a nova escreve. Fixamos as duas direções com testes: ler um bloco de formato antigo com o código novo, ler um bloco novo com o código antigo e ler um bloco de configurações antigo. Só código foi apagado; os valores salvos não foram tocados.

## A mesclagem nunca encolhe

Quando dois aparelhos têm progresso diferente, mantivemos a mesclagem própria do app. O kit também tem um mesclador, mas não o usamos. A mesclagem do app já só cresce, e manter as mesmas chaves e o mesmo formato era mais seguro deixando-a como estava.

- Estrelas e melhores marcas por fase ficam com o valor maior.
- O progresso fica com o aparelho que foi mais longe, e a tinta e as configurações só se combinam, nunca encolhem.
- Se o valor na nuvem for diferente do que enviamos por último, enviamos de novo, para nos recuperarmos de uma build antiga que sobrescreveu a mesma chave.

## O que aconteceu com a marca de compra

Uma publicação anterior dizia que a liberação não passa para outro aparelho. Este trabalho mudou isso. O bloco de sincronização agora carrega uma marca de que Liberar todos os mares foi comprado, e outro aparelho que a lê também libera. A marca **só cresce.** Um bloco sem ela não a retira; nós a enviamos de novo.

Isso é uma mudança de design seguindo a instrução de "sincronização obrigatória" do responsável, e tem um limite: depois que a marca é sincronizada, um reembolso não a retira em outros aparelhos. Como tratar reembolsos fica como decisão de política. O próprio fluxo de compra também ainda não foi executado em um aparelho real [não verificado].

## Tamanho e testes

O armazenamento chave-valor do iCloud tem um limite total (1 MB). O bloco de sincronização de um save com todas as 240 fases concluídas tem cerca de 6,3 KB, e um teste o mantém abaixo de 16 KB. Os 14 testes novos cobrem chaves e codificação inalteradas, a mesclagem de dois aparelhos, a marca de compra que se espalha e nunca é retirada, o permanecer local offline ou sem login e a mesclagem depois de voltar online. Nos quatro arquivos de testes da nuvem, 77 testes passaram.

## O que não verificamos

- **Uma sincronização real entre um iPhone e um iPad não foi verificada [não verificado].** Isso só pode ser visto em aparelhos reais ou no TestFlight.
- As exclusões não viajam para outros aparelhos, porque esta sincronização só mescla.
- O Android não se aplica. Os dados ficam no aparelho.
- Se uma build antiga em outro aparelho sobrescrever a mesma chave, a marca de compra pode sumir por um instante, e a build nova a envia de novo.
- A política de privacidade agora descreve esta sincronização: os dados do jogo ficam no iCloud do próprio jogador, não em nossos servidores, e podem ser desativados nas configurações do aparelho.

## FAQ

### O progresso do Inkisle fica salvo em um servidor?

Não. Ele é igualado entre aparelhos com o mesmo Apple ID por meio do armazenamento chave-valor do iCloud do próprio jogador, e não é enviado aos nossos servidores.

### A sincronização pode ser desativada?

Sim. Desativar o iCloud deste app nas configurações do iOS interrompe a sincronização e deixa os dados somente no aparelho.

### Sincroniza no Android?

Não. No Android os dados ficam no aparelho.
