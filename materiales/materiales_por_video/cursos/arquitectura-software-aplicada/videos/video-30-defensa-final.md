# Video 30: Cierre y defensa final de la arquitectura

## Para estudiar por tu cuenta
Este video cierra el recorrido del curso. No necesitas aprender otro patrón: vas a reunir lo que ya trabajaste para explicar una arquitectura, mostrar qué evidencia la respalda y reconocer qué falta mejorar.

La defensa no consiste en afirmar que el sistema es perfecto. Consiste en demostrar que entendiste el problema, elegiste una solución razonada, la probaste y sabes cuáles son sus límites.

## 1. El caso que vas a defender
Usa la plataforma de gestión logística de última milla del curso. La empresa necesita registrar pedidos, revisar inventario, organizar rutas, informar a los clientes y atender entregas fallidas, pero no puede detener toda la operación para reescribir sus sistemas.

El caso incluye distintos actores: clientes, operadores de tienda, almacén, repartidores, soporte y servicios externos. No tienes que construir toda la plataforma completa para esta defensa. Debes explicar qué alcance resolviste, qué dejaste fuera y por qué.

Puedes consultar el [caso base de la plataforma logística](../../../../caso_base_plataforma_logistica_compleja.md) y la [Actividad 5: pruebas, operación y defensa final](../../../../actividad_5_pruebas_operacion_y_defensa.md).

## 2. ¿Qué significa defender una arquitectura?
Defender una arquitectura es explicar una decisión con razones que otra persona pueda revisar. Para cada decisión importante debes poder responder:

- ¿Qué problema intentaba resolver?
- ¿Qué alternativas consideraste?
- ¿Por qué elegiste esta opción en este contexto?
- ¿Qué costo o riesgo aceptaste?
- ¿Qué prueba o evidencia muestra que funciona?
- ¿Qué dato te haría cambiar la decisión?

Una respuesta como “usé microservicios porque son escalables” no demuestra el razonamiento. Una explicación más clara identifica qué necesidad de crecimiento existe, cómo se comprobó y qué costo operativo se acepta.

## 3. Arma el expediente en orden
Un **expediente arquitectónico** es el conjunto organizado de documentos y pruebas que explican cómo diseñaste y verificaste tu solución. No es una carpeta de archivos sin explicación: cada elemento debe responder una pregunta del proyecto.

### Parte A: problema, actores y alcance
Escribe:

1. Qué problema de la operación logística resuelve tu versión.
2. Quiénes usan o reciben el impacto del sistema.
3. Qué funciones incluiste en tu primera versión.
4. Qué funciones dejaste fuera y por qué.

**Ejemplo:** “La primera versión permite registrar un pedido, confirmar disponibilidad y consultar su estado. No optimiza rutas automáticamente; esa capacidad requiere datos de tráfico que todavía no tenemos”.

### Parte B: necesidades y condiciones de calidad
Además de decir qué funciones existen, explica cómo deben comportarse. Estas condiciones se llaman **requisitos de calidad**: por ejemplo, proteger datos personales, permitir que soporte investigue una entrega fallida o mostrar el estado sin demoras excesivas.

Elige dos o tres condiciones importantes. Para cada una escribe cómo podrías comprobarla. Si estableces un tiempo o cantidad, aclara que es un objetivo del proyecto y explica por qué lo elegiste; no existe un número universal que sirva para todos.

| Necesidad | Cómo se comprobaría |
|---|---|
| Un cliente no debe consultar el pedido de otra persona | Prueba con dos cuentas y pedidos ficticios |
| Una entrega no se marca como completada sin evidencia | Prueba de la regla de entrega |
| Soporte debe poder investigar un fallo de asignación | Registro asociado al identificador del pedido, sin exponer datos innecesarios |

### Parte C: modelo y responsabilidades
Muestra las partes principales del sistema y el trabajo de cada una. Puedes incluir contextos como Compras y Pedidos, Inventario, Entregas y Notificaciones.

Para cada parte responde:

- ¿Qué dato conoce y mantiene?
- ¿Qué decisión le corresponde?
- ¿Qué información comparte con las demás?
- ¿Qué no debería decidir por ellas?

