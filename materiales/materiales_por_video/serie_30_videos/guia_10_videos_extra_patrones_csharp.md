# Ruta complementaria: 10 videos de patrones de arquitectura en C#

## Propósito
Esta ruta amplía el curso de Arquitectura de Software Aplicada con diez prácticas de arquitectura y patrones implementados en C# y .NET. Parte de la plataforma logística del curso: pedidos, inventario, entregas, rutas, notificaciones y atención al cliente.

El objetivo no es mostrar patrones como recetas ni afirmar que deban usarse todos juntos. En cada video se parte de una necesidad del sistema, se implementa una opción sencilla, se observan sus límites y se explica cuándo tendría sentido cambiarla.

Esta selección cubre patrones frecuentes de arquitectura en aplicaciones .NET. No es una lista literal de todos los patrones posibles; existen muchos y no todos aportan valor al mismo proyecto.

## Para quién es
La guía está escrita para estudiar por cuenta propia. Conviene conocer los fundamentos de C#: clases, interfaces, colecciones, excepciones y lectura básica de código. No hace falta dominar infraestructura o microservicios antes de empezar.

Las prácticas pueden realizarse en una solución ASP.NET Core sencilla. Usa una versión LTS de .NET que tenga soporte al grabar y fija la versión en el repositorio del ejercicio. No copies números de versión de esta guía sin revisar el soporte vigente.

## Proyecto que se construye durante la ruta
A lo largo de los diez videos ampliarás una API para una plataforma logística. El alcance inicial se mantiene pequeño:

1. Registrar un pedido.
2. Confirmar si hay inventario.
3. Preparar una entrega.
4. Consultar el estado del pedido.
5. Informar problemas sin perder trazabilidad.

Cada video agrega una decisión al mismo proyecto. No hace falta desplegar diez sistemas diferentes ni convertir cada parte en un microservicio.

## Ruta de videos

### Video extra 1: Monolito modular en C#: organizar el sistema sin microservicios
**Pregunta:** ¿Cómo mantener una aplicación sencilla sin mezclar todas sus responsabilidades?

- **Conceptos:** monolito modular, módulo, límite, feature slice y composition root.
- **Práctica en C#:** organizar `Pedidos`, `Inventario` y `Entregas` por capacidad, cada una con sus solicitudes, reglas y persistencia claramente delimitadas. Implementar el caso “crear pedido” de punta a punta dentro de un módulo.
- **Buena práctica:** empezar con módulos dentro de un solo despliegue cuando el problema no justifica distribuirlos. No crear una carpeta genérica por cada tipo de archivo si eso hace difícil seguir una funcionalidad completa.
- **Evidencia:** diagrama de módulos, árbol de carpetas y una prueba que demuestre que un módulo no accede a los datos internos de otro.
- **Qué debes poder explicar:** modular no significa microservicios; el monolito puede tener límites explícitos.

### Video extra 2: Arquitectura hexagonal en C#: separar reglas y herramientas
**Pregunta:** ¿Cómo evitar que las reglas del pedido dependan de ASP.NET Core o de Entity Framework Core?

- **Conceptos:** dominio, caso de uso, puerto, adaptador y dirección de dependencias.
- **Práctica en C#:** implementar `ConfirmarPedido` con una interfaz para consultar inventario; conectar esa interfaz a un adaptador de infraestructura y probar el caso de uso sin iniciar una base de datos.
- **Buena práctica:** las interfaces se crean para proteger un límite útil, no por obligación. Los controladores traducen HTTP; los casos de uso coordinan el flujo; las reglas importantes permanecen independientes del framework.
- **Evidencia:** diagrama sencillo de dependencias y prueba del caso de uso usando una implementación de prueba del puerto.
- **Qué debes poder explicar:** Clean Architecture y Hexagonal Architecture comparten la intención de proteger las reglas; sus nombres no obligan a una única estructura de carpetas.

