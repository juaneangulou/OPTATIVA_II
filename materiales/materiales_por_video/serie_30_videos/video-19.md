# Video 19: Architecture.md y Domain Driven Design

## Fuentes oficiales
- [Seguridad y privacidad](https://platzi.com/cursos/software-avanzado/estructura-del-archivo-architecture-md-p/)
- [Integración y contratos de API](https://platzi.com/cursos/software-avanzado/domain-driven-design-para-arquitectura-l/)

## 🔗 Navegación
[⬅️ Video anterior](video-18.md) | [➡️ Video siguiente](video-20.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Seguridad y privacidad**
La seguridad es una parte esencial de la arquitectura, no un tema opcional que se resuelve al final. Un sistema puede ser rápido y funcional, pero si no maneja bien autenticación, autorización, cifrado, validación de datos y control de acceso, puede poner en riesgo información crítica y la confianza del usuario. El video llama la atención sobre el hecho de que los problemas de seguridad no siempre aparecen como fallas técnicas evidentes: muchas veces son decisiones de diseño que dejan brechas invisibles.

También se habla de privacidad como un principio arquitectónico, no solo como cumplimiento. Diseñar con privacidad implica limitar datos, controlar acceso, definir responsabilidades y evitar recopilar más información de la necesaria. La arquitectura debe pensar en la seguridad desde las capas más básicas hasta el comportamiento del sistema en producción.

**Fuente 2: Integración y contratos de API**
La mayoría de sistemas modernos no existen aislados: dependen de servicios, clientes, proveedores y otras aplicaciones. Por eso, la capacidad de integrar componentes de forma clara y segura es crucial. Este video habla de las APIs como contratos entre sistemas: si esos contratos son ambiguos o cambian sin control, el sistema entera se vuelve frágil y difícil de mantener.

Se enfatiza la idea de que una API no es solo una ruta o un endpoint; es una interfaz formal de comunicación entre partes. Cuando se diseña bien, facilita la colaboración, reduce errores y mejora la evolución del sistema. Cuando se diseña mal, genera compatibilidad, dependencia y cambios difíciles de gestionar.

## Ideas que debes conservar
- La seguridad debe ser un eje arquitectónico, no un detalle a último momento.
- La confianza del usuario depende del manejo responsable de datos.
- Hay que proteger no solo la aplicación, sino sus flujos de datos y sus dependencias.
- La privacidad implica principio de mínimo privilegio y minimización de datos.
- Las APIs son contratos que facilitan la integración entre sistemas.
- Cambios sin versionado pueden romper dependencias.
- Debe existir claridad en formatos, validaciones, errores y semántica.
- La integración eficiente reduce riesgos de acoplamiento y mejora la escalabilidad.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **architecture.md y domain driven design**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La seguridad debe ser un eje arquitectónico, no un detalle a último momento.
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
### ❓ ¿Qué datos sensibles maneja mi sistema?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la seguridad debe ser un eje arquitectónico, no un detalle a último momento. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy limitando el acceso y la exposición de información de forma consciente?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la confianza del usuario depende del manejo responsable de datos. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Mis APIs están documentadas y versionadas de forma clara?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con hay que proteger no solo la aplicación, sino sus flujos de datos y sus dependencias. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué pasa si un cliente usa una versión anterior?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la privacidad implica principio de mínimo privilegio y minimización de datos. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa architecture.md y domain driven design y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La seguridad debe ser un eje arquitectónico, no un detalle a último momento. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Un sistema con buena arquitectura no solo resuelve necesidades funcionales, sino que protege la información, reduce riesgos y genera confianza. La seguridad y la privacidad no se agregan al final: se diseñan desde el principio.

Las integraciones son una parte central de la arquitectura moderna. Si las APIs no están bien definidas, la evolución del sistema se vuelve costosa y frágil. Diseñar contratos claros es una capacidad esencial del arquitecto.

## Preguntas para preparar la grabación
- ¿Qué datos sensibles maneja mi sistema?
- ¿Estoy limitando el acceso y la exposición de información de forma consciente?
- ¿Mis APIs están documentadas y versionadas de forma clara?
- ¿Qué pasa si un cliente usa una versión anterior?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
