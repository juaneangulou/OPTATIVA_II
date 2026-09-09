# Video 06: Dominios y límites de contexto

## 📚 Lecturas de referencia: dominio y evolución
- [Modelado de dominios y límites de contexto](https://platzi.com/cursos/fundamentos-arquitectura-software/mindset-del-arquitecto-que-abraza-el-cam/)
- [Diseño para cambio y evolución](https://platzi.com/cursos/software-avanzado/dead-letter-queue-en-productor-consumido/)

## 🔗 Del refactor a los límites del negocio
[⬅️ Video anterior](video-05.md) | [➡️ Video siguiente](video-07.md)

## 🎯 La pregunta de esta clase
Después de separar una clase demasiado grande, aparece una pregunta más profunda: ¿cómo sabemos dónde termina una responsabilidad de negocio y dónde comienza otra? Hoy no vamos a dividir por carpetas ni por tecnologías. Vamos a separar el lenguaje y las reglas de la plataforma logística.

## Escena: la palabra “disponible” significa cosas distintas
El equipo recibe una solicitud: “muestren si un pedido está disponible para entrega”. Parece una frase sencilla, pero cuatro personas la entienden de manera diferente:

- Para **Inventario**, disponible significa que existe stock reservable en una bodega.
- Para **Ruteo**, disponible significa que existe capacidad y una ruta viable.
- Para **Entregas**, disponible significa que un repartidor puede recibir una asignación.
- Para **Pedidos**, disponible significa que el cliente puede confirmar la compra.

Si guardamos esos cuatro significados en una sola propiedad llamada `IsAvailable`, vamos a crear reglas contradictorias. El cliente podría confirmar un pedido porque hay stock, aunque no exista ruta ni capacidad de entrega. Ese es el problema que resuelve un límite de contexto: una palabra puede existir en varios lugares, pero no significa lo mismo en todos.

## Los cuatro contextos que vamos a separar

| Contexto | Pregunta que responde | Regla que protege | Responsable |
|---|---|---|---|
| Pedidos | ¿El cliente puede confirmar la compra? | Un pedido confirmado tiene datos de cliente y artículos válidos. | Equipo de pedidos |
| Inventario | ¿Hay unidades reservables? | No se reserva más cantidad de la disponible. | Equipo de inventario |
| Ruteo | ¿La dirección tiene una ruta viable? | Una estimación debe indicar origen, destino y vigencia. | Equipo de ruteo |
| Entregas | ¿Quién ejecuta el traslado? | Una entrega activa tiene un solo repartidor asignado. | Operación logística |

Fíjate en que todos participan en la misma experiencia del cliente, pero ninguno debe conocer las reglas internas de los demás. Pedidos no calcula distancias; Inventario no decide qué repartidor acepta una ruta; Entregas no modifica el precio del pedido.

## Dos opciones de diseño
### Opción A: un modelo único para todo
Crear una entidad `Order` con stock, rutas, ubicación del repartidor, precio y estados de entrega. Al principio parece cómodo: todo está disponible en un solo lugar. El costo es que una regla de inventario puede romper entregas y que cualquier equipo necesite entender un modelo que no le pertenece.

### Opción B: contextos separados con contratos explícitos
Cada contexto tiene su modelo y su vocabulario. Cuando Pedidos necesita saber si puede confirmar, consulta un contrato de Inventario y solicita una estimación a Ruteo. Cuando se confirma, Entregas recibe un evento o comando con la información que necesita, no la entidad completa de Pedidos.

Para el MVP elegiría la opción B dentro de un monolito modular. No necesitamos cuatro microservicios todavía; necesitamos cuatro límites claros. Aceptamos mantener contratos internos porque reducen el costo de cambiar cada área después.

## Ejemplo en C#: el mismo concepto no viaja como el mismo objeto
```csharp
public sealed record ReservationRequest(Guid ProductId, int Quantity);
public sealed record RouteRequest(string DeliveryAddress);

public interface IInventoryAvailability
{
    Task<bool> CanReserveAsync(ReservationRequest request);
}

public interface IRoutePlanning
{
    Task<RouteEstimate> EstimateAsync(RouteRequest request);
}

public sealed class ConfirmOrderUseCase
{
    private readonly IInventoryAvailability _inventory;
    private readonly IRoutePlanning _routes;

    public ConfirmOrderUseCase(IInventoryAvailability inventory, IRoutePlanning routes)
    {
        _inventory = inventory;
        _routes = routes;
    }

    public async Task ConfirmAsync(Order order)
    {
        var hasStock = await _inventory.CanReserveAsync(
            new ReservationRequest(order.ProductId, order.Quantity));
        var route = await _routes.EstimateAsync(new RouteRequest(order.DeliveryAddress));

        if (!hasStock || !route.IsViable)
            throw new InvalidOperationException("El pedido no puede confirmarse todavía.");

        order.Confirm();
    }
}
```

El caso de uso de Pedidos no recibe una entidad `Inventory` ni modifica una entidad `Route`. Solo conoce los contratos que necesita para aplicar su propia regla: confirmar únicamente cuando hay stock y ruta viable.

## Preguntas y respuestas
### ¿Mi sistema mezcla conceptos de diferentes dominios?

Sí, si una misma propiedad intenta decidir stock, capacidad de ruta y disponibilidad del repartidor. La corrección es crear modelos separados y nombrarlos según el contexto. `StockAvailable` pertenece a Inventario; `IsViable` pertenece a Ruteo; `AssignedCourierId` pertenece a Entregas.

### ¿Dónde está el límite claro entre áreas funcionales?

El límite aparece donde cambia la pregunta del negocio y el responsable de la regla. Inventario responde por unidades; Ruteo responde por viabilidad de la ruta; Entregas responde por la asignación; Pedidos responde por la confirmación del cliente. Si una regla cambia sin que el otro equipo deba cambiar su modelo, el límite está funcionando.

### ¿Qué partes son difíciles de cambiar?

Las partes difíciles son las que comparten tablas, entidades o reglas sin contrato. Si un cambio de inventario obliga a modificar la pantalla de entregas, existe acoplamiento entre contextos. Lo comprobaría cambiando la política de reserva y verificando que el módulo de ruteo no se modifica ni vuelve a desplegarse.

## Actividad: dibuja y prueba los límites

1. Dibuja cuatro cajas: Pedidos, Inventario, Ruteo y Entregas.
2. Escribe dentro de cada caja una pregunta de negocio, una regla y un responsable.
3. Marca con flechas los contratos que cruzan los límites; no dibujes acceso directo a tablas ajenas.
4. Elige el flujo “confirmar pedido” y escribe qué datos viajan de un contexto a otro.
5. Crea interfaces C# similares a `IInventoryAvailability` e `IRoutePlanning`.
6. Cambia una regla de Inventario, por ejemplo la cantidad máxima reservable, y demuestra que `ConfirmOrderUseCase` conserva su responsabilidad.
7. Documenta la decisión en un ADR: monolito modular con contextos separados antes de considerar microservicios.

## Cómo comprobar que la actividad está bien resuelta
Pide a un compañero que responda estas tres preguntas mirando tu diagrama y tu código: ¿qué significa “disponible” en cada contexto?, ¿qué regla protege cada módulo?, ¿qué contrato usa Pedidos para confirmar? Si puede responder sin abrir una tabla compartida ni leer una clase gigante, tus límites son claros.

## Cierre
Un límite de contexto no es una pared que impide colaborar. Es una forma de permitir colaboración sin confusión. En el siguiente video compararemos qué ocurre cuando esos módulos permanecen en un monolito y qué cambia cuando intentamos distribuirlos.
