# Video 07: Monolitos, sistemas distribuidos y microservicios

## Fuentes oficiales
- [Monolito vs arquitectura distribuida](https://platzi.com/cursos/fundamentos-arquitectura-software/como-elegir-un-estilo-arquitectonico-sin/)
- [Microservicios y organización por dominios](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitectura-cliente-servidor-fundamento/)

## 🔗 Navegación
[⬅️ Video anterior](video-06.md) | [➡️ Video siguiente](video-08.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Monolito vs arquitectura distribuida**
Este video compara dos enfoques arquitectónicos muy comunes: el monolito y la arquitectura distribuida. El monolito puede ser una buena opción cuando el sistema es relativamente pequeño o cuando se desea velocidad de desarrollo y menor complejidad operativa. Sin embargo, cuando el proyecto crece y la organización requiere mayor desacople y evolución independiente, la arquitectura distribuida puede ser más apropiada.

La clave no es elegir una opción “mejor” en abstracto, sino seleccionar la que mejor se adapte a la complejidad real del sistema, el tamaño del equipo, la carga de trabajo y los objetivos de negocio. El problema aparece cuando se adopta una solución distribuida solo por moda, sin analizar su costo operativo.

**Fuente 2: Microservicios y organización por dominios**
La arquitectura basada en microservicios suele asociarse con escalabilidad y flexibilidad, pero también con mayor complejidad distribuidas. Este video explica que los microservicios no son una solución mágica: tienen sentido cuando la organización y el dominio del negocio lo justifican. Una buena división por servicios debe surgir del dominio, de las responsabilidades y de la capacidad de evolución del negocio.

La organización por dominios ayuda a definir límites claros y a separar áreas con objetivos diferentes. Cuando esto se hace bien, el sistema gana claridad. Cuando se hace mal, se vuelve difícil de operar, depurar y mantener.

## Ideas que debes conservar
- El monolito y la arquitectura distribuida tienen ventajas y costos distintos.
- La elección depende del problema real, no de la tendencia.
- El monolito reduce complejidad de operación, pero puede limitar evolución.
- La arquitectura distribuida mejora desacople y escalabilidad, pero aumenta complejidad.
- Los microservicios solo tienen valor si se justifican por el problema real.
- La división debe ser por dominio y responsabilidad, no por moda.
- El diseño por dominios ayuda a clarificar la estructura del sistema.
- Una arquitectura distribuida exige más coordinación y observabilidad.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **monolitos, sistemas distribuidos y microservicios**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: El monolito y la arquitectura distribuida tienen ventajas y costos distintos.
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
### ❓ ¿Mi sistema necesita más desacople o más simplicidad?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el monolito y la arquitectura distribuida tienen ventajas y costos distintos. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy adoptando una arquitectura por moda o por necesidad real?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la elección depende del problema real, no de la tendencia. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿La separación de servicios refleja bien el dominio del negocio?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el monolito reduce complejidad de operación, pero puede limitar evolución. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy aumentando complejidad operativa por una decisión no justificada?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura distribuida mejora desacople y escalabilidad, pero aumenta complejidad. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa monolitos, sistemas distribuidos y microservicios y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El monolito y la arquitectura distribuida tienen ventajas y costos distintos. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
No existe una arquitectura universalmente superior; la mejor opción es la que responde mejor al problema real, a la organización y a la capacidad de evolución del sistema.

Microservicios pueden ser útiles, pero solo cuando resuelven un problema real de organización, evolución y complejidad. La arquitectura debe simplificar, no complicar inútilmente.

## Preguntas para preparar la grabación
- ¿Mi sistema necesita más desacople o más simplicidad?
- ¿Estoy adoptando una arquitectura por moda o por necesidad real?
- ¿La separación de servicios refleja bien el dominio del negocio?
- ¿Estoy aumentando complejidad operativa por una decisión no justificada?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
