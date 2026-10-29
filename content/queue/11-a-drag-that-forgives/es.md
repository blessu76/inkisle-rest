---
title: Un arrastre que perdona: las pequeñas reglas detrás de un gesto
description: Enviar una flota en Inkisle es un solo arrastre. Las pequeñas reglas que lo hacen funcionar con un dedo de verdad: un área de selección más amplia, un arrastre que muestrea todo el recorrido, un dedo a la vez y mensajes claros cuando no se puede enviar.
slug: a-drag-that-forgives
lang: es
translation_of: en
category: making-of
keywords: Inkisle, controles táctiles, UX de juegos móviles, arrastrar y soltar, multitáctil, diseño de juegos
image_alt: Un pulgar arrastrando desde una isla coral a través del mar hasta una isla vecina, con una línea punteada detrás.
---
La primera fase enseña todo el control en una línea: **arrastra una isla sobre otra isla y sale un barco**. Esa frase esconde muchas decisiones pequeñas, porque un pulgar es mucho más torpe que un ratón. Esta entrada recoge las que nos parecen más seguras.

## El dedo es más grande que la isla

Una isla en pantalla puede ser más pequeña que la yema de un dedo, y el dedo la tapa mientras apuntas. Por eso, cuando pasas sobre islas durante un arrastre, el área que cuenta como "sobre esta isla" es **el radio de la isla más 12 píxeles**. Sin ese margen extra, un arrastre que visiblemente terminaba en una isla a menudo fallaba.

## Un deslizamiento rápido no puede saltarse una isla

Cuando recorres varias islas para elegirlas, la pantalla solo informa de la posición de tu dedo cada cierto tiempo. Un deslizamiento rápido podía saltar de un lado de una isla al otro sin que nunca se informara de que estaba dentro. Por eso el juego **muestrea a lo largo de la línea** entre dos informes, de modo que se cuenta cada isla que el dedo cruzó.

## Un dedo a la vez

Nuestra primera revisión de código encontró un caso en el que no habíamos pensado: si un **segundo dedo** toca la pantalla en mitad de un arrastre, el segundo toque sustituía al primero y los movimientos de los dos dedos se mezclaban. Eso podía dejar la selección en un estado extraño o enviar una flota que nadie quería enviar. La solución es sencilla: el juego sigue **solo el primer dedo** e ignora los demás hasta que se levanta. Una prueba cubre que el segundo dedo se ignora.

## Decir por qué no pasó nada

Si intentas enviar desde una isla con muy pocas tropas, el envío no ocurre. El silencio parece un fallo, así que el juego muestra un mensaje breve: una isla necesita **al menos 2 tropas** para enviar. Mantener pulsada una isla durante **0,4 segundos** selecciona todas tus islas, y un mensaje te dice que toques o arrastres hacia un objetivo para un ataque total.

## La cantidad a enviar

Cuánto sale de una isla lo marca una barra de proporción. Por defecto es **50%**. La fase 1-2 enseña a elegir la proporción, y su objetivo de tres estrellas es ganar **sin enviar nunca el 100%**, lo que te anima a probar los otros ajustes.

## Lo que no hemos comprobado

- Todo lo de aquí está comprobado con toques simulados en pruebas. **No hemos visto a personas reales** usarlo en móviles reales, y los gestos que parecen bien en una prueba pueden sentirse mal.
- Los tamaños (12 px, 0,4 s) son primeras suposiciones. Cambiarán si los jugadores fallan las islas o seleccionan todo por accidente.
