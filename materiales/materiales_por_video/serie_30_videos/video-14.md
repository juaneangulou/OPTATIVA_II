# Video 14: Cierre de fundamentos y transición

## Navegación
[⬅️ Video anterior: negociación e impacto social](video-13.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: método arquitectónico e IA](video-15.md)

## Para qué sirve esta transición
Este video no agrega otro patrón ni repite una clase de liderazgo. Funciona como un puente breve: convierte las preguntas de fundamentos en criterios para leer los videos aplicados que siguen.

La transición no significa dejar atrás los fundamentos. Significa usarlos para preguntar si una tecnología o patrón resuelve un problema del caso logístico y qué costo añade.

## 1. Recuerda el recorrido
En los fundamentos trabajaste preguntas como:

- ¿Qué problema del negocio necesita resolver el sistema?
- ¿Quién usa el sistema y quién puede verse afectado?
- ¿Qué condición debe seguir siendo verdadera?
- ¿Qué decisiones tienen consecuencias para operación, seguridad o evolución?
- ¿Cómo explicas por qué una alternativa conviene más que otra?

No tienes que memorizar nombres de patrones. Lo importante es poder volver a esas preguntas cuando aparece una propuesta técnica.

## 2. El puente hacia la plataforma logística
La empresa del caso no puede detener sus operaciones para reemplazar todo su sistema. Necesita mejorar pedidos, inventario y entregas mientras continúa atendiendo a clientes.

Antes de escoger herramientas, puedes resumir el problema:

> La empresa necesita consultar y coordinar pedidos y entregas con datos confiables, sin detener toda la operación ni exponer información de las personas.

Este resumen no es todavía una arquitectura. Es un punto de partida para estudiar una necesidad a la vez, comparar opciones y probarlas.

### Qué cambia a partir de aquí
En los siguientes videos dejarás de estudiar solamente la pregunta “¿qué debería decidir el equipo?” y empezarás a estudiar “¿cómo se organiza y se comprueba esa decisión en el software?”. Eso introduce nuevos niveles de detalle:

| Nivel | Pregunta | Evidencia esperada |
|---|---|---|
| Problema | ¿Qué necesita resolver la operación? | Descripción del caso y actores |
| Decisión | ¿Qué alternativa conviene dadas las restricciones? | Registro de decisión y trade-offs |
| Diseño | ¿Qué responsabilidades y límites tendrá el sistema? | Diagrama, contrato o modelo |
| Implementación | ¿Cómo se ejecuta el flujo? | Código, configuración o integración |
| Comprobación | ¿Cómo sabremos si funciona? | Prueba, métrica o experimento |

Una propuesta técnica es incompleta si solo responde al nivel de implementación. También debe explicar qué problema resuelve, qué costo acepta y qué evidencia permitirá revisarla.

## 3. Convierte una pregunta grande en una práctica pequeña
Una pregunta como “¿qué arquitectura necesita toda la empresa?” es demasiado amplia para empezar. Puedes acotarla:

1. Elige un flujo, por ejemplo consultar una entrega.
2. Identifica quién participa y qué información necesita.
3. Describe qué ocurre cuando todo funciona y cuando falla una dependencia.
4. Compara una solución simple con una alternativa de mayor complejidad.
5. Define qué prueba te permitiría aprender si la decisión funciona.

Así, cada patrón de los siguientes videos responde a una pregunta concreta en vez de convertirse en una receta para todo el sistema.

## 4. Ejemplo: decidir qué hacer ante una entrega demorada
**Necesidad:** el cliente quiere saber si su paquete sigue avanzando.

**Actores:** cliente, repartidor, soporte y operación.

**Condición importante:** no presentar una ubicación desconocida como si fuera actual.

**Alternativa sencilla:** mostrar el último estado confirmado y su hora.

**Alternativa de mayor alcance:** consultar ubicación en tiempo real y calcular una nueva hora estimada.

**Costo y riesgo:** la segunda alternativa requiere obtener más datos, proteger su acceso y manejar demoras del proveedor. Puede aportar más detalle, pero también aumenta dependencias.

**Comprobación:** simular que el proveedor de ubicación no responde y comprobar que el estado confirmado sigue disponible y que la pantalla indica qué información falta.

