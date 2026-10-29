---
title: O que o app não tem: sem anúncios, sem contas, sem rastreamento
description: Parte do design do Inkisle está no que foi deixado de fora. O app não pede conta e não tem anúncios nem ferramentas de rastreamento, roda em iOS e Android a partir de uma única base de código, e desenhamos um ícone novo para os dois. O que decidimos e o que ainda não verificamos.
slug: what-the-app-does-not-have
lang: pt
translation_of: en
category: making-of
keywords: Inkisle, privacidade, sem anúncios, sem conta, ícone do app, iOS, Android, Flutter, jogo para celular
image_alt: Uma ilha cor de coral desenhada como uma simples mancha de tinta sobre fundo creme, o ícone do app Inkisle.
---
Muito do que faz um app ser agradável é o que ele **não** faz. Para o primeiro lançamento do Inkisle, definimos uma lista curta de coisas a deixar de fora.

## Sem conta, sem anúncios, sem rastreamento

- **Sem conta.** Você abre o app e joga. Não há cadastro nem login.
- **Sem anúncios e sem ferramentas de rastreamento.** A lista de pacotes externos do app é curta: um para guardar pequenas configurações no celular, um para tocar sons e um para abrir uma página da web. Não há nela nenhum pacote de publicidade, nenhum pacote de análise e nenhum pacote de login.
- **O progresso fica no celular.** As estrelas salvas e a configuração de som são guardadas localmente e não são enviadas a lugar nenhum.

O app tem uma tela de informações com um link para a política de privacidade, que é a mesma página que está neste site. A única coisa que toca a rede é abrir essa página, e isso só acontece quando o jogador toca nela. A política foi escrita primeiro para este site, então ainda precisa ser revisada e atualizada para cobrir o app antes de qualquer envio a uma loja.

## Uma base de código, duas plataformas

O Inkisle é feito com Flutter, então **iOS e Android são desenvolvidos juntos** a partir do mesmo código, e toda mudança é testada nos dois. O plano é **lançar primeiro no iOS**. Mesmo assim, compilamos e testamos o Android o tempo todo, para que ele não vire um segundo projeto mais tarde. O jogo fica travado na orientação vertical nos dois. As versões mínimas são iOS 13 e Android API nível 24.

## O ícone

O ícone é uma simples **ilha de tinta cor de coral** sobre fundo creme. Um único código de desenho gera três arquivos:

- o ícone quadrado normal para iOS e para Android mais antigo,
- o primeiro plano "adaptativo" do Android, desenhado dentro da área segura de 66% em que o Android recorta,
- uma silhueta de uma só cor para os ícones temáticos do Android 13.

Lançamos um bug aqui e o corrigimos: o ícone adaptativo estava sendo reduzido duas vezes (uma por nós e outra pelas configurações de build), então ficava pequeno demais no Android. Agora a redução acontece em um único lugar.

## O que não verificamos

- Não executamos o app em um **iPhone ou celular Android de verdade** a partir de um build de loja, e não o enviamos a nenhuma das duas lojas. Coisas como a revisão das lojas, as telas do app em outros idiomas e a aparência do ícone em diferentes launchers ainda estão em aberto.
- "Sem rastreamento" descreve o que há no nosso próprio código e na nossa lista de pacotes. Não auditamos os pacotes de que dependemos além de ler as suas descrições.
