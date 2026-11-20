---
title: Mantener dos dispositivos al compás: mover la sincronización de iCloud a un kit de app compartido
description: El progreso, la tinta y los ajustes de Inkisle ya se igualaban entre dispositivos mediante iCloud. El 16 de noviembre movimos ese puente a un kit de app compartido. Cómo mantuvimos intactos los datos guardados, las reglas de combinación que nunca se reducen, cómo se trata la marca de compra y lo que no hemos comprobado en dispositivos reales.
slug: keeping-two-devices-in-step
lang: es
translation_of: en
category: making-of
keywords: Inkisle, iCloud, sincronización entre dispositivos, datos guardados, combinar, juego móvil
image_alt: Dos pantallas de distinto tamaño unidas por un hilo fino, con las islas de ambos mapas pintadas de los mismos colores.
---

En Inkisle, nuestro juego de estrategia de conquista de islas para iOS, el progreso, la tinta y los ajustes clave (idioma y apodo) se igualan entre dispositivos con el mismo Apple ID mediante el almacenamiento clave-valor de iCloud del propio jugador. Esa sincronización ya existía. Lo que hicimos el 16 de noviembre no fue crearla, sino mover a un kit de app compartido un puente que habíamos escrito nosotros, y la mayor preocupación era no perder ni un solo valor guardado. Todavía no hemos comprobado un viaje de ida y vuelta entre un iPhone y un iPad reales. El juego está en desarrollo y no publicado.

## Lo que movimos

La instrucción del responsable ese día fue que sincronizar los datos del juego entre dispositivos Apple debía ser obligatorio y que debía ir en el kit de app compartido. Encontramos el permiso clave-valor de iCloud ya activado y un puente de Swift y un envoltorio de almacenamiento propios funcionando dentro de la app. Así que:

| Parte | Qué cambió |
|---|---|
| Puente | Eliminamos nuestro puente de Swift y el envoltorio, y pasamos al almacenamiento de plataforma del kit: iCloud en iOS, solo local en el resto |
| Claves y codificación | Dejamos como estaban las claves de almacenamiento, la codificación de cadenas y el identificador de almacenamiento |
| Antes de leer | En iOS, despertar la sincronización una vez justo antes de leer (la sincronización continúa si falla) |
| Ajustes del proyecto | Añadimos también la capacidad de iCloud al archivo del proyecto |

## No perder datos

Como las claves y los formatos se mantuvieron, la nueva versión lee lo que escribió la antigua, y la antigua lee lo que escribe la nueva. Fijamos ambas direcciones con pruebas: leer un bloque de formato antiguo con el código nuevo, leer un bloque nuevo con el código antiguo y leer un bloque de ajustes antiguo. Solo se eliminó código; los valores guardados no se tocaron.

## Combinar nunca reduce

Cuando dos dispositivos tienen progreso distinto, mantuvimos la combinación propia de la app. El kit también tiene un combinador, pero no lo usamos. La combinación de la app ya solo crece, y mantener las mismas claves y el mismo formato era más seguro dejándola como estaba.

- Las estrellas y los mejores registros por etapa toman el valor mayor.
- El progreso toma el del dispositivo que llegó más lejos, y la tinta y los ajustes solo se combinan, nunca se reducen.
- Si el valor en la nube difiere de lo último que subimos, lo volvemos a subir, para recuperarnos de una versión antigua que sobrescribió la misma clave.

## Qué pasó con la marca de compra

Una entrada anterior decía que el desbloqueo no pasa a otro dispositivo. Este trabajo lo cambió. El bloque de sincronización ahora lleva una marca de que se compró Desbloquear todos los mares, y otro dispositivo que la lee también se abre. La marca **solo crece.** Un bloque sin ella no la quita; la volvemos a subir.

Es un cambio de diseño tras la instrucción de "sincronización obligatoria" del responsable, y tiene un límite: una vez sincronizada la marca, un reembolso no la retira en otros dispositivos. Cómo tratar los reembolsos queda como decisión de política. El propio flujo de compra tampoco se ha ejecutado en un dispositivo real.

## Tamaño y pruebas

El almacenamiento clave-valor de iCloud tiene un límite total (1 MB). El bloque de sincronización de una partida con las 240 etapas superadas es de unos 6,3 KB, y una prueba lo mantiene por debajo de 16 KB. Las 14 pruebas nuevas cubren claves y codificación sin cambios, la combinación de dos dispositivos, la marca de compra que se propaga y nunca se retira, el quedarse en local sin conexión o sin sesión, y la combinación tras volver a conectarse. En los cuatro archivos de pruebas de la nube pasaron 77 pruebas.

## Lo que no hemos comprobado

- **No se ha comprobado una sincronización real entre un iPhone y un iPad.** Solo se puede ver en dispositivos reales o en TestFlight.
- Las eliminaciones no viajan a otros dispositivos, porque esta sincronización solo combina.
- No se aplica a Android. Los datos permanecen en el dispositivo.
- Si una versión antigua en otro dispositivo sobrescribe la misma clave, la marca de compra puede desaparecer brevemente, y la versión nueva la vuelve a subir.
- La política de privacidad ahora describe esta sincronización: los datos del juego se guardan en el iCloud del propio jugador, no en nuestros servidores, y se pueden desactivar en los ajustes del dispositivo.

## FAQ

### ¿El progreso de Inkisle se guarda en un servidor?

No. Se iguala entre dispositivos con el mismo Apple ID mediante el almacenamiento clave-valor de iCloud del propio jugador, y no se envía a nuestros servidores.

### ¿Se puede desactivar la sincronización?

Sí. Desactivar iCloud para esta app en los ajustes de iOS detiene la sincronización y deja los datos solo en el dispositivo.

### ¿Se sincroniza en Android?

No. En Android los datos permanecen en el dispositivo.
