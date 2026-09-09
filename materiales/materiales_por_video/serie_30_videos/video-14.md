# Video 14: Cierre de fundamentos y transición

## Fuentes oficiales
- [Cierre del curso](https://platzi.com/cursos/fundamentos-arquitectura-software/consejos-para-desarrollar-carrera-como-a/)
- [Cierre del curso](https://platzi.com/cursos/fundamentos-arquitectura-software/consejos-para-desarrollar-carrera-como-a/)

## 🔗 Navegación
[⬅️ Video anterior](video-13.md) | [➡️ Video siguiente](video-15.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Cierre del curso**
El curso culmina con una reflexión integral: la arquitectura de software es una práctica de diseño, responsabilidad, criterio y sostenibilidad. No es solo elegir una tecnología o dibujar un diagrama; es construir sistemas que puedan crecer, proteger información, atender necesidades reales y sostenerse en el tiempo.

La idea final es que la arquitectura de software debe aprenderse con práctica, análisis y sentido crítico. Queda como invitación a seguir profundizando en proyectos reales, documentando decisiones, fortaleciendo el criterio y construyendo soluciones con propósito. El buen arquitecto no se limita a resolver un problema del momento; crea una base para que el sistema siga aportando valor en el futuro.

**Fuente 2: Cierre del curso**
El curso culmina con una reflexión integral: la arquitectura de software es una práctica de diseño, responsabilidad, criterio y sostenibilidad. No es solo elegir una tecnología o dibujar un diagrama; es construir sistemas que puedan crecer, proteger información, atender necesidades reales y sostenerse en el tiempo.

La idea final es que la arquitectura de software debe aprenderse con práctica, análisis y sentido crítico. Queda como invitación a seguir profundizando en proyectos reales, documentando decisiones, fortaleciendo el criterio y construyendo soluciones con propósito. El buen arquitecto no se limita a resolver un problema del momento; crea una base para que el sistema siga aportando valor en el futuro.

## Ideas que debes conservar
- La arquitectura es una disciplina estratégica, no solo técnica.
- El diseño debe equilibrar funcionalidad, calidad y responsabilidad.
- La documentación, la visión y la decisión humana son clave.
- La sostenibilidad del sistema depende de decisiones bien pensadas.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **cierre de fundamentos y transición**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La arquitectura es una disciplina estratégica, no solo técnica.
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
### ❓ ¿Qué parte de este curso quiero aplicar de inmediato en mi trabajo?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura es una disciplina estratégica, no solo técnica. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué decisiones de diseño puedo mejorar hoy?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el diseño debe equilibrar funcionalidad, calidad y responsabilidad. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué parte de este curso quiero aplicar de inmediato en mi trabajo?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la documentación, la visión y la decisión humana son clave. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué decisiones de diseño puedo mejorar hoy?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la sostenibilidad del sistema depende de decisiones bien pensadas. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa cierre de fundamentos y transición y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La arquitectura es una disciplina estratégica, no solo técnica. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
El curso cierra con una idea central: la arquitectura de software es la diferencia entre crear una solución temporal y crear una base sólida para el futuro. La verdadera calidad no está solo en el código, sino en la forma de pensar y decidir.

El curso cierra con una idea central: la arquitectura de software es la diferencia entre crear una solución temporal y crear una base sólida para el futuro. La verdadera calidad no está solo en el código, sino en la forma de pensar y decidir.

## Preguntas para preparar la grabación
- ¿Qué parte de este curso quiero aplicar de inmediato en mi trabajo?
- ¿Qué decisiones de diseño puedo mejorar hoy?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
