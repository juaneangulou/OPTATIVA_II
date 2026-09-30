# Compilación anterior: 10 videos de patrones de arquitectura en C#/.NET

> Esta es la versión consolidada de la ruta. Para estudiar, usa los diez capítulos independientes enlazados en el [índice de la serie](README.md); allí cada video tiene su propio archivo abundante. Esta compilación se conserva como referencia complementaria.

## Cómo usar esta guía
Estudia cada capítulo por tu cuenta: empieza por el problema, sigue la explicación y el ejemplo en C#, resuelve el ejercicio y compara tu respuesta con la solución para comprobar lo aprendido.

Los diez capítulos construyen una sola plataforma logística pequeña. Al terminar, tendrás un flujo que crea un pedido, verifica inventario, prepara la entrega y permite consultar su estado. La ruta no supone que debas convertir todo en microservicios ni aplicar todos los patrones a la vez.

Conviene conocer clases, interfaces, métodos, excepciones, colecciones y `async`/`await` básico de C#. Si un término aparece por primera vez, se explica antes de usarlo. Los fragmentos son ejemplos de aprendizaje; ajusta los nombres y versiones al proyecto real antes de copiarlos.

## El proyecto que acompaña las diez clases
La plataforma de última milla ya tiene pedidos, almacenes, repartidores, rutas, clientes y soporte. En esta ruta trabajaremos un alcance manejable:

1. Registrar un pedido.
2. Revisar si hay unidades disponibles.
3. Crear una entrega y asignar un repartidor.
4. Informar el estado del envío.
5. Registrar fallos sin perder la tarea ni exponer datos del cliente.

Mantendremos primero una sola aplicación ASP.NET Core organizada en módulos. Cuando un capítulo necesite mensajes, caché o servicios externos, agregaremos solo la pieza que explica el patrón. No es necesario desplegar infraestructura real para comprender el diseño.

## Antes de empezar: algunas palabras
- **Módulo:** parte del programa responsable de una capacidad, como Pedidos o Entregas.
- **Dependencia:** otra parte o herramienta que un componente necesita para trabajar.
- **Caso de uso:** una acción completa del negocio, como confirmar una compra.
- **Adaptador:** código que conecta una regla de la aplicación con una herramienta externa, como una base de datos.
- **Prueba unitaria:** comprueba una regla aislada.
- **Prueba de integración:** comprueba que varias partes reales colaboran.
- **Despliegue:** poner una versión del programa en un entorno donde pueda ejecutarse.

En cada capítulo encontrarás: el problema, la idea del patrón, una implementación C# explicada, límites, ejercicio y respuesta modelo. Los ejemplos pueden requerir ajustes pequeños al incorporarse a una solución real.

---

## Video extra 1: Monolito modular en C#: organizar el sistema sin microservicios

### El problema
La plataforma empieza como una API pequeña. Con el tiempo añade pedidos, inventario y entregas. Si todos los archivos terminan en carpetas genéricas como `Controllers`, `Services` y `Repositories`, entender una función completa puede exigir saltar entre muchas carpetas. Si cada módulo accede a las tablas de los demás, las fronteras existen solo en el nombre.

### Qué significa monolito modular
Un **monolito** es una aplicación que se construye y despliega como una unidad. **Modular** significa que dentro de esa unidad hay partes con responsabilidades y límites claros.

Podemos comenzar con esta organización:

```text
src/Logistica/
  Pedidos/
	CrearPedido.cs
	Pedido.cs
  Inventario/
	ConsultarDisponibilidad.cs
  Entregas/
	PrepararEntrega.cs
```

Los tres módulos se despliegan juntos, pero cada uno conserva su trabajo. Esto puede ser más simple que crear tres servicios distribuidos, porque evita llamadas de red, despliegues separados y operación adicional mientras el producto todavía es pequeño.

### Una solicitud pequeña en C#
El módulo de pedidos puede exponer un contrato sencillo para registrar una compra:

