# Video 08: APIs, contratos e infraestructura

## Fuentes oficiales
- [APIs y contratos de integración](https://platzi.com/cursos/fundamentos-arquitectura-software/que-son-las-arquitecturas-monoliticas-y/)
- [Infraestructura, despliegue y entorno de ejecución](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitecturas-orientadas-a-servicios-con/)

## 🔗 Navegación
[⬅️ Video anterior](video-07.md) | [➡️ Video siguiente](video-09.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: APIs y contratos de integración**
Este video centra la atención en la forma en que los sistemas se integran entre sí. Las APIs son contratos entre partes: representan cómo se comunica un servicio con otro y cómo se comparte información. Cuando esos contratos son claros, la integración es más productiva y menos frágil. Cuando no lo son, se vuelven fuentes de errores, incompatibilidades y cambios difíciles de gestionar.

El diseño de APIs incluye no solo endpoints o rutas, sino también formato, validaciones, errores, versionado y políticas de evolución. Una buena API debe ser clara, estable y fácil de consumirse por el equipo o por sistemas externos.

**Fuente 2: Infraestructura, despliegue y entorno de ejecución**
Este video muestra que la arquitectura incluye también la infraestructura que ejecuta el sistema. Un diseño puede ser excelente en código, pero si el entorno de ejecución es caótico, manual o poco reproducible, la aplicación no será sostenible. La arquitectura debe considerar tanto la capa lógica como la capa operativa que la pone en marcha.

La infraestructura debe ser fácil de reproducir, detectar fallos y trasladar entre entornos. Los despliegues automatizados y los procesos de entorno ayudan a reducir errores humanos y mejorar la confianza del sistema en producción.

## Ideas que debes conservar
- Las APIs son acuerdos de comunicación entre sistemas.
- Los contratos deben ser claros y bien documentados.
- El versionado reduce riesgos de romper dependencias.
- Una mala API genera fragilidad en la integración.
- La infraestructura es parte del diseño arquitectónico.
- El entorno debe ser reproducible y consistente.
- Un despliegue manual aumenta riesgos y errores.
- La infraestructura debe soportar diferentes contextos: desarrollo, prueba y producción.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **apis, contratos e infraestructura**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: Las APIs son acuerdos de comunicación entre sistemas.
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
### ❓ ¿Mis interfaces están bien definidas y documentadas?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con las apis son acuerdos de comunicación entre sistemas. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué pasa si un cliente usa una versión anterior?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con los contratos deben ser claros y bien documentados. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Mi entorno es reproducible y consistente?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el versionado reduce riesgos de romper dependencias. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan fácil es desplegar una versión nueva sin riesgos innecesarios?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con una mala api genera fragilidad en la integración. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa apis, contratos e infraestructura y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: Las APIs son acuerdos de comunicación entre sistemas. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
El diseño de APIs es una parte central de la arquitectura. Un buen contrato de integración mejora la evolución del sistema y reduce errores de colaboración entre equipos.

La arquitectura no termina en el código: incluye cómo se ejecuta, se despliega y se mantiene. Un sistema bien diseñado también necesita un entorno bien pensado.

## Preguntas para preparar la grabación
- ¿Mis interfaces están bien definidas y documentadas?
- ¿Qué pasa si un cliente usa una versión anterior?
- ¿Mi entorno es reproducible y consistente?
- ¿Qué tan fácil es desplegar una versión nueva sin riesgos innecesarios?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
