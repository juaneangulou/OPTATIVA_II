# Video 12: Cómo el pre-mortem guía tus tests de arquitectura

## Para estudiar por tu cuenta
El video anterior ayudó a imaginar cómo podría fallar la plataforma logística. Ahora vas a transformar uno de esos riesgos en una prueba que demuestre qué debe hacer el sistema.

Un riesgo escrito no protege el sistema por sí mismo. Para que ayude, hay que describir un escenario, un comportamiento esperado y una comprobación que pueda repetirse.

## 1. Del riesgo a una pregunta comprobable
Riesgo del pre-mortem: “Si se reintenta una tarea, la misma entrega podría asignarse dos veces”.

Una pregunta comprobable es: “Si el consumidor recibe dos veces la misma tarea de asignación, ¿queda una sola entrega activa para el pedido?”.

La segunda frase define un caso que se puede ejecutar y observar; la primera solo advierte algo que podría ocurrir.

## 2. Define el escenario de prueba
Una prueba necesita:

- **Contexto:** qué pedido y qué datos existen antes.
- **Acción:** qué evento o solicitud se ejecuta, incluyendo una repetición.
- **Resultado esperado:** qué debe permanecer verdadero después.

Ejemplo:

```text
Dado que el pedido 245 está listo para asignar
Cuando se procesa dos veces la misma solicitud de asignación
Entonces existe una sola entrega activa para el pedido 245
```

La prueba debe identificar el mismo pedido y la misma tarea; dos solicitudes distintas podrían justificar dos acciones distintas.

## 3. Elige el nivel de prueba
- **Prueba unitaria:** comprueba una regla pequeña sin base de datos ni red.
- **Prueba de integración:** verifica que el consumidor y el almacenamiento real colaboran correctamente.
- **Prueba de arquitectura:** comprueba una regla estructural, por ejemplo, que el dominio no dependa del proveedor de mensajería.

Elige el nivel que pueda demostrar el riesgo con claridad. No conviertas cada escenario en una prueba grande si una prueba pequeña puede detectar el error.

## 4. Ejemplo: sin inventario suficiente
Riesgo: el sistema confirma el pedido aunque el almacén no tenga todas las unidades.

Prueba posible:

```text
Dado que hay 1 unidad disponible
Cuando se solicitan 2 unidades
Entonces el pedido no se confirma
Y el inventario permanece en 1 unidad
```

Esta prueba define tanto el resultado de negocio como un efecto que no debería ocurrir: descontar unidades que no se reservaron.

## 5. Relaciona riesgos y pruebas
| Riesgo identificado | Comportamiento a proteger | Evidencia posible |
|---|---|---|
| Mensaje repetido | No crear dos entregas | Prueba de integración que procesa el mismo identificador dos veces |
| Proveedor de rutas sin respuesta | No inventar ubicación ni bloquear indefinidamente | Prueba de timeout y verificación de respuesta parcial |
| Pedido sin autorización | No mostrar datos ajenos | Prueba de permisos con dos cuentas de ensayo |
| Dependencia prohibida | El dominio no importa infraestructura | Prueba automatizada de arquitectura |

## 6. Actividad de autoestudio
Elige uno de estos escenarios: actualización de estado fuera de orden, mensaje repetido, proveedor externo lento o pedido sin autorización.

1. Escribe el riesgo en una frase.
2. Convierte el riesgo en Dado-Cuando-Entonces.
3. Elige el nivel de prueba y explica por qué.
4. Nombra el resultado esperado y algo que no debe ocurrir.
5. Define qué evidencia guardarías cuando la prueba se ejecuta.

### Respuesta modelo: actualización fuera de orden
**Riesgo:** una ubicación antigua llega tarde y hace retroceder el estado del pedido.

```text
Dado que el pedido 245 ya tiene una actualización de las 14:10
Cuando llega una actualización anterior, registrada a las 13:50
Entonces se conserva la actualización de las 14:10
Y el estado no retrocede
```

Usaría una prueba de integración si el orden y guardado dependen de almacenamiento real. Guardaría el resultado de la prueba y los datos de ensayo, no información personal del cliente.

## Comprueba lo que aprendiste
1. ¿Qué diferencia hay entre escribir un riesgo y escribir una prueba?
2. ¿Qué parte del escenario define cuándo falla la prueba?
3. ¿Por qué no basta con comprobar solo el camino feliz?

**Respuestas:** el riesgo señala algo que podría salir mal; la prueba define una entrada, acción y resultado observado; los fallos y límites revelan si el sistema protege sus reglas cuando las condiciones no son ideales.

## Conclusión
El pre-mortem encuentra riesgos posibles; las pruebas derivadas los vuelven comprobables. Para cada riesgo importante, define qué debe ocurrir, qué no debe ocurrir y qué prueba aporta evidencia sin depender de opiniones.
