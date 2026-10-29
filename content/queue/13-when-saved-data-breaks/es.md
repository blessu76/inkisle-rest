---
title: Cuando los datos guardados se rompen: cómo se recupera la app
description: Un teléfono puede perder, truncar o bloquear los datos guardados de una app. Cómo trata Inkisle el almacenamiento ausente, dañado, obsoleto o no disponible para el progreso, la introducción y el ajuste de sonido, y dónde nuestra recuperación sigue siendo tosca.
slug: when-saved-data-breaks
lang: es
translation_of: en
category: making-of
keywords: Inkisle, datos guardados, gestión de errores, robustez, almacenamiento local, juego móvil, guardado con versión
image_alt: Un pequeño cuaderno con una página rota junto a una fila de islas, una forma tranquila de mostrar un guardado dañado.
---
Inkisle no tiene cuentas ni servidor, así que todo el progreso vive **solo en el teléfono**. Eso hace que los datos guardados sean sencillos, y también significa que nadie puede restaurarlos por ti. La pregunta que nos hicimos: ¿qué debe hacer la app cuando lo que lee de vuelta está mal?

## Cuatro cosas que pueden salir mal

| Situación | Qué hace la app |
|---|---|
| Todavía no hay nada guardado | Empezar desde el nivel 1-1 |
| El texto guardado está dañado (no se puede leer) | Tratarlo como vacío y empezar de cero |
| Guardado por otra versión del formato | Ignorarlo y empezar de cero |
| El almacenamiento del teléfono no se puede abrir en absoluto | Jugar en memoria; nada se rompe, pero nada se conserva al cerrar |

Los datos guardados llevan un número de versión en su nombre y en su contenido, de modo que un cambio futuro del formato pueda reconocerse en vez de malinterpretarse.

## El daño en una parte no borra el resto

El registro de progreso tiene una entrada por nivel. Nuestra revisión señaló que una sola entrada dañada solía reiniciarlo todo. Ahora cada nivel se lee por separado: una entrada ilegible se omite y los demás niveles se conservan. Solo un archivo completamente ilegible, o una versión distinta, implica empezar de cero. Además, las entradas tienen que indicar que el nivel fue **ganado**, porque solo se escriben las victorias.

## Una reparación que repara

La introducción guarda su propio pequeño guardado (la bolsa barajada de una entrada anterior). Cuando se dañaba, la lectura fallaba antes de que la app escribiera nada nuevo, así que el texto roto se quedaba ahí y el problema se repetía en cada arranque. La solución: si la lectura falla, se empieza con el valor por defecto y se **escribe el valor por defecto encima**. El código de la introducción tiene pruebas para guardados rotos.

## Los ajustes vuelven a la opción silenciosa

El único ajuste es el sonido. Si sus datos guardados están rotos, la respuesta es **desactivado**, no activado. Un archivo roto nunca debería hacer que el juego suene más fuerte.

## El progreso solo puede crecer

Las estrellas y los mejores tiempos solo mejoran, y una repetición perdida no cambia nada. La regla de desbloqueo solo mira si el nivel anterior fue ganado.

## Lo que no hemos comprobado

- Probamos en el código texto dañado, versiones incorrectas y almacenamiento ausente. **No** hemos probado un teléfono sin espacio ni una copia de seguridad y restauración del sistema operativo.
- Cuando todo el archivo es ilegible, el jugador vuelve a empezar desde el nivel 1-1. Para un jugador con muchas estrellas eso sería desagradable, y no hemos decidido si añadir algo más amable.
