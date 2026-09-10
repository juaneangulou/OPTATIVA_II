# Video 08: APIs, contratos e infraestructura

## 📚 Lecturas de referencia: contratos y despliegue
- [APIs y contratos de integración](https://platzi.com/cursos/fundamentos-arquitectura-software/que-son-las-arquitecturas-monoliticas-y/)
- [Infraestructura, despliegue y entorno de ejecución](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitecturas-orientadas-a-servicios-con/)

## 🔗 De microservicios a una integración segura
[⬅️ Video anterior](video-07.md) | [➡️ Video siguiente](video-09.md)

## 🎯 La decisión de esta clase
Hoy vamos a construir el borde de la plataforma: el punto donde una aplicación externa o una interfaz web solicita crear un pedido. La pregunta no es solamente “¿qué endpoint hacemos?”. La pregunta es qué contrato prometemos, cómo evitamos romper a quienes lo consumen y dónde dejamos los detalles de infraestructura.

## Escena: una aplicación móvil ya usa tu API
El equipo móvil consume `POST /api/orders`. La próxima semana, negocio pide agregar un campo de ventana de entrega. Alguien propone cambiar `address` por un objeto complejo y renombrar `total` por `amount`. La aplicación móvil publicada no se actualizará de inmediato. Si rompemos el contrato, el cliente no podrá crear pedidos aunque el servidor funcione.

El actor principal es **la aplicación móvil del cliente**. Necesita enviar una solicitud estable y recibir un error comprensible. La regla que protegemos es: **un cambio compatible agrega información opcional; un cambio incompatible se publica como una versión nueva del contrato**.

## Contrato de entrada
```csharp
public sealed record CreateOrderRequest(
    string CustomerEmail,
    string DeliveryAddress,
    decimal Total,
    string? DeliveryWindow);

public sealed record CreateOrderResponse(
    Guid OrderId,
    string Status,
    DateTimeOffset CreatedAt);
```

`DeliveryWindow` es opcional. Una aplicación antigua puede no enviarlo y el servidor puede aplicar una regla por defecto. Si necesitáramos cambiar el significado de `Total`, no modificaríamos silenciosamente el contrato: publicaríamos `/api/v2/orders` y mantendríamos la versión anterior durante una ventana acordada.

## El controlador no contiene la regla de negocio
```csharp
[ApiController]
[Route("api/orders")]
public sealed class OrdersController : ControllerBase
{
    [HttpPost]
    public async Task<ActionResult<CreateOrderResponse>> Create(
        CreateOrderRequest request,
        [FromServices] CreateOrderUseCase useCase,
        CancellationToken cancellationToken)
    {
        var result = await useCase.ExecuteAsync(request, cancellationToken);
        return Created($"/api/orders/{result.OrderId}", result);
    }
}
```

El controlador recibe HTTP y devuelve HTTP. La validación de formato puede estar aquí; la regla “un pedido se confirma solo si hay inventario y ruta viable” vive en el caso de uso y el dominio. Así podemos cambiar ASP.NET, la aplicación móvil o un proveedor externo sin mover la regla principal.

None

## Infraestructura reproducible
Para que el contrato funcione fuera de tu computador, necesitas un entorno repetible. Define variables para conexión, proveedor de rutas, timeout y ambiente. El despliegue debe ejecutar pruebas, crear la configuración y publicar la misma versión que fue validada. No dependas de cambios manuales que nadie pueda reconstruir.

## Dos alternativas
### Opción A: controlador conectado directamente a SQL y al proveedor de mapas
Se construye rápido, pero el endpoint conoce contraseñas, queries, URL de mapas y lógica de negocio. Probarlo exige infraestructura real y cualquier cambio externo obliga a modificar la API.

### Opción B: contrato estable, caso de uso y adaptadores
El controlador llama a `CreateOrderUseCase`; el caso de uso depende de puertos para persistencia y rutas; infraestructura implementa esos puertos. Cuesta crear contratos y configuración, pero cada borde tiene una responsabilidad clara.

Elijo B. El contrato debe sobrevivir a cambios de interfaz y los detalles de infraestructura deben poder reemplazarse sin tocar la creación de pedidos.

## Preguntas y respuestas
### ¿Qué pasa si una aplicación usa una versión anterior?

La versión anterior debe continuar aceptando su formato durante el periodo anunciado. Agregar `DeliveryWindow` como opcional no rompe al cliente; cambiar el significado de un campo sí requiere versión nueva. Lo verifico con pruebas de contrato que ejecuten la misma solicitud de una aplicación antigua y una nueva.

### ¿Mis interfaces están documentadas?

Están documentadas si alguien puede saber qué campos son obligatorios, qué errores recibe, qué significa cada estado y cómo evoluciona la versión. Publicaría OpenAPI, ejemplos de solicitudes y respuestas, y códigos de error como `inventory_unavailable` o `route_not_viable`.

### ¿El entorno es reproducible?

Lo es si otro integrante puede levantar la API con las mismas variables, ejecutar pruebas y obtener el mismo comportamiento sin configurar valores manualmente. La evidencia será un archivo de configuración por ambiente y una ejecución de despliegue automatizada.

## Actividad: crea el borde del pedido

1. Define `CreateOrderRequest` y `CreateOrderResponse`.
2. Escribe tres reglas del contrato: campos obligatorios, error de inventario y compatibilidad de versiones.
3. Implementa un controlador que solo traduzca HTTP a la llamada del caso de uso.
4. Declara los puertos `IOrderRepository` e `IRouteEstimator`.
5. Agrega una prueba de contrato para una solicitud sin `DeliveryWindow`.
6. Documenta en un ADR por qué eliges agregar un campo opcional en lugar de cambiar el formato existente.
7. Escribe las variables de entorno que el adaptador de rutas necesita para ejecutarse.

## Cómo comprobar que terminaste
La actividad está bien resuelta si puedes cambiar el proveedor de rutas sin cambiar el controlador, ejecutar una solicitud de una versión anterior sin error y levantar el proyecto en otro equipo sin pasos secretos.

## Cierre
Una API es una promesa. La infraestructura es el lugar donde esa promesa se ejecuta. En el siguiente video veremos cómo saber qué ocurrió cuando esa promesa falla, sin convertir los logs en una fuga de datos.
