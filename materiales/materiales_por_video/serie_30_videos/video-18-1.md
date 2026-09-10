# Video 18.1: Actividad 4: implementación e integración

## 📚 Fuentes relacionadas
- [Escalabilidad y rendimiento](https://platzi.com/cursos/software-avanzado/quarto-como-sitio-de-documentacion-viva/)
- [Resiliencia y tolerancia a fallos](https://platzi.com/cursos/software-avanzado/agentes-de-ia-que-revisan-tu-codigo-en-g/)

## 🔗 Navegación
[⬅️ Video anterior](video-18.md) | [➡️ Video siguiente](video-19.md)

## Propósito de esta actividad
Esta clase independiente sirve para construir un flujo ejecutable desde la entrada hasta una integración externa. Aquí no agregamos teoría nueva por acumular contenido: convertimos los videos del bloque anterior en una entrega concreta del proyecto.

## Caso obligatorio
crear un pedido debe validar, reservar inventario, calcular una ruta, persistir el resultado y comunicar el estado.

## Qué debes resolver

1. Define el problema sin empezar por una tecnología.
2. Identifica actores, necesidades y restricciones.
3. Delimita qué está dentro y fuera del sistema.
4. Propón al menos dos alternativas.
5. Compara costos, riesgos, calidad y facilidad de cambio.
6. Elige una opción y declara el trade-off.
7. Define cómo comprobarás que la decisión funciona.

## Entregables
código ejecutable, API, caso de uso, persistencia, adaptador externo, manejo de errores, README y evidencia de integración.

Todos los entregables deben quedar en GitHub con commits que muestren evolución y con un video de explicación y sustentación.

## Resolución modelo
Construimos un vertical slice en C# con controlador, caso de uso, dominio, repositorio y adaptador de rutas; los errores externos se convierten en respuestas controladas.

## 🧾 Ejemplo de entrega resuelta

### Flujo implementado
`POST /api/orders` recibe la solicitud, `CreateOrderUseCase` valida la regla, `IOrderRepository` persiste y `IRouteEstimator` consulta el proveedor de mapas.

### Adaptación de errores
Un timeout del proveedor no devuelve un error técnico al cliente. Se registra con `traceId`, el pedido queda pendiente y el operador recibe una tarea de revisión.

### Decisión
Usar puertos y adaptadores para que la API, la base de datos y el proveedor externo puedan cambiar sin contaminar el dominio.

### Evidencia
Código ejecutable, README, endpoint operativo, prueba de integración, adaptador externo y captura de una ejecución exitosa.


La solución no se evalúa por usar la tecnología más compleja. Se evalúa por comprender el problema, justificar la decisión y dejar evidencia verificable.

## Guion para la sustentación

1. Presenta el problema y explica por qué importa.
2. Identifica los actores afectados.
3. Muestra las alternativas consideradas.
4. Defiende la alternativa elegida.
5. Explica qué costo aceptaste.
6. Muestra la evidencia y la condición que obligaría a revisar la decisión.

## Criterio de cierre
La actividad está completa cuando una persona externa puede entender qué problema resolviste, por qué elegiste esa arquitectura y cómo sabrás si la decisión sigue siendo válida.
