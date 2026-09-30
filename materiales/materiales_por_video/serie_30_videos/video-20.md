# Video 20: Pre-mortem y pruebas de arquitectura

## Fuentes de este video
- [Técnicas pre-mortem y cinco why para prevenir fallos](https://platzi.com/cursos/software-avanzado/tecnicas-pre-mortem-y-cinco-why-para-pre/)
- [Cómo el pre-mortem guía tus tests de arquitectura](https://platzi.com/cursos/software-avanzado/como-el-premortem-guia-tus-tests-de-arqu/)

## Para estudiar por tu cuenta
El primer video del curso ya te ayudó a imaginar fallos antes de construir. Ahora vas a dar el paso siguiente: convertir un riesgo importante en una prueba que puedas ejecutar repetidamente.

Un riesgo escrito no evita que ocurra. Una prueba ayuda a comprobar que el sistema mantiene un comportamiento necesario cuando se presentan las condiciones que podrían provocar ese fallo.

## 1. Qué es un pre-mortem
Un **pre-mortem** es un ejercicio en el que supones que el sistema ya falló y preguntas qué pudo llevarlo hasta ahí. No es una predicción ni una lista de miedos: es una forma de detectar riesgos antes de que afecten a clientes u operación.

En vez de preguntar “¿todo va a salir bien?”, plantea: “Dentro de tres meses, varios clientes recibieron dos repartidores para el mismo pedido. ¿Qué pudo provocar esa situación?”.

La respuesta inicial puede ser “el mensaje se procesó dos veces”. El pre-mortem te ayuda a buscar por qué el diseño permitiría que esa repetición duplicara el efecto.

## 2. Usa cinco porqués para profundizar
Los **cinco porqués** son una guía para preguntar por qué ocurrió una condición y seguir hasta encontrar una causa que el sistema o el proceso puedan corregir.

Ejemplo:

1. ¿Por qué se asignaron dos repartidores? La solicitud de asignación se procesó dos veces.
2. ¿Por qué se procesó dos veces? El sistema reintentó al no recibir respuesta a tiempo.
3. ¿Por qué el reintento duplicó la asignación? El consumidor no reconoció que era la misma solicitud.
4. ¿Por qué no reconoció la repetición? No guardó un identificador único de la tarea procesada.
5. ¿Por qué esa condición no apareció antes? Las pruebas no simulaban mensajes repetidos ni respuestas tardías.

La cadena no busca culpar a quien implementó el reintento. Busca entender qué protección faltó y cómo comprobarla.

## 3. De la historia a un riesgo útil
Describe el riesgo en cuatro partes:

- **Causa:** qué condición puede ocurrir.
- **Evento:** qué pasa en el sistema.
- **Consecuencia:** quién recibe el daño o costo.
- **Señal:** cómo sabrías que el riesgo está ocurriendo.

| Parte | Ejemplo de doble asignación |
|---|---|
| Causa | La confirmación tarda y la tarea se reintenta |
| Evento | Dos procesos asignan la misma entrega |
| Consecuencia | Dos repartidores reciben el mismo trabajo |
| Señal | Hay más de una asignación activa para el pedido |

Un riesgo es más fácil de tratar cuando puedes explicar su consecuencia y reconocer su señal.

## 4. Convierte el riesgo en una prueba
Una prueba debe definir:

1. El estado inicial del sistema.
2. La acción que podría desencadenar el fallo.
3. El resultado que debe ocurrir.
4. El resultado que no debe ocurrir.

Escenario:

```text
Dado que el pedido 245 está listo para asignarse
Cuando el mismo mensaje de asignación se procesa dos veces
Entonces queda una sola asignación activa
Y el sistema conserva registro de la solicitud repetida
```

La prueba convierte la frase “evitar duplicados” en un comportamiento que se puede revisar después de cada cambio.

## 5. Elige el tipo de prueba correcto
- **Prueba unitaria:** verifica una regla pequeña sin base de datos ni red, por ejemplo, que una segunda asignación para el mismo pedido se rechace.
- **Prueba de integración:** confirma que el consumidor y el almacenamiento real recuerdan que el mensaje ya se procesó.
- **Prueba de arquitectura:** revisa una regla estructural, como que solo el módulo Entregas pueda crear asignaciones.

No tienes que escribir todo en una única prueba. Elige el nivel que compruebe la causa que identificaste. Una prueba unitaria no demuestra que la base guarde correctamente; una prueba de integración no explica por sí sola la regla de negocio.

## 6. Riesgo, prueba y protección
| Riesgo del pre-mortem | Prueba derivada | Qué demuestra |
|---|---|---|
| Se crea una entrega dos veces | Procesar dos veces la misma solicitud | El segundo intento no duplica el efecto |
| Se acepta una dirección incompleta | Enviar un pedido sin ciudad | El pedido se rechaza o queda en revisión con causa explícita |
| La ubicación externa no responde | Simular una respuesta lenta o caída | La consulta termina y no inventa una ubicación actual |
| Un cliente consulta un pedido ajeno | Usar dos cuentas de ensayo | La cuenta sin permiso no recibe datos del otro cliente |

## 7. Priorización sin fingir precisión
Puedes describir cada riesgo como bajo, medio o alto según:

- posibilidad de que ocurra;
- gravedad de la consecuencia;
- facilidad para detectarlo y recuperarse.

No hace falta asignar números exactos si no tienes datos. Explica por qué lo priorizas y qué evidencia te ayudaría a cambiar esa evaluación.

## 8. Actividad de autoestudio
Escoge un posible fallo de la plataforma:

- un mensaje se procesa dos veces;
- un pedido se marca como entregado sin evidencia;
- una ubicación antigua se muestra como actual;
- una cuenta consulta datos de otro cliente.

Escribe:

1. La causa posible y la consecuencia.
2. Qué persona o área recibe el impacto.
3. La señal que permitiría detectar el fallo.
4. Un escenario Dado–Cuando–Entonces.
5. El tipo de prueba que elegirías y por qué.
6. Qué evidencia guardarías cuando se ejecuta.

## 9. Respuesta modelo: ubicación desactualizada
**Riesgo:** el proveedor de geolocalización deja de responder, pero la pantalla sigue mostrando la última ubicación como si fuera actual.

**Persona afectada:** el cliente puede esperar en un lugar equivocado; soporte puede transmitir información incorrecta.

**Prueba:**

```text
Dado que la última ubicación del pedido 245 se recibió a las 13:10
Cuando el proveedor no responde a la consulta de las 13:20
Entonces el sistema no presenta la ubicación de las 13:10 como actual
Y muestra la hora de la última actualización o informa que no está disponible
```

Usaría una prueba de integración del recorrido entre consulta, proveedor simulado y respuesta de la API. Guardaría el resultado y el caso de error, sin incluir ubicación real de una persona.

## Comprueba lo que aprendiste
1. ¿El pre-mortem asegura que ningún fallo ocurrirá?
2. ¿Qué diferencia hay entre un riesgo y una prueba?
3. ¿Qué caracteriza una prueba de arquitectura?
4. ¿Por qué conviene incluir el resultado que no debe ocurrir?

### Respuestas
1. No; ayuda a encontrar riesgos posibles y preparar respuestas.
2. El riesgo describe algo que podría salir mal; la prueba define cómo comprobar una respuesta del sistema ante ese escenario.
3. Verifica una propiedad estructural del sistema, como una dependencia o un límite entre módulos.
4. Porque la ausencia de un efecto dañino también forma parte del comportamiento esperado.

## Conclusión
El pre-mortem ayuda a imaginar causas y consecuencias antes de que sucedan. Las pruebas convierten los riesgos prioritarios en comportamientos verificables. El ciclo queda completo cuando puedes mostrar qué podría fallar, cómo lo detectas y qué evidencia confirma que la protección funciona.