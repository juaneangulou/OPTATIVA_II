# Video 7: Quarto como sitio de documentación viva

## Para estudiar por tu cuenta
La documentación de un sistema suele quedar desactualizada cuando vive lejos del código y nadie recuerda cómo publicarla. **Quarto** permite escribir documentos con texto y código en archivos fuente y generar a partir de ellos un sitio web navegable.

En esta clase crearás una pequeña sección de documentación para la plataforma logística. El objetivo no es aprender todas las funciones de Quarto, sino entender cómo mantener la documentación cerca del proyecto y cómo comprobar que se publica correctamente.

## 1. ¿Qué significa documentación viva?
La documentación es **viva** cuando se actualiza junto con el sistema y existe un proceso conocido para comprobar y publicar los cambios.

Por ejemplo, si el equipo cambia el recorrido de una entrega, el diagrama y las instrucciones de operación deben cambiar en la misma revisión o quedar anotados como una tarea pendiente.

Poner un archivo en Git no garantiza que esté actualizado. La ventaja es que sus cambios pueden revisarse con el mismo historial y proceso que el código.

## 2. ¿Qué es Quarto?
Quarto es una herramienta de publicación que convierte archivos de texto estructurados en documentos o sitios web. Un archivo `.qmd` puede combinar títulos, texto, listas, enlaces, imágenes y, según el proyecto, código o diagramas.

El archivo fuente es lo que editas; el sitio generado es lo que consultas en el navegador. Cuando el contenido cambia, se vuelve a generar el sitio.

## 3. Una página sencilla de arquitectura
Podrías crear una página llamada `arquitectura.qmd` con una estructura como esta:

```markdown
---
title: "Arquitectura de la plataforma logística"
---

## Propósito
Permitir que clientes consulten pedidos y que el equipo coordine entregas.

## Partes principales
- Pedidos registra las compras.
- Entregas organiza rutas y estados.
- Notificaciones informa cambios confirmados.

## Decisión vigente
Pedidos y Entregas se mantienen como módulos separados dentro de una aplicación.
```

El bloque inicial entre `---` contiene metadatos, como el título. El resto utiliza Markdown: encabezados, párrafos y listas.

Este ejemplo explica una decisión, pero aún no basta como documentación completa. Quien lea también necesita saber a qué alcance aplica, qué dato cruza entre módulos y cómo iniciar o probar el proyecto.

## 4. Organiza la documentación según preguntas del lector
Una estructura útil puede incluir:

1. **Inicio:** qué problema resuelve el sistema y para quién.
2. **Arquitectura:** actores, partes y dependencias principales.
3. **Decisiones:** por qué se eligió una solución y qué alternativa se descartó.
4. **Desarrollo:** cómo restaurar dependencias, ejecutar pruebas y levantar la aplicación.
5. **Operación:** dónde revisar errores y qué hacer ante fallos comunes.

No agregues páginas porque sí. Cada página debe responder una pregunta que el alumno o el equipo realmente necesita resolver.

## 5. Generar y revisar el sitio
El flujo habitual es:

1. Editar el archivo fuente `.qmd`.
2. Ejecutar el comando de renderizado configurado para el proyecto.
3. Abrir el sitio generado y revisar títulos, enlaces, imágenes y diagramas.
4. Corregir errores de renderizado o enlaces rotos.
5. Incluir fuente y cambios en la revisión del repositorio.
6. Publicar el sitio con el proceso elegido por el proyecto.

Los comandos exactos dependen de cómo se instaló y configuró Quarto. Consulta el `README` del repositorio; no asumas que todos los proyectos publican con el mismo comando.

## 6. Mantener coherentes los diagramas
Un diagrama tiene su propio archivo fuente. Si una flecha muestra que Pedidos llama directamente a una base de datos que ya no usa, la página se renderizará correctamente y aun así comunicará algo falso.

Actualiza el diagrama cuando cambien las partes o las relaciones. Añade una leyenda para explicar colores y símbolos, y evita poner clases y detalles de implementación en un diagrama que pretende mostrar el contexto general.

## 7. Actividad de autoestudio
Crea el borrador de una página de documentación para el flujo “cliente consulta el estado de una entrega”. Incluye:

1. Un título y un párrafo de propósito.
2. Los actores y partes que participan.
3. El recorrido de la consulta, desde la aplicación hasta la respuesta.
4. Qué muestra el sistema si el servicio de rutas no responde.
5. Una decisión arquitectónica y por qué se tomó.
6. Una instrucción para ejecutar o revisar una prueba del flujo.

Después revisa tu documento:

- ¿Una persona que no escribió el código puede seguir el recorrido?
- ¿Cada diagrama tiene título y significado para sus flechas?
- ¿Hay enlaces que llevan a archivos existentes?
- ¿El contenido coincide con el comportamiento actual?

### Respuesta modelo
La página podría decir que el cliente consulta a través de una entrada de la aplicación, que Pedidos confirma que el registro existe y que Entregas informa la última ubicación. Si rutas falla, se muestra el estado confirmado y se señala que la ubicación no está disponible; no se inventa un dato.

La decisión debe indicar si se consulta cada servicio directamente o mediante una Gateway y qué necesidad motivó esa elección. La instrucción de prueba debe señalar qué comportamiento espera comprobar, no limitarse a decir “ejecutar pruebas”.

## Comprueba lo que aprendiste
1. ¿Cuál es la diferencia entre el archivo `.qmd` y el sitio generado?
2. ¿Guardar un documento en Git garantiza que siga actualizado?
3. ¿Qué revisarías después de generar el sitio?

**Respuestas:** `.qmd` es la fuente editable y el sitio es el resultado publicado; no, su contenido aún puede quedar obsoleto; revisa enlaces, diagramas, títulos y que la explicación coincida con el sistema.

## Conclusión
Quarto ayuda a convertir documentación escrita en archivos fuente en un sitio organizado. Para que sea documentación viva, el equipo también necesita revisar los cambios, validar el resultado generado y actualizar las explicaciones cuando cambie la arquitectura.
