# Video 05: Principios de diseño, acoplamiento y cohesión

## Fuentes oficiales
- [Platzi: Fundamentos de diseño y principios de arquitectura](https://platzi.com/cursos/fundamentos-arquitectura-software/costo-total-de-operacion-en-arquitectura/)
- [Platzi: Acoplamiento, cohesión y calidad estructural](https://platzi.com/cursos/fundamentos-arquitectura-software/alineacion-de-arquitectura-de-software-c/)

## 🔗 Navegación
[⬅️ Video anterior](video-04.md) | [➡️ Video siguiente](video-06.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Fundamentos de diseño y principios de arquitectura**
Este video presenta los fundamentos del diseño arquitectónico: cómo una solución técnica debe estructurarse para ser clara, sostenible y adaptable. La arquitectura no se basa solo en elegir herramientas, sino en aplicar principios que guíen la organización del sistema. Entre esos principios están la modularidad, la separación de responsabilidades, la reutilización con sentido y la reducción del acoplamiento.

La idea central es que un sistema bien diseñado no solo funciona, sino que es más fácil de entender, mantener y evolucionar. Los principios de arquitectura sirven como brújula para tomar decisiones con criterio, especialmente cuando el proyecto crece en complejidad.

**Fuente 2: Acoplamiento, cohesión y calidad estructural**
Este video explica dos conceptos centrales en arquitectura: acoplamiento y cohesión. El acoplamiento mide cuán dependientes son componentes entre sí; la cohesión mide qué tan relacionadas están las responsabilidades dentro de un mismo módulo o servicio. La mejor arquitectura busca baja dependencia entre partes y alta claridad dentro de cada parte.

Cuando el acoplamiento es alto, hacer cambios implica romper varias piezas del sistema. Cuando la cohesión es baja, una entidad se vuelve confusa y difícil de mantener. La calidad estructural del software se mejora cuando se reducen dependencias innecesarias y se ordenan bien las responsabilidades.

## Ideas que debes conservar
- El diseño arquitectónico no es un detalle opcional.
- Los principios ayudan a sostener decisiones de largo plazo.
- La modularidad mejora la claridad y la evolución del sistema.
- La separación de responsabilidades reduce complejidad.
- El acoplamiento alto genera fragilidad.
- La cohesión alta mejora claridad y mantenibilidad.
- La arquitectura debe disminuir dependencias innecesarias.
- Un sistema con responsabilidades bien definidas es más fácil de evolucionar.

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
Los principios de diseño son la base para crear sistemas más claros, más sostenibles y más fáciles de hacer crecer con seguridad.

La calidad estructural de un sistema está marcada por la forma en que se separan sus responsabilidades y cómo se gestionan sus dependencias.

## Preguntas para preparar la grabación
- ¿Qué parte de mi sistema tiene responsabilidades mezcladas?
- ¿Qué principio arquitectónico me está faltando aplicar?
- ¿Qué tan acoplado está mi sistema en este momento?
- ¿Qué modulos tienen demasiadas responsabilidades mezcladas?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
