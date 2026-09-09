# Video 09: Observabilidad, seguridad y privacidad

## Fuentes oficiales
- [Observabilidad y monitoreo de sistemas](https://platzi.com/cursos/fundamentos-arquitectura-software/como-funcionan-los-eventos-en-sistemas-d/)
- [Seguridad, datos sensibles y privacidad](https://platzi.com/cursos/fundamentos-arquitectura-software/costos-ocultos-de-los-microservicios/)

## 🔗 Navegación
[⬅️ Video anterior](video-08.md) | [➡️ Video siguiente](video-10.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Observabilidad y monitoreo de sistemas**
La observabilidad es una capacidad esencial en sistemas modernos. Permite entender qué está sucediendo en producción, detectar fallos, identificar cuellos de botella y responder rápidamente ante anomalías. Si un sistema no es observable, el equipo trabaja a ciegas y la resolución de incidentes se vuelve más costosa.

La observabilidad no es solo activar logs; incluye métricas, trazabilidad, alertas y mecanismos para evaluar el comportamiento real del sistema. Cuando se diseña bien, ayuda a prevenir incidentes, entender la carga y tomar decisiones basadas en evidencia.

**Fuente 2: Seguridad, datos sensibles y privacidad**
Este video refuerza la idea de que la seguridad debe integrarse desde el inicio del diseño. No se trata solo de proteger la aplicación frente a intrusos, sino también de gestionar adecuadamente datos sensibles, permisos de acceso y riesgos derivados del tratamiento de información. Cualquier sistema que maneje datos valiosos debe diseñarse con principios de privacidad, control y minimización.

La arquitectura debe prestar atención a qué información guarda, cómo la protege y quién puede acceder a ella. Cuando se ignora esto, se generan riesgos reales tanto para la empresa como para las personas que usan el sistema.

## Ideas que debes conservar
- La observabilidad permite entender el comportamiento real del sistema.
- Los logs, métricas y trazas son herramientas esenciales de diagnósticos.
- Un sistema difícil de monitorear es más riesgoso en producción.
- La observabilidad es una decisión arquitectónica, no un detalle final.
- La seguridad debe estar integrada al diseño, no añadida al final.
- Los datos sensibles requieren más criterios de control y protección.
- La privacidad es parte del valor del sistema.
- Un sistema debe minimizar exposición de información innecesaria.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **observabilidad, seguridad y privacidad**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La observabilidad permite entender el comportamiento real del sistema.
2. **Actores afectados:** cliente, operador logístico, repartidor, equipo de soporte y equipo técnico. Cada uno necesita información y garantías diferentes.
3. **Punto de decisión:** el equipo debe decidir qué responsabilidad queda en el módulo de pedidos, qué cruza hacia ruteo o inventario y qué se delega a una dependencia externa.
4. **Riesgo:** si la decisión es débil, puede haber entregas tardías, datos expuestos, cambios costosos, mensajes perdidos o una operación imposible de diagnosticar.
5. **Evidencia:** la decisión se demuestra con el artefacto adecuado: diagrama, ADR, contrato, código, prueba, métrica, registro de despliegue o experimento controlado.

Para resolver el caso, empieza por el flujo “crear pedido”. Señala el componente que recibe la solicitud, la regla que debe protegerse, la dependencia que puede fallar y el resultado que espera cada actor. Después compara dos formas de construirlo: una solución sencilla para el MVP y otra con mayor separación. La elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Resume en tus palabras la idea central de cada fuente.
2. Combina esas ideas en un problema arquitectónico único.
3. Propón dos alternativas de solución.
4. Compara costo inicial, calidad, riesgo, operación y facilidad de cambio.
5. Elige una alternativa para el MVP y declara qué condición obligaría a revisarla.
6. Produce una evidencia: ADR, diagrama, contrato, código C#, prueba, métrica o plan de evolución.

## Respuestas a las preguntas
### ❓ ¿Qué tan claro es el estado actual de mi sistema en producción?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la observabilidad permite entender el comportamiento real del sistema. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy monitoreando lo que realmente importa?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con los logs, métricas y trazas son herramientas esenciales de diagnósticos. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué datos sensibles maneja mi sistema?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un sistema difícil de monitorear es más riesgoso en producción. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy reduciendo la exposición innecesaria de información?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la observabilidad es una decisión arquitectónica, no un detalle final. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa observabilidad, seguridad y privacidad y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La observabilidad permite entender el comportamiento real del sistema. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La observabilidad es una parte central de la arquitectura porque permite entender, prevenir y corregir problemas antes de que se vuelvan críticos.

La seguridad y la privacidad no son requisitos secundarios: son elementos fundamentales de una arquitectura responsable y confiable.

## Preguntas para preparar la grabación
- ¿Qué tan claro es el estado actual de mi sistema en producción?
- ¿Estoy monitoreando lo que realmente importa?
- ¿Qué datos sensibles maneja mi sistema?
- ¿Estoy reduciendo la exposición innecesaria de información?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
