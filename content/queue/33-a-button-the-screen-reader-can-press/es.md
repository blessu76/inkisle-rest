---
title: Un botón que el lector de pantalla puede pulsar
description: El icono de cierre y el faro de Inkisle tenían etiquetas de lectura, pero les faltaba la acción de accesibilidad. Comprobamos tanto las palabras como lo que ocurre al activar cada control.
slug: a-button-the-screen-reader-can-press
lang: es
translation_of: en
category: making-of
keywords: Inkisle, accesibilidad, lector de pantalla, interfaz, pruebas de widgets
image_alt: Una X y un icono de faro en dos tarjetas pequeñas, con un contorno de foco alrededor de cada control.
---

Inkisle es un juego de estrategia y conquista de islas en desarrollo. En una revisión de accesibilidad, examinamos cómo describe sus controles a un lector de pantalla. Destacaron dos: la X que cierra un panel y el faro del mapa, que vuelve a reproducir un final. Estamos desarrollando el juego para iOS.

## Del nombre a la acción

Los dos controles ya tenían nombre. En el árbol de accesibilidad de Flutter, el nodo con el nombre había perdido la acción de pulsación al sustituir la descripción predeterminada del icono. Conectamos la acción al mismo nodo que contiene la etiqueta. En las pruebas, activar Cerrar cierra el panel y activar el faro abre el final.

## Oírlo una sola vez

También comprobamos qué se leía dos veces. Un botón de proporción de flota mostraba el mismo porcentaje en la etiqueta y en el texto visible. El control para saltar la introducción y los marcadores numerados del mapa tenían duplicaciones parecidas. Dejamos una sola etiqueta de lectura en cada caso, con la información necesaria para identificar el control.

## Preguntas frecuentes (FAQ)

### ¿Se ha probado con un lector de pantalla en un teléfono?

Las pruebas de widgets comprobaron las etiquetas y las acciones de accesibilidad. Todavía no hemos verificado los cambios en un teléfono con VoiceOver o TalkBack.

### ¿Para qué sirve el faro del mapa?

Activa el faro para volver a reproducir un final.