```csharp
namespace Logistica.Pedidos;

public sealed record CrearPedido(Guid ClienteId, string Direccion);

public sealed record PedidoCreado(Guid PedidoId, Guid ClienteId);

public sealed class ServicioPedidos
{
	public PedidoCreado Crear(CrearPedido solicitud)
	{
		if (solicitud.ClienteId == Guid.Empty)
			throw new ArgumentException("El cliente es obligatorio.");

		if (string.IsNullOrWhiteSpace(solicitud.Direccion))
			throw new ArgumentException("La dirección es obligatoria.");

		return new PedidoCreado(Guid.NewGuid(), solicitud.ClienteId);
	}
}
```

`CrearPedido` expresa lo que se solicita; `PedidoCreado` expresa el resultado; `ServicioPedidos` mantiene esta pequeña responsabilidad. El ejemplo no guarda en una base de datos todavía: primero muestra dónde vive una operación del módulo.

### Qué debes decidir
No compartas libremente las tablas internas de Pedidos con Entregas. Define qué información necesita Entregas y ofrece un contrato claro para intercambiarla. Si un cambio de una parte obliga a reescribir las demás, el límite todavía no está protegido.

Un **vertical slice** organiza una funcionalidad de punta a punta, por ejemplo crear un pedido, con su solicitud, regla, persistencia y respuesta. Puede convivir con módulos; no es sinónimo de microservicio.

### Cuándo ayuda y cuándo no
Empieza con un monolito modular cuando un equipo puede construir y desplegar el sistema como una unidad y no existe una necesidad demostrada de separar operaciones. Considera separar un servicio cuando haya razones como escalado independiente, equipos con ciclos de entrega realmente distintos o aislamiento operativo. Dividir solo porque el sistema tiene muchas carpetas no basta.

### Ejercicio y respuesta
**Ejercicio:** decide si el cálculo de disponibilidad pertenece a Pedidos o a Inventario. Dibuja qué información necesita Pedidos y qué regla conserva Inventario.

**Respuesta posible:** Inventario conserva las cantidades y decide si hay existencias; Pedidos solicita la disponibilidad necesaria para confirmar la compra. Pedidos no debería modificar directamente las tablas internas de Inventario.

**Comprueba tu aprendizaje:** ¿qué diferencia hay entre un monolito modular y tres microservicios? Respuesta: el primero es una unidad de despliegue con módulos internos; los segundos se despliegan y operan por separado, con comunicación distribuida.

---

## Video extra 2: Arquitectura hexagonal en C#: separar reglas y herramientas

### El problema
La regla “no confirmar un pedido si el inventario no alcanza” debe funcionar tanto si la aplicación recibe una solicitud web como si se prueba sin servidor. Si la regla está mezclada con HTTP o con la biblioteca de base de datos, cambiar una herramienta puede obligar a reescribir la lógica.

### Puerto y adaptador, en sencillo
Un **puerto** es una interfaz que describe qué necesita un caso de uso. Un **adaptador** conecta esa interfaz con una herramienta real. La regla conoce la interfaz, no una marca o proveedor concreto.

La dirección deseada es:

```text
Caso de uso -> interfaz de inventario <- adaptador que consulta almacenamiento
```

### Implementación C#
```csharp
namespace Logistica.Pedidos;

public interface IInventario
{
	Task<bool> TieneDisponibilidadAsync(
		string productoId,
		int cantidad,
		CancellationToken cancellationToken);
}

public sealed class ConfirmarPedido(IInventario inventario)
{
	public async Task<bool> EjecutarAsync(
		string productoId,
		int cantidad,
		CancellationToken cancellationToken)
	{
		if (cantidad <= 0)
			throw new ArgumentOutOfRangeException(nameof(cantidad));

		return await inventario.TieneDisponibilidadAsync(
			productoId, cantidad, cancellationToken);
	}
}
```

El caso de uso depende de `IInventario`, una interfaz propia. En ejecución, la aplicación conecta esa interfaz con un adaptador que consulta la fuente real. En una prueba, puede conectarse con un objeto pequeño que devuelve “hay stock” o “no hay stock”.

### Comprobar el comportamiento
```csharp
public sealed class InventarioDePrueba(bool disponible) : IInventario
{
	public Task<bool> TieneDisponibilidadAsync(
		string productoId,
		int cantidad,
		CancellationToken cancellationToken) => Task.FromResult(disponible);
}
```

Este sustituto no es la base de datos: permite probar cómo responde el caso de uso ante cada resultado. Luego una prueba de integración comprobaría por separado que el adaptador real lee los datos correctos.

