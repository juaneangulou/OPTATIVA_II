# Video 07: Monolitos, sistemas distribuidos y microservicios

## 📚 Lecturas de referencia: elegir la estructura correcta
- [Monolito vs arquitectura distribuida](https://platzi.com/cursos/fundamentos-arquitectura-software/como-elegir-un-estilo-arquitectonico-sin/)
- [Microservicios y organización por dominios](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitectura-cliente-servidor-fundamento/)

## 🔗 De límites de contexto a decisiones de despliegue
[⬅️ Video anterior](video-06.md) | [➡️ Video siguiente](video-08.md)

## 🎯 El problema que vamos a decidir
Ya definimos Pedidos, Inventario, Ruteo y Entregas como contextos distintos. Ahora viene una pregunta que muchos equipos contestan demasiado pronto: ¿debemos convertir cada contexto en un microservicio? La respuesta no es automática. Un límite de dominio no obliga a tener un despliegue independiente.

## Escena: la campaña de viernes negro
La plataforma anuncia entregas en menos de dos horas. Durante la campaña, el tráfico de consultas de rutas se multiplica por veinte, pero la creación de pedidos y la reserva de inventario siguen dentro de su volumen normal. El equipo observa que el cálculo de rutas consume CPU y demora las confirmaciones de pedido.

El director de tecnología propone: “separemos todo en microservicios este fin de semana”. El equipo debe frenar y preguntar: ¿qué problema queremos resolver exactamente?, ¿qué módulo necesita escalar?, ¿tenemos monitoreo, despliegue automático y contratos estables para operar servicios separados?

## Opción A: monolito modular bien protegido
Pedidos, Inventario, Ruteo y Entregas siguen desplegándose juntos, pero cada módulo conserva sus contratos internos y dependencias controladas. Para la campaña, se optimiza el cálculo de rutas con caché y una cola de solicitudes. Esta opción mantiene un solo despliegue, una base operativa más simple y menos fallos de red.

**Cuándo es suficiente:** cuando el equipo es pequeño, los módulos cambian juntos, el volumen todavía cabe en una aplicación escalada horizontalmente y no hay evidencia de que otro módulo necesite autonomía real.

## Opción B: extraer Ruteo como servicio independiente
Ruteo se convierte en un servicio porque tiene un perfil de carga distinto, puede escalar por separado y usa un proveedor externo de mapas. Pedidos conserva un contrato `IRouteEstimator`; la comunicación se protege con timeout, reintentos y observabilidad. Esta opción evita que una campaña de rutas degrade la confirmación de pedidos, pero agrega despliegues, fallos de red, monitoreo distribuido y gobierno de contratos.

**Cuándo vale la pena:** cuando la métrica confirma que Ruteo es el cuello de botella, un equipo puede mantenerlo, existe automatización de entrega y la separación reduce un riesgo mayor que el costo operativo que introduce.

## La decisión para este caso
No separaría los cuatro contextos. Extraería solamente Ruteo de forma gradual si se cumplen tres señales durante dos campañas:

1. El percentil 95 de cálculo de rutas supera el objetivo acordado y bloquea la confirmación de pedidos.
2. Ruteo necesita desplegar cambios con una frecuencia distinta a Pedidos e Inventario.
3. El equipo ya puede observar trazas, errores, reintentos y despliegues de un servicio sin depender de intervención manual.

Hasta que esas señales existan, elegiría monolito modular, caché para rutas y una cola de trabajo. Esta no es una decisión conservadora por miedo: es una decisión proporcional al problema actual.

## Un contrato que permite extraer Ruteo después
```csharp
public interface IRouteEstimator
{
    Task<RouteEstimate> EstimateAsync(RouteRequest request, CancellationToken cancellationToken);
}

public sealed record RouteRequest(string Origin, string Destination);
public sealed record RouteEstimate(decimal DistanceKm, TimeSpan Eta, bool IsViable);
```

Mientras la interfaz se mantenga estable, hoy puede implementarla un módulo interno y mañana un cliente HTTP hacia un servicio de Ruteo. El caso de uso de Pedidos no necesita saber cuándo ocurre esa extracción.

## Preguntas y respuestas
### ¿Mi sistema necesita más desacople o más simplicidad?

Hoy necesita simplicidad con límites claros. Pedidos e Inventario cambian juntos y no presentan saturación; separarlos agregaría llamadas remotas y coordinación sin resolver un cuello de botella. Ruteo, en cambio, es candidato a aislamiento porque su carga y dependencia externa son distintas.

### ¿Estoy adoptando microservicios por moda o por necesidad real?

Es necesidad real solo cuando puedes señalar una métrica, un equipo responsable y un ciclo de despliegue que mejoran con la separación. Decir “Netflix usa microservicios” no responde a la campaña de nuestra plataforma ni cubre el costo de operar fallos distribuidos.

### ¿La separación refleja el dominio del negocio?

Sí, si Ruteo conserva su lenguaje, reglas y responsabilidad: estimar viabilidad, distancia y tiempo. No sería una buena separación crear un servicio “utilidades” o dividir por tablas de base de datos; eso transfiere el acoplamiento de código a la red.

### ¿Qué costo operativo aceptamos al extraer Ruteo?

Aceptamos monitorear latencia entre servicios, versionar contratos, tratar timeouts, reintentos y fallos parciales. Lo aceptamos solo si la degradación actual de pedidos durante la campaña cuesta más que operar esas capacidades.

## Actividad: decide si extraerías Ruteo

1. Dibuja el monolito modular actual con Pedidos, Inventario, Ruteo y Entregas.
2. Registra tres métricas hipotéticas de campaña: solicitudes por minuto, percentil 95 de Ruteo y errores de confirmación de pedido.
3. Define un objetivo: por ejemplo, confirmar el 95% de pedidos en menos de dos segundos.
4. Explica qué dato demostraría que Ruteo debe escalar de forma independiente.
5. Diseña el contrato `IRouteEstimator` y define timeout, reintento y respuesta cuando Ruteo no esté disponible.
6. Escribe un ADR: mantener monolito modular ahora o extraer Ruteo; incluye la condición de revisión.
7. Presenta el costo operativo de ambas opciones: despliegue, observabilidad, incidentes y coordinación de equipos.

## Cómo comprobar que la actividad está resuelta
Tu decisión es defendible si otra persona puede identificar el cuello de botella, leer la métrica que justifica la separación, entender el contrato y saber qué ocurrirá cuando Ruteo falle. Si la única razón para separar es “queremos microservicios”, la actividad aún no está resuelta.

## Cierre
Los microservicios no son el siguiente nivel natural de un monolito. Son una herramienta costosa para problemas concretos de autonomía, escala y organización. En el siguiente video trabajaremos contratos e infraestructura para que, cuando una separación sea necesaria, no rompa a quienes dependen del sistema.
