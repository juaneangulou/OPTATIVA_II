# Video 11: Evolución, riesgos y costos

## Fuentes oficiales
- [Platzi: Estructura de software y evolución del sistema](https://platzi.com/cursos/fundamentos-arquitectura-software/patrones-de-software-para-arquitectos/)
- [Platzi: Riesgos, costos y decisiones bajo incertidumbre](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitectura-mvp-de-telegram-a-remarkabl/)

## 🔗 Navegación
[⬅️ Video anterior](video-10.md) | [➡️ Video siguiente](video-12.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Estructura de software y evolución del sistema**
Este video resalta la relación entre la estructura del software y su capacidad de evolución. Los sistemas no son estáticos; cambian con el tiempo, según la carga, el negocio, las reglas y las necesidades del usuario. Por eso, la arquitectura debe permitir cambios sin provocar caos. La estructura del software debe facilitar adaptaciones, no volverlas costosas o riesgosas.

Cuando la estructura del sistema es clara, modular y bien diseñada, el cambio no rompe todo. Cuando está mal organizada, cada ajuste requiere correcciones complejas y difíciles de prever. La evolución del software depende directamente de la calidad de su arquitectura.

**Fuente 2: Riesgos, costos y decisiones bajo incertidumbre**
Este video habla de los riesgos y costos que subyacen a cada decisión arquitectónica. No siempre se tiene toda la información antes de elegir una solución. En ese contexto, el arquitecto debe evaluar qué tan reversible es la decisión, cuál es su costo real y qué riesgos conlleva. La incertidumbre es normal, pero la mala gestión de la misma puede generar decisiones impulsivas o demasiado rígidas.

La toma de decisiones bajo incertidumbre exige criterio: priorizar opciones que permitan aprender, adaptarse y cambiar sin grandes pérdidas. Así, el sistema se vuelve más resiliente frente a cambios de negocio o de contexto.

## Ideas que debes conservar
- El sistema evolucionará; la arquitectura debe anticiparlo.
- La estructura define cuán costoso es cambiar el software.
- Un diseño claro Reduce impacto de cambios y nuevos requerimientos.
- La evolución del sistema requiere capacidad de adaptación.
- La incertidumbre es parte del trabajo arquitectónico.
- Cada decisión tiene costos y riesgos que no siempre son visibles de inmediato.
- La reversibilidad ayuda a decisión bajo cambios.
- La arquitectura debe permitir aprender y ajustar.

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
La capacidad de evolución es una medida de calidad arquitectónica. Los sistemas más sólidos son aquellos que soportan cambios sin destruir su lógica ni su estabilidad.

Bajo incertidumbre, la mejor decisión no siempre es la más ambiciosa, sino la que permite aprender, adaptarse y sostener el sistema con menos riesgo.

## Preguntas para preparar la grabación
- ¿Qué tan costoso es cambiar una parte del sistema hoy?
- ¿Qué piezas del software están más rígidas o frágiles?
- ¿Qué decisiones de mi proyecto se están tomando con mucha incertidumbre?
- ¿Qué tan reversible es esta decisión si cambian las condiciones?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