Dibuja las conexiones necesarias. Evita poner una caja que “hace todo”. Si usas microservicios, explica qué necesidad justifica operarlos por separado; no los incluyas solo por moda.

### Parte D: recorrido de un caso completo
Elige un flujo importante, como confirmar y entregar el pedido 245. Describe paso a paso qué ocurre cuando todo funciona y qué pasa si algo falla.

| Paso | Acción | Evidencia o resultado esperado |
|---|---|---|
| Se registra el pedido | Se valida la información necesaria | El pedido queda identificado |
| Se revisa inventario | Se confirma o rechaza la disponibilidad | No se promete una unidad inexistente |
| Se prepara la entrega | Se asigna un repartidor | Queda registro de quién asumió la tarea |
| Se actualiza el seguimiento | Se comunica el estado | El cliente ve información confirmada |
| Ocurre una falla | Se registra y se decide reintentar o revisar | El pedido no desaparece ni se marca como entregado sin evidencia |

Tu flujo debe mostrar al menos un caso de error. Una arquitectura se entiende mejor cuando explicas qué hace si falta información o un servicio no responde.

### Parte E: pruebas y evidencia
Según el alcance del proyecto, reúne:

- **Pruebas unitarias:** comprueban una regla sin iniciar todo el sistema.
- **Pruebas de integración:** comprueban que varias partes colaboran correctamente.
- **Pruebas de seguridad:** comprueban permisos y manejo de datos.
- **Evidencia de operación:** logs, métricas o trazas útiles para investigar un problema.
- **Resultados:** qué pasó al ejecutar cada prueba y qué corregiste.

Una captura que dice “pasó” vale menos si no explicas qué se probó y qué riesgo cubre. Indica qué condición revisaste y qué resultado observaste.

### Parte F: decisiones y costos
Elige dos decisiones arquitectónicas importantes y documenta cada una con este formato:

1. **Situación:** ¿qué problema o necesidad había?
2. **Opciones:** ¿qué alternativas reales comparaste?
3. **Elección:** ¿qué decidiste?
4. **Razón:** ¿por qué esta opción encaja con el caso?
5. **Costo aceptado:** ¿qué dificultad, gasto o riesgo introduce?
6. **Verificación:** ¿qué prueba o medida observarás?
7. **Revisión:** ¿qué señal te haría cambiarla?

Una decisión puede ser mantener una aplicación modular en lugar de separarla en servicios, usar una DLQ para tareas que fallan, o conservar el historial de cambios de una entrega. No hay que documentar cada detalle técnico, solo lo que cambia significativamente el diseño o el riesgo.

## 4. Ejemplo de decisión defendida
**Situación:** las entregas pueden tardar si el servicio de rutas se encuentra temporalmente fuera de servicio.

**Opciones:** esperar indefinidamente, devolver error para toda la pantalla o mostrar el estado confirmado del pedido y señalar que la ubicación no está disponible.

**Elección:** mostrar el estado confirmado y explicar qué dato falta.

**Razón:** el cliente conserva información útil sin recibir una ubicación inventada.

**Costo aceptado:** la pantalla debe presentar resultados parciales y el equipo debe manejar una respuesta distinta cuando rutas no responde.

**Verificación:** simular una falla de rutas y comprobar que el estado del pedido sigue visible, que la ubicación se identifica como no disponible y que la consulta no queda esperando indefinidamente.

**Revisión:** revisar la decisión si el producto exige una ubicación actualizada para permitir una acción crítica.

Esta explicación puede evaluarse porque conecta necesidad, alternativas, costo y evidencia; no porque use palabras complejas.

## 5. Riesgos que debes declarar
No presentes el sistema como si no tuviera riesgos. Describe los más importantes y qué haces frente a ellos.

| Riesgo | Consecuencia posible | Respuesta o mitigación |
|---|---|---|
| Un repartidor no tiene conexión | La ubicación puede quedar desactualizada | Mostrar cuándo se recibió la última actualización |
| Un servicio externo no responde | El pedido se demora | Reintentar de manera limitada y conservar la tarea para revisión |
| Una cuenta consulta un pedido ajeno | Se exponen datos personales | Verificar permisos en el servidor y probarlos |
| Un mensaje se procesa dos veces | Puede crearse una asignación duplicada | Identificar tareas repetidas y evitar efectos duplicados |

