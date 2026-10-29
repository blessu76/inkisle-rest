---
title: Tres estrellas, una regla: cómo se puntúa una fase
description: Cada fase de Inkisle puede ganar hasta tres estrellas. Qué significa cada estrella, por qué las estrellas nunca bloquean el avance ni bajan, los 13 tipos de objetivos de tres estrellas y la etiqueta equivocada que encontramos y corregimos.
slug: three-stars-one-rule
lang: es
translation_of: en
category: making-of
keywords: Inkisle, puntuación por estrellas, progresión del juego, diseño de juegos, juego móvil, rejugabilidad
image_alt: Una fila de tres estrellas, las dos primeras rellenas de color coral y la tercera solo un contorno.
---
Cada una de las 16 fases de Inkisle da de una a tres estrellas. Las estrellas son la forma que tiene el juego de decir "puedes hacerlo mejor" sin obligarte. Esta es la regla, y un error que cometimos al explicarla.

## Qué significa cada estrella

1. **★1: ganar.** Superas la fase.
2. **★2: ganar dentro del límite de tiempo de la fase.** Cada fase tiene su propio límite.
3. **★3: el objetivo propio de la fase.** Un objetivo distinto para cada fase, que se muestra en su tarjeta.

El juego decide estas tres condiciones en un solo lugar, y las pantallas solo le piden el resultado. Suena obvio, pero cuando escribimos por primera vez el gráfico y la hoja de resultados, trozos de la regla se habían filtrado en ambos. Una revisión lo encontró y movimos las comprobaciones a pequeñas funciones auxiliares junto a la regla, así que si la regla cambia, hay un único sitio que modificar.

## Las estrellas nunca estorban

- **Las estrellas no desbloquean nada.** Ganar una fase abre la siguiente. Vencer al jefe abre el siguiente mar.
- **Las estrellas nunca bajan.** Si rejuegas una fase y pierdes, no se registra nada. Si rejuegas y ganas, el juego conserva lo mejor de todo: una estrella ganada se queda, y se guarda el mejor tiempo.

Así que rejugar solo puede ayudarte.

## Trece tipos de objetivos de tres estrellas

El objetivo de ★3 es distinto en casi todas las fases. Hasta ahora hay 13 tipos, por ejemplo:

- perder como máximo un número de tropas,
- ganar sin enviar nunca el 100%,
- tomar todas las islas vacías,
- no perder ni una sola isla,
- capturar una fortaleza en un solo ataque,
- resistir una vez un ataque enemigo simultáneo,
- no atacar la isla base del enemigo antes de un tiempo dado.

Cada objetivo está escrito con palabras sencillas en la app, por ejemplo "Gana sin enviar el 100%".

## La etiqueta equivocada

La etiqueta de ★1 decía al principio "**gana conservando tus islas**". Pero la condición era solo "ganar": podías perder islas y aun así obtener la estrella. La etiqueta prometía algo que el juego no comprobaba. Una revisión lo detectó, y ahora la etiqueta es simplemente "**ganar**".

## Lo que no hemos comprobado

- Los límites de tiempo de ★2 los fijó el prototipo y, como mostró la prueba con bots de una entrada anterior, parecen **demasiado generosos** para los bots. Todavía no sabemos cómo serán los tiempos humanos.
- No sabemos si los jugadores sentirán que 13 objetivos distintos son interesantes o solo confusos.
