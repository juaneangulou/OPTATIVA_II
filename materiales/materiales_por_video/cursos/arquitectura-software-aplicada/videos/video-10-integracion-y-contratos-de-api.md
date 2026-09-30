# Video 10: Domain Driven Design para arquitectura limpia

## Para estudiar por tu cuenta
**Domain Driven Design** (DDD), o diseño guiado por el dominio, propone entender con profundidad el negocio antes de decidir cómo organizar el software. En vez de empezar por tablas o tecnologías, empezarás por las palabras, reglas y procesos que usan las personas que realizan el trabajo.

En esta clase aplicarás DDD al ciclo de un pedido logístico y aprenderás a distinguir algunos conceptos que después pueden reflejarse en el código.

## 1. ¿Qué es el dominio?
El **dominio** es el área de actividad que el sistema ayuda a resolver. En una plataforma logística incluye vender productos, preparar pedidos, mantener inventario y entregar paquetes.

Un arquitecto aprende cómo ocurre el trabajo real y pregunta a quienes lo realizan. No basta con copiar el nombre de una tabla o convertir cada formulario en una clase.

## 2. Construye un lenguaje compartido
El **lenguaje ubicuo** es el conjunto de palabras que las personas del negocio y el equipo técnico acuerdan usar con el mismo significado.

Por ejemplo, en una conversación, “pedido confirmado” puede significar que el cliente terminó de comprar; para operaciones, alguien podría entender que el paquete ya salió. Si ambos significados se mezclan, una entrega puede iniciarse antes de que el paquete esté listo.

Para cada palabra importante, pregunta:

- ¿Qué significa exactamente?
- ¿En qué momento cambia?
- ¿Quién puede confirmarla?
- ¿Qué evidencia muestra que ocurrió?

## 3. Entidad y objeto de valor
Una **entidad** es algo que conserva su identidad aunque cambien algunos datos. Un pedido puede cambiar de estado, pero sigue siendo el pedido 245.

Un **objeto de valor** describe una característica mediante su contenido y no mediante un identificador propio. Una dirección puede representarse por calle, ciudad y código postal; interesa que esos valores sean válidos juntos.

Esta distinción ayuda a poner las reglas donde el equipo puede encontrarlas. No es una regla para convertir cada dato en una clase; se usa cuando aporta significado y validación.

## 4. Protege reglas que deben cumplirse siempre
Una regla importante del dominio, a veces llamada **invariante**, es una condición que debe cumplirse aunque la pantalla, la base de datos o el servicio externo cambien.

Ejemplos:

- Un pedido no se confirma con una cantidad menor o igual a cero.
- Una entrega no se marca como recibida sin la evidencia requerida.
- Un pedido cancelado no vuelve a “En camino” sin un proceso explícito.

Estas reglas deben vivir en una parte del diseño que se pueda probar directamente, no solo en mensajes de pantalla.

## 5. Un ejemplo sencillo en C#
```csharp
public sealed class Pedido
{
	private readonly List<LineaPedido> lineas = [];

	public Guid Id { get; }
	public string Estado { get; private set; } = "Pendiente";

	public Pedido(Guid id) => Id = id;

	public void AgregarLinea(string productoId, int cantidad)
	{
		if (cantidad <= 0)
			throw new ArgumentOutOfRangeException(nameof(cantidad));

		lineas.Add(new LineaPedido(productoId, cantidad));
	}
}

public sealed record LineaPedido(string ProductoId, int Cantidad);
```

`Pedido` conserva las líneas y evita agregar cantidades inválidas. `private set` impide que cualquier parte cambie el estado directamente; una operación del dominio debería controlar las transiciones permitidas.

Este ejemplo es deliberadamente pequeño. Todavía habría que definir cómo se confirma el pedido, qué reglas de stock aplican y cómo se guarda. DDD empieza aclarando esas reglas, no agregando capas por apariencia.

## 6. ¿Cómo se convierte el lenguaje en arquitectura?
1. Habla del proceso con ejemplos reales.
2. Anota términos ambiguos y acuerda su significado.
3. Identifica reglas que no deben romperse.
4. Agrupa datos y reglas que cambian juntos.
5. Define qué información necesita otra parte y qué contrato la comunica.
6. Solo entonces decide módulos, clases y persistencia.

DDD puede aplicarse dentro de una aplicación sencilla. No obliga a usar microservicios, una base por dominio ni una herramienta específica.

## 7. Actividad de autoestudio
Analiza el proceso de devolución de un pedido:

1. Anota cinco palabras que usaría soporte o almacén.
2. Para cada una, escribe una definición concreta.
3. Identifica una entidad y un objeto de valor posibles.
4. Escribe dos condiciones que siempre deberían cumplirse.
5. Describe una duda que debas confirmar con alguien que conozca el proceso real.

### Respuesta modelo
Palabras: devolución solicitada, producto recibido, motivo, reembolso y revisión. “Devolución solicitada” no significa que el producto ya llegó al almacén; es solo una petición. El pedido puede ser una entidad con identificador; el motivo puede ser un objeto de valor si se valida por su contenido.

Una condición puede ser que no se procese la devolución de un pedido inexistente. Otra, que un reembolso solo se solicite después de confirmar los requisitos del negocio. La política real —por ejemplo, plazos y excepciones— debe confirmarse con la organización; no conviene inventarla.

## Comprueba lo que aprendiste
1. ¿Qué hace que “pedido confirmado” necesite una definición compartida?
2. ¿Qué diferencia hay entre una entidad y un objeto de valor?
3. ¿DDD obliga a crear microservicios?

**Respuestas:** un término ambiguo puede causar acciones distintas; una entidad conserva identidad y un objeto de valor se define por sus datos; no, DDD ayuda a entender y modelar el dominio y puede usarse dentro de una sola aplicación.

## Conclusión
DDD comienza por comprender el negocio y sus palabras. Al modelar entidades, valores y reglas con significados acordados, el código puede proteger decisiones importantes y seguir siendo entendible cuando cambian pantallas o herramientas.
