# Video 28: Observabilidad en sistemas con OpenTelemetry e ingeniería del caos

## Para estudiar por tu cuenta
Una plataforma logística puede parecer saludable hasta que un cliente espera demasiado por el seguimiento de su pedido. Para entender qué pasó necesitamos datos que muestren el recorrido de las solicitudes. Y para saber si el sistema puede recuperarse, a veces debemos provocar una falla controlada y observar su respuesta.

En esta clase aprenderás qué aporta **OpenTelemetry**, qué son métricas, registros y trazas, y cómo la **ingeniería del caos** prueba una hipótesis de resiliencia sin convertir una falla en una sorpresa para usuarios.

## 1. El problema: un pedido pasa por varias partes
Cuando Ana consulta su pedido 245, la solicitud puede pasar por la aplicación, una API Gateway, el servicio de pedidos y el servicio de rutas. Si la pantalla tarda, ¿qué parte se demoró? Sin información del recorrido, el equipo puede adivinar o revisar cada componente a ciegas.

**Observabilidad** significa poder investigar lo que ocurre dentro de un sistema usando la información que el sistema produce mientras funciona. No es únicamente ver si un servidor está encendido; también es entender por qué una solicitud falló o tardó.

## 2. Tres formas de observar

### Métricas: números que resumen el comportamiento
Una **métrica** es una medida que se observa a lo largo del tiempo. Por ejemplo:

- Cuántas consultas de seguimiento se recibieron.
- Cuántas fallaron.
- Cuánto tardaron en responder.

Las métricas ayudan a ver tendencias, como un aumento de errores o un tiempo de respuesta que empeora durante la tarde. No explican por sí solas qué pedido causó un problema.

### Registros o logs: notas sobre hechos concretos
Un **log** es una anotación de algo que ocurrió, como “la consulta del pedido 245 no encontró el servicio de rutas”.

Los logs ayudan a investigar un caso particular. Deben evitar contraseñas, datos personales innecesarios y otra información que no debería quedar visible.

### Trazas: el recorrido de una solicitud
Una **traza** sigue una solicitud a través de varios componentes. Cada paso medido se llama a menudo **span** o tramo.

Para el pedido 245, la traza podría mostrar:

```text
Consulta del pedido: total 2,4 s
	Gateway:             0,1 s
	Servicio de pedidos: 0,2 s
	Servicio de rutas:   2,1 s
```

Esta traza sugiere que la mayor parte del tiempo se consumió esperando a rutas. El equipo ya tiene una pista concreta, no solo “la aplicación está lenta”.

## 3. ¿Qué es OpenTelemetry?
**OpenTelemetry**, abreviado **OTel**, es un conjunto de herramientas y acuerdos abiertos para crear y transportar datos de observabilidad, como métricas, logs y trazas.

Una analogía: OTel ayuda a que distintos componentes escriban sus mediciones en un formato que otros sistemas pueden recibir. No es automáticamente el tablero donde ves gráficos ni una base de datos que guarda para siempre toda la información. Normalmente se conecta a otros componentes que almacenan, buscan o muestran esos datos.

La idea útil es reducir la dependencia de un formato cerrado y poder seguir una solicitud entre partes diferentes. Para que funcione, cada servicio debe incluir información de contexto que permita reconocer que los pasos pertenecen al mismo recorrido.

## 4. Sigamos una consulta con una traza
1. Ana pulsa “Ver mi pedido”. La aplicación crea una solicitud de seguimiento.
2. La Gateway recibe la solicitud y registra el comienzo del recorrido.
3. Pedidos confirma que el pedido existe.
4. Rutas busca la última actualización.
5. La Gateway devuelve la respuesta.

Si cada parte comparte el identificador de esa consulta, una herramienta puede mostrar los pasos juntos como una sola traza. Así el equipo puede observar dónde se acumuló el tiempo o en qué paso apareció el error.

El identificador de traza no debe contener información personal. Es una etiqueta técnica para conectar registros relacionados.

## 5. ¿Qué es ingeniería del caos?
La **ingeniería del caos** es una forma controlada de comprobar cómo responde un sistema ante fallas que podrían ocurrir en la realidad.

No significa romper el sistema al azar ni probar cuánto daño se puede causar. Primero se formula una hipótesis, se delimita el experimento y se establecen condiciones para detenerlo.

Ejemplo de hipótesis:

> “Si el servicio de rutas deja de responder durante un minuto, el cliente todavía podrá ver el estado del pedido y recibirá un mensaje claro de que la ubicación no está disponible”.

El experimento debe comprobar esa afirmación. Si la pantalla queda esperando indefinidamente o muestra una ubicación inventada, la hipótesis no se cumplió y el equipo debe mejorar el sistema.

## 6. Experimento seguro, paso a paso

### Paso 1: define el comportamiento normal
Antes de provocar una falla, confirma cómo funciona el seguimiento cuando todos los servicios responden. Es la referencia para comparar.

### Paso 2: elige una falla pequeña y específica
Por ejemplo, hacer que una instancia de pruebas del servicio de rutas no responda. No desconectes varios servicios a la vez, porque sería difícil entender qué causó el resultado.

### Paso 3: define quién y qué podrían verse afectados
Empieza con datos ficticios y un entorno de pruebas. Si el ejercicio afecta un entorno real, requiere autorización, límites más estrictos, comunicación y un plan de interrupción inmediata.

### Paso 4: observa durante el experimento
Usa métricas para ver solicitudes y errores, logs para estudiar casos y trazas para localizar el paso afectado.

