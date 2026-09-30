# Video 18: Documentación viva y revisión con IA

## Fuentes de este video
- [Quarto como sitio de documentación viva](https://platzi.com/cursos/software-avanzado/quarto-como-sitio-de-documentacion-viva/)
- [Agentes de IA que revisan tu código en GitHub](https://platzi.com/cursos/software-avanzado/agentes-de-ia-que-revisan-tu-codigo-en-g/)

## Navegación
[⬅️ Video anterior: BDD y modelo C4](video-17.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: Architecture.md y DDD](video-19.md)

## Para estudiar por tu cuenta
Una arquitectura puede estar bien implementada y seguir siendo difícil de entender para alguien que entra al proyecto. Esta clase combina dos ayudas: mantener documentación que se genera desde archivos fuente y usar un agente de IA para revisar cambios antes de integrarlos.

Ni el sitio generado ni el agente son una autoridad automática. Tú debes comprobar que la documentación describe el sistema y que las observaciones del agente coinciden con el código y los requisitos.

## 1. Documentación como parte del proyecto
La documentación se vuelve obsoleta cuando explica rutas, decisiones o comandos que ya no existen. Guardar los archivos fuente junto al código facilita revisar esos cambios dentro del mismo historial.

**Quarto** convierte documentos fuente en páginas o sitios web. Por ejemplo, un archivo `.qmd` puede contener texto, títulos, enlaces y diagramas; al ejecutar Quarto se genera el sitio que se consulta en el navegador.

La relación es:

```text
archivo .qmd -> proceso de renderizado -> sitio web generado
```

El archivo fuente es lo que editas. El HTML o sitio generado es el resultado publicado. Si corriges solo el HTML generado y luego vuelves a renderizar, tu corrección puede desaparecer.

## 2. Una página de documentación logística
Imagina una página `seguimiento.qmd` que explique cómo una consulta llega a la respuesta:

```markdown
---
title: "Consulta de seguimiento"
---

## Qué hace
Muestra el último estado confirmado de una entrega.

## Recorrido
1. El cliente solicita el estado de un pedido.
2. La API comprueba que puede consultarlo.
3. Seguimiento devuelve el último dato conocido y su hora.

## Si falta la ubicación
Se conserva el estado confirmado y se indica que la ubicación no está disponible.
```

El archivo permite revisar texto y cambios como código. Después hay que generar y abrir el sitio para comprobar que títulos, enlaces y diagramas se muestran bien.

## 3. Qué significa “documentación viva”
No significa que el documento se actualice solo. Significa que forma parte del flujo de cambio:

1. Cambia el comportamiento del sistema.
2. Revisa si la explicación quedó desactualizada.
3. Actualiza el archivo fuente en la misma propuesta o registra una tarea concreta.
4. Ejecuta el renderizado.
5. Comprueba que el sitio publicado muestre el cambio correcto.

Un diagrama que contradice el código es información engañosa, aunque el sitio se genere sin errores.

## 4. Pull Request y agente de IA
Una **Pull Request** es una propuesta para integrar cambios de una rama a otra. Muestra las líneas modificadas y permite ejecutar pruebas y revisiones.

Un agente de IA puede analizar el código modificado y sugerir defectos, preguntas o pruebas faltantes. Esas sugerencias son hipótesis. El agente puede equivocarse, no comprender una regla del negocio o no tener todo el contexto.

El flujo responsable es:

1. Escribe en la Pull Request qué comportamiento cambió.
2. Indica el requisito o escenario que debe mantenerse.
3. Pide al agente que cite archivos o líneas relacionados.
4. Comprueba cada hallazgo contra el código y las pruebas.
5. Rechaza sugerencias que cambien el negocio sin justificación.
6. Ejecuta las comprobaciones y revisa el resultado final tú mismo.

## 5. Un ejemplo de revisión
Cambias el flujo para que un pedido solo aparezca “Entregado” después de registrar evidencia.

Una petición de revisión útil para el agente podría ser:

```text
Revisa el cambio del estado de entrega.
Busca caminos que permitan marcarlo como Entregado sin evidencia.
Cita las líneas que justifican cada hallazgo.
Separa defectos probables de preguntas y sugerencias.
No cambies archivos ni inventes requisitos del negocio.
```

Si el agente propone permitir la entrega con una foto opcional, no la aceptes de inmediato: comprueba si la política del negocio permite que la evidencia sea opcional.

## 6. Protege el repositorio y sus datos
- No incluyas tokens, contraseñas, datos personales ni documentos confidenciales en el prompt sin autorización.
- Limita los permisos del agente a las acciones que realmente necesita.
- No permitas que el agente integre sus propios cambios sin revisión.
- Revisa código generado y comandos antes de ejecutarlos.
- Registra errores sin volcar información sensible.

La combinación Quarto + IA puede ahorrar trabajo: Quarto publica explicaciones y el agente revisa diferencias. También puede propagar errores con rapidez si nadie comprueba el resultado.

## 7. Cómo se conectan las dos fuentes
Las fuentes comparten una preocupación: mantener el conocimiento accesible mientras el sistema cambia.

- Quarto presenta la explicación para quien mantiene el sistema.
- El agente ayuda a examinar la propuesta de cambio.
- Las pruebas comprueban comportamiento.
- Tú confirmas que la explicación, la implementación y las pruebas describen la misma decisión.

Una documentación actualizada no valida automáticamente el código; una revisión de IA tampoco confirma que la documentación siga vigente.

## 8. Actividad de autoestudio
El servicio de seguimiento cambia su respuesta cuando el proveedor de geolocalización no está disponible. La pantalla ahora muestra el último estado confirmado y su hora.

1. Escribe qué sección de la documentación actualizarías.
2. Describe qué cambiaría en el archivo `.qmd`.
3. Escribe una instrucción para que un agente revise que el código no presente una ubicación antigua como actual.
4. Anota dos cosas que comprobarías manualmente después de la respuesta del agente.
5. Explica qué datos no incluirías en el prompt.

### Respuesta modelo
Actualizaría la página que describe el seguimiento y su comportamiento cuando falla Geolocalización. En Quarto escribiría que se conserva el último estado confirmado y se muestra su hora; después renderizaría el sitio y comprobaría el enlace a esa página.

Al agente le pediría buscar rutas que muestren la ubicación previa sin identificar su hora. Revisaría el código citado, consultaría el requisito y ejecutaría una prueba con el proveedor simulado como no disponible. No compartiría tokens ni ubicaciones reales de clientes o repartidores.

## Comprueba lo que aprendiste
1. ¿Qué archivo se debe editar: el `.qmd` o solo el sitio generado?
2. ¿Qué demuestra una observación de un agente de IA?
3. ¿Por qué debes renderizar y abrir el sitio después de editar?
4. ¿Qué responsabilidad no se puede delegar al agente?

### Respuestas
1. El `.qmd` es el archivo fuente; el sitio generado se vuelve a crear desde él.
2. Que existe una observación que merece verificarse, no que el defecto sea cierto.
3. Para comprobar que el resultado generado contiene texto, diagramas y enlaces correctos.
4. Decidir si el cambio cumple la necesidad del negocio y aprobarlo para integración.

## Conclusión
Quarto facilita publicar documentación desde archivos revisables. Un agente de IA puede ampliar la revisión de una Pull Request. El resultado solo es confiable cuando el alumno verifica la fuente, el sitio generado, las sugerencias, las pruebas y el tratamiento de datos.

## Actividad práctica
Continúa con la [Actividad 4: implementación e integración](video-18-1.md), donde aplicarás estas ideas al flujo de pedidos y entregas.