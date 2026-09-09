# Video 26: Process Manager, Durable State y Event Sourcing

## Fuentes oficiales
- [Platzi: Estrategia tecnológica y roadmap](https://platzi.com/cursos/software-avanzado/que-es-el-patron-process-manager/)
- [Platzi: Evaluación de tecnologías y decisiones de stack](https://platzi.com/cursos/software-avanzado/durable-state-vs-event-sourcing-en-siste/)

## 🔗 Navegación
[⬅️ Video anterior](video-25.md) | [➡️ Video siguiente](video-27.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Estrategia tecnológica y roadmap**
El video aborda el papel de la estrategia tecnológica en la arquitectura. No basta con elegir una buena herramienta o un patrón útil; también hace falta una dirección clara para el camino del sistema. Una estrategia tecnológica define hacia dónde va la solución, qué capacidades se priorizan, qué riesgos se asumen y qué inversiones son necesarias para que la arquitectura evolucione de forma ordenada.

El roadmap se convierte en la herramienta que convierte la visión en acción. Cuando hay estrategia y planificación, el equipo evita decisiones aisladas y poco alineadas. El arquitecto tiene un rol importante en definir no solo cómo se construye el sistema, sino también qué se prioriza y en qué orden.

**Fuente 2: Evaluación de tecnologías y decisiones de stack**
La elección de tecnologías es una decisión arquitectónica y no una cuestión de moda. Cada stack tiene ventajas, costos y limitaciones. El video insiste en que seleccionar una tecnología debe hacerse con base en el problema, la capacidad del equipo, los requisitos de operación, la curva de aprendizaje y la sostenibilidad a largo plazo.

Muchas veces se adopta una tecnología por popularidad, pero eso no garantiza que se adapte bien al caso real. La evaluación del stack debe incluir mantenimiento, soporte, costos operativos, compatibilidad, seguridad y potencial de crecimiento. Así, la decisión de usar determinada herramienta o framework se vuelve más estratégica y menos impulsiva.

## Ideas que debes conservar
- La estrategia tecnológica guía la evolución del sistema.
- Un roadmap ayuda a convertir visión en decisiones secuenciales.
- Las decisiones deben priorizar capacidades que generen valor real.
- Sin estrategia, la arquitectura puede volverse reactiva y caótica.
- Las tecnologías deben elegirse por contexto, no por tendencia.
- Cada stack implica costos de operación, entrenamiento y mantenimiento.
- Un buen stack debe facilitar velocidad de entrega y sostenibilidad.
- La elección tecnológica debe estar alineada con la estrategia del sistema.

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
La estrategia y el roadmap son lo que hacen que la arquitectura deje de ser una respuesta improvisada y se convierta en una dirección clara. Un sistema necesita visión para crecer sin perder coherencia.

Elegir tecnologías es una forma de diseñar la capacidad del sistema para seguir funcionando bien en el futuro. La mejor decisión es la que resuelve el problema real con menos deuda técnica y menos riesgo.

## Preguntas para preparar la grabación
- ¿Qué dirección tecnológica está tomando mi proyecto?
- ¿Tengo una hoja de ruta clara o solo decisiones aisladas?
- ¿Estoy eligiendo tecnología por necesidad o por tendencia?
- ¿Qué tan bien se adapta mi stack a los objetivos del proyecto?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
