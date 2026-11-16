---
title: Notas de la versión dentro de la app: una hoja en 12 idiomas y un control de longitud
description: Las notas de la versión de Inkisle son una hoja dentro de Ajustes, no una página web. Cómo se escriben las notas de cada compilación en 12 idiomas, los controles de número de elementos y longitud, y el error de prueba que mostró una hoja vacía.
slug: release-notes-inside-the-app
lang: es
translation_of: en
category: making-of
keywords: Inkisle, notas de la versión, localización, multilingüe, pruebas, juego móvil
image_alt: Una hoja de papel que sube desde la parte inferior de una pantalla, con doce pequeñas pestañas de idioma en fila encima.
---

Las notas de la versión de Inkisle, nuestro juego de estrategia de conquista de islas para iOS, son una hoja dentro de la app que se abre desde Ajustes, no una página web. Las notas de cada compilación se escriben en 12 idiomas, y un script de control verifica el número de elementos y la longitud. El control de la compilación 34 dio 0 errores y 0 advertencias. El juego sigue en desarrollo y no se ha publicado.

## Quitamos la página web

Al principio, la pantalla principal tenía un enlace "Notas de la versión" y un botón de información (ⓘ). En la compilación 32 quitamos ambos. Lo que contenía la ventana de información (política de privacidad, condiciones, versión, licencias de código abierto, operador, contacto y el aviso de +16) pasó a Ajustes, y las notas de la versión se convirtieron en una hoja que se abre desde una fila "Notas de la versión" en esa pantalla. La página de notas de la versión del sitio web también se retiró el 15 de noviembre. Sin un sitio aparte, el texto dentro de la app es la única fuente.

La hoja usa el mismo marco que nuestras otras ventanas emergentes (InkSheet). Ocupa como máximo el 60 % de la altura de la pantalla, la fila del título y la X de cerrar (48×48) se quedan fijas, y solo se desplaza el contenido dentro de la hoja.

## Una compilación, un archivo, 12 idiomas

Para cada compilación, `release_notes/<build>.json` contiene un título, una introducción y los elementos en 12 idiomas (ko, en, ja, zh-Hant, es, pt-BR, fr, de, id, th, vi, tr). Los archivos se empaquetan en `assets/release_notes.json`, que se incluye en la app, y la hoja lo lee.

## Controles de longitud y número

Un script de control lee los archivos e informa de las infracciones de las reglas.

- **RN06:** un elemento debe tener 200 caracteres o menos. El texto en alemán era largo, así que el elemento de fin de temporada de la compilación 34 se redujo a 183 caracteres. En la compilación 31 dividimos un elemento de compra en dos para que entrara en el límite.
- **RN05:** se recomiendan de 3 a 6 elementos. Es solo una advertencia y no bloquea una publicación. Las advertencias restantes están en compilaciones antiguas con 1 o 2 elementos; son un registro fiel de lo que se escribió, así que las dejamos.
- Una prueba falla si no hay una entrada para la versión y el número de compilación actuales, así que cada cambio de compilación exige escribir antes la nota en 12 idiomas.
- El script de subida a iOS ejecuta el control de notas de la versión antes de la puerta de verificación (formato, análisis, pruebas).

## La prueba que veía una hoja vacía

Dos pruebas de la hoja de notas de la versión empezaron a ver una hoja vacía. La causa estaba en la prueba, no en la app. El paquete es un archivo de recursos real, y al crecer, `pumpAndSettle`, que espera a que la pantalla se estabilice, terminaba antes de que se leyera el archivo. Cambiamos las pruebas para abrir la hoja, esperar 300 ms con `runAsync` y volver a dibujar. El código de la app no cambió.

## Lo que no hemos comprobado

- Las traducciones distintas del coreano y el inglés son hechas por máquina y no han pasado por una revisión de hablantes nativos [sin verificar].
- No hemos visto la hoja abierta al 60 % en un dispositivo real. Las pruebas de widgets a 375×667 y 320×568 hacen esa función [sin verificar].

## Preguntas frecuentes

### ¿Dónde encuentro las notas de la versión de Inkisle?

En la app, pulsa la fila "Notas de la versión" en Ajustes y se abre una hoja. No hay una página web aparte. El juego todavía no se ha publicado.

### ¿En cuántos idiomas están escritas?

En 12 idiomas. Salvo el coreano y el inglés, son traducciones automáticas y todavía no se han revisado.

### ¿Qué pasa si un elemento es demasiado largo?

Si un elemento supera los 200 caracteres, el script de control informa de un error, y entonces lo acortamos o lo dividimos en dos.