### Cuándo conviene y cuándo puede sobrar
Esta separación ayuda cuando la regla debe probarse sin infraestructura, cuando podría cambiar el proveedor o cuando el límite protege una regla importante. No crees una interfaz para cada clase automáticamente; si no hay una frontera o motivo de cambio, puede añadir nombres sin aportar claridad.

### Ejercicio y respuesta
**Ejercicio:** agrega el caso “no hay existencias” y describe qué debería recibir la API.

**Respuesta posible:** el caso de uso devuelve un resultado de negocio que indica inventario insuficiente. El endpoint transforma ese resultado en una respuesta HTTP; la regla no necesita conocer HTTP.

**Comprueba tu aprendizaje:** si cambias SQL por un servicio externo, ¿qué parte debería cambiar? Respuesta: el adaptador de `IInventario`, no la regla que decide si se confirma el pedido.

---

## Video extra 3: Repositorios con EF Core en C#: cuándo abstraer el acceso a datos

### El problema
El servicio de pedidos necesita guardar pedidos y líneas de producto. Si cada caso de uso escribe consultas distintas, pueden aparecer diferencias en cómo se cargan, actualizan y guardan los datos.

Un **repositorio** es una interfaz que presenta operaciones de almacenamiento con lenguaje del dominio, por ejemplo “buscar pedido” o “agregar pedido”. **EF Core** es un ORM: una herramienta que permite trabajar con objetos de C# y persistirlos en una base de datos.

### Una implementación pequeña
```csharp
public interface IPedidosRepository
{
	Task<Pedido?> BuscarAsync(
		Guid id,
		CancellationToken cancellationToken);

	void Agregar(Pedido pedido);
	Task GuardarCambiosAsync(CancellationToken cancellationToken);
}

public sealed class PedidosRepository(LogisticaDbContext db)
	: IPedidosRepository
{
	public Task<Pedido?> BuscarAsync(
		Guid id,
		CancellationToken cancellationToken) =>
		db.Pedidos.SingleOrDefaultAsync(
			pedido => pedido.Id == id, cancellationToken);

	public void Agregar(Pedido pedido) => db.Pedidos.Add(pedido);

	public Task GuardarCambiosAsync(CancellationToken cancellationToken) =>
		db.SaveChangesAsync(cancellationToken);
}
```

`LogisticaDbContext` pertenece a EF Core. El caso de uso ve la interfaz y expresa la operación del negocio. La implementación concreta ejecuta consultas con EF Core.

### ¿Dónde está Unit of Work?
Una **transacción** agrupa varios cambios para que se confirmen o fallen como una operación coordinada. EF Core ya rastrea cambios y `SaveChangesAsync` normalmente los guarda en una transacción para esa llamada. Por eso, añadir una clase genérica `UnitOfWork` sobre cada operación puede duplicar lo que el framework ya hace.

Usa una abstracción extra cuando permita delimitar una transacción que cruza operaciones o proteja una frontera real; no solo por repetir el nombre de un patrón.

### Una API no debería exponer el objeto de base de datos
Para responder al cliente, crea un tipo de salida que contenga los campos permitidos. No devuelvas automáticamente la entidad de EF: podría incluir datos internos, navegación a otras tablas o propiedades que no querías publicar.

### Ejercicio y respuesta
**Ejercicio:** una operación guarda el pedido y una línea de producto. ¿Qué pasa si se guarda el pedido, pero falla la línea?

**Respuesta posible:** la operación debería definir una transacción para que ambos cambios se guarden juntos o ninguno quede guardado. Comprueba esa garantía con una prueba de integración.

**Comprueba tu aprendizaje:** ¿EF Core significa que debes crear un repositorio genérico por tabla? Respuesta: no; crea repositorios cuando aporten una frontera útil y mantengan las consultas del dominio claras.

---

## Video extra 4: CQRS en C#: separar consultas y cambios sin duplicar el sistema

### El problema
La pantalla de seguimiento necesita una respuesta simple para mostrar al cliente. La operación que confirma un pedido, en cambio, debe validar inventario y cambiar datos. Una misma forma de entrada y salida no siempre resulta cómoda para ambas tareas.

**CQRS** significa separar la responsabilidad de modificar información de la responsabilidad de consultarla. Un **comando** pide un cambio; una **consulta** pide información y no debería cambiar el estado.

