# Video 06: Dominios y límites de contexto

## Fuentes oficiales
- [Modelado de dominios y límites de contexto](https://platzi.com/cursos/fundamentos-arquitectura-software/mindset-del-arquitecto-que-abraza-el-cam/)
- [Diseño para cambio y evolución](https://platzi.com/cursos/software-avanzado/dead-letter-queue-en-productor-consumido/)

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
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **dominios y límites de contexto**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: El dominio del negocio debe reflejarse en la estructura del software.
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
### ❓ ¿Mi sistema mezcla conceptos de diferentes dominios?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el dominio del negocio debe reflejarse en la estructura del software. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Dónde está el límite claro entre áreas funcionales?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con los límites de contexto ayudan a ordenar responsabilidades. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué partes de mi sistema son difíciles de cambiar?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con mezclar dominios distintos genera confusión y errores. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy diseñando para el futuro o solo para la versión actual?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un diseño basado en el dominio es más comprensible y sostenible. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa dominios y límites de contexto y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El dominio del negocio debe reflejarse en la estructura del software. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


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
