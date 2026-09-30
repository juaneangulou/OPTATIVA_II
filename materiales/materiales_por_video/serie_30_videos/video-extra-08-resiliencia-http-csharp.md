# Video extra 8: Resiliencia HTTP en C#: timeout, reintento y circuit breaker

## Para estudiar por tu cuenta
El servicio de rutas puede responder tarde o dejar de responder. Si la API de Pedidos espera sin límite, puede agotar conexiones y afectar solicitudes que no dependen de Rutas.

En este capítulo aprenderás a establecer límites de espera y a reintentar solo cuando sea razonable. También reconocerás por qué los reintentos ingenuos pueden empeorar una caída.

## 1. Una llamada remota puede fallar
Una llamada HTTP puede fallar por conexión, DNS, timeout, respuesta del servidor o una condición del negocio. No todas las fallas tienen el mismo tratamiento.

- **Timeout:** cuánto tiempo espera una operación antes de cancelarla.
- **Reintento:** repetir una operación después de una falla considerada transitoria.
- **Circuit breaker:** dejar de enviar solicitudes temporalmente después de observar demasiadas fallas, permitiendo que el servicio remoto se recupere.
- **Fallback:** respuesta alternativa cuando la operación principal no está disponible. Debe conservar un significado válido para el negocio.

## 2. Propagar cancelación y limitar espera
```csharp
public sealed class RutasClient
{
    private readonly HttpClient _httpClient;

    public RutasClient(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<string> ConsultarRutaAsync(
        Guid entregaId,
        CancellationToken cancellationToken)
    {
        using var response = await _httpClient.GetAsync(
            $"api/entregas/{entregaId}/ruta",
            cancellationToken);

        response.EnsureSuccessStatusCode();
        return await response.Content.ReadAsStringAsync(cancellationToken);
    }
}
```

Configura un timeout con un valor basado en el presupuesto de latencia de la operación y propaga `CancellationToken`. No uses un tiempo arbitrario sin medir ni configures un timeout tan alto que agote los recursos esperando.

`HttpClient` debe gestionarse mediante `IHttpClientFactory` o una estrategia equivalente; crear y destruir uno por solicitud puede causar problemas de conexiones y resolución DNS.

## 3. Reintentar solo fallas que pueden recuperarse
Un reintento puede ayudar ante una interrupción breve o una respuesta transitoria. No arregla un identificador inválido ni una regla de negocio rechazada.

Antes de reintentar, pregunta:

1. ¿La falla es transitoria?
2. ¿La operación es segura de repetir?
3. ¿Cuántos intentos caben en el tiempo total permitido?
4. ¿El servicio remoto está saturado?

Lecturas GET suelen ser repetibles. Una solicitud que crea una entrega puede duplicar efectos; requiere una clave de idempotencia o una deduplicación en el servidor antes de reintentar.

## 4. Espera incremental y dispersión
Repetir inmediatamente muchas solicitudes produce una estampida. Los clientes pueden aumentar gradualmente el tiempo entre intentos y añadir una variación aleatoria, llamada **jitter**, para repartir la carga.

Un esquema conceptual:

```text
intento 1: espera corta
intento 2: espera mayor + jitter
intento 3: espera aún mayor + jitter
luego: devolver el error controlado
```

Limita el número de reintentos y el tiempo total. Respeta `Retry-After` cuando la API lo indique y la política de la aplicación lo permita.

## 5. Circuit breaker y fallback
Si el servicio de rutas falla repetidamente, el circuit breaker puede abrirse y rechazar llamadas rápidamente. Después de un periodo permite una solicitud de prueba; si funciona, vuelve a cerrar el circuito.

El fallback no debe inventar una ruta. Una alternativa segura podría ser mostrar “ruta temporalmente no disponible” o encolar una solicitud para procesamiento posterior, siempre que el flujo de negocio lo permita.

No registres como “éxito” un fallback que en realidad no completó la operación original. Métricas y logs deben diferenciar resultados reales y alternativos.

## 6. Evita amplificar una falla
Si diez instancias reintentan cada solicitud muchas veces, el servicio caído recibe aún más carga. Combina límites, backoff, circuit breaker, control de concurrencia y monitoreo. Alinea los reintentos con la política del dueño del servicio remoto.

Una política de reintento también puede estar configurada en varios niveles. Si cada capa reintenta, los intentos se multiplican. Define una sola estrategia coherente por operación.

## 7. Actividad de autoestudio
Tu cliente crea una entrega mediante POST. El servidor registra la entrega, pero la respuesta se pierde por timeout.

1. ¿Por qué repetir sin protección es peligroso?
2. ¿Qué clave enviarías para detectar la misma solicitud?
3. ¿Qué información debe guardar el servidor para deduplicar?
4. ¿Qué comportamiento mostrarías cuando el circuito está abierto?
5. ¿Cómo medirías si la política ayuda o amplifica fallas?

### Respuesta modelo
El primer intento quizá sí creó la entrega. Repetir podría crear una segunda. El cliente envía una clave de idempotencia estable para esa operación; el servidor conserva la clave y el resultado asociado, y responde de forma consistente al duplicado. Con el circuito abierto puede informar indisponibilidad temporal o encolar si el negocio lo admite. Se miden latencia, tasas de error, intentos por solicitud, circuitos abiertos y duplicados.

## Comprueba lo que aprendiste
1. ¿Qué problema resuelve un timeout?
2. ¿Cuándo es riesgoso reintentar?
3. ¿Qué hace un circuit breaker?
4. ¿Por qué un fallback debe ser honesto?

### Respuestas
1. Evita esperar indefinidamente y ayuda a limitar recursos ocupados.
2. Cuando la operación puede haber producido un efecto y no es idempotente.
3. Detiene temporalmente llamadas a un destino que falla repetidamente.
4. El cliente no debe creer que una operación se completó si solo se ofreció una alternativa.

## Cierre
La resiliencia consiste en fallar de manera controlada, no en ocultar fallas. Usa timeouts, reintentos acotados e idempotencia coordinados con el presupuesto de la operación y las capacidades del servicio remoto.