### Modelos sencillos en C#
```csharp
public sealed record ConfirmarPedido(Guid PedidoId);
public sealed record PedidoConfirmado(Guid PedidoId, DateTimeOffset ConfirmadoEn);

public sealed record ConsultarSeguimiento(Guid PedidoId);
public sealed record SeguimientoPedido(
	Guid PedidoId,
	string Estado,
	DateTimeOffset? ActualizadoEn);
```

Los nombres expresan dos intenciones distintas. `ConfirmarPedido` puede verificar reglas y guardar cambios. `ConsultarSeguimiento` reúne lo necesario para presentar una respuesta, sin confirmar ni modificar el pedido.

### CQRS no exige dos bases de datos
Puedes mantener dos caminos de código y utilizar la misma base de datos. Separar almacenes, colas y sincronización agrega complejidad; se justifica solo si una necesidad concreta, como carga de lectura muy distinta, lo requiere.

### Qué probar
- Al confirmar un pedido sin stock, no debe cambiarse a confirmado.
- Al consultar seguimiento, el estado devuelto debe corresponder al pedido solicitado.
- Una consulta no debe producir una reserva ni una notificación.

### Ejercicio y respuesta
**Ejercicio:** clasifica `CancelarPedido`, `ConsultarEstado` y `ActualizarDireccion` como comandos o consultas.

**Respuesta:** `CancelarPedido` es comando; `ConsultarEstado` es consulta; `ActualizarDireccion` es comando porque modifica datos.

**Comprueba tu aprendizaje:** ¿CQRS equivale a Event Sourcing? Respuesta: no. CQRS separa lectura y escritura; Event Sourcing guarda una secuencia de hechos como fuente principal. Se pueden usar por separado.

---

## Video extra 5: Patrón Decorator en C#: envolver un caso de uso con comportamiento adicional

### El problema
Varios casos de uso necesitan medir cuánto tardan y registrar errores. Copiar el mismo código de medición dentro de cada uno dificulta mantenerlo. A la vez, no queremos esconder una regla de negocio dentro de código técnico.

El patrón **Decorator** envuelve un objeto y añade comportamiento antes o después de delegar el trabajo al objeto original. El objeto envuelto mantiene su responsabilidad principal.

### Implementación C# simplificada
```csharp
public interface IConfirmarPedido
{
	Task EjecutarAsync(Guid pedidoId, CancellationToken cancellationToken);
}

public sealed class MedirConfirmacion(
	IConfirmarPedido siguiente,
	ILogger<MedirConfirmacion> logger) : IConfirmarPedido
{
	public async Task EjecutarAsync(
		Guid pedidoId,
		CancellationToken cancellationToken)
	{
		var inicio = Stopwatch.GetTimestamp();

		try
		{
			await siguiente.EjecutarAsync(pedidoId, cancellationToken);
		}
		catch (Exception exception)
		{
			logger.LogError(exception,
				"Falló la confirmación del pedido {PedidoId}", pedidoId);
			throw;
		}
		finally
		{
			var duracion = Stopwatch.GetElapsedTime(inicio);
			logger.LogInformation(
				"Confirmación del pedido {PedidoId}: {Duracion}",
				pedidoId, duracion);
		}
	}
}
```

El decorador mide y registra, luego delega la confirmación. Relanza la excepción para no ocultar el fallo. No registra dirección, contraseña ni datos personales innecesarios.

### El orden también importa
Si agregas validación y medición, define en qué orden suceden. Si el dato es inválido, quizá convenga rechazarlo antes de llamar al caso de uso. Prueba el orden, no supongas que la configuración hizo lo que esperabas.

### Ejercicio y respuesta
**Ejercicio:** ¿dónde pondrías el registro “no hay inventario”? ¿En el decorador o en la regla de confirmación?

**Respuesta posible:** la medición del tiempo puede ir en Decorator; la decisión de rechazar por falta de inventario pertenece al caso de uso o al dominio, porque es una regla del negocio.

**Comprueba tu aprendizaje:** ¿qué añade Decorator? Respuesta: un comportamiento alrededor del componente original, conservando su contrato y delegando la operación.

---

## Video extra 6: Transactional Outbox en C#: guardar el pedido y publicar el aviso

