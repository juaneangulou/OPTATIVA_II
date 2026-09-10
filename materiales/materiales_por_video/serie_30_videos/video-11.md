# Video 11: Evolución, riesgos y costos

## 📚 Lecturas de referencia: cambiar sin destruir
- [Estructura de software y evolución del sistema](https://platzi.com/cursos/fundamentos-arquitectura-software/patrones-de-software-para-arquitectos/)
- [Riesgos, costos y decisiones bajo incertidumbre](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitectura-mvp-de-telegram-a-remarkabl/)

## 🔗 De la entrega automatizada a las decisiones reversibles
[⬅️ Video anterior](video-10.md) | [➡️ Video siguiente](video-12.md)

## 🎯 La situación que vamos a decidir
El algoritmo actual de rutas funciona para el volumen del MVP, pero el negocio quiere agregar entregas con ventanas de horario, múltiples bodegas y restricciones de vehículos. El equipo tiene dos impulsos peligrosos: reescribir todo inmediatamente o continuar agregando condiciones hasta que nadie pueda entender el código.

La pregunta correcta es: ¿qué parte del cambio debemos aislar ahora y qué evidencia necesitamos antes de invertir en una transformación mayor?

## Registro de riesgos

| Riesgo | Probabilidad | Impacto | Señal temprana | Respuesta |
|---|---:|---:|---|---|
| El cálculo de rutas no soporta ventanas horarias | Media | Alto | p95 supera 3 s | Experimento con datos reales |
| Una reescritura interrumpe entregas | Media | Muy alto | errores en piloto | Migración gradual |
| El proveedor de mapas aumenta precio | Media | Medio | cambio de tarifa | Adaptador y segundo proveedor |
| El equipo no puede operar servicios nuevos | Alta | Alto | alertas sin atender | Mantener monolito modular |

No todos los riesgos se resuelven escribiendo código. Algunos se reducen con una medición, una prueba, un contrato o una decisión de alcance.

## Dos decisiones posibles
### Opción A: reescribir el motor de rutas ahora
Promete una solución más limpia y preparada para crecer, pero concentra el riesgo en un proyecto largo. Mientras se reescribe, el negocio sigue necesitando entregas; además, podríamos descubrir tarde que nuestras suposiciones sobre volumen y ventanas eran incorrectas.

### Opción B: introducir una política nueva detrás de una interfaz
Conservamos el flujo actual, definimos `IRoutingPolicy` y probamos una implementación para ventanas horarias con una muestra de pedidos. Si el experimento demuestra valor, activamos la política gradualmente; si falla, retiramos el cambio sin perder todo el sistema.

```csharp
public interface IRoutingPolicy
{
    RoutePlan BuildPlan(IReadOnlyList<Delivery> deliveries, RoutingContext context);
}

public sealed class CurrentRoutingPolicy : IRoutingPolicy
{
    public RoutePlan BuildPlan(
        IReadOnlyList<Delivery> deliveries,
        RoutingContext context)
    {
        return RoutePlan.FromNearestStop(deliveries);
    }
}
```

La interfaz es una decisión reversible: permite probar una política nueva sin destruir la actual. El costo es mantener dos implementaciones durante un tiempo, pero el riesgo queda limitado a un experimento.

## Cómo evaluar la decisión
Antes de activar la nueva política, mediremos:

- tiempo de cálculo p50 y p95,
- porcentaje de entregas dentro de la ventana,
- kilómetros recorridos,
- reasignaciones manuales,
- errores del proveedor de mapas,
- costo por entrega.

La decisión se revisa si la nueva política mejora puntualidad sin multiplicar costo y complejidad. Si no aporta valor, la retiramos. Diseñar para evolución significa aceptar que una hipótesis puede ser descartada.

## Qué decisión es reversible y cuál no
Cambiar la implementación de `IRoutingPolicy` es relativamente reversible: podemos apagar la política nueva y conservar el contrato del caso de uso. Cambiar el modelo de datos de todos los pedidos, migrar cientos de millones de registros o repartir el flujo en varios servicios es mucho más costoso de deshacer.

Por eso, antes de tomar una decisión irreversible, quiero que me respondas cuatro preguntas:

1. ¿Qué evidencia todavía nos falta?
2. ¿Podemos probar la hipótesis con una muestra pequeña?
3. ¿Qué costo tendría retirar la decisión?
4. ¿Qué señal concreta nos obligaría a continuar, detenernos o cambiar de dirección?

La arquitectura madura no intenta eliminar toda la incertidumbre. La convierte en experimentos pequeños, fechas de revisión y límites de pérdida aceptables.

## Matriz de decisión

| Alternativa | Aprendizaje | Costo inicial | Costo de retirarla | Riesgo operativo | Decisión |
|---|---:|---:|---:|---:|---|
| Reescribir todo el motor | Bajo al inicio | Muy alto | Muy alto | Alto | No ahora |
| Nueva política detrás de interfaz | Alto | Medio | Bajo | Bajo | Experimentar |
| Agregar condiciones al motor actual | Bajo | Bajo | Medio | Medio | Solo temporal |

La elección de la política intercambiable gana porque nos permite aprender sin comprometer todo el producto. Esa es una decisión arquitectónica, aunque todavía no hayamos creado un microservicio.

## Preguntas y respuestas
### ¿Qué parte del sistema está más rígida?

El motor de rutas es rígido si cualquier nueva regla exige modificar el flujo de pedidos, persistencia y notificaciones. La solución es aislar la política detrás de `IRoutingPolicy` y medir el cambio con un experimento.

### ¿Qué decisión se está tomando con incertidumbre?

No sabemos todavía si el volumen y las ventanas horarias justifican una reescritura. Por eso no la aprobamos por intuición: probamos una política acotada, definimos métricas y dejamos una condición explícita de continuación o retiro.

### ¿Qué tan reversible es la opción elegida?

La opción de una política intercambiable es más reversible que una reescritura. Podemos retirar `CurrentRoutingPolicy` o `TimeWindowRoutingPolicy` sin cambiar el contrato del caso de uso.

## Actividad: construye una decisión bajo incertidumbre

1. Elige un cambio del caso logístico: ventanas horarias, múltiples bodegas o segundo proveedor de mapas.
2. Registra tres riesgos con probabilidad, impacto y señal temprana.
3. Propón una opción de reescritura y otra incremental.
4. Define qué parte puede aislarse detrás de una interfaz.
5. Especifica un experimento de máximo una semana y sus métricas.
6. Escribe un ADR con la decisión reversible y la condición de revisión.
7. Presenta qué harías si la evidencia contradice tu hipótesis inicial.

### Entrega modelo

**Hipótesis:** una política de rutas con ventanas horarias reducirá entregas tardías sin aumentar más del 10% los kilómetros recorridos.

**Experimento:** ejecutar la política nueva con el 5% de las entregas durante cinco días, sin cambiar el flujo principal.

**Métricas:** puntualidad, kilómetros por pedido, tiempo p95 de cálculo, reasignaciones manuales y errores del proveedor.

**Regla de decisión:** continuar si la puntualidad mejora al menos 15% y el costo por entrega no aumenta más del 10%; retirar si la latencia o los errores superan el umbral acordado.

**Riesgo aceptado:** mantener temporalmente dos políticas y aumentar el esfuerzo de prueba. El riesgo queda limitado porque la activación puede apagarse sin migrar todo el sistema.

## Cierre
La arquitectura madura no promete acertar siempre. Promete que el costo de aprender no será destructivo. En el siguiente video convertiremos estas decisiones en una estrategia y un roadmap que el equipo pueda ejecutar.