### Paso 5: decide cuándo parar
Detén el experimento si afecta usuarios no incluidos, si las métricas superan el límite seguro o si los datos se comportan de forma inesperada.

### Paso 6: restaura y comprueba la recuperación
Vuelve a habilitar el servicio y confirma que el sistema recuperó su funcionamiento. Documenta qué aprendiste y qué cambio se hará después.

## 7. Las guardas de seguridad del experimento
Antes de iniciar, define:

- **Alcance:** qué servicio, entorno y solicitudes participan.
- **Hipótesis:** qué comportamiento debe mantener el sistema.
- **Señal normal:** qué métricas o resultados mostrarán que el sistema está sano.
- **Límite de seguridad:** qué condición obliga a detenerse.
- **Responsable:** quién observa y puede cancelar la prueba.
- **Restauración:** cómo devolver el sistema a su estado normal.
- **Comunicación:** a quién avisar antes, durante y después.

Si no puedes explicar cómo detener la prueba y restaurar el sistema, no empieces el experimento.

## 8. OpenTelemetry e ingeniería del caos juntos
La ingeniería del caos crea una falla controlada para preguntar “¿qué hará el sistema?”. OpenTelemetry ayuda a observar “¿qué hizo realmente?”

En el ejemplo:

1. El equipo simula que Rutas no responde en el entorno de pruebas.
2. Una métrica muestra cuántas consultas terminaron con ubicación no disponible.
3. Una traza identifica cuánto esperó la Gateway.
4. Los logs ayudan a entender si el mensaje de error fue registrado correctamente.
5. El equipo confirma si el estado del pedido siguió visible y si la ubicación no se inventó.

Sin observación, el experimento podría fallar y el equipo no sabría dónde. Sin una pregunta de resiliencia, recolectar datos puede producir gráficos que nadie usa para mejorar el sistema.

## 9. Errores frecuentes
- **Confundir observabilidad con monitoreo de disponibilidad:** saber que el servicio está encendido no explica cada falla.
- **Pensar que OpenTelemetry es una plataforma de tableros completa:** OTel facilita generar y transportar telemetría; normalmente se conecta a otras herramientas para almacenarla y verla.
- **Registrar datos privados en logs o trazas:** una herramienta de diagnóstico también necesita protección y límites de acceso.
- **Hacer experimentos sin hipótesis:** no se sabe qué resultado se intenta comprobar.
- **Probar demasiadas fallas al tiempo:** después es difícil identificar la causa.
- **Experimentar directamente sobre clientes sin autorización ni límites:** convierte una prueba en un incidente.
- **No restaurar ni documentar:** se deja el entorno alterado y se pierde el aprendizaje.

## 10. Actividad de autoestudio
Quieres comprobar esta hipótesis: “Si el servicio de rutas deja de responder, el cliente todavía puede consultar el estado confirmado del pedido y ve un aviso claro de que falta la ubicación”.

Escribe:

1. En qué entorno harías la prueba y por qué.
2. Qué servicio alterarías y por cuánto tiempo.
3. Qué métrica, log y traza revisarías.
4. Qué resultado demostraría que la hipótesis se cumple.
5. Qué condición te haría detener el experimento.
6. Cómo restaurarías el servicio y confirmarías la recuperación.

### Pistas
- Usa pedidos ficticios primero.
- No basta con medir que el servicio de rutas falló; observa lo que vio la aplicación.
- Define una señal concreta para detener la prueba.

## 11. Solución comentada
1. Empezaría en un entorno de pruebas aislado con pedidos ficticios, para no afectar clientes.
2. Haría que solo una instancia de rutas deje de responder durante un período breve previamente acordado.
3. Revisaría cuántas consultas fallan, los logs de la Gateway y una traza que muestre la espera en rutas.
4. La hipótesis se cumple si el pedido sigue visible, la ubicación se marca como no disponible y la solicitud termina dentro del límite acordado.
5. Detendría la prueba si se afectan datos o servicios fuera del alcance, si se supera el límite de errores o si no se puede restaurar la instancia.
6. Rehabilitaría el servicio y haría una consulta nueva para confirmar que volvió a responder; luego registraría el resultado.

## 12. Comprueba lo que aprendiste
1. ¿Qué información ofrece una métrica, un log y una traza?
2. ¿OpenTelemetry es necesariamente el sistema que muestra y guarda todos los gráficos?
3. ¿Qué diferencia hay entre una falla controlada y romper el sistema al azar?
4. ¿Qué elementos deben definirse antes de hacer un experimento de caos?

### Respuestas
1. La métrica resume cantidades o tiempos; el log anota hechos concretos; la traza muestra el recorrido de una solicitud por varios pasos.
2. No. OTel genera y transporta telemetría; suele conectarse a herramientas que la almacenan y presentan.
3. La falla controlada parte de una hipótesis, tiene alcance, límites, observación y restauración. Romper al azar no protege a usuarios ni produce evidencia clara.
4. Hipótesis, alcance, señales normales, límites de seguridad, responsable, comunicación y plan de restauración.

## Conclusión
OpenTelemetry ayuda a generar y transportar métricas, logs y trazas para entender cómo se comporta un sistema. La ingeniería del caos prueba, de forma planificada y limitada, si el sistema resiste fallas esperadas.

Ambas prácticas se complementan: primero decides qué comportamiento proteger, luego provocas una falla controlada, observas lo que ocurre y usas la evidencia para mejorar. La seguridad de las personas y de sus datos es parte del experimento, no un paso opcional.