Este ejemplo demuestra el tipo de razonamiento que usarás en la parte aplicada: primero contexto y personas; después diseño y tecnología.

## 5. Caso completo: elegir una primera mejora
Supón que la plataforma recibe muchas consultas sobre entregas demoradas. El equipo propone tres alternativas:

| Alternativa | Beneficio | Costo inicial | Riesgo principal | Primera comprobación |
|---|---|---|---|---|
| A. Estado y hora del último cambio | Es simple y usa datos existentes | Bajo | Puede no explicar una demora reciente | Medir consultas después de mostrar la hora |
| B. Estado, estimación y ubicación aproximada | Reduce incertidumbre con más detalle | Medio | La estimación puede quedar desactualizada | Simular retrasos y proveedor no disponible |
| C. Ubicación exacta en tiempo real | Ofrece máximo detalle | Alto | Expone más datos y crea más dependencias | Revisar privacidad, latencia y consentimiento |

Una decisión razonable para el primer corte es comenzar con A. No porque sea la solución definitiva, sino porque permite aprender con poco costo. Si la evidencia demuestra que el cliente necesita más información, se puede experimentar con B bajo límites de acceso, retención y frescura.

### Cómo documentar esa decisión
Puedes escribirla así:

```text
Decisión: mostrar estado confirmado y hora de actualización antes de incorporar ubicación.
Contexto: soporte recibe consultas porque el cliente no sabe si el pedido sigue avanzando.
Alternativas: estado simple, ubicación aproximada activa y ubicación exacta continua.
Razón: la primera alternativa usa datos que ya existen y expone menos información personal.
Costo aceptado: algunas personas seguirán necesitando contactar a soporte.
Prueba: comparar consultas y reclamos durante dos semanas con la hora visible.
Revisión: evaluar la alternativa B si la incertidumbre continúa y la prueba de privacidad es favorable.
```

Este formato evita dos errores: presentar una preferencia como si fuera un hecho y convertir una decisión temporal en una regla permanente.

## 6. Cómo leer los videos aplicados
Para aprovechar cada capítulo siguiente, utiliza esta ficha mientras estudias:

1. **Problema:** escribe la situación que el patrón o herramienta intenta resolver.
2. **Límite:** indica qué parte del sistema no debe conocer o modificar esa solución.
3. **Flujo:** describe qué ocurre cuando la operación funciona.
4. **Falla:** describe qué ocurre si una dependencia tarda, rechaza o repite una operación.
5. **Costo:** anota qué complejidad de código, operación, datos o equipo se añade.
6. **Evidencia:** define una prueba, métrica o experimento que permita mantener o retirar la decisión.

Por ejemplo, al estudiar una cola de mensajes no basta con escribir “la cola desacopla servicios”. Debes preguntar qué pasa si el mensaje se duplica, quién revisa los mensajes fallidos, cuánto retraso acepta el negocio y cómo se demuestra que la cola mejora el problema original.

## 7. Errores frecuentes al pasar de fundamentos a aplicación

### Elegir la tecnología antes de formular el problema
“Usaremos microservicios” no explica qué necesidad existe. Empieza con una situación observable: una parte del sistema necesita escalar de forma independiente, un equipo requiere desplegar sin bloquear a otro o una falla no debe detener todo el flujo.

### Confundir más componentes con más arquitectura
Agregar colas, bases, servicios y herramientas puede producir un diagrama grande sin resolver el problema. La arquitectura también incluye decisiones de simplicidad, límites de operación y capacidad real del equipo.

### Confundir una prueba exitosa con una solución completa
Que una prueba pase demuestra una condición concreta. No demuestra que el sistema sea seguro, barato, mantenible y adecuado para todos los escenarios. Relaciona cada prueba con la afirmación que realmente verifica.

### Olvidar la operación
Una solución aplicada necesita saber quién la monitorea, qué ocurre durante una falla, cómo se recuperan los datos y qué señal indica que hay que intervenir. Si nadie puede operarla, el diseño no está terminado.

### Tratar las decisiones como irreversibles
Algunas decisiones cuestan poco cambiar; otras dejan datos, contratos o dependencias difíciles de retirar. Declara esa diferencia y diseña experimentos pequeños antes de comprometerte con una inversión grande.