Un riesgo mitigado no desaparece necesariamente. Explica qué queda pendiente y quién lo atendería.

## 6. Cómo organizar la sustentación
Prepara una explicación breve y ordenada. Puedes usar diapositivas o una demostración, pero cada pantalla debe apoyar una idea concreta.

1. **Problema y alcance:** qué necesidad elegiste resolver y qué dejaste fuera.
2. **Recorrido principal:** muestra cómo una solicitud atraviesa el sistema.
3. **Decisiones:** explica dos elecciones y las alternativas que descartaste.
4. **Pruebas:** muestra qué comprobaste, por qué y qué resultado obtuviste.
5. **Fallas y riesgos:** explica cómo responde la solución cuando una dependencia falla.
6. **Próximo paso:** nombra una mejora que priorizarías con nueva evidencia.

Evita dedicar toda la presentación a enumerar tecnologías. Quien escucha necesita entender qué problema resuelven y qué evidencia tienes.

## 7. Actividad final: prepara tu defensa
Crea una carpeta o documento de expediente con estas secciones:

1. Resumen del problema, actores y alcance.
2. Diagrama de contexto o componentes con responsabilidades.
3. Recorrido funcional, incluyendo al menos una falla.
4. Dos decisiones con alternativas, costos y condiciones de revisión.
5. Evidencia de pruebas unitarias e integración pertinentes.
6. Riesgos de operación, seguridad y datos.
7. Plan de evolución: qué harías después y qué evidencia justificaría esa prioridad.
8. Guion o grabación de sustentación y enlace con permisos de acceso.

### Pistas para revisar tu propio expediente
- ¿Una persona que no participó en el proyecto puede seguir el flujo?
- ¿Se entiende quién es responsable de cada dato y decisión?
- ¿Cada afirmación de calidad tiene alguna forma de comprobarse?
- ¿Explicaste una falla realista y la respuesta del sistema?
- ¿Nombraste los costos que aceptas?
- ¿Tu siguiente paso responde a una necesidad o solo agrega tecnología?

## 8. Lista de comprobación final
Antes de entregar, verifica:

- El repositorio contiene código, documentación y pruebas relevantes.
- Se explica qué cubre cada prueba y qué resultado tuvo.
- Hay al menos un riesgo operativo y uno de seguridad documentados.
- El recorrido principal muestra una respuesta ante fallos.
- Las decisiones incluyen alternativas y costos.
- El expediente indica qué queda fuera y qué se haría después.
- El video de sustentación tiene un enlace accesible; no adjuntes el archivo de video al repositorio si la Actividad 5 pide entregar solo el enlace.
- No se han publicado contraseñas, claves ni datos personales reales.

## 9. Autoevaluación
Marca “sí”, “parcialmente” o “todavía no” y corrige antes de cerrar:

| Pregunta | Mi respuesta |
|---|---|
| Puedo explicar el problema sin empezar por una tecnología | |
| Puedo dibujar cómo una solicitud atraviesa el sistema | |
| Puedo explicar qué hace cada componente y qué no hace | |
| Puedo mostrar evidencia de que una regla crítica funciona | |
| Puedo explicar qué ocurre cuando una dependencia falla | |
| Puedo nombrar el costo y el riesgo de mis decisiones | |
| Puedo decir qué evidencia me haría revisar una elección | |

No necesitas responder “sí” a todo para que el proyecto sea honesto. Sí necesitas distinguir lo demostrado de lo pendiente.

## Cierre del curso
Una arquitectura defendible no es la más grande ni la que usa más patrones. Es una solución cuyo propósito se entiende, cuyos límites están escritos y cuyos comportamientos importantes se han comprobado.

Al cerrar el expediente, deja a la siguiente persona suficiente contexto para continuar: qué problema resolviste, por qué elegiste ese camino, qué riesgos aceptaste y qué señales observarías para evolucionarlo. Esa claridad es parte del resultado técnico.
