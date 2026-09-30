# Video 21: Métricas y migración Strangler Fig

## Fuentes de este video
- [Métricas cuantitativas para evaluar arquitecturas limpias](https://platzi.com/cursos/software-avanzado/metricas-cuantitativas-para-evaluar-arqu/)
- [Strangler Fig para migrar arquitecturas limpias](https://platzi.com/cursos/software-avanzado/strangler-fig-para-migrar-arquitecturas/)

## Navegación
[⬅️ Video anterior: pre-mortem y pruebas de arquitectura](video-20.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: bases de datos y API Gateway](video-22.md)

## Para estudiar por tu cuenta
Una plataforma puede necesitar renovar una parte antigua sin apagar toda la operación. Si migras sin observar el resultado, no sabrás si el sistema nuevo realmente mejoró. Este capítulo conecta dos herramientas de decisión: medir una característica antes y después, y mover el tráfico por etapas mediante Strangler Fig.

## 1. El caso: seguimiento lento en el sistema antiguo
Los clientes consultan el estado de sus pedidos, pero la página demora y el equipo no sabe si la causa está en la base de datos, en una integración o en el código antiguo.

El equipo quiere reemplazar el seguimiento poco a poco por uno nuevo. Antes de empezar necesita una **línea base**: una medición de cómo se comporta hoy la función bajo condiciones anotadas.

Sin esa referencia, decir “el nuevo sistema es más rápido” sería una impresión, no una comparación.

## 2. Qué medir antes de migrar
Elige medidas relacionadas con la experiencia y el riesgo:

- cuántas consultas se completan y cuántas fallan;
- cuánto tardan, incluyendo las más lentas;
- cuántas muestran un estado que luego se corrige;
- qué costo operativo tiene mantener la parte actual.

No intentes medir todo. Elige una pregunta y una forma repetible de contestarla. Por ejemplo: “¿Cuántas consultas de seguimiento superan el tiempo acordado durante una muestra de tráfico habitual?”. El límite debe definirse con el producto y los usuarios; no existe un valor universal para todos los sistemas.

## 3. Strangler Fig: cambiar por partes
Strangler Fig es una estrategia de migración gradual. El sistema nuevo asume una función pequeña; el antiguo continúa atendiendo las demás. Una entrada decide a qué sistema enviar cada solicitud.

```text
Cliente -> Entrada de seguimiento -> Sistema nuevo (consulta elegida)
                                  -> Sistema antiguo (lo demás)
```

No tienes que migrar toda la aplicación de una vez. Puedes empezar con la consulta del estado para un grupo de pedidos o una función claramente delimitada.

## 4. Combina migración con medición
1. **Define la función y el grupo de prueba.** Por ejemplo, consulta de estado para pedidos de una zona de prueba.
2. **Mide la versión antigua.** Registra duración, errores y exactitud con la misma forma de medir que usarás luego.
3. **Copia el comportamiento necesario.** Implementa en el nuevo sistema solo la consulta elegida.
4. **Dirige una porción pequeña de solicitudes.** La mayoría continúa en el sistema antiguo.
5. **Compara resultados.** Revisa que el nuevo muestre el mismo estado correcto y que no empeore el tiempo ni los errores.
6. **Amplía o vuelve atrás.** Continúa si la evidencia cumple los objetivos; regresa al sistema anterior si aparece un fallo importante.

## 5. Qué significa tener un mecanismo para volver atrás
Volver atrás no es borrar los cambios del sistema. Significa poder cambiar el enrutamiento de esa función para que vuelva a atenderla el sistema antiguo mientras se investiga.

Antes de migrar, comprueba que:

- el sistema antiguo todavía puede responder;
- el mismo pedido no se modifica en ambos sistemas de forma incompatible;
- existe una métrica que permita detectar el problema;
- una persona sabe cómo detener la migración.

## 6. Tabla de comparación
| Qué se observa | Sistema antiguo, antes | Sistema nuevo, muestra de prueba | Qué significa |
|---|---|---|---|
| Consultas con error | 4 de cada 100 | 1 de cada 100 | El nuevo parece reducir fallas en esta muestra |
| Estado incorrecto | 0 detectados | 2 detectados | El nuevo no debe ampliarse todavía |
| Consultas lentas | 12 de cada 100 | 5 de cada 100 | Mejora aparente; se debe comprobar la misma carga |

Las cifras son inventadas para mostrar cómo leer la tabla. En un proyecto real, mide datos propios, períodos comparables y define qué resultado es aceptable antes de migrar.

El ejemplo también muestra por qué no basta con una métrica: el sistema nuevo es más rápido, pero muestra estados incorrectos. La exactitud del pedido es una condición prioritaria.

## 7. Actividad de autoestudio
La empresa quiere migrar la consulta de seguimiento, pero no puede detener la operación.

1. Define una función concreta que migrarías primero.
2. Elige dos medidas que registrarías en el sistema antiguo.
3. Describe cómo dirigirías una pequeña muestra al sistema nuevo.
4. Escribe dos condiciones para ampliar la migración.
5. Escribe una condición que obligaría a volver al sistema antiguo.
6. Explica cómo comprobarías que ambos muestran el estado correcto.

### Respuesta modelo
Empezaría con consultar el estado de pedidos de prueba. Mediría duración y errores antes y después, y compararía los estados obtenidos con una fuente verificada. Dirigiría un grupo pequeño de consultas al nuevo sistema mientras las demás siguen en el antiguo.

Ampliaría si la nueva versión muestra estados correctos y cumple los objetivos de tiempo y error acordados. Volvería atrás si aparecen estados falsos, se pierden consultas o se excede el límite de errores. Registrar el grupo, la hora y el resultado permite comparar muestras equivalentes.

## Comprueba lo que aprendiste
1. ¿Para qué sirve una línea base?
2. ¿Qué aporta Strangler Fig que no ofrece una reescritura de una vez?
3. ¿Una mejora en tiempo de respuesta basta para ampliar la migración?
4. ¿Qué es volver atrás en este contexto?

### Respuestas
1. Permite comparar el comportamiento anterior con el nuevo en condiciones conocidas.
2. Reduce el tamaño de cada cambio y mantiene funciones antiguas mientras se valida la nueva.
3. No; hay que comprobar exactitud y otras condiciones importantes.
4. Enviar nuevamente la función al sistema anterior mientras se corrige el nuevo.

## Taller aplicado: plan de migración de seguimiento
Construye un plan en cuatro cortes:

1. **Línea base:** mide latencia, errores, exactitud del estado y volumen de consultas del sistema actual.
2. **Corte pequeño:** mueve solo una consulta de prueba o una zona controlada al componente nuevo.
3. **Comparación:** registra qué versión atendió cada solicitud y compara resultados equivalentes.
4. **Decisión:** amplía, corrige o vuelve atrás según umbrales definidos antes del experimento.

El mecanismo para volver atrás debe ser operativo, no una frase. Define quién cambia el enrutamiento, cuánto tarda, qué datos deben permanecer compatibles y cómo se informa el incidente. Una migración madura conserva trazabilidad para explicar qué versión respondió a cada pedido.

## Conclusión
Strangler Fig limita el tamaño de una migración; las métricas muestran si cada paso aporta el resultado esperado. Define la línea base, migra una función pequeña, compara con datos equivalentes y conserva una forma de detener o revertir el cambio.