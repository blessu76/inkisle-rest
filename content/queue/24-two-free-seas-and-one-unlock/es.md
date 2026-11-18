---
title: Dos mares gratis y un solo desbloqueo: cómo simplificamos el pago
description: Inkisle mantiene los mares 1 y 2 gratis y abre el resto con una sola compra, Desbloquear todos los mares. Cómo se configura la tinta consumible, cómo se calcula el bloqueo en el código, las líneas que trazamos en la restauración y los reembolsos, y lo que aún no hemos probado.
slug: two-free-seas-and-one-unlock
lang: es
translation_of: en
category: making-of
keywords: Inkisle, compra dentro de la app, no consumible, mares gratis, restaurar compras, juego móvil
image_alt: Dos islas abiertas, y detrás una fila de islas con candados, y una llave atravesada sobre la fila.
---

Inkisle, nuestro juego de estrategia de conquista de islas para iOS, mantiene gratis los mares 1 y 2 y abre los mares 3 a 30 (28 mares) con una sola compra, Desbloquear todos los mares. La tinta consumible está en la configuración de venta, pero no está publicada ni probada en un dispositivo. Los seis artículos de propina siguen igual. Los productos de la tienda están en la fase de registro, pero aún no se han enviado a revisión ni se han probado en un dispositivo, así que la compra todavía no está confirmada. El juego está en desarrollo y no publicado, y esta entrada no indica ningún precio ni fecha.

## Qué cambió

El primer diseño hacía gratuitas todas las etapas, y la tinta que reduce la dificultad se vendía en pequeños artículos consumibles. El 15 de noviembre el responsable lo cambió. **Los mares 1 y 2 son gratis, y Desbloquear todos los mares es una compra única no consumible.** La tinta consumible (paquetes de 5 y de 15) está en la configuración de venta, pero no está publicada ni probada en un dispositivo. También se obtiene tinta con estrellas: una por cada 5 estrellas, y 2 por vencer a un jefe. La tinta comprada antes sigue funcionando.

## El bloqueo se calcula

El número de mares bloqueados no se escribe a mano en el código. Es la cantidad de mares menos la cantidad de mares gratuitos. Hoy eso es 30 − 2 = 28, y cuando se añadan mares, el texto de la hoja de compra "abre N mares" se actualizará solo. El texto de venta que preparamos promete que los mares nuevos quedan incluidos.

- En el mapa, las etapas desde el mar 3 llevan un candado rojo, y al tocar una se abre la tienda en lugar de la etapa.
- Al comprar o restaurar, se abren todos.
- Tras una victoria, si la siguiente etapa está en un mar bloqueado, el juego vuelve al mapa.

## La app tiene que funcionar sin producto

Si la tienda todavía no tiene el producto, o si falla la consulta del precio, solo se desactiva el botón de compra y aparece una nota de "próximamente". La app no se rompe. El precio se vuelve a consultar cada vez que se abre la hoja, así que cuando exista el producto funciona sin cambiar el código. Ahí estamos ahora. La configuración del producto está bloqueada en el lado de la tienda, por lo que nunca hemos ejecutado el flujo de compra real.

## Líneas que trazamos a propósito

| Caso | Comportamiento |
|---|---|
| Un jugador que ya superó el mar 2 | Queda bloqueado. Los registros y las estrellas se conservan, y una compra o restauración vuelve a abrirlos |
| Otro dispositivo | El progreso llega por iCloud, pero el desbloqueo no. Pulsa "Restaurar compras" allí |
| Reembolsos | No retiramos el acceso |
| "Abrir todo" en TestFlight | Quita el bloqueo del progreso, pero no el bloqueo de pago, así que el flujo de compra se puede probar en el entorno de pruebas |

No retirar el acceso tras un reembolso es a la vez una decisión y un límite. El paquete `in_app_purchase` de Flutter no tiene ningún estado que informe de un reembolso, y a esta escala decidimos no verificar los recibos en un servidor. Ese juicio es una estimación [sin verificar].

## Lo que no hemos comprobado

- No hemos comprado ni restaurado en un dispositivo real [sin verificar]. Hasta ahora hay pruebas de widgets (candado, tienda, compra, desbloqueo) y una comprobación de la configuración de StoreKit.
- Las vistas de 375 px y 320 px se cubrieron con pruebas de widgets, no con un simulador [sin verificar].
- Android usa la misma ruta de código, pero sin un producto registrado no pudimos probar el pago allí [sin verificar].
- El texto de compra en los 11 idiomas distintos del coreano es traducido por máquina [sin verificar].

## Preguntas frecuentes

### ¿Cuánto de Inkisle es gratis?

Los mares 1 y 2. Los otros 28 mares se abren juntos cuando se compra Desbloquear todos los mares. El juego todavía no se ha publicado.

### ¿Cuántas veces hay que comprar?

Una vez. Es una compra no consumible, diseñada para incluir también los mares nuevos.

### ¿Las propinas afectan al juego?

No. Los seis artículos de propina no dan ninguna ventaja dentro del juego y se mantienen como están.
