# Video 24: Mensajes, eventos y productor-consumidor

## Fuentes oficiales
- [Madurez arquitectónica y evolución continua](https://platzi.com/cursos/software-avanzado/mensajes-vs-eventos-en-microservicios/)
- [Cierre del curso y próximos pasos](https://platzi.com/cursos/software-avanzado/patron-productor-consumidor-vs-fan-in-y/)

## 🔗 Navegación
[⬅️ Video anterior](video-23.md) | [➡️ Video siguiente](video-25.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Madurez arquitectónica y evolución continua**
Este video reflexiona sobre la madurez de una arquitectura: no se trata de llegar a una solución “perfecta” de una vez, sino de ir desarrollando capacidades para manejar complejidad, cambios y crecimiento sin perder control. La madurez arquitectónica se observa cuando un equipo es capaz de aprender del sistema, ajustar decisiones, evolucionar sus procesos y mantener calidad aunque el negocio cambie.

La evolución continua es parte esencial de la arquitectura moderna. Un sistema no debe quedar congelado en una decisión inicial; debe poder adaptarse a nuevos requerimientos, nuevas tecnologías y nuevos riesgos. Esa capacidad de evolución depende tanto del diseño como del hábito de revisión, observación y mejora constante.

**Fuente 2: Cierre del curso y próximos pasos**
El curso culmina con una visión integradora: la arquitectura de software es una disciplina de pensamiento, decisión y responsabilidad. No se trata de seguir patrones por moda ni de aplicar herramientas por entusiasmo, sino de construir sistemas que resuelvan problemas reales, respeten el contexto y puedan evolucionar con el tiempo. La arquitectura exige equilibrio entre rigor técnico, sensibilidad de negocio y capacidad de liderazgo.

El cierre invita a la reflexión sobre el camino profesional: el arquitecto no nace solo con conocimiento, sino con la habilidad de combinar criterio, experiencia, observación y mejora constante. La invitación final es continuar aprendiendo, enfrentando problemas reales, cuestionando decisiones y construyendo software con propósito. La diferencia entre un buen desarrollador y un buen arquitecto no está en la cantidad de herramientas que conoce, sino en cómo piensa y decide ante la complejidad.

## Ideas que debes conservar
- La madurez arquitectónica se construye con el tiempo.
- Un sistema no se vuelve mejor solo por agregar más tecnología.
- La evolución continua permite mantener claridad a medida que crece la complejidad.
- El equipo debe aprender a revisar decisiones y rediseñar cuando sea necesario.
- La arquitectura es una disciplina de decisión y pensamiento, no solo de herramientas.
- La práctica real es donde se desarrollan las habilidades arquitectónicas.
- Los mejores arquitectos combinan técnica, estrategia y criterio humano.
- La evolución profesional se construye con experiencia, análisis y reflexión.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **mensajes, eventos y productor-consumidor**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La madurez arquitectónica se construye con el tiempo.
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
### ❓ ¿Mi arquitectura está creciendo con el sistema o volviéndose rígida?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la madurez arquitectónica se construye con el tiempo. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy revisando mis decisiones de forma periódica?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un sistema no se vuelve mejor solo por agregar más tecnología. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué aspectos del curso más me impactaron como profesional?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la evolución continua permite mantener claridad a medida que crece la complejidad. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué decisiones arquitectónicas quiero aplicar en mis proyectos reales?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el equipo debe aprender a revisar decisiones y rediseñar cuando sea necesario. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa mensajes, eventos y productor-consumidor y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La madurez arquitectónica se construye con el tiempo. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La madurez arquitectónica no es un estado final; es un proceso de aprendizaje, ajuste y mejora constante. La arquitectura más sólida es la que puede evolucionar sin perder coherencia ni calidad.

El curso se cierra con una idea clave: el software de calidad no se construye solo con código, sino con visión, método, criterio y responsabilidad. Los próximos pasos consisten en aplicar estas ideas en proyectos reales, seguir aprendiendo y asumir la arquitectura como una práctica de crecimiento profesional y de impacto real.

## Preguntas para preparar la grabación
- ¿Mi arquitectura está creciendo con el sistema o volviéndose rígida?
- ¿Estoy revisando mis decisiones de forma periódica?
- ¿Qué aspectos del curso más me impactaron como profesional?
- ¿Qué decisiones arquitectónicas quiero aplicar en mis proyectos reales?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
