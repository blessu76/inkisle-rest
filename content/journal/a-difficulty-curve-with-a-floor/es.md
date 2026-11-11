---
title: Una curva de dificultad con suelo: ningún nivel que el bot más simple no pueda ganar jamás
description: Con cientos de niveles, unos pocos difíciles no son unos pocos difíciles, son un muro. Reajustamos los 14 mares a una curva con un nivel de descanso en cada mar, pusimos un tope a la fuerza de la IA enemiga y añadimos una prueba que falla si el bot más simple gana 0 de 40. El antes y el después.
slug: a-difficulty-curve-with-a-floor
lang: es
translation_of: en
category: making-of
keywords: Inkisle, curva de dificultad, equilibrio del juego, simulación con bots, diseño de niveles, tasa de victorias, nivel de IA
image_alt: Una hilera sinuosa de islas que sube y baja como una ola, dibujada en suaves colores vectoriales.
published: 2026-11-11T19:00+09:00
---
Un comentario del propietario cambió este trabajo: si solo se pueden ganar 40 de 800 niveles, el juego es demasiado difícil, aunque cada nivel parezca bien por separado. Así que dejamos de ajustar los niveles uno a uno y escribimos una **curva**.

## La curva

- Cada mar tiene ocho niveles con un **papel**: apertura, preparación, un nivel de descanso, subida y jefe. El nivel de descanso debe ser fácil: el bot más simple tiene que ganar al menos el 80 % de las veces.
- La tasa de victorias objetivo también sigue una **onda a lo largo de los volúmenes**: un mar es un poco más difícil que el anterior, y luego vuelve a haber un mar más suave.
- Los mares 1 a 3 ya están en las compilaciones de TestFlight, así que dejamos en paz sus valores fáciles.

## Un tope para el enemigo

Algunos niveles eran difíciles porque la IA enemiga era demasiado lista, no porque el mapa fuera duro. Añadimos un **techo de IA**: el nivel 5 solo para niveles con varios enemigos, el nivel 4 para los mares 11 en adelante, los jefes y el séptimo nivel desde el mar 6, y el nivel 3 en todos los demás. Cualquier IA por encima de su techo se baja al cargar el nivel. Un ejemplo: en 10-8, el almirante pasó del nivel 5 al 3, y la defensa del faro neutral de 10 a 5.

## La medición

Los 14 mares, cinco bots, 40 semillas cada uno. El "bot simple" es el más débil de los cinco y hace las veces de una persona.

| | Antes | Después |
|---|---|---|
| Niveles que el bot simple nunca gana | **9** (3-8, 4-3, 4-6, 5-5, 6-8, 7-6, 10-3, 10-8, 14-2) | **0** |
| Nivel más débil | 0 victorias de 40 | 4 victorias de 40 (8-8), luego 5 de 40 (10-8) |
| Niveles de descanso, bot simple | sin medir | al menos 80 % |

Algunos ejemplos de victorias del bot simple sobre 40: 3-8: 0 → 30. 4-3: 0 → 18. 6-1: 2 → 39. 7-6: 0 → 17.

## Una prueba que mantiene el suelo

`curve_floor_test` falla si el bot simple gana 0 de 40 en cualquier nivel, si un nivel de descanso cae por debajo del 80 % o si el promedio de los cinco bots se aleja demasiado del objetivo de la curva. Los objetivos viven en un solo archivo, así que cambiar la curva es cambiar una tabla.

## Qué se hizo más fácil a propósito, y el coste

Facilitar los niveles hizo que los objetos de **Tinta** valieran más, porque un nivel más fácil de ganar también se beneficia más de una bonificación. Para conservar los niveles que queríamos, aflojamos dos salvaguardas de la Tinta: el tope de la tasa de victorias de un jefe con Tinta pasó del 55 % al 75 % en cinco niveles de jefe, y la ganancia de un uso de Tinta pasó de 25 a 35 puntos porcentuales en cuatro niveles. Son excepciones que dejamos por escrito, y aún falta decidir cuánto debe valer la Tinta. **[sin verificar como política]**

## Lo que no hemos comprobado

- Las tasas de victorias vienen de bots. Unos pocos niveles (4-6, 5-7, 9-5, 10-2, 10-3, 11-6) están unos diez puntos por encima o por debajo del objetivo, y 10-8 tiene un promedio de bots del 62 % frente a un objetivo del 33 %, porque el almirante es muy duro para el bot más simple pero fácil para los demás.
- Nadie ha jugado la nueva curva a mano, así que lo de "40 de 800 es demasiado difícil" solo está resuelto en las cifras de los bots. **[sin verificar]**
- El juego está en desarrollo y no se ha lanzado.
