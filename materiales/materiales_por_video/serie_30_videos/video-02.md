# Video 02: Rol del arquitecto y comunicación

## Fuentes oficiales
- [Platzi: Rol del arquitecto de software](https://platzi.com/cursos/fundamentos-arquitectura-software/78360-que-hace-un-arquitecto-de-software/)
- [Platzi: Comunicar la arquitectura](https://platzi.com/cursos/fundamentos-arquitectura-software/problemas-esenciales-vs-accidentales-en/)

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
Analiza cómo este tema afecta pedidos, inventario, ruteo, entregas, notificaciones, incidentes y operación. Elige un flujo concreto y explica qué responsabilidad, dependencia o atributo de calidad queda protegido.

## Actividad de construcción
1. Resume en tus palabras la idea central de cada fuente.
2. Combina esas ideas en un problema arquitectónico único.
3. Propón dos alternativas de solución.
4. Compara costo inicial, calidad, riesgo, operación y facilidad de cambio.
5. Elige una alternativa para el MVP y declara qué condición obligaría a revisarla.
6. Produce una evidencia: ADR, diagrama, contrato, código C#, prueba, métrica o plan de evolución.

## Respuesta orientadora
Una respuesta sólida conecta las fuentes con el caso. No basta decir que una tecnología es mejor: debes explicar qué problema resuelve, qué costo introduce, qué alternativa descartas y cómo comprobarás la decisión.

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
