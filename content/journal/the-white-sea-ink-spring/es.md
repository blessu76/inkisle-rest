---
title: El manantial de tinta del mar blanco: cuando una regla de tres estrellas no se puede conseguir
description: El mar 14 tiene un manantial que extiende tinta a las islas cercanas. Los bots no lograron el objetivo de tres estrellas "haz que el manantial se extienda a N islas", así que medimos, probamos a mover islas y sustituimos la regla por un conteo de pulsos del manantial. Lo que probamos y lo que aún no hemos comprobado.
slug: the-white-sea-ink-spring
lang: es
translation_of: en
category: making-of
keywords: Inkisle, diseño de niveles, regla de tres estrellas, manantial de tinta, simulación con bots, equilibrio del juego, mar 14
image_alt: Un mar pálido con una pequeña isla manantial en el centro y unas pocas islas alrededor, dibujado en suaves colores vectoriales.
published: 2026-11-10T19:00+09:00
---
El mar 14, el mar blanco, añade una regla: un **manantial de tinta**. Si mantienes la isla del manantial, cada 150 ticks pulsa y extiende tinta a una isla cercana. El primer pulso llega 150 ticks después de capturarlo. El objetivo de tres estrellas que escribimos al principio era "haz que el manantial se extienda a N islas". Ese objetivo resultó ser una promesa que nadie podía cumplir.

## La medición

El objetivo se usaba en siete fases. En seis de ellas escribimos un guion con la mejor jugada que se nos ocurrió: capturar el manantial en el tick 0 y luego dejarlo en paz durante 900 ticks, con cuatro semillas cada una. (14-8 no se puede programar así, porque el enemigo tiene el manantial desde el principio.)

| Fase | Extensiones necesarias | Extensiones obtenidas |
|---|---|---|
| 14-1 | 2 | 0 |
| 14-2 | 2 | 0 |
| 14-3 | 3 | 0 |
| 14-5 | 2 | 0 |
| 14-6 | 2 | 0 |
| 14-7 | 3 | 0 |

El enemigo toma las islas pequeñas junto al manantial entre el tick 70 y el tick 250. El primer pulso llega en el tick 150 o más tarde, así que muchas veces ya no queda nada adonde extenderse.

## Tres cosas que probamos

1. **Mover las islas.** Una búsqueda sobre las islas pequeñas junto al manantial encontró disposiciones que alcanzan el número necesario en 14-1 y 14-5, pero solo poniendo cuatro o cinco islas pequeñas junto al manantial. Eso rompe nuestro propio tope de tres, y 14-5 deja de cumplir el mínimo de que "el bot más simple tiene que ganar al menos unas cuantas veces". Dentro del tope, ninguna disposición dio más de una extensión.
2. **Adelantar el primer pulso.** Con el primer pulso a los 60 ticks, 14-1 se vuelve posible y las otras cinco fases se quedan en 0 o 1. También hizo que 14-8 cayera por debajo de nuestro mínimo para el bot más simple. No lo conservamos.
3. **Cambiar la regla.** El objetivo debería premiar lo que el jugador controla: mantener el manantial. Así que el objetivo de tres estrellas pasó a ser el **número de pulsos de tu propio manantial**. Los números, elegidos en o por debajo de lo que los bots alcanzaron realmente en partidas ganadas: 14-1: 4, 14-2: 3, 14-3: 2, 14-5: 3, 14-6: 1, 14-7: 3, 14-8: 1. La fase 14-4 conserva su objetivo propio.

Elegimos la tercera. Solo afecta al mar 14, así que los hashes y los archivos golden de los mares 1 a 13 no cambiaron.

## Un último repaso al mar

De paso, ensanchamos el centro de 14-1 (una isla central pasó de 4 a 12) y suavizamos 14-6, donde un bot ganaba bastante más que los demás. Ahora hay una prueba nueva que dice que ningún bot puede llevarse más de la mitad de las victorias en 14-8; hoy son 8, 17, 12 y 24 victorias para cuatro bots y 0 para el quinto.

## Lo que no hemos comprobado

- En 14-6 y 14-8 el enemigo tiene el manantial, así que un pulso es lo máximo con lo que se puede contar. Los bots rara vez llegaron a él, de modo que los números se apoyan en pocos datos. **[sin verificar]**
- Nadie ha jugado estas fases a mano. Si "haz que el manantial pulse" se entiende bien en la tarjeta de la fase y en la pantalla de resultados, hace falta comprobarlo en un teléfono real. **[sin verificar]**
- El juego está en desarrollo y no se ha lanzado.
