# Video 05: Principios de diseño, acoplamiento y cohesión

## Fuentes oficiales
- [Fundamentos de diseño y principios de arquitectura](https://platzi.com/cursos/fundamentos-arquitectura-software/costo-total-de-operacion-en-arquitectura/)
- [Acoplamiento, cohesión y calidad estructural](https://platzi.com/cursos/fundamentos-arquitectura-software/alineacion-de-arquitectura-de-software-c/)

## 🔗 Navegación
[⬅️ Video anterior](video-04.md) | [➡️ Video siguiente](video-06.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Fundamentos de diseño y principios de arquitectura**
Este video presenta los fundamentos del diseño arquitectónico: cómo una solución técnica debe estructurarse para ser clara, sostenible y adaptable. La arquitectura no se basa solo en elegir herramientas, sino en aplicar principios que guíen la organización del sistema. Entre esos principios están la modularidad, la separación de responsabilidades, la reutilización con sentido y la reducción del acoplamiento.

La idea central es que un sistema bien diseñado no solo funciona, sino que es más fácil de entender, mantener y evolucionar. Los principios de arquitectura sirven como brújula para tomar decisiones con criterio, especialmente cuando el proyecto crece en complejidad.

**Fuente 2: Acoplamiento, cohesión y calidad estructural**
Este video explica dos conceptos centrales en arquitectura: acoplamiento y cohesión. El acoplamiento mide cuán dependientes son componentes entre sí; la cohesión mide qué tan relacionadas están las responsabilidades dentro de un mismo módulo o servicio. La mejor arquitectura busca baja dependencia entre partes y alta claridad dentro de cada parte.

Cuando el acoplamiento es alto, hacer cambios implica romper varias piezas del sistema. Cuando la cohesión es baja, una entidad se vuelve confusa y difícil de mantener. La calidad estructural del software se mejora cuando se reducen dependencias innecesarias y se ordenan bien las responsabilidades.

## Ideas que debes conservar
- El diseño arquitectónico no es un detalle opcional.
- Los principios ayudan a sostener decisiones de largo plazo.
- La modularidad mejora la claridad y la evolución del sistema.
- La separación de responsabilidades reduce complejidad.
- El acoplamiento alto genera fragilidad.
- La cohesión alta mejora claridad y mantenibilidad.
- La arquitectura debe disminuir dependencias innecesarias.
- Un sistema con responsabilidades bien definidas es más fácil de evolucionar.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **principios de diseño, acoplamiento y cohesión**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: El diseño arquitectónico no es un detalle opcional.
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
### ❓ ¿Qué parte de mi sistema tiene responsabilidades mezcladas?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el diseño arquitectónico no es un detalle opcional. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué principio arquitectónico me está faltando aplicar?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con los principios ayudan a sostener decisiones de largo plazo. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan acoplado está mi sistema en este momento?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la modularidad mejora la claridad y la evolución del sistema. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué modulos tienen demasiadas responsabilidades mezcladas?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la separación de responsabilidades reduce complejidad. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa principios de diseño, acoplamiento y cohesión y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El diseño arquitectónico no es un detalle opcional. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Los principios de diseño son la base para crear sistemas más claros, más sostenibles y más fáciles de hacer crecer con seguridad.

La calidad estructural de un sistema está marcada por la forma en que se separan sus responsabilidades y cómo se gestionan sus dependencias.

## Preguntas para preparar la grabación
- ¿Qué parte de mi sistema tiene responsabilidades mezcladas?
- ¿Qué principio arquitectónico me está faltando aplicar?
- ¿Qué tan acoplado está mi sistema en este momento?
- ¿Qué modulos tienen demasiadas responsabilidades mezcladas?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
