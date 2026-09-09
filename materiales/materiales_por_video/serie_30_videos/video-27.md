# Video 27: Máquinas de estado y seguridad de aplicaciones

## Fuentes oficiales
- [Platzi: Riesgos, costos y sostenibilidad financiera](https://platzi.com/cursos/software-avanzado/maquinas-de-estado-finito-en-el-front-en/)
- [Platzi: Arquitectura para equipos distribuidos](https://platzi.com/cursos/software-avanzado/tecnicas-sast-dast-y-pen-testing-para-se/)

## 🔗 Navegación
[⬅️ Video anterior](video-26.md) | [➡️ Video siguiente](video-28.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Riesgos, costos y sostenibilidad financiera**
La arquitectura de software también tiene implicaciones económicas. Un sistema no solo debe funcionar desde el punto de vista técnico; también debe ser viable desde el punto de vista financiero, operativo y de mantenimiento. Este video muestra que las decisiones de arquitectura implican costos directos e indirectos: infraestructura, equipos, tiempo, soporte, seguridad, correcciones y capacidad de adaptación.

La sostenibilidad financiera no es solo una preocupación del negocio; también afecta la arquitectura. Si el sistema es demasiado costoso de operar o difícil de mantener, su valor real disminuye. Por ello, el arquitecto debe ser capaz de medir el costo total de una solución y no solo el costo inicial de desarrollo.

**Fuente 2: Arquitectura para equipos distribuidos**
Cuando los equipos trabajan de forma distribuida, la arquitectura necesita ser más clara y más explícita. La comunicación, la coordinación y la documentación se vuelven críticos, porque el sistema no puede depender exclusivamente de la familiaridad entre personas. Un diseño bien estructurado permite que diferentes miembros del equipo trabajen en paralelo sin generar fricción o conflictos por responsabilidades ambiguas.

El video enfatiza que una arquitectura fuerte es también una herramienta de colaboración. Si el sistema está bien dividido, la documentación es clara y las interfaces están bien definidas, el equipo puede avanzar con menos fricción. Esto reduce errores de integración, soporta trabajo distribuido y mejora el flujo global del proyecto.

## Ideas que debes conservar
- La arquitectura tiene un costo real en infraestructura, operación y mantenimiento.
- Los riesgos técnicos y financieros deben evaluarse en conjunto.
- Un diseño barato al principio puede volverse muy costoso después.
- La sostenibilidad financiera depende del equilibrio entre valor y costo.
- La arquitectura facilita o complica el trabajo en equipo.
- Equipos distribuidos necesitan más claridad en interfaces y responsabilidades.
- La documentación y la comunicación son parte de la arquitectura efectiva.
- El diseño debe facilitar coordinación, no solo funcionalidad.

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
El software no es solo una decisión técnica: es también una decisión financiera y estratégica. Una arquitectura sostenible es la que crea valor sin generar costos ocultos que la vuelvan inviable con el tiempo.

La arquitectura no solo sirve para resolver un problema técnico; también permite que múltiples personas trabajen de manera coordinada y sostenida. En un equipo distribuido, la claridad arquitectónica es una ventaja de productividad y calidad.

## Preguntas para preparar la grabación
- ¿Qué costo total real tiene mi solución?
- ¿Estoy optimizando solo el desarrollo inicial o la sostenibilidad del sistema?
- ¿Qué tan claro está el sistema para otros miembros del equipo?
- ¿Hay dependencias ocultas que bloquean el trabajo colaborativo?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