### El problema de dos operaciones
Al confirmar una compra, el sistema debe guardar el pedido y avisar a Entregas. Son dos operaciones: guardar en la base de datos y enviar un mensaje a otro servicio.

Si guardas el pedido primero y la aplicación se apaga antes de enviar el aviso, Entregas nunca se entera. Si envías el aviso primero y falla el guardado, Entregas recibe una confirmación de un pedido que no existe.

### ¿Qué hace Outbox?
El patrón **Transactional Outbox** guarda el pedido y un registro que describe el evento dentro de la misma transacción de base de datos. Un proceso posterior lee los registros pendientes y los publica.

```csharp
await using var transaction =
	await db.Database.BeginTransactionAsync(cancellationToken);

db.Pedidos.Add(pedido);
db.OutboxMessages.Add(OutboxMessage.Crear(
	"PedidoConfirmado",
	JsonSerializer.Serialize(new { pedido.Id })));

await db.SaveChangesAsync(cancellationToken);
await transaction.CommitAsync(cancellationToken);
```

Si la transacción se confirma, existen tanto el pedido como el registro Outbox. Si falla, ninguno queda confirmado. El publicador es otro paso: lee registros pendientes, los envía y marca su resultado.

### No supongas entrega exactamente una vez
El proceso podría publicar el mensaje y apagarse antes de marcarlo enviado. Al reiniciar, puede publicarlo de nuevo. Por eso el consumidor debe identificar eventos repetidos y evitar, por ejemplo, crear dos entregas para el mismo pedido.

Una clave de idempotencia identifica una operación para reconocer que ya produjo efecto. El identificador de pedido puede participar, pero define una clave adecuada para la operación y el consumidor.

### Ejercicio y respuesta
**Ejercicio:** el publicador se apaga después de enviar `PedidoConfirmado` pero antes de actualizar el registro Outbox. ¿Qué puede pasar y cómo se protege el sistema?

**Respuesta:** el mensaje puede volver a enviarse. El consumidor comprueba si ya procesó el identificador de evento y no duplica la entrega.

**Comprueba tu aprendizaje:** ¿la tabla Outbox envía mensajes sola? Respuesta: no; conserva publicaciones pendientes, y un proceso publicador debe leerlas y enviarlas.

---

## Video extra 7: Process Manager en C#: coordinar una entrega con varios pasos

### El problema
Una entrega requiere reservar inventario, asignar un repartidor y notificar al cliente. Un paso puede tardar o fallar. Si el programa solo mantiene el progreso en memoria, un reinicio podría dejar el pedido sin saber qué hacer después.

Un **Process Manager** es un componente que guarda el estado de un proceso de varios pasos y decide cuál sigue según los resultados recibidos. No realiza el trabajo de Inventario ni de Entregas: les solicita acciones y conserva el progreso global.

### Los estados del proceso
Una primera versión podría tener:

```csharp
public enum EstadoPreparacion
{
	EsperandoReserva,
	EsperandoRepartidor,
	Completada,
	RequiereRevision
}
```

Al confirmar el pedido, el gestor guarda `EsperandoReserva` y solicita unidades a Inventario. Si la reserva se confirma, cambia a `EsperandoRepartidor`; si falta stock, pasa a `RequiereRevision`.

### Compensar sin borrar el pasado
Si Inventario reservó productos pero no se encuentra repartidor, el gestor puede solicitar que se libere la reserva. Esa acción es una **compensación**: intenta contrarrestar un efecto anterior. No borra el hecho de que la reserva ocurrió.

Guarda los mensajes y estados de forma que el flujo sobreviva a reinicios. Relaciona cada resultado con el pedido correcto y diseña los pasos para tolerar respuestas repetidas.

### Ejercicio y respuesta
**Ejercicio:** la reserva se confirma, pero Entregas rechaza la asignación. ¿Qué registrarías y cuál sería el paso siguiente?

**Respuesta posible:** registrar que la reserva ocurrió y que la asignación falló; solicitar liberar las unidades; si liberar también falla, conservar ese estado y enviarlo a revisión en lugar de marcar el pedido como completado.

**Comprueba tu aprendizaje:** ¿qué decide el Process Manager y qué decide Inventario? El gestor decide el siguiente paso del proceso; Inventario decide si puede reservar y actualizar sus cantidades.

