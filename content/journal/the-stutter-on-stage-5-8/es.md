---
title: El tirón en el nivel 5-8: era la pantalla, no el motor del juego
description: El nivel 5-8 de Inkisle iba a trompicones. Medimos antes de tocar nada, vimos que el coste estaba en dibujar la pantalla y no en las reglas del juego, y bajamos el coste de un fotograma de 3,4 a 1,3 ms en un ordenador. Qué cambiamos, qué dejamos y qué no hemos comprobado en un móvil.
slug: the-stutter-on-stage-5-8
lang: es
translation_of: en
category: making-of
keywords: Inkisle, rendimiento, tirones, tiempo de fotograma, diseño de juegos, juego móvil, optimización
image_alt: Cuatro barras moradas altas a la izquierda y cuatro barras coral bajas a la derecha, con una flecha en medio y una línea discontinua que marca el presupuesto.
published: 2026-11-25T15:15+09:00
---

Inkisle, nuestro juego de estrategia de conquista de islas para iOS, iba a trompicones en el nivel 5-8 durante las pruebas. La suposición fácil era que el motor del juego, la parte que mueve las flotas y decide las capturas, se había vuelto demasiado pesado. Primero medimos. El problema no era el motor, sino la pantalla que lo rodea. Tras el cambio, el coste de un fotograma en el nivel 5-8 bajó de 3,4 ms a 1,3 ms en nuestro ordenador. El juego está en desarrollo y no se ha lanzado, y estas cifras no vienen de un móvil.

## Qué medimos

Un fotograma tiene dos tipos de trabajo: avanzar un tick las reglas del juego y construir y dibujar la pantalla. En el nivel 5-8, un tick de las reglas costaba de media solo de 3 a 5 microsegundos. La pantalla costaba unas mil veces más.

La mayor parte de ese coste de pantalla venía de tres cosas:

1. **Todo el HUD se reconstruía en cada fotograma.** El controlador del juego anunciaba un cambio en cada fotograma, así que las barras de poder, el texto del objetivo, la hoja de resultados, la barra de proporción, las insignias, la barra de selección, la capa de crisis y el botón de marea se reconstruían aunque nada hubiera cambiado. Unos 2,5 ms de los 3,4 ms se iban en construir widgets.
2. **Las etiquetas numéricas fallaban la caché.** La clave de la caché incluía la transparencia y el tamaño exactos de cada número, y estos cambian de forma continua durante la expansión de una captura o un desvanecimiento. Así, cada fotograma generaba maquetaciones nuevas, y cuando la caché pasaba de 600 entradas se vaciaba entera, de modo que un fotograma tenía que maquetar todo de nuevo. El tiempo de dibujo en el 1 % de fotogramas más lentos era de 5 a 10 veces la media.
3. **Pequeño trabajo repetido.** Cada flota buscaba dos veces su color de tinta, la posición y el radio de cada isla se recalculaban para cada flota, y una caché de shaders usaba una clave de texto.

## Qué cambiamos

- El HUD ahora escucha una pequeña señal que se dispara solo cuando cambia algo de lo que muestra, como el tick, la pausa, la velocidad, el estado de crisis, los objetivos o las pistas. El pintado sigue haciéndose en cada fotograma, como antes.
- Las etiquetas numéricas se redondean a pasos gruesos (transparencia en 32 pasos, tamaño en cuartos de píxel) para que la caché acierte, y cuando se llena solo se elimina la mitad más antigua.
- Las búsquedas repetidas se calculan una vez por fotograma, y la clave del shader pasó de ser una cadena a un registro.

El redondeo del tamaño y de la transparencia no se ve a simple vista.

## Las cifras

Se midieron en un ordenador, con una pantalla de 375 × 667, en un modo que solo sirve para comparar el antes y el después.

| | antes | después |
|---|---|---|
| Nivel 5-8, fotograma completo, media | 3.433 µs | 1.267 µs |
| Nivel 5-8, fotograma completo, 1 % más lento | 10.803 µs | 5.182 µs |
| Nivel 5-8, dibujo, media | 818 µs | 201 µs |
| Nivel 5-8, dibujo, 1 % más lento | 4.540 µs | 1.284 µs |

Un juego a 60 fotogramas por segundo tiene unos 16,6 ms por fotograma, así que incluso antes del cambio el trabajo cabía en ese presupuesto en un ordenador. Por eso los tirones que notamos pueden tener también otra causa (véase abajo).

## Qué dejamos como estaba

No cambiamos ni una línea de las reglas ni del código de equilibrio. Solo cambió la capa de pantalla: cómo el controlador anuncia las actualizaciones, qué widgets escuchan y las cachés de dibujo. La misma semilla sigue produciendo el mismo resultado de 600 ticks, y las comprobaciones existentes de imágenes de referencia, juego determinista y simulaciones de bots siguieron en verde.

También dejamos para después un coste real. La previsión de crisis se ejecuta en el hilo de la pantalla: en el nivel más pesado que medimos, el 17-3, tardó de media 3,4 ms y su 1 % más lento llegó a 11,8 ms, lo que puede causar un pequeño tirón cada medio segundo. Repartir ese trabajo entre varios fotogramas daría el mismo resultado, pero arriesga cambiar decisiones, así que no lo hicimos ahora. En el nivel 5-8 cuesta 0,17 ms y no importa.

## Qué añadimos

Un benchmark del motor sin pantalla y una prueba de rendimiento con límites superiores holgados. Detecta el tipo de regresión en que el coste se dispara con el número de flotas o en que cada fotograma reserva demasiada memoria. Mantuvimos los límites holgados a propósito, porque unos estrictos fallarían siempre que la máquina de pruebas esté ocupada. Por defecto, las más pesadas de estas pruebas se omiten y solo se ejecutan cuando se piden.

## Qué no hemos comprobado

- **La tasa de fotogramas en un móvil real, a 60 o 120 fotogramas por segundo, no está comprobada.** Nuestras cifras son coste del hilo de pantalla en un ordenador, no coste gráfico en un dispositivo.
- **El velo de niebla y las capas de banda ni se han medido ni se han cambiado.** Se dibujan con un desenfoque a pantalla completa, que cuesta al chip gráfico y no al procesador. Si el nivel 5-8 sigue dando tirones en un móvil, es nuestro primer sospechoso.
- No miramos el renderizado en el navegador a 320, 375, 768 y 1280 px, porque no cambió ningún diseño.
- Que la entrada se sienta más ágil es solo una expectativa nuestra.

## FAQ

### ¿Por qué iba a trompicones el nivel 5-8 de Inkisle?

Nuestra medición apuntaba a que la pantalla se reconstruía y las etiquetas numéricas se volvían a maquetar en cada fotograma, no a las reglas del juego. Lo arreglamos; la tasa de fotogramas en un móvil real aún no está comprobada.

### ¿La optimización cambió cómo se juega?

No. No tocamos las reglas ni el código de equilibrio, y la misma semilla da el mismo resultado que antes.

### ¿Sigue dando tirones en un móvil?

Todavía no lo sabemos. Nuestras cifras vienen de un ordenador. Lo comprobaremos en un dispositivo real en TestFlight.
