# Video 25: Máquinas de estado finito en el front-end

## Para estudiar por tu cuenta
Una pantalla puede estar esperando una respuesta, mostrando datos o informando un error. Si esos casos se programan como condiciones sueltas, la interfaz puede mostrar combinaciones confusas, como “cargando” y “entregado” al mismo tiempo.

Una **máquina de estado finito** ayuda a nombrar las situaciones posibles de una interfaz y definir cómo pasa de una a otra. En esta clase diseñarás el flujo de una pantalla de seguimiento sin necesidad de programar.

## 1. Estado: ¿en qué situación está la pantalla?
Un **estado** es una situación reconocible del sistema o de la interfaz en un momento concreto.

Para consultar una entrega, la pantalla podría encontrarse en uno de estos estados:

- **Sin consulta:** la persona aún no ha pedido el seguimiento.
- **Cargando:** se envió la consulta y se espera la respuesta.
- **Resultado disponible:** llegó información del pedido.
- **No encontrado:** la respuesta indica que no existe un pedido con ese identificador.
- **Error temporal:** no se pudo consultar por un problema de conexión.

Si sabemos en qué estado está la pantalla, podemos elegir qué mensaje y qué botones mostrar.

## 2. Evento y transición
- Un **evento** es algo que ocurre y puede provocar un cambio: la persona toca “Consultar”, llega una respuesta o vence el tiempo de espera.
- Una **transición** es el paso de un estado a otro cuando ocurre un evento permitido.

Ejemplo: desde “Sin consulta”, cuando la persona toca “Consultar”, la pantalla pasa a “Cargando”.

```text
Sin consulta ── toca Consultar ──> Cargando
```

No todas las transiciones deben permitirse. Por ejemplo, no tiene sentido mostrar “Resultado disponible” antes de que llegue una respuesta.

## 3. ¿Por qué se llama máquina de estado finito?
Se llama **finito** porque definimos un conjunto limitado de estados posibles para una parte del sistema. En vez de permitir cualquier combinación de banderas, nombramos las situaciones que sí entendemos.

Una **bandera** es un valor que puede estar activo o inactivo, como `cargando = sí` o `error = sí`. Con varias banderas independientes podrían aparecer combinaciones imposibles: cargando, con resultado exitoso y mostrando error a la vez.

Una máquina de estados hace explícito que la pantalla está en una situación definida y que debe seguir transiciones conocidas.

## 4. Diseñemos la pantalla de seguimiento
La persona introduce el número 245 y toca “Consultar”.

### Paso 1: iniciar la consulta
La pantalla pasa de “Sin consulta” a “Cargando” y muestra que está trabajando. Esto evita que la persona crea que el botón no funcionó.

### Paso 2: recibir una respuesta correcta
Si el pedido existe y el servidor devuelve el estado “En camino”, la pantalla pasa a “Resultado disponible” y muestra la información.

### Paso 3: recibir “no encontrado”
Si el servidor confirma que el número no existe, la pantalla pasa a “No encontrado”. No debe mostrar el último pedido consultado como si fuera el nuevo.

### Paso 4: no recibir respuesta
Si ocurre un problema temporal, la pantalla pasa a “Error temporal” y permite volver a intentar. No debe presentar el pedido como entregado.

### Paso 5: volver a consultar
Desde “Error temporal”, la persona puede volver a intentarlo. La interfaz regresa a “Cargando”; no salta directamente a “Resultado disponible”.

## 5. Tabla de transiciones
| Estado actual | Evento o resultado | Nuevo estado | Qué muestra la pantalla |
|---|---|---|---|
| Sin consulta | La persona toca “Consultar” | Cargando | Indicador de espera |
| Cargando | La respuesta confirma el pedido | Resultado disponible | Estado y datos recibidos |
| Cargando | La respuesta indica que no existe | No encontrado | Mensaje para revisar el número |
| Cargando | Falla la conexión o vence la espera | Error temporal | Aviso y opción de reintentar |
| Error temporal | La persona toca “Reintentar” | Cargando | Indicador de espera |
| Resultado disponible | La persona pide actualizar | Cargando | Se consulta información nueva |

La tabla ayuda a encontrar huecos. Pregunta: ¿qué ocurre si la respuesta llega después de que la persona ya inició otra consulta? El diseño debe evitar mostrar una respuesta antigua como si perteneciera a la solicitud más reciente.

## 6. Estado de la pantalla y estado del pedido no son lo mismo
Hay dos conceptos que pueden compartir la palabra “estado”:

- **Estado de interfaz:** indica qué está haciendo la pantalla. Por ejemplo, “Cargando”.
- **Estado del pedido:** describe el proceso logístico. Por ejemplo, “En camino”.

El pedido puede estar “En camino” mientras la pantalla está “Cargando” porque aún espera los datos. Cuando llegan, la interfaz queda en “Resultado disponible” y muestra el estado del pedido.

La pantalla no debería inventar ni decidir que el pedido está entregado. Esa información procede del sistema responsable del pedido.

## 7. Reglas que protegen el flujo
Puedes escribir condiciones sencillas para evitar errores:

- Solo se muestra “Resultado disponible” después de recibir una respuesta válida.
- Mientras se espera una consulta, el botón no debe crear múltiples solicitudes accidentales.
- Un resultado debe corresponder al número de pedido que la persona consultó.
- Una falla temporal no cambia el estado real del pedido.
- Desde “No encontrado” se puede corregir el número y comenzar una consulta nueva.

Estas condiciones son parte del comportamiento esperado. Pueden verificarse con pruebas manuales o automatizadas.

## 8. ¿Cuándo conviene una máquina de estados?
Puede ayudar cuando:

- Hay varias situaciones posibles que cambian lo que la pantalla permite hacer.
- Existen transiciones inválidas que queremos impedir.
- Aparecen errores difíciles de reproducir por combinaciones de condiciones.
- Varias personas necesitan entender el flujo de la interfaz.

Para una pantalla estática con un solo botón y una sola respuesta, definir muchas capas de estados puede ser innecesario. El objetivo es hacer explícito un flujo que ya tiene complejidad, no crear complejidad para usar el patrón.

## 9. Actividad de autoestudio
Diseña la pantalla para cancelar una entrega:

1. Escribe los estados posibles de la interfaz antes, durante y después de pedir la cancelación.
2. Anota qué evento hace que la pantalla cambie de estado.
3. Decide qué muestra si el servicio confirma la cancelación.
4. Decide qué muestra si el servicio informa que la entrega ya está en camino y no puede cancelarse desde la aplicación.
5. Decide qué muestra si no llega una respuesta.
6. Escribe una transición que no debería permitirse.

### Pistas
- La pantalla no debe mostrar “Cancelada” antes de recibir confirmación.
- Que la aplicación tenga un error de red no significa que el servidor no haya recibido la solicitud.
- Separa el estado visual de la pantalla del estado real de la entrega.

## 10. Solución comentada
| Estado actual | Evento | Nuevo estado | Explicación |
|---|---|---|---|
| Mostrando entrega | Persona pide cancelar | Solicitando cancelación | La pantalla todavía no afirma que se canceló |
| Solicitando cancelación | Servidor confirma cancelación | Cancelada | Existe confirmación del sistema responsable |
| Solicitando cancelación | Servidor indica que ya va en camino | No se puede cancelar desde aquí | La interfaz explica el límite y ofrece contacto si aplica |
| Solicitando cancelación | Se pierde la conexión | Resultado por confirmar | Puede que la solicitud sí haya llegado; conviene consultar antes de repetirla |
| Resultado por confirmar | Se consulta el estado real | Cargando verificación | La interfaz averigua qué ocurrió antes de permitir otra acción |

Una transición que no debería permitirse es pasar de “Solicitando cancelación” a “Cancelada” solo porque se tocó el botón. El clic inicia una solicitud; la confirmación determina el resultado.

## 11. Comprueba lo que aprendiste
1. ¿Qué diferencia hay entre estado y evento?
2. ¿Cuál es la diferencia entre “Cargando” y “En camino”?
3. ¿Por qué una falla de conexión no confirma que la entrega se canceló?
4. ¿Qué problema ayuda a evitar definir transiciones?

### Respuestas
1. El estado describe una situación actual; el evento es algo que ocurre y puede hacer cambiar esa situación.
2. “Cargando” describe la interfaz; “En camino” describe la entrega.
3. La solicitud pudo llegar al servidor aunque la respuesta no volviera. Hay que consultar el estado antes de repetir acciones que puedan duplicarse.
4. Evita combinaciones imposibles y cambios a estados que no corresponden al flujo.

## Conclusión
Una máquina de estado finito nombra las situaciones posibles de una interfaz y describe qué eventos permiten pasar de una a otra. Ayuda a mostrar información coherente, impedir acciones inválidas y probar los casos normales y los errores.

El estado visual no sustituye al estado real que mantiene el servidor. La pantalla informa y permite actuar; el sistema responsable confirma qué ocurrió.
