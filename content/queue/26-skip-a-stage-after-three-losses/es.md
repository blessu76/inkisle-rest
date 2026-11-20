---
title: Saltar un nivel tras tres derrotas: una oferta amable con un costo
description: En Inkisle, perder tres veces el mismo nivel ofrece saltarlo por 3 Ink. Cuándo se ofrece, qué niveles quedan fuera, cómo se ve un nivel saltado en la carta y cómo se guarda.
slug: skip-a-stage-after-three-losses
lang: es
translation_of: en
category: making-of
keywords: Inkisle, saltar nivel, dificultad, diseño de juegos, datos guardados, juego móvil
image_alt: Una carta náutica con una isla marcada por una pequeña bandera de coral y un camino punteado que pasa de largo hacia la siguiente isla.
---

En Inkisle, nuestro juego de estrategia de conquista de islas para iOS, perder tres veces el mismo nivel hace aparecer una pregunta: «¿Saltar este nivel e intentarlo más tarde?». Saltar cuesta 3 Ink. El nivel saltado recibe una bandera en la carta y se puede jugar cuando se quiera. El juego sigue en desarrollo y no ha sido lanzado, y todavía no hemos visto este aviso en un dispositivo real.

## Por qué ofrecer un salto

Algunos niveles siguen siendo difíciles incluso después del ajuste de dificultad. No queríamos que un jugador se quedara parado en una isla. La oferta le permite avanzar y volver, en lugar de abandonar el juego.

## Cuándo se ofrece

- El aviso aparece tras la **tercera derrota** del mismo nivel, cuando la hoja de resultados se ha asentado (1,1 segundos).
- Si el jugador dice que no, no vuelve a preguntar en la 4.ª y la 5.ª derrota. Pregunta otra vez en la **6.ª, la 9.ª** y así sucesivamente. Preguntar siempre sería insistir; preguntar solo una vez dejaría de lado a quien sigue atascado.
- Las derrotas se cuentan por nivel. Ganar el nivel pone la cuenta a 0. Las derrotas en un nivel ya superado o saltado no cuentan.

## Cuánto cuesta

Saltar cuesta **3 Ink**, el mismo Ink que el jugador ya gana en el juego o compra. No se añadió ninguna moneda ni producto nuevo. El valor es una sola constante en el código, y el texto del aviso, el botón y el enlace a la tienda la siguen.

Primero lo fijamos en 1 Ink y lo subimos a 3 cuando el propietario pidió entre 2 y 3. Si el jugador tiene menos de 3 Ink, el botón de saltar pasa a ser «Sin Ink, abrir la tienda» y abre la hoja de tienda existente. Con 3 o más, vuelve el botón de saltar.

## Qué niveles quedan fuera

- Los niveles 1-1 a 1-4, el tramo de tutorial sin Ink. Saltarlos significaría no aprender nunca los controles.
- El nivel 1-5, donde el juego regala su primer Ink.
- El último nivel, porque no hay un siguiente nivel que abrir.
- Los niveles de jefe sí están incluidos.

## Qué significa un nivel saltado

- Se abre el siguiente nivel, y el nivel saltado tiene **0 estrellas**. Saltar no es superar, así que las estrellas no se pueden comprar.
- En la carta, el nodo recibe una bandera de coral. Los lectores de pantalla añaden «saltado». La ficha del nivel dice: «Este nivel se saltó. Vuelve a intentarlo cuando quieras.»
- Si se supera más tarde, la bandera desaparece y las estrellas se registran con normalidad.
- Un mar solo se completa cuando sus niveles están superados, así que un nivel con bandera aún hay que ganarlo para completar el mar.
- El final solo se abre con una victoria real, así que saltar el nivel 10-8 no lo abre.

## Cómo se guarda

El registro de progreso existente recibe dos claves opcionales: el número de derrotas por nivel y la lista de niveles saltados. Si ambas están vacías, las claves no se escriben, de modo que un guardado antiguo sigue siendo idéntico byte a byte. Al leer, se descartan los id desconocidos y los valores negativos o de texto, y un nivel ya superado pierde su marca de salto, porque la victoria prevalece.

En la fusión con iCloud se conserva el mayor número de derrotas, las listas de saltados se unen y una victoria en otro dispositivo prevalece. Fusionar de nuevo la misma instantánea no cambia nada, y una prueba lo comprueba.

## Lo que no hemos comprobado

- El aviso y la bandera en un dispositivo real o simulador. Las pruebas de widgets con anchos de 375 y 320 px no encontraron desbordamiento en 16 columnas de idioma, pero no hemos mirado capturas de pantalla.
- Si una versión antigua de la app que sobrescriba la instantánea de iCloud pierde las dos claves nuevas. Si ocurre, los niveles superados y las estrellas se conservan y creemos que solo se perderían las marcas de salto.
- Las traducciones distintas del coreano y el inglés no han sido revisadas por hablantes nativos.

## FAQ

### ¿Cuándo ofrece Inkisle saltar un nivel?

Tras perder tres veces el mismo nivel, y de nuevo tras la 6.ª, la 9.ª derrota y así sucesivamente si sigues intentándolo. Los primeros niveles, el nivel del regalo 1-5 y el último nivel quedan fuera.

### ¿Cuánto cuesta saltar y se obtienen estrellas?

Cuesta 3 Ink. Un nivel saltado da 0 estrellas. Si lo superas más tarde, las obtienes como de costumbre.

### ¿Saltar completa un mar o abre el final?

No. Un mar se considera completo solo cuando sus niveles están superados, y el final solo se abre con una victoria real.
