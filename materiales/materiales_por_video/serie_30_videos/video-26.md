# Video 26: Process Manager, Durable State y Event Sourcing

## Fuentes oficiales
- [Estrategia tecnológica y roadmap](https://platzi.com/cursos/software-avanzado/que-es-el-patron-process-manager/)
- [Evaluación de tecnologías y decisiones de stack](https://platzi.com/cursos/software-avanzado/durable-state-vs-event-sourcing-en-siste/)

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
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **process manager, durable state y event sourcing**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La estrategia tecnológica guía la evolución del sistema.
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
### ❓ ¿Qué dirección tecnológica está tomando mi proyecto?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la estrategia tecnológica guía la evolución del sistema. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Tengo una hoja de ruta clara o solo decisiones aisladas?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un roadmap ayuda a convertir visión en decisiones secuenciales. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy eligiendo tecnología por necesidad o por tendencia?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con las decisiones deben priorizar capacidades que generen valor real. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan bien se adapta mi stack a los objetivos del proyecto?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con sin estrategia, la arquitectura puede volverse reactiva y caótica. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa process manager, durable state y event sourcing y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La estrategia tecnológica guía la evolución del sistema. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


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
