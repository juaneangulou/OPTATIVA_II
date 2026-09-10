# Video 10: Testing, DevOps y entrega continua

## 📚 Lecturas de referencia: comprobar y entregar con confianza
- [Testing y validación de arquitectura](https://platzi.com/cursos/fundamentos-arquitectura-software/paradigmas-y-principios-solid-explicados/)
- [DevOps y automatización de entrega](https://platzi.com/cursos/fundamentos-arquitectura-software/que-hace-limpia-a-una-arquitectura-de-so/)

## 🔗 De observar incidentes a prevenirlos
[⬅️ Video anterior](video-09.md) | [➡️ Video siguiente](video-11.md)

## 🎯 El cambio que no debe romper una entrega
El equipo modifica la regla de confirmación: ahora un pedido solo puede confirmarse si tiene inventario reservado y una ruta viable. En el computador de quien programó funciona. Sin embargo, nadie ejecutó pruebas en otro entorno y el viernes el despliegue manual publica una versión que permite confirmar pedidos sin ruta.

El actor más afectado es **el cliente**, porque puede recibir una promesa de entrega que la operación no puede cumplir. El segundo actor es **el equipo de operación**, porque debe corregir pedidos ya confirmados. La regla que protegemos es: **un pedido no puede pasar a Confirmed si Inventario o Ruteo informan que el flujo no es viable**.

## La prueba que protege la regla
```csharp
public sealed class ConfirmOrderUseCaseTests
{
        [Fact]
        public async Task Does_not_confirm_when_route_is_not_viable()
        {
                var inventory = new FakeInventoryAvailability(hasStock: true);
                var routes = new FakeRoutePlanning(isViable: false);
                var useCase = new ConfirmOrderUseCase(inventory, routes);
                var order = Order.Create("cliente@correo.com", 150_000m);

                await Assert.ThrowsAsync<InvalidOperationException>(
                        () => useCase.ConfirmAsync(order));

                Assert.Equal(OrderStatus.Pending, order.Status);
        }
}
```

Esta prueba no comprueba que un método privado fue llamado ni que un mock recibió una llamada exacta. Comprueba comportamiento: cuando Ruteo no ofrece una ruta viable, el pedido sigue pendiente. Ese es el tipo de prueba que protege una decisión arquitectónica.

## 🧩 Cómo leer esta prueba en .NET
`public sealed class ConfirmOrderUseCaseTests` es una clase de pruebas. `sealed` indica que no se diseñó para herencia; cada prueba debe ser simple e independiente. `[Fact]` es un atributo de xUnit que marca un método como caso de prueba sin parámetros.

`async Task` permite esperar operaciones asíncronas. `await Assert.ThrowsAsync<InvalidOperationException>(...)` verifica que el caso de uso rechaza el pedido. `Assert.Equal` compara el estado final. Los nombres `FakeInventoryAvailability` y `FakeRoutePlanning` indican implementaciones controladas para pruebas: no abren una base de datos ni llaman una API real.

El modificador `public` permite que xUnit descubra la prueba. Las variables `var inventory` y `var routes` son locales al método: viven solo durante esa prueba. En producción, las mismas interfaces reciben adaptadores reales mediante inyección de dependencias; en la prueba reciben falsos controlados.

## Dos estrategias de entrega
### Opción A: probar y desplegar manualmente
Cada desarrollador ejecuta lo que recuerda en su máquina y alguien publica archivos en producción. Es rápida al inicio, pero no garantiza que se ejecuten pruebas, que la configuración sea correcta ni que el artefacto desplegado sea el que se revisó.

### Opción B: pipeline que valida antes de publicar
Cada cambio ejecuta restauración, compilación, pruebas y análisis. Solo si esas etapas pasan se crea un artefacto versionado y se despliega. La entrega tarda unos minutos más, pero elimina pasos manuales y deja evidencia de qué versión superó las pruebas.

Para la plataforma elijo B. No significa que el pipeline reemplace el criterio humano; significa que los controles repetibles no dependen de que alguien los recuerde bajo presión.

## Pipeline mínimo
```yaml
name: verify-order-flow
on: [pull_request]

jobs:
    test:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v4
            - uses: actions/setup-dotnet@v4
                with:
                    dotnet-version: 8.0.x
            - run: dotnet restore
            - run: dotnet build --configuration Release --no-restore
            - run: dotnet test --configuration Release --no-build
```

Este flujo se ejecuta en cada pull request. `dotnet restore` descarga dependencias; `dotnet build` compila; `dotnet test` ejecuta los casos de prueba. `--no-restore` y `--no-build` evitan repetir trabajo en las últimas etapas porque ya se hicieron antes. Si falla una prueba, el cambio no debería fusionarse hasta entender la causa.

## Preguntas y respuestas
### ¿Qué tan bien validamos la estructura del sistema?

La validamos cuando una prueba comprueba una regla relevante y una revisión confirma que Pedidos depende de contratos, no de infraestructura concreta. En este caso, la prueba demuestra que una ruta inviable no confirma el pedido; una prueba de integración puede demostrar después que el adaptador de rutas traduce correctamente la respuesta externa.

### ¿Qué tan fácil es detectar un problema antes de producción?

Debe detectarse en el pull request. Si el cambio rompe la regla de confirmación, `dotnet test` falla antes de crear un artefacto. Si el pipeline solo se ejecuta después de desplegar, el control llega demasiado tarde.

### ¿Qué tan automatizado está el proceso de entrega?

Está automatizado cuando restaurar, compilar, probar y generar el artefacto ocurren con el mismo pipeline para todos. Una lista de pasos en un documento no es automatización; es una tarea manual que puede olvidarse.

## Actividad: protege un cambio con una prueba y un pipeline

1. Implementa la regla de confirmación en `ConfirmOrderUseCase`.
2. Crea dos falsos: uno con inventario disponible y otro con ruta inviable.
3. Escribe una prueba que confirme que el pedido sigue `Pending` cuando falle Ruteo.
4. Escribe una segunda prueba de caso feliz con inventario y ruta viable.
5. Crea `.github/workflows/verify-order-flow.yml` con `restore`, `build` y `test`.
6. Introduce temporalmente un error en la regla y observa que la prueba falla.
7. Corrige el error, ejecuta el pipeline y guarda el enlace o captura de la ejecución exitosa.

## Cómo comprobar que terminaste
Tu solución está completa si puedes mostrar una prueba que falla cuando la regla se rompe, una prueba que pasa cuando el flujo es válido y una ejecución de GitHub Actions que impide integrar el cambio defectuoso.

## Cierre
Probar no es confirmar que el código compila. Entregar continuamente no es desplegar muchas veces. Ambas prácticas construyen una barrera confiable entre una idea y un cambio que llega a producción. En el siguiente video estudiaremos cómo estimar el costo y el riesgo de evolucionar esa arquitectura.