---

## Video extra 8: Resiliencia en C# para llamadas a proveedores externos

### El problema
El servicio de geolocalización puede tardar o dejar de responder. Una solicitud que espera sin límite puede dejar al cliente viendo una pantalla detenida; repetirla muchas veces puede saturar al proveedor.

Un **timeout** es el tiempo máximo que aceptamos esperar. Un **reintento** repite una operación que falló. Un **circuit breaker** deja de llamar temporalmente a una dependencia que falla repetidamente. Una **respuesta alternativa** comunica lo que sí sabemos cuando falta un dato.

### Configura límites con el cliente HTTP
En versiones de .NET compatibles, `Microsoft.Extensions.Http.Resilience` ofrece manejadores estándar:

```csharp
builder.Services
	.AddHttpClient<IRutasClient, RutasClient>(client =>
	{
		client.BaseAddress = new Uri("https://rutas.example/");
	})
	.AddStandardResilienceHandler();
```

La configuración exacta depende de la versión de .NET y del paquete. Revisa el límite de espera, cantidad de reintentos y qué errores se reintentan. No agregues reintentos duplicados en varios niveles sin calcular el total de intentos.

### No toda acción se puede repetir
Leer una ubicación suele poder repetirse. Crear una entrega o cobrar dinero puede duplicar efectos si se reintenta sin protección. Usa una clave de idempotencia o comprueba si la operación ya se realizó.

Si geolocalización falla, puedes mostrar la última ubicación confirmada con su hora, o avisar que no está disponible. No presentes una ubicación antigua como si fuera actual.

### Ejercicio y respuesta
**Ejercicio:** la solicitud para consultar ubicación falla por timeout. ¿Qué mostrarías y qué evitarías?

**Respuesta posible:** devolver el estado confirmado del pedido y un mensaje de ubicación temporalmente no disponible; si se usa la ubicación anterior, indicar su hora. Evitar reintentar sin límite o afirmar una posición actual que no se conoce.

---

## Video extra 9: Cache-Aside en C#: acelerar consultas sin perder claridad

### El problema
Muchos clientes consultan el estado de una entrega. Leer repetidamente la base de datos puede aumentar carga. Una **caché** guarda temporalmente una copia para acelerar lecturas posteriores.

En **Cache-Aside**, la aplicación pregunta primero a la caché; si no encuentra el dato, lo lee de la fuente principal y guarda una copia temporal. La base de datos continúa siendo la fuente de verdad.

### Ejemplo C# con memoria local
```csharp
public async Task<Seguimiento?> ConsultarAsync(
	Guid pedidoId,
	CancellationToken cancellationToken)
{
	var clave = $"seguimiento:{pedidoId}";
	var guardado = await cache.GetAsync<Seguimiento>(clave);

	if (guardado is not null)
		return guardado;

	var actual = await repositorio.BuscarSeguimientoAsync(
		pedidoId, cancellationToken);

	if (actual is not null)
		await cache.SetAsync(clave, actual, TimeSpan.FromMinutes(1));

	return actual;
}
```

`GetAsync` y `SetAsync` representan una interfaz de caché de ejemplo; adapta las llamadas al proveedor elegido. La expiración corta reduce cuánto tiempo puede quedar visible un estado antiguo.

Cuando Entregas actualiza el estado, el sistema debe invalidar o actualizar la clave. Si la aplicación corre en varias instancias, una caché en memoria local no se comparte automáticamente: elige una solución compartida solo si el caso lo requiere.

No guardes datos personales en caché sin necesidad. No conviertas la caché en la única copia del pedido.

### Ejercicio y respuesta
**Ejercicio:** un pedido cambia de “En camino” a “Entregado”, pero la caché tiene “En camino”. ¿Qué acción evita seguir devolviendo ese estado?

**Respuesta posible:** invalidar la clave del pedido cuando se confirma la entrega y, si la consulta vuelve a ocurrir, leer el estado nuevo de la fuente principal. También se conserva una expiración como límite de respaldo.

---

## Video extra 10: Pruebas de arquitectura en C#: proteger límites y conectar el sistema

