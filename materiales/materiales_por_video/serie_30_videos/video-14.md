# Video 14: Cierre de fundamentos y transición

## Navegación
[⬅️ Video anterior: negociación e impacto social](video-13.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: método arquitectónico e IA](video-15.md)

## Para qué sirve esta transición
Este video no agrega otro patrón ni repite una clase de liderazgo. Funciona como un puente breve: convierte las preguntas de fundamentos en criterios para leer los videos aplicados que siguen.

La transición no significa dejar atrás los fundamentos. Significa usarlos para preguntar si una tecnología o patrón resuelve un problema del caso logístico y qué costo añade.

## 1. Recuerda el recorrido
En los fundamentos trabajaste preguntas como:

- ¿Qué problema del negocio necesita resolver el sistema?
- ¿Quién usa el sistema y quién puede verse afectado?
- ¿Qué condición debe seguir siendo verdadera?
- ¿Qué decisiones tienen consecuencias para operación, seguridad o evolución?
- ¿Cómo explicas por qué una alternativa conviene más que otra?

No tienes que memorizar nombres de patrones. Lo importante es poder volver a esas preguntas cuando aparece una propuesta técnica.

## 2. El puente hacia la plataforma logística
La empresa del caso no puede detener sus operaciones para reemplazar todo su sistema. Necesita mejorar pedidos, inventario y entregas mientras continúa atendiendo a clientes.

Antes de escoger herramientas, puedes resumir el problema:

> La empresa necesita consultar y coordinar pedidos y entregas con datos confiables, sin detener toda la operación ni exponer información de las personas.

Este resumen no es todavía una arquitectura. Es un punto de partida para estudiar una necesidad a la vez, comparar opciones y probarlas.

## 3. Convierte una pregunta grande en una práctica pequeña
Una pregunta como “¿qué arquitectura necesita toda la empresa?” es demasiado amplia para empezar. Puedes acotarla:

1. Elige un flujo, por ejemplo consultar una entrega.
2. Identifica quién participa y qué información necesita.
3. Describe qué ocurre cuando todo funciona y cuando falla una dependencia.
4. Compara una solución simple con una alternativa de mayor complejidad.
5. Define qué prueba te permitiría aprender si la decisión funciona.

Así, cada patrón de los siguientes videos responde a una pregunta concreta en vez de convertirse en una receta para todo el sistema.

## 4. Ejemplo: decidir qué hacer ante una entrega demorada
**Necesidad:** el cliente quiere saber si su paquete sigue avanzando.

**Actores:** cliente, repartidor, soporte y operación.

**Condición importante:** no presentar una ubicación desconocida como si fuera actual.

**Alternativa sencilla:** mostrar el último estado confirmado y su hora.

**Alternativa de mayor alcance:** consultar ubicación en tiempo real y calcular una nueva hora estimada.

**Costo y riesgo:** la segunda alternativa requiere obtener más datos, proteger su acceso y manejar demoras del proveedor. Puede aportar más detalle, pero también aumenta dependencias.

**Comprobación:** simular que el proveedor de ubicación no responde y comprobar que el estado confirmado sigue disponible y que la pantalla indica qué información falta.

Este ejemplo demuestra el tipo de razonamiento que usarás en la parte aplicada: primero contexto y personas; después diseño y tecnología.

## 5. Tu punto de partida para el bloque aplicado
Antes de estudiar cada herramienta, revisa si puedes explicar:

- qué necesidad concreta resolverías primero;
- qué actor recibe el beneficio y quién podría cargar con un riesgo;
- qué información sabes y cuál solo estás suponiendo;
- qué opción sencilla existe;
- qué evidencia te permitiría mantener o revisar la decisión.

Si una respuesta todavía es incierta, anótala como pregunta abierta. No hace falta inventar certeza para empezar a diseñar.

## Actividad de autoestudio
Elige una situación de la plataforma: pedido duplicado, falta de inventario, entrega demorada o devolución.

1. Describe el problema en dos frases sin nombrar tecnología.
2. Nombra a las personas afectadas.
3. Escribe un hecho y una suposición.
4. Propón una solución pequeña que permita aprender.
5. Define qué comprobarías antes de ampliar la solución.
6. Escribe una pregunta que esperas resolver en el bloque aplicado.

### Respuesta modelo
“Algunos pedidos aparecen dos veces y el almacén puede preparar el mismo paquete más de una vez. El operador necesita saber cuál registro es el válido”.

Hecho del ejercicio: el sistema puede recibir más de una solicitud para la misma compra. Suposición: la duplicación se debe a que la persona pulsa dos veces; habría que revisar registros para confirmarlo.

Una primera solución podría reconocer una clave única del pedido y rechazar duplicados. Antes de ampliar el diseño, comprobaría con una prueba que dos solicitudes iguales no creen dos pedidos.

Pregunta para el bloque aplicado: ¿cómo distinguirías una repetición válida del mismo pedido de una compra nueva?

## Comprueba tu comprensión
1. ¿Por qué el bloque aplicado sigue dependiendo de los fundamentos?
2. ¿Qué diferencia hay entre una necesidad y una tecnología?
3. ¿Qué haces cuando todavía no tienes evidencia suficiente?

### Respuestas
1. Los fundamentos ayudan a elegir y evaluar tecnologías según el problema, los actores y los riesgos.
2. La necesidad describe lo que alguien requiere; la tecnología es una forma posible de resolverlo.
3. Registras la suposición o pregunta pendiente y defines cómo obtener evidencia.

## Cierre
El aprendizaje de arquitectura no termina con una lista de conceptos. Continúa cuando aplicas esos conceptos a situaciones reales, justificas decisiones y compruebas sus consecuencias.

En los siguientes videos llevarás los fundamentos a herramientas y prácticas concretas. Conserva esta secuencia: entender el problema, conocer a las personas afectadas, comparar opciones, decidir y comprobar.
