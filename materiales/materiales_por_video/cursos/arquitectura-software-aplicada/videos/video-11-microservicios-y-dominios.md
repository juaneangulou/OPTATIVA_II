# Video 11: Técnicas pre-mortem y cinco why para prevenir fallos

## Para estudiar por tu cuenta
Un **pre-mortem** es un ejercicio para imaginar que un proyecto ya fracasó y trabajar hacia atrás para buscar causas posibles antes de que ocurran. No es una predicción: es una forma estructurada de descubrir riesgos que quizá no se habían mencionado.

En esta clase aplicarás el ejercicio a la plataforma logística y usarás “cinco porqués” para investigar una causa sin detenerte en el primer síntoma.

## 1. Imagina el fallo antes de que suceda
Piensa que dentro de seis meses la plataforma no pudo operar con normalidad: los pedidos aparecen duplicados, las entregas se retrasan y soporte no puede explicar qué pasó.

En un pre-mortem no preguntas “¿qué podría fallar?” en abstracto. Imaginas un resultado concreto y buscas caminos que pudieron llevar hasta él. Escribir varias causas permite que el grupo analice riesgos que una conversación optimista podría pasar por alto.

## 2. Separa causa, consecuencia y señal
- **Causa:** qué condición produjo el fallo.
- **Consecuencia:** qué efecto tuvo en la operación o en una persona.
- **Señal:** qué dato temprano podría mostrar que el riesgo empieza a ocurrir.

Ejemplo:

| Parte | Ejemplo |
|---|---|
| Causa | Una tarea de entrega se procesa dos veces después de un reintento |
| Consecuencia | Se asignan dos repartidores al mismo pedido |
| Señal | Hay más de una asignación activa para un mismo pedido |

## 3. Usa los cinco porqués sin culpar a una persona
La técnica de **cinco porqués** consiste en preguntar repetidamente por qué ocurrió un problema hasta encontrar una causa que se pueda atender. Cinco es una guía, no un número obligatorio.

Ejemplo:

1. ¿Por qué se asignaron dos repartidores? La tarea de asignación se procesó dos veces.
2. ¿Por qué se procesó dos veces? Hubo un reintento cuando la primera respuesta tardaba.
3. ¿Por qué el reintento repitió la asignación? El consumidor no reconocía una tarea ya procesada.
4. ¿Por qué no existía esa protección? La identidad de la tarea no se guardaba como parte de la operación.
5. ¿Por qué no se había detectado? Las pruebas no simulaban respuestas demoradas y mensajes repetidos.

La cadena sugiere controles: identificar cada tarea, hacer la operación segura ante repetición y probar ese caso. No concluyas “la persona se equivocó” si el sistema permitía que el error se propagara.

## 4. Prioriza riesgos con cuidado
No todo riesgo tiene la misma consecuencia. Puedes describir cualitativamente:

- qué tan posible parece;
- qué tan grave sería;
- qué tan fácil sería detectarlo antes de que afecte a alguien.

No hace falta fabricar un número preciso cuando no hay datos. Es mejor explicar por qué un riesgo parece alto o bajo y qué evidencia ayudaría a confirmarlo.

## 5. Actividad de autoestudio
Imagina este escenario: el sistema se lanzó, pero durante un día de alta demanda algunos clientes reciben estados de entrega incorrectos.

1. Escribe tres causas posibles, sin culpar a personas.
2. Elige una causa y pregunta por qué ocurrió hasta que identifiques una condición que el diseño o las pruebas puedan cambiar.
3. Anota la consecuencia para un cliente o un área operativa.
4. Define una señal temprana que permita detectar el problema.
5. Propón una acción preventiva y una prueba que la compruebe.

### Respuesta modelo
Una causa posible es que una actualización antigua llegue después de una más reciente y reemplace el estado actual. Los porqués pueden revelar que no se compara la hora o secuencia del evento antes de actualizar.

La consecuencia es que el cliente ve “En camino” después de que el paquete ya se entregó. Una señal es que los estados retrocedan en la secuencia definida. Una medida preventiva es rechazar actualizaciones más antiguas que el estado vigente; una prueba envía primero una actualización nueva y luego una antigua, y verifica que la información actual no retroceda.

## Comprueba lo que aprendiste
1. ¿El pre-mortem predice con seguridad el futuro?
2. ¿Qué busca la técnica de cinco porqués?
3. ¿Por qué conviene describir señales tempranas además de las consecuencias?

**Respuestas:** no, explora riesgos posibles; busca causas que puedan corregirse, no culpables; las señales permiten detectar que un riesgo empieza antes de que se convierta en un incidente grande.

## Conclusión
El pre-mortem ayuda a descubrir escenarios de fallo antes de publicar. Los cinco porqués ayudan a profundizar en una causa posible. El resultado útil no es una lista para asustarse, sino riesgos con consecuencias, señales y acciones comprobables.
