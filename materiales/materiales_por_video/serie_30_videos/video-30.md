# Video 30: Cierre y defensa de la arquitectura

## Fuentes oficiales
- [Cierre profesional y legado arquitectónico](https://platzi.com/cursos/software-avanzado/sabiduria-y-criterio-en-arquitectura-de/)

## 🔗 Navegación
[⬅️ Video anterior](video-29.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Cierre profesional y legado arquitectónico**
El curso finaliza con una reflexión sobre el legado que deja un arquitecto. No se trata solo de construir sistemas que funcionen durante un proyecto, sino de dejar una base sólida, una cultura de calidad y una forma de pensar que perdure en el tiempo. El verdadero legado de la arquitectura no son los diagramas o las herramientas elegidas, sino la capacidad de crear sistemas que sigan aportando valor y que puedan ser entendidos, mejorados y heredados por otras personas.

Este cierre reúne todos los temas del curso: paciencia, criterio, responsabilidad, visión, estrategia, empatía y mejora continua. El arquitecto no crea solo software; crea una infraestructura de conocimiento, decisiones y confianza que acompaña la evolución del negocio y del equipo.

## Ideas que debes conservar
- El verdadero legado arquitectónico no es solo el sistema, sino la forma en que se construyó.
- La arquitectura deja huella en el equipo, en la organización y en la forma de pensar.
- Un buen diseño puede ser heredado y mejorado por otras personas.
- La calidad del trabajo arquitectónico se refleja en la sostenibilidad y el valor a largo plazo.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **cierre y defensa de la arquitectura**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: El verdadero legado arquitectónico no es solo el sistema, sino la forma en que se construyó.
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
### ❓ ¿Qué legado quiero dejar en mis sistemas y en mi equipo?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el verdadero legado arquitectónico no es solo el sistema, sino la forma en que se construyó. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tipo de arquitecto quiero ser en el futuro?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura deja huella en el equipo, en la organización y en la forma de pensar. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa cierre y defensa de la arquitectura y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El verdadero legado arquitectónico no es solo el sistema, sino la forma en que se construyó. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
El camino de un arquitecto va más allá del código. Su legado es la capacidad de construir sistemas con propósito, mejorar la forma de trabajar del equipo y dejar una base sólida para que el futuro pueda crecer sin perder claridad ni calidad.

## Preguntas para preparar la grabación
- ¿Qué legado quiero dejar en mis sistemas y en mi equipo?
- ¿Qué tipo de arquitecto quiero ser en el futuro?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
