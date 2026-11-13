---
title: Dos objetos de tinta a la vez: ranuras, pausas y lo que nos dijeron los bots
description: En los primeros mares solo podías usar un objeto de tinta a la vez. Desde el mar 5 puedes usar dos, y más adelante tres, con una pausa entre cada inicio. La tabla de reglas, cómo lo muestra el botón y una simulación que encontró un efecto mucho menor del que esperábamos.
slug: two-inks-at-once
lang: es
translation_of: en
category: making-of
keywords: Inkisle, objetos de tinta, diseño de juegos, equilibrio del juego, simulación con bots, interfaz móvil, accesibilidad
image_alt: Dos pequeñas gotas de tinta, una junto a la otra, sobre una fila de islas, dibujadas en suaves colores vectoriales.
published: 2026-11-13T22:44+09:00
---
Los objetos de tinta (oleada, ancla, niebla, linterna, vuelta de marea) se usaban de uno en uno. Es fácil de entender, pero también significa que una fase avanzada nunca da la sensación de tener más herramientas. Por eso dimos al botón de tinta **ranuras**.

## La regla

| Mar | Ranuras a la vez | Pausa entre inicios |
|---|---|---|
| 1 a 4 | 1 | ninguna (como antes) |
| 5 a 10 | 2 | 10 segundos |
| Volumen 2, mares 11 a 20 | 2 | 5 segundos |
| Volumen 3, desde el mar 21 | 3 | 5 segundos |

Lo que no cambia: un jefe suma 5 segundos a la pausa; el límite de usos por fase (5 o 6) se comparte entre todas las ranuras; no se pueden usar dos de la misma clase; la ranura de un ancla o de niebla se libera cuando se captura su isla; y los primeros 20 segundos de una fase siguen bloqueando toda la tinta.

## Cómo lo muestra el botón

El botón de tinta tiene un punto por ranura, que se rellena mientras la ranura está en uso. Un anillo fino dentro del botón cuenta la pausa antes de que puedas iniciar el siguiente. En la hoja del puerto, una tarjeta bloqueada dice "próxima tinta en N segundos" durante la pausa, o "extendiéndose" cuando las ranuras están llenas. La etiqueta de accesibilidad dice algo como "1 de 2 ranuras". Todo esto está en 12 idiomas.

## Por qué el motor no necesitó un hash nuevo

El estado del juego ya guarda una lista de horas de fin de la tinta en uso y el número de usos, así que los mares 1 a 4 se comportan y generan el hash exactamente como antes. Las pruebas cubren cada fila de la tabla, el comportamiento del primer mar, el rechazo de la misma clase, las ranuras llenas, tres ranuras, el límite compartido y la liberación al capturar, además del botón a 320 y 375 px.

## Lo que dijeron los bots

Simulamos 80 fases del mar 5 al 14, con cinco bots y 24 semillas cada uno, para cuatro planes de dos o tres objetos que empiezan a los 20 segundos, y comparamos el mejor plan con la regla antigua (una ranura, sin pausa) con la regla nueva.

- La ganancia media fue de **+1,1 puntos porcentuales** (+0,9 en los mares 5 a 10, +1,5 en los mares 11 a 14). Esperábamos entre 3 y 8.
- En los jefes fue de +0,9. La mejor tasa de victorias con tinta frente a no usarla fue de +36 puntos, dentro de nuestro límite de 40.
- Fase por fase, el cambio osciló entre −7 y +10, que es más o menos el ruido de 24 semillas.

Los bots rara vez aprovechan bien la segunda ranura, así que la cifra pequeña puede decir más de los bots que de la regla. **[sin verificar]** Una persona podría ganar más.

## Lo que no hemos comprobado

- Si una persona entiende con claridad las dos ranuras y la pausa, o si le parece un bloqueo. No lo hemos probado en un teléfono real. **[sin verificar]**
- Todavía no hemos creado un aviso de una línea para la primera vez que un jugador llega a un mar de dos ranuras (5-1).
- El juego está en desarrollo y no se ha publicado.
