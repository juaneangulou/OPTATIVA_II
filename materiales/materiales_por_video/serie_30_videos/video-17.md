# Video 17: BDD y modelo C4

## Fuentes oficiales
- [IA, visión y liderazgo arquitectónico](https://platzi.com/cursos/software-avanzado/behavior-driven-development-para-alinear/)
- [Arquitectura y decisiones de diseño](https://platzi.com/cursos/software-avanzado/modelo-c4-para-diagramar-arquitecturas/)

## 🔗 Navegación
[⬅️ Video anterior](video-16.md) | [➡️ Video siguiente](video-18.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: IA, visión y liderazgo arquitectónico**
El video cierra la idea de que la arquitectura de software no es solo técnica, sino también estratégica y humana. Con el crecimiento de la inteligencia artificial, el arquitecto puede apoyarse en herramientas para analizar soluciones, detectar riesgos, simular escenarios y ampliar su capacidad de decisión. Sin embargo, la IA no sustituye la visión, el criterio y la responsabilidad de tomar decisiones de impacto real.

La arquitectura moderna exige un liderazgo que combine conocimiento técnico con pensamiento crítico, capacidad de comunicación y visión de negocio. El papel del arquitecto no es solo diseñar diagramas o elegir tecnologías, sino influir en el equipo, ayudar a los stakeholders a tomar mejores decisiones y construir sistemas que perduren. La IA puede acelerar análisis, pero la dirección y la intención siguen siendo humanas.

**Fuente 2: Arquitectura y decisiones de diseño**
En este video se enfoca en la idea de que la arquitectura no es solo un conjunto de componentes, sino una serie de decisiones que ordenan cómo funciona un sistema. Cada elección de diseño tiene consecuencias sobre mantenibilidad, complejidad, acoplamiento, tiempo de entrega y calidad general. El arquitecto no solo define una estructura; define un conjunto de reglas que guían el crecimiento del sistema.

La clave es entender que las decisiones arquitectónicas no se toman solo por gustos técnicos. Se basan en restricciones del negocio, capacidades del equipo, objetivos de evolución, riesgos y costos. El video muestra que una arquitectura sana toma decisiones con intención y no por accidente. Cuando el diseño está guiado por principios claros, el sistema avanza sin convertirse en una estructura caótica.

## Ideas que debes conservar
- La IA puede apoyar la evaluación de decisiones y la identificación de riesgos.
- La tecnología no reemplaza la visión del arquitecto; la potencia.
- El arquitecto debe conectar tecnología, negocio y operación.
- Un buen diseño depende de la capacidad de comunicar y guiar decisiones.
- La arquitectura es un conjunto de decisiones con impacto a largo plazo.
- Cada diseño tiene beneficios y costos asociados.
- El acoplamiento y la cohesión son criterios clave para evaluar un diseño.
- Un sistema bien diseñado reduce la fricción para cambiar y escalar.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **bdd y modelo c4**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La IA puede apoyar la evaluación de decisiones y la identificación de riesgos.
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
### ❓ ¿Cómo puedo usar IA para mejorar decisiones arquitectónicas sin perder criterio?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la ia puede apoyar la evaluación de decisiones y la identificación de riesgos. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan claro es mi liderazgo técnico dentro del equipo?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la tecnología no reemplaza la visión del arquitecto; la potencia. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué decisiones de diseño están guiando mi sistema hoy?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el arquitecto debe conectar tecnología, negocio y operación. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy tomando decisiones por intuición o por un criterio explícito?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un buen diseño depende de la capacidad de comunicar y guiar decisiones. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa bdd y modelo c4 y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La IA puede apoyar la evaluación de decisiones y la identificación de riesgos. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La arquitectura del futuro combina técnica, análisis, liderazgo y uso responsable de la IA. El arquitecto no es solo un especialista del sistema, sino un guía que transforma complejidad en claridad y ayuda a construir soluciones con sentido, dirección y valor de largo plazo.

Una buena arquitectura no aparece por azar; se construye deliberadamente. El valor de la arquitectura radica en la claridad con la que guía el crecimiento del sistema y en la capacidad de soportar decisiones futuras sin destruir la base actual.

## Preguntas para preparar la grabación
- ¿Cómo puedo usar IA para mejorar decisiones arquitectónicas sin perder criterio?
- ¿Qué tan claro es mi liderazgo técnico dentro del equipo?
- ¿Qué decisiones de diseño están guiando mi sistema hoy?
- ¿Estoy tomando decisiones por intuición o por un criterio explícito?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