## 8. Tu punto de partida para el bloque aplicado
Antes de estudiar cada herramienta, revisa si puedes explicar:

- qué necesidad concreta resolverías primero;
- qué actor recibe el beneficio y quién podría cargar con un riesgo;
- qué información sabes y cuál solo estás suponiendo;
- qué opción sencilla existe;
- qué evidencia te permitiría mantener o revisar la decisión.

Si una respuesta todavía es incierta, anótala como pregunta abierta. No hace falta inventar certeza para empezar a diseñar.

## 9. Actividad de autoestudio
Elige una situación de la plataforma: pedido duplicado, falta de inventario, entrega demorada o devolución.

1. Describe el problema en dos frases sin nombrar tecnología.
2. Nombra a las personas afectadas.
3. Escribe un hecho y una suposición.
4. Propón una solución pequeña que permita aprender.
5. Define qué comprobarías antes de ampliar la solución.
6. Escribe una pregunta que esperas resolver en el bloque aplicado.

7. Completa esta matriz:

| Elemento | Tu respuesta |
|---|---|
| Decisión que tomarías | |
| Alternativa más simple | |
| Costo que aceptarías | |
| Falla que debes manejar | |
| Evidencia de éxito | |
| Señal para revisar la decisión | |

8. Explica qué parte de tu solución podría retirarse o cambiarse más adelante sin rehacer todo el sistema.

### Respuesta modelo
“Algunos pedidos aparecen dos veces y el almacén puede preparar el mismo paquete más de una vez. El operador necesita saber cuál registro es el válido”.

Hecho del ejercicio: el sistema puede recibir más de una solicitud para la misma compra. Suposición: la duplicación se debe a que la persona pulsa dos veces; habría que revisar registros para confirmarlo.

Una primera solución podría reconocer una clave única del pedido y rechazar duplicados. Antes de ampliar el diseño, comprobaría con una prueba que dos solicitudes iguales no creen dos pedidos.

Pregunta para el bloque aplicado: ¿cómo distinguirías una repetición válida del mismo pedido de una compra nueva?

La matriz se completaría así: la decisión es rechazar una segunda creación con la misma clave de compra; la alternativa simple es una restricción única y una respuesta que devuelva el pedido existente; el costo es que el cliente debe conservar una clave estable; la falla a manejar es que dos solicitudes lleguen al mismo tiempo; la evidencia es que las solicitudes repetidas no creen dos pedidos; la señal de revisión es que existan compras legítimas que estén compartiendo la misma clave.

La solución puede evolucionar si la regla de deduplicación queda aislada detrás de una operación clara. No conviene empezar repartiendo el sistema en servicios solo para resolver este caso; primero hay que comprobar el volumen, la causa y la capacidad de la base de datos.

## 10. Comprueba tu comprensión
1. ¿Por qué el bloque aplicado sigue dependiendo de los fundamentos?
2. ¿Qué diferencia hay entre una necesidad y una tecnología?
3. ¿Qué haces cuando todavía no tienes evidencia suficiente?
4. ¿Qué cinco elementos debes registrar al evaluar una herramienta o patrón?
5. ¿Por qué una arquitectura aplicada debe incluir operación y pruebas?
6. ¿Qué diferencia hay entre una alternativa simple y una alternativa definitiva?

### Respuestas
1. Los fundamentos ayudan a elegir y evaluar tecnologías según el problema, los actores y los riesgos.
2. La necesidad describe lo que alguien requiere; la tecnología es una forma posible de resolverlo.
3. Registras la suposición o pregunta pendiente y defines cómo obtener evidencia.
4. Problema, límite, flujo, falla y costo; después defines la evidencia que los comprobará.
5. Porque una solución que no puede observarse, recuperarse o comprobarse puede fallar en producción aunque el diseño parezca correcto.
6. La alternativa simple permite aprender con menor costo; la definitiva solo debería elegirse cuando la evidencia justifica su complejidad.

## Cierre
El aprendizaje de arquitectura no termina con una lista de conceptos. Continúa cuando aplicas esos conceptos a situaciones reales, justificas decisiones y compruebas sus consecuencias.

En los siguientes videos llevarás los fundamentos a herramientas y prácticas concretas. Conserva esta secuencia: entender el problema, conocer a las personas afectadas, comparar opciones, decidir y comprobar.