### Video extra 3: Repositorios con EF Core en C#: cuándo abstraer el acceso a datos
**Pregunta:** ¿Cómo guardar y consultar pedidos sin acoplar las reglas de negocio al almacenamiento?

- **Conceptos:** repositorio, unidad de trabajo, seguimiento de cambios, transacción y persistencia.
- **Práctica en C#:** persistir un pedido y sus líneas con EF Core; definir qué interfaz necesita el caso de uso y probar el comportamiento usando una base de datos de prueba.
- **Buena práctica:** EF Core ya implementa ideas parecidas a Repository y Unit of Work. No agregues un repositorio genérico sobre cada `DbSet` si no mejora el límite, la prueba o la claridad. Evita devolver entidades de EF directamente desde la API.
- **Evidencia:** prueba de integración que guarda y vuelve a leer un pedido, más una explicación de dónde comienza y termina la transacción.
- **Qué debes poder explicar:** una capa adicional no es automáticamente mejor; conserva solo abstracciones que resuelven un problema concreto.

### Video extra 4: CQRS en C#: separar consultas y cambios sin duplicar el sistema
**Pregunta:** ¿Las operaciones que cambian datos necesitan la misma forma que las consultas que los muestran?

- **Conceptos:** comando, consulta, modelo de escritura y modelo de lectura. CQRS significa separar responsabilidades de lectura y escritura; no exige dos bases de datos.
- **Práctica en C#:** implementar `ConfirmarPedido` como comando y `ConsultarSeguimiento` como consulta. Crear una respuesta de lectura específica para la pantalla del cliente.
- **Buena práctica:** comienza con una separación lógica dentro de la misma aplicación y la misma base de datos. Añade almacenamiento independiente solo si una necesidad medida lo justifica. Usa nombres que expresen intención y no conviertas cada método en un objeto si no mejora la claridad.
- **Evidencia:** dos pruebas: una verifica que el comando aplica la regla de negocio y otra que la consulta devuelve solo los datos necesarios.
- **Qué debes poder explicar:** CQRS no es Event Sourcing. Puedes separar lectura y escritura y seguir guardando el estado actual.

### Video extra 5: Patrón Decorator en C#: validar y registrar sin duplicar lógica
**Pregunta:** ¿Cómo aplicar validación, medición o registro sin copiar el mismo código en cada caso de uso?

- **Conceptos:** preocupación transversal, Decorator, pipeline y composición de dependencias.
- **Práctica en C#:** envolver el manejo de una solicitud para validar datos, medir duración y registrar errores de forma consistente antes y después del caso de uso.
- **Buena práctica:** conserva el orden de ejecución visible y evita que el registro incluya contraseñas o datos personales innecesarios. No uses un pipeline para esconder reglas de negocio que deberían poder leerse en el caso de uso.
- **Evidencia:** prueba que demuestra el orden esperado de validación y ejecución, y un registro estructurado de una solicitud de ensayo.
- **Qué debes poder explicar:** Decorator añade un comportamiento alrededor de otro; no debería cambiar silenciosamente la intención del caso de uso.

### Video extra 6: Transactional Outbox en C#: guardar datos y publicar eventos de forma confiable
**Pregunta:** ¿Cómo guardar un pedido y anunciar su confirmación sin perder uno de los dos pasos?

- **Conceptos:** transacción local, Outbox, publicación posterior, consumidor y operación idempotente.
- **Práctica en C#:** guardar el pedido y un registro Outbox en la misma transacción de EF Core; publicar los registros pendientes con un proceso separado; hacer que el consumidor detecte eventos repetidos.
- **Buena práctica:** asume que un mensaje podría entregarse más de una vez. No prometas “exactamente una vez” si el diseño no puede garantizarlo de extremo a extremo. No marques un registro como publicado antes de confirmar que el envío ocurrió.
- **Evidencia:** prueba que simula una caída entre guardar el pedido y publicar el aviso; al reiniciar, el mensaje se publica y no se crea un segundo pedido.
- **Qué debes poder explicar:** Outbox resuelve la brecha entre guardar datos y publicar mensajes; requiere limpieza, reintentos y observación de registros atascados.

