# Video 09: Observabilidad, seguridad y privacidad

## 📚 Lecturas de referencia: detectar sin exponer
- [Observabilidad y monitoreo de sistemas](https://platzi.com/cursos/fundamentos-arquitectura-software/como-funcionan-los-eventos-en-sistemas-d/)
- [Seguridad, datos sensibles y privacidad](https://platzi.com/cursos/fundamentos-arquitectura-software/costos-ocultos-de-los-microservicios/)

## 🔗 Del contrato de API a la operación responsable
[⬅️ Video anterior](video-08.md) | [➡️ Video siguiente](video-10.md)

## 🎯 El incidente que vamos a investigar
Un cliente informa que su pedido aparece como “en preparación” desde hace cuarenta minutos. Operaciones no sabe si falló inventario, ruteo, notificación o la API. Un desarrollador propone registrar el correo, la dirección completa y el token de acceso en cada log “para investigar más rápido”. Esa solución puede resolver un incidente y crear otro: exponer datos sensibles.

Hoy diseñaremos una observabilidad útil: suficiente para reconstruir el flujo, limitada para no revelar información que soporte no necesita ver.

## El flujo y sus señales
Cuando llega `POST /api/orders`, el sistema crea un `traceId`. Ese identificador acompaña la reserva de inventario, la estimación de ruta y la notificación. Soporte puede buscar el `traceId` y entender dónde se detuvo el pedido sin ver el correo ni la dirección exacta del cliente.

```csharp
logger.LogInformation(
    "Order {OrderId} moved to {Status}. Trace {TraceId}",
    order.Id,
    order.Status,
    Activity.Current?.TraceId);
```

## 🧩 Cómo leer el código de observabilidad en .NET

`logger` representa `ILogger<T>`, la abstracción de logging de .NET. La clase no decide si el registro termina en consola, Application Insights, OpenTelemetry o un archivo; esa configuración ocurre al iniciar la aplicación. Esto mantiene el código de negocio independiente del destino del log.

`LogInformation` registra un evento normal. Si hay una falla de Ruteo usaríamos `LogWarning` o `LogError` y pasaríamos la excepción para conservar el detalle técnico sin mostrarlo al cliente.

Los textos `{OrderId}`, `{Status}` y `{TraceId}` no son interpolación de cadenas. Son propiedades estructuradas: el sistema guarda cada valor con nombre. Por eso soporte puede buscar todos los registros de un pedido o construir una métrica por estado sin analizar texto libre.

`Activity.Current?.TraceId` obtiene el identificador de trazabilidad de la solicitud actual. El operador `?.` significa “si `Activity.Current` existe, toma su `TraceId`; si no existe, devuelve `null` sin lanzar una excepción”. Ese identificador conecta API, Inventario y Ruteo en una misma investigación.

Nunca coloques correo, dirección, token, contraseña o cuerpo HTTP completo dentro de las propiedades del log. Una traza debe explicar el comportamiento del sistema, no copiar datos privados del cliente.


El actor principal es **el equipo de soporte**. Necesita responder al cliente con información confiable. La regla es: **los registros deben permitir reconstruir el flujo sin almacenar secretos, tokens, direcciones completas ni datos personales innecesarios**.

## Qué observamos

| Señal | Pregunta que responde | Ejemplo |
|---|---|---|
| Log estructurado | ¿Qué transición ocurrió? | pedido confirmado, reserva rechazada |
| Métrica | ¿Con qué frecuencia ocurre? | porcentaje de rutas fallidas |
| Traza | ¿Dónde se demoró el flujo? | API -> Inventario -> Ruteo |
| Alerta | ¿Cuándo debemos intervenir? | p95 de ruteo supera 2 segundos |
| Auditoría | ¿Quién consultó datos sensibles? | operador consultó detalle de entrega |

## Dos opciones
### Opción A: registrar todo para depurar
Incluye cuerpos HTTP, correos, direcciones, tokens y respuestas externas. La investigación parece rápida, pero aumenta riesgo de fuga, incumplimiento y acceso innecesario.

### Opción B: observabilidad estructurada y minimizada
Usa `orderId`, `traceId`, tipo de error, duración, estado y dependencia afectada. Protege atributos sensibles con enmascaramiento y limita la auditoría a roles autorizados. Es más trabajo inicial, pero soporte obtiene señales útiles sin usar datos personales como herramienta de depuración.

Elijo B. Una traza útil no necesita conocer la vida privada del cliente.

## Preguntas y respuestas
### ¿Qué tan claro es el estado del sistema en producción?

Es claro si soporte puede seguir un pedido por `traceId` y ver en qué paso se detuvo. Si solo existen mensajes libres como “error inesperado”, el sistema no es observable. Lo comprobaría simulando una caída del proveedor de rutas y verificando que la traza muestra el error, la duración y el estado final.

### ¿Estoy monitoreando lo que importa?

Para este flujo, mediría confirmaciones exitosas, latencia p95 de Inventario y Ruteo, número de reintentos y pedidos estancados por más de diez minutos. No mediría solamente uso de CPU; esa métrica no le dice a operaciones si el cliente está esperando una entrega sin respuesta.

### ¿Qué datos sensibles maneja el sistema?

Correo, dirección, teléfono, ubicación y tokens de sesión. Cada uno necesita un propósito, un rol de acceso y una política de retención. En los logs usaría `orderId` y `traceId`; la consulta del detalle personal ocurre solo en el sistema autorizado y queda auditada.

### ¿Cómo reduzco exposición innecesaria?

No escribas cuerpos completos de solicitud en logs. Enmascara campos, elimina tokens, cifra datos en tránsito y restringe paneles de observabilidad por rol. Lo verifico con una prueba que revise los logs de un pedido y confirme que no contienen correo, dirección ni token.

## Actividad: investiga un pedido sin mirar datos privados

1. Define una secuencia de estados: `Created`, `InventoryReserved`, `RouteEstimated`, `Assigned`, `Failed`.
2. Agrega `traceId`, `orderId`, estado, duración y tipo de error a cada log.
3. Define tres métricas: porcentaje de pedidos confirmados, p95 de ruteo y pedidos estancados.
4. Crea una alerta cuando un pedido lleve más de diez minutos sin transición.
5. Escribe una lista de datos que no deben aparecer en logs: correo, dirección, teléfono, token y ubicación precisa.
6. Simula que Ruteo responde con timeout y documenta qué verá soporte.
7. Agrega una prueba automatizada que falle si un correo o token aparece en el registro.
8. Agrega una prueba de acceso denegado para comprobar que un usuario sin rol de soporte no puede abrir la traza detallada.

## Cómo comprobar que terminaste
Entrega una traza de ejemplo donde soporte identifica un timeout de Ruteo usando `traceId`. Entrega también el log enmascarado y la prueba que demuestra que los datos privados no están allí. Si puedes diagnosticar el incidente sin abrir información personal, la solución es correcta.

## Cierre
Observar no significa guardar todo. Significa tener las señales necesarias para actuar con rapidez y proteger a las personas mientras lo hacemos. En el siguiente video llevaremos esta disciplina a pruebas automatizadas, despliegue y entrega continua.
