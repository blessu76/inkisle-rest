---
title: Lo que la app no tiene: sin anuncios, sin cuentas, sin rastreo
description: Parte del diseño de Inkisle consiste en lo que se deja fuera. La app no pide cuenta y no tiene anuncios ni herramientas de rastreo, funciona en iOS y Android desde una sola base de código, y dibujamos un icono nuevo para ambos. Lo que decidimos y lo que no hemos comprobado.
slug: what-the-app-does-not-have
lang: es
translation_of: en
category: making-of
keywords: Inkisle, privacidad, sin anuncios, sin cuenta, icono de la app, iOS, Android, Flutter, juego móvil
image_alt: Una isla de color coral dibujada como una simple mancha de tinta sobre fondo crema, el icono de la app de Inkisle.
---
Gran parte de lo que hace agradable a una app es lo que **no** hace. Para el primer lanzamiento de Inkisle decidimos una lista corta de cosas que dejar fuera.

## Sin cuenta, sin anuncios, sin rastreo

- **Sin cuenta.** Abres la app y juegas. No hay registro ni inicio de sesión.
- **Sin anuncios ni herramientas de rastreo.** La lista de paquetes externos de la app es corta: uno para guardar pequeños ajustes en el teléfono, uno para reproducir sonidos y uno para abrir una página web. No hay ningún paquete de publicidad, ningún paquete de analítica ni ningún paquete de inicio de sesión.
- **El progreso se queda en el teléfono.** Las estrellas guardadas y el ajuste de sonido se almacenan localmente y no se envían a ninguna parte.

La app tiene una pantalla de información con un enlace a la política de privacidad, que es la misma página que hay en este sitio web. Lo único que toca la red es abrir esa página, y solo ocurre cuando el jugador la pulsa. La política se escribió primero para este sitio web, así que todavía hay que revisarla y actualizarla para que cubra la app antes de enviar nada a una tienda.

## Una base de código, dos plataformas

Inkisle está hecho con Flutter, así que **iOS y Android se desarrollan juntos** a partir del mismo código, y cada cambio se prueba en ambos. El plan es **lanzar primero en iOS**. Aun así compilamos y probamos Android todo el tiempo, para que no se convierta más adelante en un segundo proyecto. El juego está bloqueado en orientación vertical en ambos. Las versiones mínimas son iOS 13 y Android API nivel 24.

## El icono

El icono es una sencilla **isla de tinta color coral** sobre fondo crema. Un solo código de dibujo genera tres archivos:

- el icono cuadrado normal para iOS y versiones antiguas de Android,
- el primer plano "adaptativo" de Android, dibujado dentro del área segura del 66% a la que Android recorta,
- una silueta de un solo color para los iconos temáticos de Android 13.

Aquí publicamos un error y lo corregimos: el icono adaptativo se reducía dos veces (una por nosotros y otra por la configuración de compilación), por lo que se veía demasiado pequeño en Android. Ahora la reducción ocurre en un solo lugar.

## Lo que no hemos comprobado

- No hemos ejecutado la app en un **iPhone o teléfono Android real** con una compilación de tienda, y no la hemos enviado a ninguna de las dos tiendas. Cosas como la revisión de las tiendas, las pantallas de la app en otros idiomas y el aspecto del icono en distintos lanzadores siguen abiertas.
- "Sin rastreo" describe lo que hay en nuestro propio código y en la lista de paquetes. No hemos auditado los paquetes de los que dependemos más allá de leer sus descripciones.
