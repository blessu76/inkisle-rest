---
title: Ajustar la dificultad con bots: cinco niveles que estaban mal
description: Jugamos cada nivel con bots sencillos durante 40 semillas por nivel y encontramos niveles imposibles, demasiado cortos o demasiado difíciles. Los cinco cambios, los porcentajes de victoria antes y después, y por qué los bots no son personas.
slug: tuning-the-difficulty
lang: es
translation_of: en
category: making-of
keywords: Inkisle, equilibrio del juego, ajuste de dificultad, simulación con bots, porcentaje de victorias, diseño de niveles
image_alt: Una batalla concurrida entre varios bandos de colores en el prototipo de Inkisle.
---
Todavía no tenemos probadores, así que nos hicimos otra pregunta: ¿qué niveles están *obviamente* mal? Dos bots sencillos jugaron cada nivel 40 veces, con 40 semillas distintas, y leímos los porcentajes de victoria.

## Los dos bots

- **Bot sencillo:** cada 10 ticks ataca la isla más barata que puede vencer. Representa a un jugador casual.
- **Bot experto:** cada 5 ticks reúne hasta tres islas y ataca en conjunto.

Ninguno es una persona. Nos indican una dirección, no la dificultad tal como la siente un humano.

## Cinco niveles que estaban mal

| Nivel | Problema | Cambio | Bot sencillo antes → después |
|---|---|---|---|
| 1-1 | El objetivo de tres estrellas «perder como máximo 5» era imposible: solo las islas neutrales costaban 13 | Objetivo cambiado a «como máximo 14» | Tres estrellas 0% → 100% |
| 1-5 | Terminaba en 18 segundos | Base enemiga 20 → 26, una isla neutral entregada al enemigo | 100%, ahora 30 s |
| 1-8 jefe | Prácticamente imposible de vencer | Segunda isla del enemigo más pequeña, isla de la bandera 24 → 26, una isla pequeña entregada al jugador | **0% → 53%** |
| 2-2 | Terminaba en 23 segundos | Base del jugador 15 → 20, una isla entregada al enemigo | 100%, ahora 38 s |
| 2-8 jefe | Demasiado difícil | Isla de la bandera 24 → 28, una fortaleza enemiga convertida en fortaleza neutral de 14 | **10% → 38%** |

Dejamos los otros 11 niveles como estaban. El objetivo era un nivel de jefe que un jugador casual venza tras un reintento, es decir, entre el 40 y el 60% para el bot sencillo.

## Efectos secundarios que notamos

- En un conjunto de 20 semillas, el porcentaje de victorias global del bot sencillo pasó del 84% al 91% y el del bot experto del 78% al 82%.
- El nivel 2-2 se volvió *más difícil* para el bot experto: del 100% al 65%. Creemos que el bot tiene la costumbre de vaciar las fortalezas, pero eso es **[sin verificar]**.
- Los niveles 2-4 y 2-7 muestran porcentajes bajos para el bot experto, 40% y 38%. En un combate concurrido, reunir las fuerzas podría perjudicar. También **[sin verificar]**.
- Los límites de tiempo de dos estrellas parecen demasiado generosos, ya que los bots casi siempre los cumplen. Los ajustaremos cuando veamos tiempos de personas.

![Tres pantallas de teléfono con combates concurridos en el prototipo. El texto de las capturas está en coreano.](/assets/posts/img/tuning-boss.jpg)
*Niveles concurridos del prototipo: una refriega en mitad del mar, un nivel de jefe con la isla de la bandera rodeada y una pantalla de 320 px de ancho.*

## Por qué los bots no son personas

Un bot nunca lee mal un número, nunca se aburre y nunca arrastra mal. Los primeros 30 minutos de una persona son la prueba real: dónde reintenta, dónde abandona, cuánto tarda en llegar a «siguiente». El plan es añadir primero un registro de partidas y luego observar a entre cinco y ocho personas. Hasta entonces, estos números solo dicen que ningún nivel está claramente roto, y eso es una afirmación más débil que «la dificultad es la correcta».
