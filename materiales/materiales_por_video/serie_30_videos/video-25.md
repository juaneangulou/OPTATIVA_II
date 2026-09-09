# Video 25: Dead Letter Queue y consumidores en tiempo real

## Fuentes oficiales
- [Diseño para cambio y evolución](https://platzi.com/cursos/software-avanzado/dead-letter-queue-en-productor-consumido/)
- [Calidad de servicio y experiencia de usuario](https://platzi.com/cursos/software-avanzado/patron-comparing-consumers-para-procesam/)

## 🔗 Navegación
[⬅️ Video anterior](video-24.md) | [➡️ Video siguiente](video-26.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Diseño para cambio y evolución**
Este video introduce una de las ideas más importantes de la arquitectura moderna: un sistema no solo debe resolver el problema actual, sino prepararse para cambiar cuando cambien las necesidades del negocio o el contexto. El diseño arquitectónico debe pensar en la evolución como una variable esperada, no como una excepción. Por eso se enfatizan principios como la modularidad, la flexibilidad, la separación de responsabilidades y la protección de las capas críticas del sistema.

Cuando el software se diseña para el cambio, se vuelve más sostenible. En cambio, si se construye como una estructura rígida y demasiado acoplada, cualquier cambio pequeño termina convirtiéndose en una tarea riesgosa. La arquitectura entonces deja de ser una estructura estática y pasa a ser una base que permite crecer y adaptarse con menos fricción.

**Fuente 2: Calidad de servicio y experiencia de usuario**
La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna.

## Ideas que debes conservar
- La evolución es una característica normal del software, no un problema excepcional.
- Un buen diseño reduce el costo de cambiar.
- La modularidad permite aislar áreas del sistema y facilitar adaptaciones.
- La arquitectura debe proteger los puntos sensibles del negocio.
- La experiencia del usuario es una consecuencia del diseño arquitectónico.
- Calidad técnica y calidad de servicio no son conceptos separados.
- El tiempo de respuesta, la estabilidad y la claridad influyen en la percepción del sistema.
- Un servicio bueno no solo funciona; funciona con un nivel de calidad soportable.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **dead letter queue y consumidores en tiempo real**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La evolución es una característica normal del software, no un problema excepcional.
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
### ❓ ¿Qué partes de mi sistema son difíciles de cambiar?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la evolución es una característica normal del software, no un problema excepcional. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy diseñando para el futuro o solo para la versión actual?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un buen diseño reduce el costo de cambiar. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan buena es la experiencia de uso de mi sistema?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la modularidad permite aislar áreas del sistema y facilitar adaptaciones. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué factores técnicos afectan la percepción del usuario?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura debe proteger los puntos sensibles del negocio. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa dead letter queue y consumidores en tiempo real y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La evolución es una característica normal del software, no un problema excepcional. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La arquitectura más útil es la que acepta que el sistema cambiará. Cuando el diseño está preparado para la evolución, el software se vuelve más robusto, adaptable y sostenible.

La arquitectura debe diseñarse para entregar valor no solo dentro del equipo técnico, sino también en la experiencia real del usuario. La calidad de servicio aparece como indicador de que la solución responde bien a las necesidades del entorno.

## Preguntas para preparar la grabación
- ¿Qué partes de mi sistema son difíciles de cambiar?
- ¿Estoy diseñando para el futuro o solo para la versión actual?
- ¿Qué tan buena es la experiencia de uso de mi sistema?
- ¿Qué factores técnicos afectan la percepción del usuario?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