### Video extra 7: Process Manager en C#: coordinar un flujo logístico de varios pasos
**Pregunta:** ¿Cómo coordinar reserva de inventario, asignación de entrega y cancelación cuando no hay repartidor?

- **Conceptos:** saga, Process Manager, estado duradero, pasos, resultados y compensación.
- **Práctica en C#:** modelar el flujo de un pedido con estados explícitos; solicitar reserva; esperar resultado de asignación; si el proceso no puede continuar, liberar la reserva y registrar el motivo.
- **Buena práctica:** guarda el estado del proceso, relaciona cada mensaje con el identificador del pedido y diseña pasos seguros ante repeticiones. Una compensación es una nueva acción que corrige un efecto; no siempre borra lo ocurrido.
- **Evidencia:** prueba del camino exitoso y del camino de fallo, incluyendo una respuesta duplicada.
- **Qué debes poder explicar:** una saga coordina una operación de varios pasos sin una única transacción que abarque todos los servicios.

### Video extra 8: Resiliencia en C#: proteger llamadas a servicios externos
**Pregunta:** ¿Cómo proteger la aplicación cuando fallan los servicios de geolocalización o notificaciones?

- **Conceptos:** timeout (límite de espera), reintento limitado, circuit breaker (cortacircuitos) y fallback (respuesta alternativa).
- **Práctica en C#:** configurar un cliente HTTP tipado con políticas de resiliencia mediante las extensiones compatibles con la versión .NET elegida. Simular lentitud y errores del proveedor de rutas.
- **Buena práctica:** solo reintenta automáticamente operaciones que se puedan repetir sin duplicar efectos; limita cantidad y duración; propaga `CancellationToken`; no uses un fallback que presente datos antiguos como actuales.
- **Evidencia:** prueba o demostración que muestra que una llamada lenta termina dentro del límite y que el fallo se comunica sin bloquear indefinidamente el flujo.
- **Qué debes poder explicar:** un cortacircuitos no repara al proveedor; evita insistir mientras está fallando y permite que el sistema responda de forma controlada.

### Video extra 9: Cache-Aside en C#: acelerar consultas y cuidar la actualidad de los datos
**Pregunta:** ¿Cómo acelerar la lectura frecuente del seguimiento sin mostrar datos desactualizados indefinidamente?

- **Conceptos:** caché, Cache-Aside, expiración, invalidación y consistencia.
- **Práctica en C#:** consultar primero una caché; si el dato no existe, leerlo de la fuente principal, devolverlo y guardarlo temporalmente. Al cambiar el estado del pedido, invalidar o actualizar la entrada relacionada.
- **Buena práctica:** mide antes y después; establece una expiración; evita almacenar secretos o información personal sin necesidad; considera qué sucede si la caché se pierde. No conviertas la caché en la única fuente de verdad.
- **Evidencia:** prueba de lectura repetida y prueba de actualización que comprueba que el siguiente lector no recibe un estado antiguo fuera del límite acordado.
- **Qué debes poder explicar:** una caché puede mejorar velocidad a cambio de memoria, complejidad de invalidación y posible desactualización.

### Video extra 10: Pruebas de arquitectura en C#: proteger límites y reglas del sistema
**Pregunta:** ¿Cómo demostrar que la solución completa mantiene sus límites y puede evolucionar?

