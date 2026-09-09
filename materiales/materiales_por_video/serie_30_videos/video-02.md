# Video 02: Rol del arquitecto y comunicación

## Fuentes oficiales
- [Rol del arquitecto de software](https://platzi.com/cursos/fundamentos-arquitectura-software/78360-que-hace-un-arquitecto-de-software/)
- [Comunicar la arquitectura](https://platzi.com/cursos/fundamentos-arquitectura-software/problemas-esenciales-vs-accidentales-en/)

## 🔗 Navegación
[⬅️ Video anterior](video-01.md) | [➡️ Video siguiente](video-03.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Rol del arquitecto de software**
En este video se redefine el rol del arquitecto, dejando atrás la idea de que solo dibuja diagramas. El arquitecto debe diseñar sistemas sólidos y sostenibles, simplificar la complejidad, cuestionar supuestos y negociar con distintos stakeholders. Además, tiene que entender que cada decisión técnica tiene consecuencias reales.

El trabajo del arquitecto no es imponer una solución elegante por gusto; es crear sistemas confiables, duraderos y bien pensados para el futuro. Esto implica abstraer lo esencial, priorizar la claridad, identificar riesgos y tomar decisiones con criterio técnico y de negocio.

**Fuente 2: Comunicar la arquitectura**
El video resalta un problema muy común: la falta de claridad a la hora de documentar decisiones. Cuando la arquitectura no se comunica bien, el mantenimiento, la evolución y la comprensión del sistema se vuelven mucho más difíciles. El resultado es un proyecto más frágil y más costoso de sostener.

La solución propuesta es crear un archivo ARCHITECTURE.md en la raíz del repositorio. Ese documento debe explicar el propósito del software, sus módulos, sus restricciones y los riesgos más importantes. La idea es que la arquitectura sea comprensible y que cualquiera pueda entenderla sin tener que leer todo el sistema desde cero.

## Ideas que debes conservar
- El arquitecto no es solo un dibujante de diagramas.
- Debe abstraer la complejidad y simplificar lo esencial.
- Tiene que cuestionar supuestos, tanto técnicos como de negocio.
- Debe negociar con usuarios, directivos y equipo.
- La falta de documentación dificulta mantenimiento y evolución.
- La arquitectura debe ser comunicada, no solo construida.
- Un ARCHITECTURE.md ayuda a dejar claridad documental del sistema.
- Debe incluir propósito general, módulos principales y restricciones.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **rol del arquitecto y comunicación**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: El arquitecto no es solo un dibujante de diagramas.
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
### ❓ ¿Qué tan claro es mi papel como arquitecto o líder técnico en el proyecto?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el arquitecto no es solo un dibujante de diagramas. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy cuestionando suposiciones o aceptando decisiones sin analizar consecuencias?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con debe abstraer la complejidad y simplificar lo esencial. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Mi proyecto está documentado lo suficiente para entender su propósito?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con tiene que cuestionar supuestos, tanto técnicos como de negocio. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan fácil es para otra persona entender la arquitectura actual?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con debe negociar con usuarios, directivos y equipo. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa rol del arquitecto y comunicación y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El arquitecto no es solo un dibujante de diagramas. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
El papel del arquitecto es más amplio que la solución técnica: es diseñar sistemas con estrategia, criterio y responsabilidad. La arquitectura sirve para transformar complejidad en claridad.

El sistema no solo debe funcionar; también debe entenderse. Comunicar la arquitectura es una práctica que mejora la sostenibilidad del proyecto y reduce la deuda técnica.

## Preguntas para preparar la grabación
- ¿Qué tan claro es mi papel como arquitecto o líder técnico en el proyecto?
- ¿Estoy cuestionando suposiciones o aceptando decisiones sin analizar consecuencias?
- ¿Mi proyecto está documentado lo suficiente para entender su propósito?
- ¿Qué tan fácil es para otra persona entender la arquitectura actual?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