### El problema
Un diagrama puede mostrar que Pedidos no depende de Infraestructura, pero una persona podría agregar esa referencia en el siguiente cambio. Una **prueba de arquitectura** convierte una regla estructural en una comprobación repetible.

### Ejemplo de regla entre módulos
Con una biblioteca como NetArchTest, podrías expresar que el dominio no debe depender de infraestructura:

```csharp
using NetArchTest.Rules;

var resultado = Types
	.InAssembly(typeof(Pedido).Assembly)
	.That()
	.ResideInNamespace("Logistica.Dominio")
	.ShouldNot()
	.HaveDependencyOn("Logistica.Infraestructura")
	.GetResult();

Assert.True(resultado.IsSuccessful);
```

El nombre de los namespaces y la ubicación de los proyectos dependen de tu solución. La prueba impide una clase concreta de dependencia; no demuestra que todas las decisiones de arquitectura sean correctas.

### Completa el flujo
Integra `crear pedido → reservar inventario → preparar entrega → consultar estado`. Añade:

- pruebas unitarias para las reglas de stock y transición de estado;
- una prueba de integración para persistir y leer un pedido;
- una prueba de arquitectura para el límite entre dominio e infraestructura;
- un caso de error en el que el proveedor de rutas no responda.

Guarda resultados de pruebas, diagrama y una decisión breve con alternativas, costo y señal de revisión. No copies datos reales ni secretos al repositorio.

### Ejercicio de cierre y solución modelo
**Ejercicio:** define una regla arquitectónica, escribe una prueba que la proteja y explica un límite de esa prueba.

**Respuesta posible:** “El dominio no referencia EF Core”. La prueba de arquitectura verifica dependencias entre namespaces. Su límite es que solo detecta ese tipo de referencia; no garantiza que el dominio tenga responsabilidades bien diseñadas ni que el comportamiento sea correcto.

**Comprueba tu aprendizaje:** ¿qué diferencia hay entre una prueba unitaria y una prueba de arquitectura? La primera revisa un comportamiento pequeño; la segunda revisa una propiedad estructural del sistema.

---

## Buenas prácticas C#/.NET que se aplican en los diez capítulos

### Diseño y legibilidad
- Separa el dominio de ASP.NET Core, EF Core y proveedores externos cuando esa frontera proteja reglas que necesitas mantener o probar.
- Usa interfaces para representar límites útiles, no por obligación.
- Mantén endpoints pequeños y deja que los casos de uso coordinen las operaciones.
- Evita una clase que concentre validación, acceso a datos, mensajería y respuestas HTTP.
- No devuelvas directamente las entidades de persistencia como respuestas públicas.

### Código asíncrono y errores
- Usa `async`/`await` para entrada/salida y evita bloquear con `.Result` o `.Wait()`.
- Propaga `CancellationToken` en llamadas que puedan tardar.
- Valida entradas en los límites y mantiene las reglas críticas dentro del dominio.
- Captura excepciones cuando puedas hacer algo útil; no ocultes fallos devolviendo valores inventados.
- Devuelve mensajes seguros al cliente y conserva detalles técnicos solo en registros protegidos.

### Datos, seguridad y pruebas
- Define qué cambios deben guardarse juntos y no mantengas transacciones de base de datos abiertas durante llamadas de red largas.
- Supón que un mensaje puede repetirse; evita duplicar pedidos, reservas o avisos.
- No guardes claves, contraseñas ni tokens en Git, respuestas o logs.
- Comprueba autorización en el servidor para cada pedido; ocultar un botón no protege los datos.
- Prueba casos normales, errores, cancelación, repetición y datos faltantes.
- Mide antes de agregar caché, servicios o infraestructura.

## Recorrido final de autoestudio
Al terminar, explica con tus palabras:

1. ¿Qué necesidad concreta resolvía cada patrón que decidiste conservar?
2. ¿Qué patrón descartaste porque agregaba complejidad sin aportar valor?
3. ¿Qué pruebas demuestran que el flujo logístico funciona y respeta sus límites?
4. ¿Qué puede fallar y cómo se entera el equipo?
5. ¿Qué señal te haría revisar una decisión?

No es necesario usar los diez patrones juntos. Un resultado sólido es una aplicación pequeña cuyos límites se entienden, con patrones elegidos por necesidad y evidencia que permita comprobar su comportamiento.
