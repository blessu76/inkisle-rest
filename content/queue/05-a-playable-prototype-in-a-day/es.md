---
title: Un prototipo jugable en un día
description: Dieciséis niveles, dos mares y un único archivo HTML de unos 95 KB sin peticiones externas. Cómo está construido el prototipo, qué probamos en un navegador sin interfaz y qué no pudimos probar.
slug: a-playable-prototype-in-a-day
lang: es
translation_of: en
category: making-of
keywords: Inkisle, prototipo, prototipo web, motor de juego determinista, juego HTML, juego móvil, canvas
image_alt: Muchas islas pequeñas con números de tropas y una flota cruzando el mar en el prototipo de Inkisle.
---
Antes de construir una app queríamos algo jugable en un teléfono. El 2026-10-29 construimos un prototipo web en un solo día. Esta entrada describe qué contiene, cómo está armado y, igual de importante, qué no pudimos comprobar.

![Tres pantallas del prototipo en el teléfono: la carta marina con una tarjeta de nivel, una batalla con un arrastre en curso y un resultado de victoria con tres estrellas. El texto de las capturas está en coreano.](/assets/posts/img/proto-shots.jpg)
*La carta marina con una tarjeta de nivel, una batalla con un arrastre en curso y la pantalla de resultado.*

## Qué contiene

- **Dieciséis niveles:** el mar 1, "Bahía Calma" (Calm Bay), tiene ocho, y el mar 2, "Estrecho del Viento" (Windy Strait), tiene ocho. Los mares siguientes aparecen como tarjetas bloqueadas.
- **El ciclo:** carta, tarjeta de nivel, batalla, resultado con una a tres estrellas, siguiente nivel.
- **Desbloqueo:** supera un nivel y se abre el siguiente. Vence al jefe y se abre el siguiente mar. Las estrellas nunca bloquean el avance; son objetivos extra.
- **Sonido:** sintetizado en el navegador, con una escala pentatónica distinta para cada mar y una nota que sube con cada captura en cadena.
- **El progreso** se guarda en el almacenamiento local del navegador, y el juego sigue funcionando en memoria si el almacenamiento está bloqueado.

## Cómo está construido

- **Un solo archivo.** Unos 95 KB, sin peticiones externas ni fuentes web, así que funciona sin conexión y dentro de un marco.
- **Motor y pantalla están separados.** El motor es un módulo puro sin DOM, sin reloj y sin llamadas aleatorias. La interfaz solo encola órdenes como "enviar el 50 % de la isla 0 a la isla 1", y un bucle avanza el motor cada 100 ms.
- **La aceleración funciona avanzando más rápido**, no cambiando las reglas, de modo que los límites de tiempo de las estrellas siguen siendo justos al doble de velocidad.
- **La pausa** detiene los ticks, y el juego se pausa solo cuando la pestaña queda oculta.

Mantener el motor puro fue una apuesta de futuro: el mismo código podrá ejecutarse más adelante por turnos a través de una red, y una lista de órdenes grabada puede reproducir una partida.

## Qué probamos

Manejamos el prototipo con un Chrome sin interfaz. En una pantalla de 375 por 812 arrancó con el almacenamiento vacío, envió flotas con arrastre de ratón y con arrastre táctil, hizo una pausa (el contador de ticks se quedó congelado), ganó el nivel 1-1 en unos 12 segundos con tres estrellas, guardó el progreso, desbloqueó el 1-2 y conservó el progreso tras recargar. A 320 por 568 nada se desbordó hacia los lados. La consola del navegador no mostró errores.

También hicimos una comprobación determinista: el mismo mapa y las mismas órdenes dieron el mismo resultado en cada ejecución, y ejecutar en tiempo real y por turnos produjo el mismo desenlace.

## Qué no pudimos probar

- **Dispositivos reales.** iOS Safari y un teléfono Android de gama media **no están comprobados**. La emulación táctil de un navegador sin interfaz no es un dedo.
- **Rendimiento.** Nuestro objetivo es 22 islas y 300 flotas a 60 fotogramas por segundo. No se ha medido.
- **Funciones que faltan:** un modo de juego libre, una forma de exportar registros de juego, guardado a mitad de nivel y varias animaciones.
- **Asperezas conocidas:** la etiqueta del arrastre puede tapar el número de una isla vecina, y la tarjeta de nivel puede tapar nodos de la carta.

Los siguientes pasos son una prueba de 30 minutos con entre cinco y ocho personas, con un registro de juego integrado de antemano. La siguiente entrada trata del trabajo de equilibrio que hicimos sin humanos.