- **Conceptos:** pruebas unitarias, integración, pruebas de arquitectura, contrato de API y revisión de seguridad básica.
- **Práctica en C#:** completar el flujo “crear pedido → reservar inventario → asignar entrega → consultar estado”; agregar una prueba que impida dependencias no permitidas entre módulos y ejecutar pruebas de integración con una base de datos de ensayo.
- **Buena práctica:** usa mocks para aislar reglas cuando aporten claridad, pero comprueba integraciones reales con pruebas de integración. Mantén configuraciones y secretos fuera del código; valida entradas y permisos en el servidor; devuelve errores consistentes sin filtrar detalles internos.
- **Evidencia:** diagrama actualizado, decisiones ADR breves, pruebas ejecutadas, resultados y una explicación de qué riesgos siguen pendientes.
- **Qué debes poder explicar:** una prueba de arquitectura protege una regla estructural de forma repetible, pero no demuestra por sí sola que todo el sistema sea correcto.

## Buenas prácticas C#/.NET que atraviesan la serie

### Diseño y dependencias
- Mantén el dominio libre de referencias a ASP.NET Core, EF Core y proveedores externos cuando una frontera independiente tenga valor.
- Usa inyección de dependencias en el punto de composición de la aplicación; evita localizar servicios globalmente o usar estado estático compartido.
- Prefiere interfaces pequeñas con propósito claro. No crees interfaces solo porque una clase exista.
- Mantén controladores y endpoints delgados: traducen la solicitud y delegan el caso de uso.
- No expongas directamente entidades de persistencia como contratos públicos de API.

### C# moderno y confiable
- Activa nullable reference types y trata las advertencias importantes como señales que requieren explicación.
- Usa `async`/`await` para operaciones de entrada/salida; evita bloquear con `.Result` o `.Wait()`.
- Propaga `CancellationToken` en operaciones que puedan tardar.
- Valida los datos en los límites de entrada y mantén invariantes importantes dentro del dominio.
- Usa tipos y nombres que expresen intención; evita métodos gigantes, clases “Manager” sin responsabilidad concreta y capturas genéricas de excepciones que oculten fallos.

### Persistencia e integración
- Define transacciones alrededor de operaciones de negocio que deban guardarse juntas.
- No hagas llamadas de red dentro de transacciones de base de datos largas.
- Diseña consumidores que toleren duplicados cuando el transporte pueda repetir mensajes.
- Limita reintentos y conserva evidencia de tareas fallidas para poder investigarlas.
- Versiona contratos y cambios de base de datos; coordina cambios incompatibles con sus consumidores.

### Seguridad y operación
- No guardes contraseñas, tokens ni claves en Git ni en logs.
- Aplica autorización en el servidor para cada recurso; ocultar un botón en la interfaz no protege los datos.
- Registra información estructurada y útil, pero minimiza datos personales.
- Devuelve errores comprensibles al cliente y conserva detalles técnicos en registros protegidos.
- Mide rendimiento, errores y saturación antes de optimizar o agregar infraestructura.

### Pruebas y mantenibilidad
- Prueba las reglas críticas del negocio de forma aislada.
- Prueba la integración con la base de datos y servicios reales en entornos de ensayo.
- Incluye casos de error, cancelación, duplicación y datos incompletos, no solo el camino feliz.
- Ejecuta formato, análisis y pruebas en integración continua.
- Documenta decisiones significativas y la condición que las haría revisarse.

## Formato sugerido para cada video
Cada video de la serie puede seguir esta secuencia de autoestudio:

1. Problema que enfrenta la plataforma logística.
2. Explicación en palabras sencillas del patrón.
3. Alternativa sencilla y límites que presenta.
4. Implementación paso a paso en C#.
5. Pruebas del comportamiento esperado y de un fallo.
6. Buenas prácticas y errores frecuentes.
7. Decisión: cuándo usar el patrón y cuándo no.
8. Ejercicio, solución razonada y evidencia para el repositorio.

## Resultado final de la ruta
Al terminar, tendrás una aplicación C# pequeña pero coherente y un expediente que explica por qué se usaron los patrones, qué se decidió no implementar y cómo se verifican los comportamientos importantes.

La meta no es usar los diez patrones en cualquier aplicación. La meta es poder reconocer qué problema resuelve cada uno, implementar una versión comprensible y evitar complejidad cuando no aporta valor.
