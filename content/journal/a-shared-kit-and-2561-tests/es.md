---
title: Qué protegemos al actualizar un kit compartido: una puerta de 2.561 pruebas
description: Cada vez que Inkisle actualiza el kit compartido que usan nuestras apps, debe pasar una puerta de formato, análisis y pruebas completas. Por qué no sustituimos una función entera del kit, cómo vacilaron las pruebas de tiempo bajo carga, qué archivos cambiaron en la última actualización y qué no hemos comprobado.
slug: a-shared-kit-and-2561-tests
lang: es
translation_of: en
category: making-of
keywords: Inkisle, kit compartido, pruebas, Game Center, actualización, juego móvil
image_alt: Varios bloques pequeños de la misma forma dentro de un marco, con un único punto verde que pasa sobre ellos.
published: 2026-11-24T12:45+09:00
---

Inkisle, nuestro juego de estrategia de conquista de islas para iOS, usa un kit compartido en el que se apoyan varias de nuestras apps. Cada vez que subimos la versión del kit, una puerta ejecuta formato, análisis estático y la suite completa de pruebas antes de confirmar el cambio. El 19 de noviembre pasamos el kit de 0.15.2 a 0.15.3: la puerta superó 2.561 pruebas (8 omitidas) y solo cambiaron dos archivos, `pubspec.yaml` y `pubspec.lock`. Esta entrada trata de cómo se mantiene esa cifra y de lo que vaciló por el camino. El juego está en desarrollo y no se ha lanzado.

## La puerta tiene tres pasos

Un script los ejecuta en orden antes de confirmar: el formato del código no debe cambiar, el análisis estático debe informar de 0 problemas y todas las pruebas deben pasar. Si alguno falla, no confirmamos. Cuando otra persona dice «pasó», lo volvemos a ejecutar nosotros antes de confirmar.

## 14 de noviembre: no sustituimos toda la función del kit

Al pasar el kit de 0.12.0 a 0.13.0, este pudo encargarse del apodo y de la clasificación de Game Center. La instrucción del responsable era que cada juego permita al jugador fijar un apodo en el primer inicio y aparecer en la clasificación de Game Center. **No cambiamos por la función de jugador completa del kit.** Teníamos cuatro razones para pensar que nuestra versión era mejor:

1. El apodo vive dentro del registro de ajustes, que se sincroniza entre dispositivos mediante iCloud. Moverlo al almacenamiento del kit rompería esa sincronización.
2. Ya tenemos una hoja de apodo en 16 idiomas y pruebas congeladas para combinaciones de idioma y tamaño de pantalla.
3. Las clasificaciones son 24 tableros dinámicos, con valores derivados del registro de progreso sincronizado. Moverlas dejaría dos lugares que guardan una mejor puntuación.
4. Play Games en Android sigue necesitando la biblioteca que usa.

Así que solo la conexión de Game Center en iOS pasó al kit, y los ID de tablero, los apodos guardados y las mejores puntuaciones se conservaron sin cambios. El reenvío de datos pendientes tras iniciar sesión tarde y el rellenado previo del apodo con el nombre de Game Center se incorporaron a la vez. Añadimos 10 pruebas, y la puerta superó entonces 1.990 pruebas (7 omitidas).

## Las pruebas de tiempo vacilaron

Dos veces en esta puerta, una prueba que mide tiempo vaciló bajo carga. Una prueba de presupuesto de fotogramas que dibuja 800 carreteras falló una vez cuando las pruebas corrían en paralelo, y durante el trabajo de iCloud falló una vez una prueba de presupuesto de rendimiento. Ambas pasaron al ejecutarlas solas o al repetir la suite completa. Lo interpretamos como carga, no como nuestro cambio, aunque no rastreamos la causa. No relajamos los presupuestos.

## 19 de noviembre: dos archivos cambiados

La versión 0.15.3 deja la API pública como estaba; hace que un recuento en la sincronización de iCloud se detenga tras el desmontaje y añade documentación. No cambiamos ni código ni pruebas en la app. El límite de tamaño que usa la app (512 KB) es intencionado, así que lo mantuvimos. Los archivos cambiados fueron `pubspec.yaml` y `pubspec.lock`, y la puerta pasó a la primera, esta vez sin vacilaciones de tiempo. La cifra de pruebas creció de 1.990 el 14 de noviembre a 2.561.

## Lo que no hemos comprobado

- **El inicio de sesión de Game Center, el envío de puntuaciones, la pantalla de clasificación y un viaje de ida y vuelta de iCloud no se han comprobado en un dispositivo real.** Lo veremos en TestFlight.
- Las vistas de 375 px y 320 px se cubrieron con pruebas de widgets a 320×568 en lugar de verlas directamente.
- No encontramos la causa raíz de las pruebas que vacilaron bajo carga.
- Las cifras de aquí son los resultados de la puerta de ese día, y el número de pruebas cambiará más adelante.

## Preguntas frecuentes

### ¿Qué es el kit compartido?

Un conjunto de código que usan juntas varias de nuestras apps. Inkisle usa sus partes de apodo, Game Center y sincronización de iCloud.

### ¿Qué comprobáis al actualizar el kit?

Un script comprueba que el formato no cambia, que el análisis estático informa de 0 problemas y que todas las pruebas pasan. Si alguno falla, no confirmamos.

### ¿Está lanzado el juego?

No. Sigue en desarrollo y no se ha lanzado.
