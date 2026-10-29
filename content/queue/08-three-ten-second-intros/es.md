---
title: Una intro de diez segundos en tres versiones: cielo, mar y tierra
description: Inkisle empieza con una intro de diez segundos que tiene tres versiones. Cómo comparten un mismo final, por qué una bolsa mezclada decide cuál ves, cuándo se acorta a tres segundos y qué pasa con la opción de reducir movimiento activada.
slug: three-ten-second-intros
lang: es
translation_of: en
category: making-of
keywords: Inkisle, intro del juego, inicio de la app, botón de omitir, reducir movimiento, accesibilidad, juego móvil
image_alt: Islas en un mar verde menta con tinta de color coral extendiéndose sobre una de ellas, la imagen inicial de la intro de Inkisle.
---
Lo primero que ves al abrir Inkisle es una intro. Queríamos que las primeras veces se sintiera como un pequeño acontecimiento y que después **no estorbara**. Esta entrada describe cómo está construida la intro y las reglas que deciden lo que ves.

## Un final, tres comienzos

La intro completa dura **10 segundos**. Los primeros 7 segundos tienen tres versiones: **cielo**, **mar** y **tierra**. Los últimos 3 segundos son iguales en todas: el final que lleva al menú. Compartir el final significa que lo dibujamos una sola vez y que todas las versiones llegan al mismo lugar.

## ¿Cuál te toca?

Elegir al azar puede mostrar la misma intro tres veces seguidas, y eso parece un fallo. Por eso la app usa una **bolsa mezclada**: mete las tres versiones en una bolsa en orden aleatorio y saca una en cada inicio. Cuando la bolsa se vacía, se vuelve a llenar. Dos consecuencias:

- Dentro de una misma ronda, **tres inicios seguidos muestran las tres versiones**.
- La primera versión de una ronda nueva nunca es igual a la última que viste.

La bolsa se guarda en el teléfono, así que sigue funcionando entre un inicio y otro.

## Larga al principio, corta después

Durante los **tres primeros inicios** ves los 10 segundos completos. A partir del cuarto inicio, la app reproduce solo el final compartido, de **3 segundos**. Un botón de omitir aparece **0,6 segundos** después de que empieza la intro, para que quien la ve por primera vez no tenga que omitirla antes de ver nada. Omitir llama al mismo paso de "terminado" que cuando la intro acaba, y una prueba comprueba que solo se ejecuta una vez.

## Reducir movimiento

Si el ajuste de reducir movimiento del teléfono está activado (en iOS, "Reducir movimiento"; en Android, las animaciones desactivadas), la intro **no se mueve**. Muestra el fotograma final ya terminado durante **1,2 segundos** y pasa al menú. El botón de omitir está presente desde el principio.

## Cuando la bolsa guardada está dañada

Nuestra revisión de código descubrió que una bolsa guardada dañada nunca se reparaba: la app no lograba leerla, empezaba de cero en cada inicio y seguía mostrando la versión completa de 10 segundos. La solución es tratar los datos ilegibles como "sin datos" y escribir una bolsa nueva de inmediato. Si el almacenamiento no está disponible en absoluto, la app elige una versión al azar y reproduce la intro completa, y nunca bloquea el inicio del juego. Hay pruebas para estos casos.

## Lo que no hemos comprobado

- No hemos medido cómo funciona la intro en un **teléfono real**. Las pruebas cubren las reglas anteriores, no la fluidez de la animación.
- Si diez segundos es la duración adecuada para un primer inicio es una suposición hasta que otras personas la vean.
