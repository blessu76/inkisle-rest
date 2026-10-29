---
title: Sonido desactivado por defecto: una escala para cada mar
description: Inkisle empieza en silencio y es el jugador quien activa el sonido. Cómo se crean los sonidos en código sin archivos de audio, cómo cada mar tiene su propia escala de cinco notas y por qué una cadena de capturas sube por la escala.
slug: sound-off-by-default
lang: es
translation_of: en
category: making-of
keywords: Inkisle, audio de juego, sonido procedural, escala pentatónica, juego móvil, accesibilidad, ajustes
image_alt: Cinco notas ascendentes dibujadas como pequeños puntos de tinta sobre una fila de islas.
---
Mucha gente juega en el teléfono en público o en la cama. Un juego que empieza con ruido es un juego que se cierra. Por eso en Inkisle **el sonido está desactivado hasta que el jugador lo activa**, y ese ajuste se guarda.

## Desactivado de verdad

Cuando el sonido está desactivado, el código de audio ni siquiera se inicia: el reproductor de sonido se crea la primera vez que realmente hace falta un sonido. Un juego silenciado nunca toca el sistema de audio del teléfono. Si el ajuste guardado está dañado o falla el almacenamiento, la respuesta vuelve a ser «desactivado». La app también respeta el interruptor de silencio del teléfono. Los errores dentro del código de audio se capturan en lugar de escaparse, lo cual fue una corrección tras una revisión de código que descubrió que un tipo de error de audio podía saltarse la red de seguridad.

## Sin archivos de sonido

Cada sonido se **crea en código**. La app construye para cada tono un WAV breve de 16 bits y mono a 22.050 muestras por segundo: una onda (sinusoidal, triangular o de diente de sierra), un ataque de 12 ms y un decaimiento exponencial. No hay archivos grabados que licenciar. Los parámetros de los tonos vienen del prototipo web, así que la app suena como sonaba el prototipo.

## Una escala para cada mar

Cada mar tiene su propia **escala pentatónica**, cinco notas que suenan bien en cualquier orden:

| Mar | Pasos sobre la nota base (semitonos) |
|---|---|
| Bahía Calma (Calm Bay) | 0, 2, 4, 7, 9 |
| Estrecho del Viento (Windy Strait) | 0, 2, 5, 7, 9 |

La nota base es 523,25 Hz. El segundo mar se diferencia en una sola nota, el tercer paso (5 en lugar de 4).

## Las cadenas suben

Cuando capturas varias islas seguidas, **cada captura suena un paso más alta** en la escala del mar. Tras cinco pasos la escala sube una octava, y por encima del décimo paso se queda en la nota más alta. Así, una buena cadena se oye como una línea ascendente y, como la escala solo tiene notas que encajan entre sí, una cadena rápida se mantiene afinada.

## Lo que no hemos comprobado

- Las pruebas comprueban las notas y que silenciado significa en silencio. No pueden decirnos si **suena agradable**. Nadie ajeno al equipo lo ha escuchado en el altavoz de un teléfono real ni con auriculares.
- Estos tonos son simples pitidos. Si se quedan como sonido final o se sustituyen no está decidido.
