# Video 27: Máquinas de estado y seguridad de aplicaciones

## Fuentes de este video
- [Máquinas de estado finito en el front-end](https://platzi.com/cursos/software-avanzado/maquinas-de-estado-finito-en-el-front-en/)
- [SAST, DAST y pentesting para seguridad en software](https://platzi.com/cursos/software-avanzado/tecnicas-sast-dast-y-pen-testing-para-se/)

## Navegación
[⬅️ Video anterior: Process Manager y Durable State](video-26.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: Fitness Functions, OpenTelemetry y caos](video-28.md)

## Para estudiar por tu cuenta
La pantalla de seguimiento puede pasar por varios estados: esperando, cargando, resultado disponible o error. Si no defines cuándo puede pasar de uno a otro, la interfaz puede mostrar información contradictoria.

Al mismo tiempo, una pantalla correcta no garantiza seguridad. Un usuario podría intentar consultar un pedido ajeno directamente. Este capítulo conecta la máquina de estados de la interfaz con distintas formas de revisar la aplicación y sus permisos.

## 1. Máquina de estados finitos en la interfaz
Un **estado** describe una situación actual. Un **evento** es algo que ocurre y puede cambiarla. Una **transición** indica de qué estado a cuál se puede pasar.

Para consultar una entrega, la interfaz podría usar:

```text
Sin consulta -> Cargando -> Resultado
                         -> No encontrado
                         -> Error temporal
```

Si el cliente toca “Consultar”, la interfaz pasa a “Cargando”. Solo al recibir respuesta muestra resultado, pedido no encontrado o error. No debe enseñar como entregado un pedido antes de recibir confirmación.

Una máquina se llama **finita** porque define un conjunto limitado de estados para ese flujo. Evita combinaciones de banderas contradictorias, como “cargando y resultado confirmado” al mismo tiempo.

## 2. Estado de pantalla y estado del pedido
La palabra “estado” puede referirse a dos cosas distintas:

- **Estado de interfaz:** la pantalla está “Cargando”.
- **Estado del pedido:** el sistema informa que está “En camino”.

El pedido puede estar en camino mientras la pantalla espera los datos. La interfaz describe lo que está haciendo la pantalla; el servicio de pedidos conserva la verdad del flujo logístico.

## 3. Dibuja transiciones válidas
| Estado actual de la interfaz | Evento o respuesta | Nuevo estado |
|---|---|---|
| Sin consulta | El cliente pulsa Consultar | Cargando |
| Cargando | Pedido autorizado y encontrado | Resultado disponible |
| Cargando | El pedido no existe o no puede mostrarse | No encontrado |
| Cargando | El servicio no responde | Error temporal |
| Error temporal | El cliente vuelve a intentar | Cargando |

Una transición inválida sería pasar a “Entregado” apenas el cliente pulsa un botón. La acción del usuario inicia una solicitud; el sistema responsable debe confirmarla.

## 4. Seguridad: la pantalla no es la frontera de confianza
Ocultar un botón en el front-end mejora la experiencia, pero no protege datos. La solicitud puede enviarse por otros medios. El servidor debe comprobar quién consulta y si esa persona tiene permiso para ver ese pedido.

No confíes en un identificador enviado por la pantalla como prueba de autorización. Comprueba la relación entre cuenta y pedido en el servidor y devuelve solo la información necesaria.

## 5. Tres formas de revisar seguridad

### SAST: revisar código sin ejecutar
**SAST** analiza código fuente para detectar patrones sospechosos. Puede encontrar señales en una consulta o una configuración antes de ejecutar la aplicación. Puede producir avisos que requieren interpretación y no detecta todas las fallas.

### DAST: probar la aplicación funcionando
**DAST** envía solicitudes a una aplicación en ejecución y observa sus respuestas. Puede ayudar a comprobar si una cuenta de prueba accede a un pedido ajeno. Se ejecuta con autorización y preferiblemente sobre un entorno de ensayo.

### Pentesting: evaluación humana con permiso
**Pentesting** es una prueba controlada en la que una persona autorizada intenta encontrar y demostrar vulnerabilidades dentro de un alcance acordado. Antes se define qué sistemas, horarios y métodos están permitidos.

Las tres técnicas se complementan: SAST ve señales en el código, DAST prueba comportamiento y pentesting explora escenarios con criterio humano. Ninguna prueba por sí sola garantiza que no haya riesgos.

## 6. Una falla de red no determina el estado real
Si la pantalla intenta cancelar una entrega y se pierde la conexión, no sabes automáticamente si el servidor recibió la solicitud. La interfaz podría mostrar “Resultado por confirmar” y consultar nuevamente el estado antes de repetir la acción.

Así evitas dos errores:

- mostrar “Cancelada” sin confirmación;
- repetir una operación que el servidor ya completó.

## 7. Pruebas para la pantalla y para la seguridad
- Prueba que pulsar “Consultar” cambia la interfaz a “Cargando”.
- Prueba que solo se muestra un pedido autorizado.
- Prueba que un timeout muestra un estado de error claro.
- Prueba que una respuesta atrasada no reemplaza datos de otra consulta.
- Prueba que una cuenta no puede obtener información de otra cambiando el identificador.

Los datos de ensayo deben ser ficticios. No pruebes cuentas reales ni sistemas de terceros sin permiso.

## 8. Actividad de autoestudio
Diseña la pantalla de cancelación de una entrega:

1. Escribe los estados de la interfaz antes, durante y después.
2. Dibuja las transiciones válidas.
3. Define qué muestra el sistema si el servidor confirma la cancelación.
4. Define qué muestra si se pierde la conexión.
5. Escribe una comprobación de autorización para que una cuenta no cancele un pedido ajeno.
6. Clasifica qué revisión ayudaría: SAST, DAST o pentesting.

### Respuesta modelo
Estados: “Mostrando entrega”, “Solicitando cancelación”, “Cancelada”, “No se puede cancelar” y “Resultado por confirmar”. La transición a “Cancelada” requiere confirmación del servidor.

Una prueba DAST en un entorno autorizado puede iniciar sesión como una cuenta de ensayo y consultar o cancelar el pedido de otra. SAST podría revisar la ruta de autorización en el código. Pentesting puede buscar otros caminos dentro del alcance aprobado.

## Comprueba lo que aprendiste
1. ¿La interfaz puede decidir por sí sola que una entrega se canceló?
2. ¿Qué revisa SAST? ¿Qué revisa DAST?
3. ¿Qué debe quedar acordado antes de un pentest?
4. ¿Por qué una máquina de estados ayuda a probar la interfaz?

### Respuestas
1. No; el sistema que administra la entrega debe confirmar la operación.
2. SAST examina código sin ejecutarlo; DAST prueba la aplicación en ejecución.
3. Permiso, alcance, sistemas incluidos, métodos, horarios y contacto ante una falla grave.
4. Hace explícitos los estados y transiciones permitidas, incluidos errores y respuestas atrasadas.

## Taller aplicado: revisar una transición con seguridad
Analiza el botón “Cancelar entrega” con dos preguntas separadas:

1. ¿La interfaz puede mostrar el botón para este estado?
2. ¿El servidor autoriza a esta cuenta a cancelar esta entrega?

Escribe pruebas para una cancelación válida, una entrega ya completada, una cuenta sin permiso y una respuesta tardía del servidor. Comprueba que la pantalla no pase a `Cancelada` solo porque la persona hizo clic: debe esperar una confirmación confiable.

Para la revisión de seguridad, SAST puede localizar rutas sin autorización; DAST puede comprobar el comportamiento de la API en un entorno autorizado; un pentest puede explorar combinaciones dentro de un alcance pactado. Ninguna herramienta sustituye la corrección de la regla de negocio ni autoriza probar sistemas ajenos.

## Conclusión
Una máquina de estados hace explícito qué puede mostrar y hacer una interfaz en cada momento. SAST, DAST y pentesting aportan evidencias distintas sobre seguridad. El servidor sigue siendo responsable de proteger los datos y confirmar los cambios que afectan una entrega.