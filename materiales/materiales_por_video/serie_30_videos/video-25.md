# Video 25: Dead Letter Queue y consumidores en tiempo real

## Fuentes oficiales
- [Platzi: Diseño para cambio y evolución](https://platzi.com/cursos/software-avanzado/dead-letter-queue-en-productor-consumido/)
- [Platzi: Calidad de servicio y experiencia de usuario](https://platzi.com/cursos/software-avanzado/patron-comparing-consumers-para-procesam/)

## 🔗 Navegación
[⬅️ Video anterior](video-24.md) | [➡️ Video siguiente](video-26.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Diseño para cambio y evolución**
Este video introduce una de las ideas más importantes de la arquitectura moderna: un sistema no solo debe resolver el problema actual, sino prepararse para cambiar cuando cambien las necesidades del negocio o el contexto. El diseño arquitectónico debe pensar en la evolución como una variable esperada, no como una excepción. Por eso se enfatizan principios como la modularidad, la flexibilidad, la separación de responsabilidades y la protección de las capas críticas del sistema.

Cuando el software se diseña para el cambio, se vuelve más sostenible. En cambio, si se construye como una estructura rígida y demasiado acoplada, cualquier cambio pequeño termina convirtiéndose en una tarea riesgosa. La arquitectura entonces deja de ser una estructura estática y pasa a ser una base que permite crecer y adaptarse con menos fricción.

**Fuente 2: Calidad de servicio y experiencia de usuario**
La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna.

## Ideas que debes conservar
- La evolución es una característica normal del software, no un problema excepcional.
- Un buen diseño reduce el costo de cambiar.
- La modularidad permite aislar áreas del sistema y facilitar adaptaciones.
- La arquitectura debe proteger los puntos sensibles del negocio.
- La experiencia del usuario es una consecuencia del diseño arquitectónico.
- Calidad técnica y calidad de servicio no son conceptos separados.
- El tiempo de respuesta, la estabilidad y la claridad influyen en la percepción del sistema.
- Un servicio bueno no solo funciona; funciona con un nivel de calidad soportable.

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
La arquitectura más útil es la que acepta que el sistema cambiará. Cuando el diseño está preparado para la evolución, el software se vuelve más robusto, adaptable y sostenible.

La arquitectura debe diseñarse para entregar valor no solo dentro del equipo técnico, sino también en la experiencia real del usuario. La calidad de servicio aparece como indicador de que la solución responde bien a las necesidades del entorno.

## Preguntas para preparar la grabación
- ¿Qué partes de mi sistema son difíciles de cambiar?
- ¿Estoy diseñando para el futuro o solo para la versión actual?
- ¿Qué tan buena es la experiencia de uso de mi sistema?
- ¿Qué factores técnicos afectan la percepción del usuario?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
