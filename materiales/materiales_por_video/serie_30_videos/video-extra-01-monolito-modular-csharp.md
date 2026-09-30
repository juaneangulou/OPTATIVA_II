# Video extra 1: Monolito modular en C#: organizar el sistema sin microservicios

## Para estudiar por tu cuenta
En este primer extra vas a construir una base organizada para la plataforma logística. Aprenderás a separar pedidos, inventario y entregas dentro de una sola aplicación, sin desplegar tres servicios por separado.

La meta es que al terminar puedas dibujar los límites, explicar qué información cruza entre módulos e implementar una regla C# que no permita acceder directamente a los datos privados de otra área.

## 1. El problema
La plataforma empieza con un flujo pequeño: registrar pedidos. Más adelante aparecen inventario, devoluciones, rutas y notificaciones. Si cualquier clase puede leer o modificar cualquier tabla, el programa funciona al principio, pero un cambio en inventario puede romper entregas sin que resulte obvio por qué.

Dividir todo en microservicios tampoco es gratis. Cada servicio necesita despliegue, configuración, comunicación por red, monitoreo y respuestas ante fallas. Antes de distribuir el sistema, vamos a ordenar sus límites dentro de una aplicación.

## 2. Monolito y módulo
Un **monolito** es una aplicación que se construye y despliega como una unidad. No significa necesariamente que todo su código deba estar mezclado.

Un **módulo** es una parte del programa responsable de una capacidad. Para esta plataforma podemos comenzar con:

- **Pedidos:** crea la compra, conserva cliente y productos y decide su estado comercial.
- **Inventario:** conserva existencias y responde si puede reservar unidades.
- **Entregas:** asigna repartidor, registra recorrido y confirma recepción.

Un **monolito modular** mantiene esos límites dentro de una aplicación y un proceso de despliegue. La **separación física** en servidores o servicios es una decisión diferente que se puede tomar más adelante si existe una razón comprobable.

## 3. Cómo se conectan sin abrir los datos internos
Imagina que Pedidos necesita confirmar si hay existencias. Una conexión frágil sería leer directamente las tablas internas de Inventario. Si cambia la estructura, Pedidos también debe cambiar.

Una conexión más clara es que Inventario ofrezca una operación pública como “consultar disponibilidad” o “solicitar reserva”. Pedidos usa esa capacidad sin conocer cómo se guardan las cantidades.

```text
Pedido -> solicita disponibilidad -> Inventario
```

El contrato comunica lo necesario; no revela la base de datos completa.

## 4. Una organización posible en C#
Puedes organizar un proyecto pequeño por módulos:

```text
Logistica/
  Pedidos/
    Pedido.cs
    CrearPedido.cs
    ConsultarPedido.cs
  Inventario/
    Existencias.cs
    ConsultarDisponibilidad.cs
  Entregas/
    Entrega.cs
    AsignarRepartidor.cs
```

No es obligatorio usar exactamente estos nombres. La pregunta importante es si puedes localizar el comportamiento de “crear pedido” sin atravesar una docena de carpetas genéricas.

## 5. Una regla del módulo de Pedidos
```csharp
namespace Logistica.Pedidos;

public sealed record LineaPedido(string ProductoId, int Cantidad);

public sealed class Pedido
{
    private readonly List<LineaPedido> _lineas = [];

    public Guid Id { get; }
    public IReadOnlyList<LineaPedido> Lineas => _lineas;
    public string Estado { get; private set; } = "Pendiente";

    public Pedido(Guid id)
    {
        if (id == Guid.Empty)
            throw new ArgumentException("El identificador no puede estar vacío.");

        Id = id;
    }

    public void AgregarLinea(string productoId, int cantidad)
    {
        if (string.IsNullOrWhiteSpace(productoId))
            throw new ArgumentException("Indica un producto.");

        if (cantidad <= 0)
            throw new ArgumentOutOfRangeException(nameof(cantidad));

        _lineas.Add(new LineaPedido(productoId, cantidad));
    }
}
```

La lista interna es privada. Otras partes pueden leer las líneas, pero no agregar valores inválidos directamente. La regla queda junto al pedido, no escondida solo en una pantalla.

Este ejemplo aún no guarda nada en una base de datos ni consulta Inventario. Es un primer límite de dominio; los siguientes videos agregan puertos y persistencia.

## 6. Qué significa Vertical Slice
Un **vertical slice** organiza una funcionalidad de extremo a extremo. Por ejemplo, `CrearPedido` puede contener su solicitud, reglas, coordinación de almacenamiento y respuesta. No obliga a copiar todo en una sola clase; sirve para que la funcionalidad sea fácil de seguir.

Puedes combinar módulos con vertical slices: `Pedidos/CrearPedido` y `Pedidos/CancelarPedido` están dentro del límite de Pedidos, pero cada flujo tiene sus piezas cercanas.

## 7. Cuándo sirve y cuándo no
Un monolito modular suele ser una buena base si:

- un equipo desarrolla y opera el producto;
- el sistema puede desplegarse como una unidad;
- los límites entre responsabilidades todavía están cambiando;
- el costo de operar muchos servicios no está justificado.

Considera extraer un módulo si hay evidencia: necesidad de escalar por separado, equipos que requieren ciclos independientes o requisitos de disponibilidad diferentes. No lo hagas solo porque un sistema tenga varios sustantivos o carpetas.

## 8. Actividad de autoestudio
Dibuja cómo se relacionan Pedidos, Inventario y Entregas al crear una entrega.

1. Escribe qué información pertenece a cada módulo.
2. Marca qué operación necesita Pedidos de Inventario.
3. Marca qué información recibe Entregas.
4. Identifica un acceso directo que rompería la frontera.
5. Define una prueba que demuestre que la regla de cantidad no puede ser menor o igual a cero.

### Respuesta modelo
Pedidos conserva la compra y sus líneas; Inventario conserva existencias y reservas; Entregas conserva asignación y recorrido. Pedidos solicita a Inventario disponibilidad o reserva y comparte con Entregas solo los datos necesarios para preparar la entrega.

Una mala dependencia sería que Entregas modifique directamente la tabla de Pedidos. La prueba de cantidad crea un pedido, intenta agregar cero unidades y comprueba que la operación se rechaza.

## Comprueba lo que aprendiste
1. ¿Monolito modular significa que el sistema no tiene límites?
2. ¿Qué diferencia hay entre módulo y microservicio?
3. ¿Por qué no conviene que Entregas actualice directamente las tablas de Pedidos?
4. ¿Qué evidencia justificaría extraer un módulo?

### Respuestas
1. No; tiene límites dentro de una misma aplicación.
2. El módulo es un límite de organización; microservicio implica además un despliegue y operación independientes.
3. Porque puede saltarse las reglas de Pedidos y quedar acoplado a sus detalles internos.
4. Una necesidad observada de escalado, despliegue o responsabilidad independiente.

## Cierre
Empieza separando reglas y responsabilidades dentro de una aplicación. Cuando los límites estén claros y exista una necesidad medible, podrás decidir si también deben separarse en despliegue. El monolito modular evita asumir complejidad distribuida antes de necesitarla.
