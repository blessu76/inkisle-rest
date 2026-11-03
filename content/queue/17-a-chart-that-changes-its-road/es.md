---
title: Una carta marina que cambia de camino: un estilo de línea por mar
description: Con 14 mares en una sola carta con scroll, el camino entre fases se veía igual en todas partes. Dimos a cada mar su propio estilo de línea, color y ondulación, hicimos que el ángulo continúe en las fronteras entre mares y solo dibujamos lo que está en pantalla. Los valores, las pruebas y lo que aún no hemos visto en un teléfono.
slug: a-chart-that-changes-its-road
lang: es
translation_of: en
category: making-of
keywords: Inkisle, carta marina, mapa de niveles, estilo de ruta, interfaz móvil, Flutter, rendimiento de renderizado
image_alt: Un camino sinuoso de puntos entre islas que cambia de una línea de cuerda a una línea de ola, dibujado en colores vectoriales suaves.
---
La carta es la pantalla donde pasas el tiempo tranquilo entre batallas: un largo camino de fases. Con 14 mares, el camino se veía igual de principio a fin. Un scroll largo sin cambios parece un solo mar repetido. Así que cada mar tiene ahora su propio camino.

## Qué cambia en cada mar

| Mar | Línea | Color de un camino completado |
|---|---|---|
| 1 | continua (como antes) | coral |
| 2 | cuerda | beige de vela |
| 3 | guiones largos, tenue | blanco de faro |
| 4 | ola | verde azulado |
| 5 | cuentas | rosa coral |
| 6 | guiones largos | oro arena |
| 7 | continua gruesa | azul marino |
| 8 | continua fina | cobalto |
| 9 | cuentas | oro de farol |
| 10 | continua gruesa | oro |
| 11 | pincel | tinta |
| 12 | línea doble | plata |
| 13 | ola | vela blanca |
| 14 | cuentas | tinta profunda |

Cada mar tiene además su propio vaivén (cuánto se desvía el camino hacia los lados y con qué frecuencia). Siete tipos de línea se comparten entre los 14 mares, y los colores son todos distintos. El camino que lleva a una fase se dibuja con el estilo del mar al que pertenece esa fase. Después del mar 14 los estilos se repiten, de forma provisional.

## Dos cosas que no eran de aspecto

- **Sin saltos en las fronteras entre mares.** El vaivén es una única función continua, así que el ángulo continúa donde termina un mar y empieza el siguiente, y las islas no saltan hacia un lado.
- **Dibujar solo lo visible.** La carta tendrá cientos de fases, por lo que se omiten las islas y los caminos fuera del área visible. En una prueba de widget, dibujar diez caminos visibles tardó menos de 16 ms.

## Las decoraciones vinieron después

Un segundo paso añadió pequeñas marcas a lo largo del camino en cada mar: nudos, corchetes, huellas, estrellas, gotas de tinta. Después, en los mares 7, 10 y 11 las cambiamos por un remolino, un faro y una dispersión, y la gota del mar 14 por una puntiaguda.

## Pruebas

Siete pruebas comprueban que todos los mares tienen un estilo, que el vaivén se mantiene por debajo de .32, que los 14 colores son todos distintos, que se usa cada tipo de línea, que un camino completado tiene un contraste de al menos 3:1 con su borde, que las islas permanecen dentro del 18% al 82% del ancho a 320 px, y que cada mar dibuja píxeles diferentes. El diseño del primer mar no se mueve.

## Lo que no hemos comprobado

- Todos los renders hasta ahora son capturas de prueba, donde la fuente es un bloque. No lo hemos visto en un iPhone ni en un teléfono Android reales. **[sin verificar]**
- No medimos el tiempo de fotograma con las 800 fases, solo la comprobación de diez caminos. **[sin verificar]**
- En los mares nocturnos oscuros (11 y 14), el camino color tinta se sostiene con un borde blanco. Si se ve bien es una revisión de diseño que aún nos debemos.
- El juego está en desarrollo y no ha sido lanzado.
