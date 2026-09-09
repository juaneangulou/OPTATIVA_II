# Video 06: Dominios y límites de contexto

## Fuentes oficiales
- [Platzi: Modelado de dominios y límites de contexto](https://platzi.com/cursos/fundamentos-arquitectura-software/mindset-del-arquitecto-que-abraza-el-cam/)
- [Platzi: Diseño para cambio y evolución](https://platzi.com/cursos/software-avanzado/dead-letter-queue-en-productor-consumido/)

## 🔗 Navegación
[⬅️ Video anterior](video-05.md) | [➡️ Video siguiente](video-07.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Modelado de dominios y límites de contexto**
Este video habla sobre un enfoque clásico en arquitectura: modelar el dominio del negocio y definir límites claros entre contextos. El objetivo es separar áreas con responsabilidades distintas para evitar mezclar conceptos y reglas de negocio que no pertenecen al mismo problema. Cuando esto no se hace, el sistema termina con lógica mezclada, reglas contradictorias y mayor complejidad.

El modelado del dominio permite entender mejor qué es lo que realmente hace el negocio, y cómo la solución debe reflejarlo. Los límites de contexto ayudan a definir dónde termina una responsabilidad y comienza otra, reduciendo confusión en la lógica del sistema.

**Fuente 2: Diseño para cambio y evolución**
Este video introduce una de las ideas más importantes de la arquitectura moderna: un sistema no solo debe resolver el problema actual, sino prepararse para cambiar cuando cambien las necesidades del negocio o el contexto. El diseño arquitectónico debe pensar en la evolución como una variable esperada, no como una excepción. Por eso se enfatizan principios como la modularidad, la flexibilidad, la separación de responsabilidades y la protección de las capas críticas del sistema.

Cuando el software se diseña para el cambio, se vuelve más sostenible. En cambio, si se construye como una estructura rígida y demasiado acoplada, cualquier cambio pequeño termina convirtiéndose en una tarea riesgosa. La arquitectura entonces deja de ser una estructura estática y pasa a ser una base que permite crecer y adaptarse con menos fricción.

## Ideas que debes conservar
- El dominio del negocio debe reflejarse en la estructura del software.
- Los límites de contexto ayudan a ordenar responsabilidades.
- Mezclar dominios distintos genera confusión y errores.
- Un diseño basado en el dominio es más comprensible y sostenible.
- La evolución es una característica normal del software, no un problema excepcional.
- Un buen diseño reduce el costo de cambiar.
- La modularidad permite aislar áreas del sistema y facilitar adaptaciones.
- La arquitectura debe proteger los puntos sensibles del negocio.

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
Modelar correctamente el dominio y definir límites de contexto es esencial para crear sistemas más claros y coherentes con la realidad del negocio.

La arquitectura más útil es la que acepta que el sistema cambiará. Cuando el diseño está preparado para la evolución, el software se vuelve más robusto, adaptable y sostenible.

## Preguntas para preparar la grabación
- ¿Mi sistema mezcla conceptos de diferentes dominios?
- ¿Dónde está el límite claro entre áreas funcionales?
- ¿Qué partes de mi sistema son difíciles de cambiar?
- ¿Estoy diseñando para el futuro o solo para la versión actual?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
