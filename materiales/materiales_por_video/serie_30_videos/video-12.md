# Video 12: Estrategia tecnológica y roadmap

## Fuentes oficiales
- [Estrategia tecnológica y roadmap](https://platzi.com/cursos/fundamentos-arquitectura-software/evolucionar-un-mvp-sin-rearquitectar-des/)
- [Estrategia tecnológica y roadmap](https://platzi.com/cursos/fundamentos-arquitectura-software/evolucionar-un-mvp-sin-rearquitectar-des/)

## 🔗 Navegación
[⬅️ Video anterior](video-11.md) | [➡️ Video siguiente](video-13.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Estrategia tecnológica y roadmap**
Este video enfatiza que la arquitectura no debe ir a la deriva. Debe estar guiada por una estrategia tecnológica clara que defina prioridades, inversiones y objetivos a largo plazo. El roadmap transforma la visión en un plan de acción, permitiendo que el sistema evolucione de manera ordenada y con menos improvisación.

Cuando no hay estrategia, cada decisión responde más a una urgencia que a un criterio sostenible. En ese contexto, el sistema crece sin dirección, y la deuda técnica se acumula. El roadmap ayuda a alinear equipo, negocio y tecnología.

**Fuente 2: Estrategia tecnológica y roadmap**
Este video enfatiza que la arquitectura no debe ir a la deriva. Debe estar guiada por una estrategia tecnológica clara que defina prioridades, inversiones y objetivos a largo plazo. El roadmap transforma la visión en un plan de acción, permitiendo que el sistema evolucione de manera ordenada y con menos improvisación.

Cuando no hay estrategia, cada decisión responde más a una urgencia que a un criterio sostenible. En ese contexto, el sistema crece sin dirección, y la deuda técnica se acumula. El roadmap ayuda a alinear equipo, negocio y tecnología.

## Ideas que debes conservar
- La estrategia tecnológica da dirección al sistema.
- Un roadmap ayuda a priorizar y organizar el crecimiento.
- La arquitectura debe responder a objetivos de negocio y capacidades reales.
- Sin estrategia, la solución se vuelve reactiva.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **estrategia tecnológica y roadmap**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La estrategia tecnológica da dirección al sistema.
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

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la estrategia tecnológica da dirección al sistema. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Tengo un plan claro de evolución o solo reacciones inmediatas?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un roadmap ayuda a priorizar y organizar el crecimiento. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué dirección tecnológica está tomando mi proyecto?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura debe responder a objetivos de negocio y capacidades reales. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Tengo un plan claro de evolución o solo reacciones inmediatas?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con sin estrategia, la solución se vuelve reactiva. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa estrategia tecnológica y roadmap y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La estrategia tecnológica da dirección al sistema. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La estrategia tecnológica es la base que le da sentido a la arquitectura. Sin ella, la solución se vuelve más reactiva y menos sostenida.

La estrategia tecnológica es la base que le da sentido a la arquitectura. Sin ella, la solución se vuelve más reactiva y menos sostenida.

## Preguntas para preparar la grabación
- ¿Qué dirección tecnológica está tomando mi proyecto?
- ¿Tengo un plan claro de evolución o solo reacciones inmediatas?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
