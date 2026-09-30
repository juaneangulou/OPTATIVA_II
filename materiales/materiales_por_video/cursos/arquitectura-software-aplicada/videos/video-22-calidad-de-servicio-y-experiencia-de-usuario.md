# Video 22: Patrón Comparing Consumers para procesamiento en tiempo real

## Para estudiar por tu cuenta
Este video trata una pregunta práctica: **¿cómo probamos una nueva forma de procesar información real sin ponerla inmediatamente a cargo de las decisiones que afectan a los usuarios?**

Usaremos el seguimiento de entregas. El sistema actual calcula una hora estimada de llegada y funciona, pero el equipo quiere probar un cálculo nuevo. En lugar de reemplazarlo de inmediato, compara en paralelo lo que produciría la versión actual y la nueva.

## 1. Antes del patrón: quién consume la información
Un **consumidor** es un programa que recibe información y la procesa. Por ejemplo, el consumidor de seguimiento recibe actualizaciones de repartidores y calcula qué estado mostrar.

Imagina que la versión actual del consumidor calcula que el pedido llegará a las 14:30. El equipo desarrolla una versión nueva que considera tráfico y clima. Antes de confiarle la respuesta al cliente, necesita saber si calcula resultados útiles y cómo se comporta con datos reales.

## 2. ¿Qué significa Comparing Consumers?
**Comparing Consumers** (comparación de consumidores) es un patrón para ejecutar dos versiones de un consumidor con la misma información y comparar sus resultados antes de cambiar cuál de ellas tiene efecto real.

- El consumidor **actual** sigue siendo el que determina lo que ve el usuario.
- El consumidor **candidato** recibe una copia de la misma información, pero sus resultados se registran solo para compararlos.
- El equipo estudia las diferencias y decide si el candidato está listo.

Al candidato se le puede llamar **consumidor sombra** porque trabaja en paralelo sin dirigir la operación real. No es solo un tablero donde se comparan números: ambos consumidores procesan entradas equivalentes y el equipo revisa qué salida produce cada uno.

## 3. Recorrido del ejemplo, paso a paso

### Paso 1: definir qué queremos mejorar
El equipo quiere que la hora estimada de llegada sea más precisa cuando hay tráfico. No empieza diciendo “necesitamos una tecnología nueva”; empieza identificando el problema observado por el cliente.

### Paso 2: elegir una medida de comparación
El equipo decide qué significa “más precisa”. Por ejemplo, compara cada estimación con la hora real de entrega y calcula la diferencia. También puede comparar qué porcentaje de entregas llega dentro de un margen acordado.

Sin una medida definida, dos personas podrían mirar la misma tabla y llegar a conclusiones distintas.

### Paso 3: enviar los mismos datos a ambas versiones
Cada actualización de ruta llega al consumidor actual y a una copia del consumidor candidato:

```text
Actualización de ruta ──┬──> Consumidor actual ──> Hora usada en la aplicación
						└──> Consumidor candidato ──> Resultado guardado para comparar
```

La palabra **copia** importa: el candidato necesita recibir los mismos hechos para que la comparación sea justa.

### Paso 4: proteger el sistema real
El candidato calcula su hora estimada, pero no envía mensajes al cliente, no cambia el estado del pedido ni asigna repartidores. Si pudiera hacer esos efectos, el equipo recibiría notificaciones duplicadas o decisiones contradictorias.

Esta ejecución sin efectos reales se llama **modo sombra**. El candidato observa y calcula; el consumidor actual sigue siendo la autoridad.

### Paso 5: comparar los resultados
El equipo revisa, por ejemplo:

| Pedido | Hora estimada actual | Hora estimada candidata | Hora real | Qué revisar |
|---|---:|---:|---:|---|
| 245 | 14:30 | 14:20 | 14:24 | ¿El cálculo nuevo estuvo más cerca? |
| 246 | 15:10 | 15:40 | 15:18 | ¿Qué dato hizo que el candidato se alejara? |

Son cifras ilustrativas. No significan que la versión candidata sea mejor en todos los casos. El equipo debe revisar muchos ejemplos, incluidos los que empeoraron.

### Paso 6: decidir con evidencia
Si el candidato mejora la precisión sin elevar demasiado el tiempo de respuesta o el costo, el equipo puede probarlo con un grupo pequeño de solicitudes reales. Si produce errores o resultados peores, se mantiene el consumidor actual y se investiga.

## 4. Comparar no es competir por quién responde primero
En una **cola compartida**, varios consumidores pueden repartirse los mensajes: uno procesa una tarea y los demás otras. Eso aumenta capacidad, pero no garantiza que todos procesen cada mensaje.

En Comparing Consumers, ambas versiones deben recibir entradas equivalentes porque queremos comparar sus resultados. Si ponemos las dos versiones a competir por una cola que entrega cada mensaje a una sola, no podremos comparar: cada una verá pedidos diferentes.

La diferencia es:

| Forma de trabajo | Qué recibe cada mensaje | Objetivo |
|---|---|---|
| Consumidores que compiten por una cola | Normalmente uno de los trabajadores | Repartir tareas y procesar más trabajo |
| Consumidores comparados | Las dos versiones reciben la misma entrada o copias equivalentes | Comparar resultados antes de elegir una versión |

## 5. ¿Qué conviene comparar?
La respuesta depende del problema. En el ejemplo se podría comparar:

- **Corrección:** ¿la hora estimada es razonable y se calcula con los datos correctos?
- **Precisión:** ¿qué tan cerca queda de la hora real?
- **Rapidez:** ¿cuánto tarda cada versión en producir una respuesta?
- **Estabilidad:** ¿con qué frecuencia una versión falla?
- **Costo:** ¿cuántos recursos adicionales consume ejecutar el candidato?
- **Equidad entre casos:** ¿funciona peor para ciertas zonas, horarios o tipos de entrega?

No elijas solo los casos que favorecen al candidato. Conserva ejemplos típicos y excepcionales, y compara el mismo período o las mismas entradas.

## 6. Un plan seguro para adoptar el candidato
1. Prueba ambas versiones primero con datos históricos o de ensayo.
2. Ejecuta el candidato en modo sombra con entradas actuales.
3. Guarda resultados sin permitir que el candidato afecte al usuario.
4. Compara una muestra suficiente y explica las diferencias importantes.
5. Si hay evidencia favorable, deja que el candidato responda a un grupo pequeño y controlado.
6. Observa errores, tiempos y comentarios de ese grupo.
7. Amplía gradualmente o regresa a la versión actual si empeora la experiencia.

El **retroceso** es volver a la versión anterior si el nuevo comportamiento causa problemas. Debe ser posible cambiar cuál versión tiene autoridad sin perder los datos ni duplicar efectos.

## 7. Qué puede salir mal

### El candidato recibe datos distintos
La comparación no es justa. Guarda qué entrada recibió cada versión y confirma que ambas procesen la misma actualización.

### El candidato produce acciones reales
Podría enviar dos avisos, crear dos asignaciones o modificar el mismo pedido. En modo sombra, sus efectos secundarios deben desactivarse o enviarse a un espacio aislado.

### Se compara solo un promedio
Un promedio puede ocultar que el nuevo cálculo falla en una zona o en pedidos urgentes. Revisa también los casos extremos y las diferencias por grupo.

### El candidato usa datos que no debería ver
Duplicar entradas puede exponer datos personales a una versión nueva o a un entorno menos protegido. Limita la información y los accesos.

### No se define cuándo termina la prueba
Sin una duración, cantidad de casos o criterio acordado, el equipo puede mantener dos consumidores indefinidamente y pagar el costo sin aprender nada.

## 8. Cuándo tiene sentido
Puede ser útil cuando el nuevo consumidor cambia cálculos o decisiones importantes y un error podría afectar clientes, entregas o dinero. También puede ayudar a migrar una regla antigua hacia una versión nueva con evidencia real.

No siempre hace falta. Si el cambio es pequeño, fácil de probar y reversible, ejecutar dos versiones podría costar más que el riesgo que reduce. El patrón tampoco reemplaza las pruebas: amplía la comparación a entradas y comportamiento representativos.

## 9. Actividad de autoestudio
La versión actual calcula rutas con la distancia más corta. El equipo crea una versión candidata que también considera tráfico. Resuelve:

1. ¿Qué problema del cliente se intenta mejorar?
2. ¿Qué datos deben recibir ambas versiones para comparar justamente?
3. ¿Qué resultados medirías además de la distancia?
4. ¿Qué acciones debe tener prohibidas la versión candidata durante el modo sombra?
5. ¿Qué evidencia pedirías antes de darle efecto a la ruta candidata?
6. Si funciona bien en algunos horarios y peor en otros, ¿qué harías?

### Pistas
- Piensa en el tiempo real de viaje, no solo en kilómetros.
- La candidata no debe mandar un repartidor real a una ruta todavía no aprobada.
- Una diferencia importante necesita explicación antes de ampliar el cambio.

## 10. Solución comentada
1. Reducir entregas tardías y ofrecer una hora estimada más confiable.
2. Las mismas actualizaciones de ubicación, destino, hora y datos de tráfico disponibles para ambas versiones.
3. Diferencia entre hora prometida y hora real, tiempo de cálculo, fallos y resultados por zona y horario.
4. No debe asignar rutas reales, cambiar el estado ni enviar mensajes a clientes durante la comparación sombra.
5. Resultados comparados en suficientes rutas y horarios, explicación de casos donde empeoró y capacidad de volver a la versión actual.
6. Mantener la versión actual para los horarios problemáticos, investigar la causa y probar ajustes antes de ampliar el candidato.

## 11. Comprueba lo que aprendiste
1. ¿Por qué el consumidor actual conserva la autoridad durante el modo sombra?
2. ¿Por qué las dos versiones necesitan entradas equivalentes?
3. ¿Qué diferencia hay entre comparar consumidores y repartir una cola entre trabajadores?
4. ¿Qué costo se acepta al comparar dos versiones?

### Respuestas
1. Para que un candidato todavía no comprobado no cambie lo que ve o recibe el cliente.
2. Para atribuir las diferencias al procesamiento y no a que las versiones vieron pedidos distintos.
3. Comparar requiere que ambas procesen los mismos hechos; repartir trabajo normalmente entrega cada tarea a un solo trabajador.
4. Se usan recursos adicionales y hay que guardar y revisar más resultados durante la prueba.

## Conclusión
Comparing Consumers permite comparar el comportamiento de una versión conocida y otra candidata con las mismas entradas. Mientras se reúne evidencia, el consumidor actual sigue atendiendo el sistema y el nuevo trabaja sin efectos reales.

El patrón es útil cuando el riesgo de cambiar una lógica importante justifica el costo de ejecutar y comparar dos versiones. La decisión de adoptar el candidato debe basarse en resultados, casos desfavorables incluidos, y en un plan claro para avanzar o regresar.
