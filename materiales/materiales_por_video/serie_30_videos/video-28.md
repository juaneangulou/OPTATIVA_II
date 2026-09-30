# Video 28: Fitness Functions, OpenTelemetry y caos

## Fuentes de este video
- [Fitness Functions para medir tu arquitectura](https://platzi.com/cursos/software-avanzado/fitness-functions-para-medir-tu-arquitec/)
- [Observabilidad con OpenTelemetry e ingeniería del caos](https://platzi.com/cursos/software-avanzado/observabilidad-en-sistemas-con-opentelem/)

## Navegación
[⬅️ Video anterior: máquinas de estado y seguridad](video-27.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: criterio y arquitectura responsable](video-29.md)

## Para estudiar por tu cuenta
Una decisión arquitectónica no queda protegida solo porque esté escrita. Un cambio futuro podría romperla sin que el equipo lo note. Este capítulo conecta tres herramientas: una comprobación repetible, datos para observar el sistema y un experimento controlado para comprobar su comportamiento ante fallos.

## 1. Fitness Function: comprobar una cualidad del sistema
Una **Fitness Function** (función de adecuación arquitectónica) es una prueba o medición que comprueba de manera repetible una característica importante del sistema.

Ejemplos:

- el dominio no depende directamente de EF Core;
- una consulta de seguimiento cumple el tiempo objetivo acordado;
- una falla de rutas no hace que la API invente una ubicación;
- el número de errores no supera el umbral definido para el servicio.

La función protege una pregunta concreta; no asigna una nota total a toda la arquitectura.

## 2. Define el objetivo antes del número
Supón que el equipo dice “el seguimiento debe ser rápido”. Esa frase no especifica cuánto ni cómo comprobarlo.

Una condición más útil sería: “En el entorno y carga de prueba acordados, el 95% de las consultas termina dentro de la meta de respuesta definida con producto”.

El **percentil 95** indica un punto que alcanza o mejora el 95% de las respuestas; ayuda a ver las más lentas sin usar solo un promedio. La meta exacta depende de la experiencia que necesita el producto, el costo y la capacidad; no se copia de otra aplicación sin contexto.

## 3. ¿Qué es OpenTelemetry?
**OpenTelemetry (OTel)** es un conjunto de herramientas y formatos para generar y transportar datos de observabilidad. No es necesariamente la base que almacena los datos ni el tablero donde aparecen los gráficos; normalmente se conecta con otras herramientas para guardarlos y mostrarlos.

Las tres señales más conocidas son:

- **Métrica:** número agregado, como cantidad de consultas o tiempo de respuesta.
- **Log:** registro de un hecho específico, como “el proveedor de rutas no respondió”.
- **Traza:** recorrido de una solicitud por componentes, como API → Pedidos → Rutas.

## 4. Sigue la consulta del pedido 245
Ana consulta el seguimiento. La API recibe su solicitud, Pedidos confirma que puede ver el pedido y Rutas devuelve la última ubicación.

Una traza podría mostrar:

```text
Consulta total:       1,8 s
API:                  0,1 s
Pedidos:              0,2 s
Rutas:                1,5 s
```

Esto indica que Rutas tomó la mayor parte del tiempo. La traza ayuda a localizar el paso; la métrica muestra si el problema se repite; el log conserva detalles de una solicitud concreta.

Evita incluir contraseñas, tokens, direcciones exactas u otros datos personales que el diagnóstico no necesita. Los identificadores de trazas ayudan a unir pasos relacionados y no deben contener datos sensibles.

## 5. Cómo se conectan las tres ideas
- La **Fitness Function** declara qué condición debe comprobarse.
- **OpenTelemetry** ayuda a observar qué hizo el sistema durante la comprobación.
- El **experimento de caos** introduce una falla controlada para probar una hipótesis de resiliencia.

Ejemplo:

> Hipótesis: si Rutas deja de responder, el cliente aún puede ver el estado confirmado del pedido y recibe un aviso claro sobre la ubicación faltante.

La prueba simula el fallo; OTel ayuda a observar cuánto espera la API y qué respuesta produce; la Fitness Function comprueba que no se pierda el estado confirmado y que la consulta termine dentro del límite acordado.

## 6. Experimento de caos seguro
Ingeniería del caos no significa romper sistemas al azar. Es probar de forma controlada cómo responde un sistema ante una falla posible.

Antes de empezar define:

1. **Hipótesis:** qué comportamiento esperas mantener.
2. **Alcance:** qué servicio y entorno participan.
3. **Datos de ensayo:** evita afectar pedidos reales.
4. **Señales:** qué métricas, logs y trazas observarás.
5. **Límite para detener:** qué error o efecto obliga a parar.
6. **Responsable de restaurar:** cómo volver al estado normal.

Si no sabes cómo detener el experimento o restaurar el servicio, todavía no está listo para ejecutarse.

## 7. Una Fitness Function como prueba
Una prueba de arquitectura puede afirmar que el sistema no convierte una falla de geolocalización en un falso estado “Entregado”. Otra puede revisar que el módulo de dominio no dependa directamente de infraestructura.

En C#, una prueba de comportamiento podría preparar un cliente de rutas que falle y comprobar que el caso de uso devuelve “ubicación no disponible” mientras conserva el estado del pedido. El doble de prueba simula la dependencia; una prueba separada verificará que la integración real produce las señales de OTel configuradas.

No necesitas automatizar todo en un solo test. Cada prueba debe tener un objetivo claro y un resultado que puedas explicar.

## 8. Riesgos y límites
- Una métrica promedio puede ocultar respuestas muy lentas.
- OTel transporta señales, pero no garantiza que alguien las revise.
- Una traza puede exponer datos sensibles si se instrumenta sin cuidado.
- Una falla de prueba que afecta a producción no es un experimento controlado.
- Una Fitness Function mal calibrada puede generar alertas constantes que nadie atiende.
- Pasar las comprobaciones no demuestra que todas las propiedades estén protegidas.

## 9. Actividad de autoestudio
Comprueba la hipótesis: “Si el proveedor de rutas no responde, el cliente todavía puede ver el estado confirmado del pedido y sabe que la ubicación falta”.

1. Elige el entorno y los datos que usarías.
2. Define una métrica, un log y una traza que observarías.
3. Escribe la Fitness Function en forma de condición verificable.
4. Define una señal para detener el experimento.
5. Describe cómo restaurarías y confirmarías el funcionamiento.

### Respuesta modelo
Empezaría con pedidos ficticios en un entorno aislado. Mediría los errores y la duración de consultas, registraría que Rutas no respondió y usaría la traza para confirmar cuánto esperó la API.

La Fitness Function podría comprobar que el estado del pedido se devuelve y que la respuesta identifica la ubicación como no disponible dentro del límite de espera acordado. Detendría la prueba si afecta servicios fuera del alcance o si no puedo restablecer Rutas. Después haría una consulta nueva para confirmar la recuperación.

## Comprueba lo que aprendiste
1. ¿Qué diferencia hay entre una métrica, un log y una traza?
2. ¿Qué pregunta responde una Fitness Function?
3. ¿Qué hace que una prueba de caos sea controlada?
4. ¿OpenTelemetry guarda y visualiza necesariamente todos los datos?

### Respuestas
1. La métrica resume números; el log registra hechos; la traza muestra el recorrido de una solicitud.
2. Si una condición arquitectónica concreta se cumple.
3. Tiene hipótesis, alcance, señales, límites de seguridad y plan de restauración.
4. No; OTel genera y transporta señales, y suele conectarse a otros sistemas que las almacenan o muestran.

## Taller aplicado: construir una Fitness Function operable
Escribe la condición completa para el seguimiento:

```text
Cuando Rutas no responde dentro del límite acordado,
la API debe devolver el último estado confirmado,
mostrar la hora de actualización,
identificar que la ubicación no está disponible
y registrar la correlación de la solicitud.
```

Ahora define cómo comprobarla: pedido ficticio, proveedor simulado, timeout controlado, métrica de duración, log de la falla y traza desde la API hasta Rutas. Establece un límite para detener el experimento y una consulta posterior que demuestre que el sistema se recuperó.

La función no debe medir “arquitectura buena” en abstracto. Debe proteger una propiedad concreta que importe al negocio y tener un dueño que revise sus fallos.

## Conclusión
Una Fitness Function comprueba una cualidad definida; OpenTelemetry aporta datos para observar el comportamiento; la ingeniería del caos prueba una hipótesis mediante fallos controlados. Juntas convierten una preocupación abstracta en evidencia, siempre que protejas a las personas y puedas restaurar el sistema.