# Video 30: Cierre y defensa de la arquitectura

## Material de referencia
- [Caso base de la plataforma logística](../../caso_base_plataforma_logistica_compleja.md)
- [Actividad 5: pruebas, operación y defensa final](../../actividad_5_pruebas_operacion_y_defensa.md)
- [Video 30.1: actividad de pruebas, operación y defensa](video-30-1.md)

## Navegación
[⬅️ Video anterior: criterio y arquitectura responsable](video-29.md) | [📚 Índice de la serie](README.md)

## Para estudiar por tu cuenta
Este es el cierre del recorrido. No necesitas afirmar que el sistema es perfecto ni que todas sus partes están terminadas. Necesitas explicar qué resolviste, cómo funciona, qué evidencia tienes y qué limitaciones siguen pendientes.

Una **defensa arquitectónica** es una explicación que conecta el problema, las decisiones, sus costos y las pruebas. No es una lista de tecnologías ni una presentación de diagramas sin contexto.

## 1. Delimita qué construiste
La plataforma logística puede abarcar pedidos, inventario, pagos, rutas, notificaciones, devoluciones y soporte. Para el proyecto seleccionaste un alcance manejable.

Escribe:

- qué flujo sí implementaste;
- qué parte quedó fuera;
- qué actor puede usar la función;
- qué límite técnico o de tiempo influyó en el alcance.

Ejemplo: “Implementé registrar el pedido, comprobar inventario y mostrar su estado. Dejé fuera el cálculo automático de rutas porque no cuento todavía con datos de tráfico ni integración con un proveedor”.

Explicar lo que no hiciste evita que tu entrega prometa capacidades inexistentes.

## 2. Presenta el problema antes del diagrama
Empieza con la necesidad del usuario o de operación. Por ejemplo: soporte recibe muchas consultas porque el estado de las entregas no coincide entre almacén y cliente.

Después identifica:

1. quién reporta el problema;
2. quién recibe el impacto;
3. qué resultado necesita;
4. qué evidencia tienes de que el problema existe;
5. qué restricción limita la solución.

No empieces diciendo “elegí microservicios”, “usé CQRS” o “instalé una base de datos”. Esas son decisiones que vienen después de entender el problema.

## 3. Explica el recorrido más importante
Elige un flujo principal y síguelo desde la acción inicial hasta el resultado:

1. El cliente registra un pedido.
2. Pedidos valida los datos y consulta inventario.
3. El pedido se guarda si cumple las reglas.
4. Entregas recibe la información necesaria para preparar el envío.
5. El cliente consulta el estado confirmado.

En cada paso indica qué parte es responsable y qué información cruza. Si dibujas un diagrama, usa nombres comprensibles y explica sus flechas.

## 4. Muestra qué ocurre cuando algo falla
Un flujo no está completo si solo explica el camino exitoso. Elige una falla realista:

- no hay unidades disponibles;
- el servicio de rutas no responde;
- una tarea se recibe dos veces;
- un cliente intenta consultar el pedido de otra cuenta;
- se pierde la conexión después de enviar una solicitud.

Para la falla elegida explica:

1. qué sabe el sistema;
2. qué información no debe inventar;
3. qué respuesta recibe el usuario;
4. cómo se registra o investiga el incidente;
5. qué prueba demuestra el comportamiento.

## 5. Defiende dos decisiones importantes
Una decisión arquitectónica puede escribirse con esta estructura:

| Pregunta | Qué debes explicar |
|---|---|
| Problema | Qué necesidad o riesgo motivó la decisión |
| Alternativas | Qué opciones realistas comparaste |
| Elección | Qué opción usaste |
| Razón | Por qué encaja con el contexto actual |
| Costo aceptado | Qué complejidad, tiempo o riesgo añade |
| Evidencia | Qué prueba o medición respalda la decisión |
| Revisión | Qué señal te haría reconsiderarla |

### Ejemplo
**Problema:** tareas de entrega fallidas se pierden cuando el consumidor se reinicia.

**Alternativas:** registrar fallos manualmente o usar una cola separada para tareas que agotaron sus reintentos.

**Elección:** conservar las tareas fallidas en una DLQ con identificador y motivo.

**Costo aceptado:** se necesita monitorear y revisar esa cola.

**Evidencia:** una prueba induce un fallo repetido y verifica que la tarea queda disponible para investigación.

**Revisión:** reconsiderar la política si la cola acumula tareas que no pueden resolverse o el volumen supera la capacidad operativa.

Una respuesta puede elegir otra opción si explica el problema y demuestra por qué la alternativa encaja mejor.

## 6. Pruebas: qué afirmación demuestra cada una
No basta decir “las pruebas pasan”. Relaciona cada prueba con la regla que protege:

| Prueba o evidencia | Qué comprueba |
|---|---|
| Unit test de confirmación | El pedido no se confirma sin inventario suficiente |
| Prueba de integración | Pedido y líneas se guardan de manera coherente |
| Prueba de permisos | Una cuenta no consulta pedidos ajenos |
| Prueba de fallo de proveedor | El sistema conserva información útil si rutas no responde |
| Métrica o traza | El equipo puede detectar y localizar demoras |

Si una prueba no comprueba la afirmación, cambia la prueba o cambia lo que afirmas. No uses cobertura de código como sustituto de evidencia sobre comportamiento.

## 7. Evalúa riesgos sin exagerar
Escribe los riesgos que siguen abiertos y quién podría verse afectado. Por ejemplo:

| Riesgo pendiente | A quién afecta | Qué harías |
|---|---|---|
| La ubicación puede quedar desactualizada | Cliente y soporte | Mostrar hora de actualización y medir antigüedad |
| No se midieron picos grandes de pedidos | Operación y clientes | Hacer prueba de carga antes de ampliar el servicio |
| El proveedor externo puede fallar | Repartidor y cliente | Definir timeout, respuesta parcial y procedimiento de recuperación |

Reconocer un riesgo pendiente no debilita tu defensa. Ocultarlo sí debilita la confianza en el expediente.

## 8. Organiza el expediente para otra persona
Tu entrega debe poder revisarse sin que tengas que estar presente. Incluye enlaces y nombres claros para:

1. requisitos, actores y alcance;
2. diagrama actualizado;
3. decisiones y alternativas descartadas;
4. contratos y recorrido principal;
5. pruebas y resultados;
6. riesgos, observabilidad y recuperación;
7. cambios pendientes y siguiente paso;
8. video de sustentación.

La [Actividad 5](../../actividad_5_pruebas_operacion_y_defensa.md) indica que el repositorio debe incluir el trabajo final y que la sustentación debe entregarse mediante enlace. Revisa sus requisitos completos antes de enviar.

## 9. Guion breve para preparar tu defensa
Usa este orden para organizar tu propia presentación:

1. **Problema y alcance:** qué necesidad elegiste resolver.
2. **Personas afectadas:** quién usa la solución y quién podría recibir un riesgo.
3. **Arquitectura:** qué partes construiste y cómo se comunican.
4. **Decisiones:** dos elecciones con sus alternativas y costos.
5. **Evidencia:** qué pruebas ejecutaste y qué resultados obtuviste.
6. **Fallas y riesgos:** qué ocurre cuando una dependencia no responde.
7. **Evolución:** qué cambiarías con más tiempo o nueva evidencia.

Practica explicar cada término técnico con el ejemplo del pedido. Si solo puedes defender una elección repitiendo el nombre de un patrón, vuelve a conectarla con el problema que resuelve.

## 10. Actividad final de autoestudio
Completa tu expediente y graba una explicación de tu arquitectura. Antes de grabar, comprueba que puedas responder:

- ¿Qué problema resolviste y qué dejaste fuera?
- ¿Qué parte es responsable de cada dato y regla?
- ¿Qué alternativa descartaste y qué costo aceptaste?
- ¿Qué prueba demuestra una regla crítica?
- ¿Qué pasa cuando falla una dependencia?
- ¿Qué riesgo queda pendiente?
- ¿Qué dato nuevo te haría revisar una decisión?

### Respuesta modelo resumida
“El sistema registra pedidos y permite consultar el estado de una entrega. Pedidos mantiene la compra; Entregas mantiene el traslado. Elegí una aplicación modular porque el equipo y la carga actuales no justifican operar servicios separados. La prueba de permisos confirma que cada cliente consulta solo sus pedidos. Si el proveedor de ubicación falla, mostramos el último estado con su hora y señalamos que falta información. Aún falta medir el comportamiento con carga alta; realizaré esa prueba antes de ampliar el servicio”.

No copies esta respuesta como si describiera tu proyecto. Úsala para revisar si la tuya explica alcance, responsabilidades, motivos, evidencia y límites.

## Autoevaluación final
Marca “sí”, “parcialmente” o “todavía no”:

| Puedo… | Mi respuesta |
|---|---|
| explicar el problema sin comenzar por una tecnología | |
| dibujar el recorrido principal y nombrar las responsabilidades | |
| justificar dos decisiones con alternativas y costos | |
| vincular pruebas con reglas y riesgos concretos | |
| explicar una respuesta de fallo sin inventar datos | |
| reconocer riesgos pendientes y proponer un siguiente paso | |

Si respondiste “todavía no”, vuelve a la sección correspondiente y completa esa evidencia antes de cerrar el expediente.

## Conclusión
Defender una arquitectura significa mostrar un razonamiento comprobable, no afirmar que existe una solución perfecta. Deja el expediente en condiciones para que otra persona entienda qué construiste, por qué, qué probaste y qué falta aprender.