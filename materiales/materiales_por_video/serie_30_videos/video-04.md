# Video 04: Responsabilidad, escalabilidad, seguridad y ética

## Fuentes oficiales
- [Arquitectura como responsabilidad humana](https://platzi.com/cursos/fundamentos-arquitectura-software/espacio-de-problema-vs-solucion-en-arqui/)
- [Escalabilidad, seguridad y ética](https://platzi.com/cursos/fundamentos-arquitectura-software/requisitos-funcionales-y-no-funcionales/)

## 🔗 Navegación
[⬅️ Video anterior](video-03.md) | [➡️ Video siguiente](video-05.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Arquitectura como responsabilidad humana**
Este video conecta la arquitectura con la responsabilidad y el impacto humano. Un gran poder en tecnología trae grandes consecuencias. Cuando se crea software crítico o de alto impacto, cada decisión tiene un peso mucho mayor. La arquitectura ya no es solo un problema técnico; es una responsabilidad con personas, usuarios y contextos reales.

La idea es que un sistema puede cambiar vidas, facilitar decisiones o poner en riesgo seguridad, salud o confianza. Por eso, el arquitecto debe ser consciente de que el software no es neutral ni inofensivo: tiene un impacto concreto en la sociedad.

**Fuente 2: Escalabilidad, seguridad y ética**
Este video reúne varios ejes esenciales de la arquitectura: escalabilidad, seguridad y ética. La idea es que un sistema no puede considerarse bueno solo porque escala bien o porque funciona bajo carga. Si no protege datos, no piensa en accesibilidad ni considera el impacto humano, termina generando problemas más allá de lo técnico.

La arquitectura debe equilibrar rendimiento con responsabilidad. Un diseño escalable y seguro es valioso, pero si ignora principios éticos o de inclusión, su impacto puede ser negativo. La arquitectura debe pensarse como un conjunto de decisiones integradas, no como políticas aisladas.

## Ideas que debes conservar
- El poder técnico conlleva responsabilidad.
- Los sistemas críticos requieren más rigor y criterio.
- La arquitectura afecta más que el rendimiento técnico.
- La responsabilidad humana es central en la toma de decisiones.
- Escalabilidad sin seguridad es una solución incompleta.
- La seguridad debe pensarse desde el diseño, no como parche final.
- La ética no es un tema ajeno; forma parte del valor del sistema.
- Un sistema debe ser útil y responsable al mismo tiempo.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **responsabilidad, escalabilidad, seguridad y ética**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: El poder técnico conlleva responsabilidad.
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
### ❓ ¿Qué tipo de impacto tiene el software que estoy diseñando?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el poder técnico conlleva responsabilidad. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy asumiendo una responsabilidad real con las personas que lo usan?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con los sistemas críticos requieren más rigor y criterio. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Mi sistema considera cuestiones de seguridad y ética desde el inicio?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura afecta más que el rendimiento técnico. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan preparado está para crecer sin perder responsabilidad?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la responsabilidad humana es central en la toma de decisiones. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa responsabilidad, escalabilidad, seguridad y ética y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El poder técnico conlleva responsabilidad. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La arquitectura de software tiene un lado humano muy claro. Un buen diseño no solo resuelve un problema; también protege a quienes lo usan y respeta la responsabilidad del creador.

La arquitectura sólida combina crecimiento, protección y responsabilidad. Un sistema digno de confianza debe pensar en la gente que lo usa, no solo en la eficiencia técnica.

## Preguntas para preparar la grabación
- ¿Qué tipo de impacto tiene el software que estoy diseñando?
- ¿Estoy asumiendo una responsabilidad real con las personas que lo usan?
- ¿Mi sistema considera cuestiones de seguridad y ética desde el inicio?
- ¿Qué tan preparado está para crecer sin perder responsabilidad?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
