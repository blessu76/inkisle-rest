---
title: Enviar desde varias islas a la vez: tres reescrituras de un solo control
description: Atacar una isla desde varias de las tuyas era el control más difícil de Inkisle. La primera versión basada en arrastrar, la corrección de tocar para seleccionar y la versión de deslizar para seleccionar, y lo que nos enseñó cada una.
slug: three-rewrites-of-multi-island-attack
lang: es
translation_of: en
category: making-of
keywords: Inkisle, controles táctiles, UX de juegos móviles, selección múltiple, arrastrar y soltar, diseño de juegos, iteración
image_alt: Una batalla en la que varias islas envían flotas hacia una isla enemiga.
---
Enviar una flota es fácil: arrastras desde tu isla hasta el objetivo. Lo difícil de los controles de Inkisle es **enviar desde varias islas a la vez**, porque los niveles avanzados se ganan llegando juntos. Reescribimos ese control tres veces en pocas horas, y la historia muestra por qué.

## v0.1: todo a la vez

El primer prototipo admitía varias formas de hacerlo:

- Arrastrar desde una isla hasta un objetivo y **pasar por encima de tus otras islas por el camino** para añadirlas como orígenes.
- **Mantener pulsada** (0,4 segundos) una isla para seleccionar todas las tuyas y luego arrastrar para un ataque total.
- Tocar un origen y luego tocar el objetivo, como alternativa a arrastrar.

Sobre el papel lo cubría todo. En la práctica, el pulgar tapa justo la isla por la que está pasando, y un nivel que enseñaba «pasa por encima de las islas mientras arrastras» pedía un gesto difícil de ver y difícil de apuntar.

## v0.1.1: seleccionar primero, luego ir

La solución fue dividir el gesto en dos. **Toca tus islas una por una para seleccionarlas**, luego toca el objetivo y todas parten. Arrastrar una isla seleccionada sigue enviando a todo el grupo. Añadimos:

- una pequeña insignia sobre la selección que muestra cuántas islas hay elegidas,
- un toque en el mar vacío para borrar la selección,
- un área de selección más amplia al unirse mientras se arrastra (radio de la isla más 12 px), porque un dedo es más grande que una isla,
- una pista que se muestra las primeras veces, y además las tarjetas de nivel que enseñan el control ahora describen el toque.

Tocar es preciso y tranquilo, pero con muchas islas supone **muchos toques** antes de cada ataque. En un juego en tiempo real, eso es tiempo.

## v0.1.2: barrer para elegir

La versión más reciente permite **deslizar el dedo sobre tus islas para elegirlas de un solo trazo**, y luego escoger el objetivo. Seleccionar cuatro islas es ahora un solo movimiento en lugar de cuatro toques. Si los métodos anteriores se mantienen como alternativa, y cómo se siente el barrido en detalle, no es algo definitivo **[sin verificar en el momento de escribir]**.

## Lo que aprendimos y lo que no sabemos

- **Un gesto que exige que el dedo caiga sobre un objetivo pequeño mientras se mueve es frágil en un teléfono.** La primera corrección eliminó el apuntar; la segunda eliminó la repetición.
- Cada versión resolvió un problema y dejó al descubierto el siguiente, lo cual es normal, pero también significa que el control todavía no está asentado.
- **No tenemos datos de jugadores externos** sobre ninguna de las tres versiones. La sensación exacta de la v0.1.2 está **[sin verificar]** hasta que otros la prueben.

La prueba con cinco a ocho personas es donde este control será juzgado de verdad. Si aún dudan antes de atacar, lo cambiaremos por cuarta vez.
