# Video 21: Métricas y migración Strangler Fig

## Fuentes oficiales
- [Observabilidad y operabilidad](https://platzi.com/cursos/software-avanzado/metricas-cuantitativas-para-evaluar-arqu/)
- [DevOps, despliegue y automatización](https://platzi.com/cursos/software-avanzado/strangler-fig-para-migrar-arquitecturas/)

## 🔗 Navegación
[⬅️ Video anterior](video-20.md) | [➡️ Video siguiente](video-22.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Observabilidad y operabilidad**
El video destaca que una arquitectura no termina cuando el sistema “funciona” en un entorno local. La verdadera prueba de madurez llega cuando el equipo puede entender qué está sucediendo en producción, detectar fallos y responder con rapidez. Por eso la observabilidad es una parte esencial del diseño: métricas, logs, trazas y alertas ayudan a transformar el sistema en algo operable y diagnósticable.

Cuando una solución no es observable, el equipo se mueve a ciegas y las correcciones se vuelven reactivas. La operabilidad mejora cuando se diseña para monitoreo, diagnóstico y recuperación. El video deja claro que observar el sistema es una decisión arquitectónica, no un extra de operaciones.

**Fuente 2: DevOps, despliegue y automatización**
Este video conecta arquitectura con entrega continua y operación real. La forma en que se despliega una aplicación afecta directamente la estabilidad, velocidad y capacidad de innovación del equipo. Cuando el despliegue es manual, propenso a errores o difícil de repetir, la arquitectura se vuelve frágil incluso si el diseño técnico es bueno.

La automatización del despliegue, la integración continua, la orquestación y la infraestructura como código permiten que el sistema evolucione con menos riesgos. El video muestra que la arquitectura moderna no se limita a la aplicación, sino al flujo completo de entrega: código, integración, pruebas, despliegue, observabilidad y rollback. Esto hace que la calidad del sistema dependa también del proceso que lo lleva a producción.

## Ideas que debes conservar
- La observabilidad permite entender el comportamiento real del sistema.
- Logs, métricas y trazas ayudan a detectar fallas y cuellos de botella.
- Un sistema difícil de diagnosticar termina costando más en producción.
- La operación debe estar integrada en el diseño desde el principio.
- El despliegue es parte de la arquitectura, no una etapa separada.
- La automatización reduce errores humanos y acelera la entrega.
- La infraestructura debe ser reproducible y controlada.
- La calidad del proceso impacta la calidad del sistema.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **métricas y migración strangler fig**.

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
### ❓ ¿Qué tanto sabemos realmente qué está pasando en producción?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la observabilidad permite entender el comportamiento real del sistema. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Mi sistema me alerta antes de que el usuario lo note?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con logs, métricas y trazas ayudan a detectar fallas y cuellos de botella. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Mi despliegue es repetible y automatizado?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un sistema difícil de diagnosticar termina costando más en producción. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan rápido puedo revertir un cambio problemático?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la operación debe estar integrada en el diseño desde el principio. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa métricas y migración strangler fig y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La observabilidad permite entender el comportamiento real del sistema. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Un sistema bien diseñado no solo responde a requerimientos, sino que también puede ser comprendido y mantenido en producción. La observabilidad es uno de los pilares para convertir una solución técnica en una solución operable.

La arquitectura moderna integra desarrollo, operación y entrega. Un sistema no se considera bien diseñado si no puede entregarse, operar y evolucionar de manera segura y repetible.

## Preguntas para preparar la grabación
- ¿Qué tanto sabemos realmente qué está pasando en producción?
- ¿Mi sistema me alerta antes de que el usuario lo note?
- ¿Mi despliegue es repetible y automatizado?
- ¿Qué tan rápido puedo revertir un cambio problemático?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
