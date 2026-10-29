---
title: Las reglas en una página: islas, tropas, conquista
description: Todas las reglas de Inkisle en una página: cómo producen tropas las islas, cómo vuelan las flotas, cómo se calcula la conquista y cómo termina una partida. Valores iniciales, antes de las pruebas.
slug: the-rules-on-one-page
lang: es
translation_of: en
category: making-of
keywords: Inkisle, reglas del juego, conquista de islas, motor determinista, diseño de juegos, reglas de conquista
image_alt: Islas con números de tropas y rutas de puntos por donde viajan las flotas entre ellas.
published: 2026-10-30T05:40+09:00
---
Los buenos juegos de estrategia se explican en un minuto. Este es nuestro intento de explicar las reglas de Inkisle en una página. **Todos los números de aquí son valores iniciales del documento de diseño.** Esperamos cambiar algunos tras las pruebas.

## Las islas producen tropas

Los números de abajo son los de la isla normal. Hay cuatro tipos de isla en total, y los valores iniciales de los otros tres son: la **isla pequeña** produce 1 tropa cada 1,6 segundos con un tope de 25; la **isla grande** produce 1 tropa cada 0,6 segundos con un tope de 80; la **fortaleza** produce 1 tropa cada 2 segundos con un tope de 60 y un multiplicador de defensa de 1,5.

- Cada isla que posees añade **1 tropa por segundo** (un «tick» son 100 ms, es decir, una tropa cada 10 ticks).
- Hay un **tope** de 45. Al llegar al tope, la isla deja de producir, y las tropas sobrantes de los refuerzos bajan de nuevo hasta el tope a razón de 1 por segundo. Así se evita que amontones todo en una isla y esperes.
- **Las islas neutrales no producen.** Su número es fijo, así que se lee como una etiqueta de precio.
- Empiezas con una isla base de 20 tropas. El enemigo suele empezar igual, y si no, lo indica la tarjeta del nivel.

## Enviar flotas

Arrastra desde una de tus islas hasta otra isla y suelta. Una barra en la parte inferior elige la proporción: **25, 50, 75 o 100%**. Envías la parte entera de las tropas por la proporción, como mínimo 1. Con 100% envías «todo menos una», de modo que la isla nunca queda vacía y sigue siendo tuya.

Una flota vuela en línea recta a **2,5 unidades de mapa por segundo**. Una isla vecina a 4 u 8 unidades tarda entre 1,6 y 3,2 segundos, y cruzar todo el mapa lleva unos 11 segundos. Las flotas no combaten en el mar; se cruzan. Eso mantiene honesta la vista previa de llegada y conserva la tensión del género: un viaje largo es un riesgo, porque el objetivo sigue creciendo mientras viajas.

## Conquista, calculada a la llegada

- Si llegas a una isla propia, se suman las tropas.
- Si llegas a una isla enemiga o neutral, necesitas más que **la defensa por el multiplicador**. El multiplicador es 1,0 normalmente y **1,5 para una fortaleza**.
- Si atacas por encima del requisito: conquistas, y la nueva defensa es lo que sobra. Si es igual: el defensor resiste con 0 (los empates favorecen al defensor). Si es menos: el defensor pierde una parte.

Dos ejemplos. Una flota de 18 llega a una fortaleza de 10. El requisito es ceil(10 × 1,5) = 15, así que la conquistas con 3 de sobra. Una flota de 12 que llega a la misma fortaleza la deja con 2.

Si varias flotas llegan en el mismo tick, se resuelven una a una en el orden en que salieron.

## Cómo termina una partida

- **Victoria:** el enemigo no tiene islas ni flotas.
- **Victoria decisiva:** si tienes el triple de las tropas totales del enemigo y al menos el 60% de las islas durante 5 segundos, el enemigo se rinde. Así se evita la aburrida limpieza final de una partida ya ganada.
- **Derrota:** no tienes islas ni flotas, o pierdes una isla que debías proteger.
- **Límite de tiempo:** a los 8 minutos simulados gana el jugador con más islas. Casi nunca debería activarse.

## Un motor para tiempo real y por turnos

El estado del juego depende solo del mapa inicial, una semilla y una lista de comandos, sin reloj ni aleatoriedad dentro del motor. La misma entrada da el mismo resultado en todos los dispositivos. Eso permite que el mismo motor funcione en tiempo real ahora y en turnos en red más adelante, y hace que las repeticiones y los informes de errores se reduzcan a guardar una lista de comandos.
