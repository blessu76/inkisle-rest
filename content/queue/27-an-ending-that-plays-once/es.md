---
title: Un final que se reproduce una sola vez, y un faro para volver a verlo
description: El final de la temporada 1 de Inkisle se reproduce solo exactamente una vez, la primera vez que se supera la última fase del acto 30. Cómo fijamos las reglas de repetición, cómo se trata a los jugadores que ya lo superaron y el final del acto 10, y qué no hemos comprobado en las traducciones ni en un dispositivo real.
slug: an-ending-that-plays-once
lang: es
translation_of: en
category: making-of
keywords: Inkisle, temporada 1, final, final abierto, faro, diseño de juegos, juego móvil
image_alt: Una isla solitaria en un mar en calma con un faro encendido, y la ruta de la carta náutica que se detiene frente a él.
---

El final de la temporada 1 de Inkisle, nuestro juego de estrategia de conquista de islas para iOS, se reproduce solo una vez, la primera vez que se supera la fase 8 del acto 30. Para verlo otra vez, el jugador toca el faro en la parte superior del acto 30. El final no tiene palabra de cierre; la única marca es «Inkisle · Season 1». Esta entrada trata menos de lo que muestra el final y más de cuándo se reproduce y cuándo no, y de cómo fijamos esas reglas. El juego está en desarrollo y no se ha lanzado.

## Cuatro reglas

Estas son las reglas de repetición que fijamos cuando se incorporó el final.

- **Una vez, en la primera superación.** Se reproduce solo en el momento en que se gana por primera vez la fase 8 del acto 30.
- **Nunca más por sí solo.** Volver a ganar la misma fase o reiniciar la app no lo reproduce automáticamente.
- **Se puede saltar en cualquier momento.** Un toque lleva al último fotograma fijo, y un dispositivo con reducir movimiento activado empieza en el fotograma fijo.
- **Repetir es el faro.** Hay un faro en la parte superior del acto 30, y al tocarlo se reproduce de nuevo el mismo final.

Incluso cuando un final dura menos de 30 segundos, decidimos que «una vez, justo después de ganar» es un regalo y «cada vez que ganas» es una interrupción.

## Dónde se guarda «ya visto»

Si se ha reproducido o no se guarda como una clave de historia en los datos de la partida. La clave del final de temporada está **deliberadamente separada** de la clave del final del acto 10. Si ambos usaran una sola clave, a un jugador que hubiera visto el final del acto 10 se le podría contar el final de temporada como ya visto. Una prueba lo comprueba: ver el final del acto 10 deja intacta la clave de temporada.

## Jugadores que ya lo superaron

Alguien puede haber superado la fase 8 del acto 30 antes de que existiera el final. Para esa partida el momento de la primera superación ya pasó, así que no se reproduce nada solo y únicamente aparece el faro. Decidimos no forzar un momento que ya no existe y dejar que el jugador lo pulse cuando quiera.

En el mismo cambio, el faro del acto 10 se movió a la parte superior del acto 10, que es donde le corresponde.

## Qué fijan las pruebas

El final tiene 18 pruebas. Las ligadas a estas reglas:

- Se reproduce exactamente una vez en la primera victoria de la fase 8 del acto 30, y no cuando el jugador vuelve a entrar.
- No se reproduce nada en la fase 7 del acto 30 ni en la fase 8 del acto 29.
- Una partida que ya superó la fase 8 del acto 30 no recibe reproducción automática, solo el faro.
- A 375px y 320px, en pruebas de widgets, funcionan reproducir, saltar y salir a mitad.
- El texto de los 12 idiomas cabe sin desbordarse.

## Sin palabra de cierre

La última línea, en coreano, es «lo profundo del agua se refleja.» (「깊은 물이 비친다.」). Ninguna versión de idioma lleva una palabra como «Fin», y la marca inferior es «Inkisle · Season 1». Las reglas de repetición nacen de la misma idea: la historia se cierra, pero la app no. Después del acto 30 los jugadores aún pueden repetir actos, reunir tres estrellas y mirar las tablas de puntuación.

## Qué no hemos comprobado

- **El texto del final en los 10 idiomas distintos del coreano y el inglés está traducido automáticamente y no se ha revisado [sin verificar].** Con solo unas pocas líneas en pantalla, la calidad de una traducción se nota enseguida.
- El desvanecimiento lento, las letras doradas y el volumen de la campana no se han visto en un dispositivo real [sin verificar].
- Las vistas de 375px y 320px se comprobaron solo en pruebas de widgets, cuya fuente de prueba es mucho más ancha que la real [sin verificar].
- No está decidido si habrá una temporada 2, y no hay fecha de lanzamiento.

## FAQ

### ¿Cuántas veces se reproduce el final por sí solo?

Una vez, la primera vez que se supera la fase 8 del acto 30. Después, el jugador toca el faro en la parte superior del acto 30 para verlo otra vez.

### ¿Se puede saltar el final?

Sí. Un toque salta al último fotograma fijo, y con reducir movimiento activado empieza en el fotograma fijo.

### ¿Está revisado el texto del final en todos los idiomas?

No. Las traducciones distintas del coreano y el inglés son automáticas y aún no se han revisado.
