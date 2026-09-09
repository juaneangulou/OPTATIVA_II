# Video 16: Monorepos, trunk-based development y calidad

## Fuentes oficiales
- [Contexto, negocio y decisiones arquitectónicas](https://platzi.com/cursos/software-avanzado/monorepos-con-pantsbuild-en-proyectos-re/)
- [Principios, calidad y trade-offs](https://platzi.com/cursos/software-avanzado/trunk-based-development-con-rulesets-en/)

## 🔗 Navegación
[⬅️ Video anterior](video-15.md) | [➡️ Video siguiente](video-17.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Contexto, negocio y decisiones arquitectónicas**
El video muestra que la arquitectura de software no se construye en un vacío técnico. Cada decisión depende del contexto del negocio, los objetivos del cliente, las personas involucradas, las restricciones de tiempo, costo, seguridad y operación. Un sistema excelente para un caso puede ser inútil para otro si no se toma en cuenta el entorno.

Por eso, el arquitecto debe interpretar no solo requisitos funcionales, sino también necesidades de negocio, riesgos, evolución esperada, experiencia del usuario y capacidad operativa del equipo. La arquitectura deja de ser una actividad puramente técnica y se convierte en una actividad de análisis, negociación y toma de decisiones. En otras palabras, no se diseña solo para resolver un problema lógico; se diseña para resolver un problema real dentro de un contexto real.

**Fuente 2: Principios, calidad y trade-offs**
Este video habla de una realidad central en arquitectura de software: no existe una solución perfecta para todos los casos, sino decisiones que equilibran objetivos en conflicto. A menudo el equipo quiere velocidad, el negocio quiere menor costo, la operación quiere estabilidad y el usuario quiere experiencia rápida. La arquitectura de software consiste en resolver esas tensiones con criterio técnico y estratégico.

La idea principal es que la calidad del diseño no se mide solo por cuán elegante es, sino por cuán bien se adapta al problema real. Un sistema puede ser técnicamente sofisticado y aun así ser un mal diseño si no considera costo, complejidad, operatividad y capacidad de evolución. El video enfatiza la importancia de principios, ya que los principios ayudan a tomar decisiones cuando no hay una respuesta única.

## Ideas que debes conservar
- Los requisitos técnicos no son suficientes; el negocio da la forma de la solución.
- El contexto define qué es una buena decisión y qué no lo es.
- Un gran diseño debe equilibrar funcionalidad, costos, tiempo y complejidad.
- El arquitecto actúa como traductor entre negocio y tecnología.
- No todo en arquitectura es absoluto; muchas decisiones implican trade-offs.
- La calidad del diseño depende del contexto, no de una fórmula universal.
- Un sistema debe balancear velocidad, claridad, costo, rendimiento y sostenibilidad.
- Los principios técnicos ayudan a evitar decisiones impulsivas o improvisadas.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **monorepos, trunk-based development y calidad**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: Los requisitos técnicos no son suficientes; el negocio da la forma de la solución.
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
### ❓ ¿Qué restricciones del negocio están impactando mi diseño actual?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con los requisitos técnicos no son suficientes; el negocio da la forma de la solución. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy resolviendo el problema real o solo la versión técnica de ese problema?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el contexto define qué es una buena decisión y qué no lo es. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué trade-off estoy asumiendo sin darme cuenta en mi proyecto?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un gran diseño debe equilibrar funcionalidad, costos, tiempo y complejidad. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy priorizando la solución más elegante o la más adecuada?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el arquitecto actúa como traductor entre negocio y tecnología. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa monorepos, trunk-based development y calidad y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: Los requisitos técnicos no son suficientes; el negocio da la forma de la solución. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Una buena arquitectura no se mide solo por su elegancia técnica, sino por su capacidad de responder a un problema auténtico con sentido de negocio. El mejor diseño es aquel que sirve al contexto y no el que solo parece bonito desde el punto de vista teórico.

La arquitectura no es una búsqueda de perfección abstracta, sino de equilibrio. El arquitecto debe aprender a elegir entre alternativas con sentido, entendiendo que cada decisión tiene consecuencias en costo, mantenimiento y evolución del sistema.

## Preguntas para preparar la grabación
- ¿Qué restricciones del negocio están impactando mi diseño actual?
- ¿Estoy resolviendo el problema real o solo la versión técnica de ese problema?
- ¿Qué trade-off estoy asumiendo sin darme cuenta en mi proyecto?
- ¿Estoy priorizando la solución más elegante o la más adecuada?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
