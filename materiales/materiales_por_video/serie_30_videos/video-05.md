# Video 05: Principios de diseño, acoplamiento y cohesión

## 📚 Lecturas de referencia: diseño y calidad estructural
- [Fundamentos de diseño y principios de arquitectura](https://platzi.com/cursos/fundamentos-arquitectura-software/costo-total-de-operacion-en-arquitectura/)
- [Acoplamiento, cohesión y calidad estructural](https://platzi.com/cursos/fundamentos-arquitectura-software/alineacion-de-arquitectura-de-software-c/)

## 🔗 Del caso de privacidad al código
[⬅️ Video anterior](video-04.md) | [➡️ Video siguiente](video-06.md)

## 🎯 El objetivo del refactor
En esta clase vamos a dejar de hablar de “código limpio” como una frase bonita. Vas a ver una clase que intenta hacer demasiado, identificarás por qué es frágil y la convertirás en componentes que cambian por razones distintas. El objetivo no es tener más archivos: es lograr que una regla de rutas no obligue a modificar pagos, notificaciones y acceso a datos al mismo tiempo.

## El problema: una clase que conoce todo
En la plataforma logística, alguien creó `OrderService`. Con el tiempo le agregaron validación de pedidos, cálculo de rutas, descuento de inventario, guardado en base de datos y envío de correos. La clase funciona hoy, pero cada cambio se vuelve riesgoso: una modificación en la ruta puede romper una notificación; una falla de correo puede impedir que se guarde el pedido.

Esto es baja cohesión: una clase contiene responsabilidades que no pertenecen juntas. También es alto acoplamiento: la lógica de negocio conoce detalles de mapas, base de datos y correo. Las fuentes nos dan dos criterios para corregirlo: separar responsabilidades y reducir dependencias innecesarias.

## Antes del refactor
```csharp
public class OrderService
{
    public void Create(string customerEmail, decimal total, string address)
    {
        if (total <= 0) throw new ArgumentException("Total inválido");

        var route = new MapsClient().Calculate(address);
        new SqlOrderRepository().Save(customerEmail, total, route.Distance);
        new EmailSender().Send(customerEmail, "Pedido creado");
    }
}
```

Te pregunto: ¿cuántas razones tiene esta clase para cambiar? Si cambia la regla de total, el proveedor de mapas, la base de datos o el correo, debemos modificarla. Ese es el síntoma; no necesitamos medirlo con una fórmula para reconocer el peligro.

## Dos formas de resolverlo
### Opción A: mantener `OrderService` y agregar más condiciones
Es la solución rápida. Podemos agregar `if`, `try/catch` y más métodos privados. El costo es que la clase seguirá teniendo muchas responsabilidades y cada prueba necesitará infraestructura real o mocks complejos.

### Opción B: separar el caso de uso de sus dependencias
El caso de uso conserva la regla de crear un pedido. Un puerto calcula rutas, otro guarda pedidos y otro notifica. Cada componente tiene una razón clara para cambiar.

```csharp
public interface IRouteEstimator
{
    Task<RouteEstimate> EstimateAsync(string address);
}

public interface IOrderRepository
{
    Task SaveAsync(Order order);
}

public interface IOrderNotifier
{
    Task NotifyCreatedAsync(Order order);
}

public sealed class CreateOrderUseCase
{
    private readonly IRouteEstimator _routes;
    private readonly IOrderRepository _orders;
    private readonly IOrderNotifier _notifier;

    public CreateOrderUseCase(
        IRouteEstimator routes,
        IOrderRepository orders,
        IOrderNotifier notifier)
    {
        _routes = routes;
        _orders = orders;
        _notifier = notifier;
    }

    public async Task ExecuteAsync(string email, decimal total, string address)
    {
        var order = Order.Create(email, total);
        order.AssignRoute(await _routes.EstimateAsync(address));
        await _orders.SaveAsync(order);
        await _notifier.NotifyCreatedAsync(order);
    }
}
```

## Qué mejoró y qué costo aceptamos
- **Cohesión:** `CreateOrderUseCase` solo coordina la creación del pedido.
- **Acoplamiento:** los detalles de mapas, SQL y correo quedan detrás de interfaces.
- **Pruebas:** podemos probar la regla del pedido con adaptadores falsos.
- **Costo:** hay más contratos y debemos mantener la composición de dependencias.

Elijo la opción B porque el flujo de pedidos cambiará por varias razones durante el proyecto. No separo para impresionar con patrones; separo porque los cambios ya tienen causas distintas.

## 💬 Respuestas sobre cohesión y dependencias
### ¿Qué parte de mi sistema tiene responsabilidades mezcladas?

`OrderService` mezcla una regla de negocio, una consulta a mapas, persistencia y notificación. La corrección es mover cada detalle a un puerto y dejar en el caso de uso solo la coordinación del flujo. Lo verifico cambiando el proveedor de mapas: si `CreateOrderUseCase` no cambia, reduje el acoplamiento.

### ¿Qué principio arquitectónico me está faltando aplicar?

Falta separación de responsabilidades e inversión de dependencias. El caso de uso debe depender de `IRouteEstimator`, no de `MapsClient`; así la regla de crear pedido no queda atada a un proveedor concreto.

### ¿Qué tan acoplado está mi sistema?

Está demasiado acoplado si una prueba de creación de pedido necesita una base de datos, una API de mapas y un servidor de correo. Después del refactor, una prueba puede usar implementaciones falsas y concentrarse en la regla: un pedido con total positivo se guarda y se notifica.

### ¿Qué módulos tienen demasiadas responsabilidades mezcladas?

Busca módulos que mezclen dominio, infraestructura y presentación. En este caso, `OrderService` era el problema. También revisaría controladores que validan reglas de negocio o repositorios que calculan rutas; ambos indican que la cohesión se está perdiendo.

## Actividad: refactor guiado

1. Crea una versión inicial de `OrderService` con al menos tres responsabilidades mezcladas.
2. Marca con colores o comentarios qué parte es dominio, infraestructura y notificación.
3. Extrae tres interfaces: `IRouteEstimator`, `IOrderRepository` e `IOrderNotifier`.
4. Crea `CreateOrderUseCase` y mueve allí solo la coordinación.
5. Escribe una prueba que use implementaciones falsas y compruebe que un pedido válido se guarda.
6. Cambia la implementación del estimador de rutas sin modificar el caso de uso.
7. Documenta en un ADR por qué aceptaste el costo de las interfaces.

## Cómo comprobar que terminaste
El refactor está bien si puedes responder sí a estas preguntas: ¿puedo cambiar el proveedor de mapas sin cambiar el caso de uso?, ¿puedo probar la creación de pedido sin abrir una base de datos?, ¿cada clase tiene una razón principal para cambiar? Si alguna respuesta es no, todavía hay acoplamiento que revisar.

## ✅ Cierre: cada cambio debe tener su lugar
La cohesión no significa que todas las clases sean pequeñas. Significa que cada una tiene un propósito claro. El bajo acoplamiento no significa que los módulos no se hablen; significa que se relacionan mediante contratos que permiten cambiar sin romper todo. En el siguiente video llevaremos esta separación a un nivel mayor: dominios y límites de contexto.
