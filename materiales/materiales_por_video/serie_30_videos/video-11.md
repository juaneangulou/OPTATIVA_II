# Video 11: Evolución, riesgos y costos

## Fuentes oficiales
- [Estructura de software y evolución del sistema](https://platzi.com/cursos/fundamentos-arquitectura-software/patrones-de-software-para-arquitectos/)
- [Riesgos, costos y decisiones bajo incertidumbre](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitectura-mvp-de-telegram-a-remarkabl/)

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
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **evolución, riesgos y costos**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: El sistema evolucionará; la arquitectura debe anticiparlo.
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
### ❓ ¿Qué tan costoso es cambiar una parte del sistema hoy?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el sistema evolucionará; la arquitectura debe anticiparlo. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué piezas del software están más rígidas o frágiles?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la estructura define cuán costoso es cambiar el software. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué decisiones de mi proyecto se están tomando con mucha incertidumbre?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un diseño claro reduce impacto de cambios y nuevos requerimientos. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan reversible es esta decisión si cambian las condiciones?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la evolución del sistema requiere capacidad de adaptación. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa evolución, riesgos y costos y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El sistema evolucionará; la arquitectura debe anticiparlo. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


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
