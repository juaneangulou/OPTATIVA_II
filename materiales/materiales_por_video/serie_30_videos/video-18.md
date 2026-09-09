# Video 18: Documentación viva y revisión con IA

## Fuentes oficiales
- [Escalabilidad y rendimiento](https://platzi.com/cursos/software-avanzado/quarto-como-sitio-de-documentacion-viva/)
- [Resiliencia y tolerancia a fallos](https://platzi.com/cursos/software-avanzado/agentes-de-ia-que-revisan-tu-codigo-en-g/)

## 🔗 Navegación
[⬅️ Video anterior](video-17.md) | [➡️ Video siguiente](video-19.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Escalabilidad y rendimiento**
El video aborda la diferencia entre un sistema que funciona con pocos usuarios y un sistema que mantiene calidad cuando la carga aumenta. La escalabilidad no es un concepto abstracto: se refiere a la capacidad del sistema para crecer sin perder rendimiento, estabilidad o calidad de servicio. También se menciona que no siempre la solución correcta es “hacerlo más grande”, sino diseñarlo para adaptarse a la demanda con una estrategia clara.

El rendimiento no depende solo de servidores o hardware; también influye la estructura del sistema, la forma en que se comunican componentes, el uso de caché, la distribución de responsabilidades y la calidad del diseño. Aquí aparece la idea de que la escalabilidad debe planearse desde el inicio, pero no siempre con una arquitectura más compleja que el problema justifique.

**Fuente 2: Resiliencia y tolerancia a fallos**
Este video introduce la idea de que ningún sistema es completamente estable ni inmune a fallos. Internet, servicios externos, bases de datos, dependencias y cambios de carga pueden afectar el funcionamiento normal. Por eso, una arquitectura robusta no se define por la ausencia de errores, sino por la capacidad de responder a ellos sin colapsar el servicio completo.

La resiliencia consiste en diseñar sistemas que puedan degradar con elegancia, recuperar automáticamente y continuar ofreciendo valor incluso cuando una parte falle. El video enfatiza que la tolerancia a fallos no es una característica extra; es un criterio de diseño funcional en sistemas reales. Esto incluye reintentos, timeouts, circuit breakers, replicas, backups y una estrategia clara de recuperación.

## Ideas que debes conservar
- Escalabilidad significa crecer sin romper el sistema.
- El rendimiento es un problema de diseño, no solo de infraestructura.
- Un sistema puede ser lento por mala arquitectura, no solo por falta de recursos.
- Aumentar capacidad no siempre es la mejor solución; a veces hay que mejorar diseño.
- Los fallos son inevitables en sistemas distribuidos y complejos.
- La resiliencia es la capacidad de recuperarse sin perder el servicio completo.
- La degradación controlada es mejor que un colapso total.
- La arquitectura debe anticipar errores en dependencias y en infraestructura.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **documentación viva y revisión con ia**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: Escalabilidad significa crecer sin romper el sistema.
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
### ❓ ¿Mi sistema está preparado para crecer en usuarios, tráfico o complejidad?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con escalabilidad significa crecer sin romper el sistema. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué cuellos de botella reales existen hoy?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el rendimiento es un problema de diseño, no solo de infraestructura. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué pasa si uno de mis servicios falla hoy?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un sistema puede ser lento por mala arquitectura, no solo por falta de recursos. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Mi sistema degrada de forma controlada o colapsa por completo?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con aumentar capacidad no siempre es la mejor solución; a veces hay que mejorar diseño. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa documentación viva y revisión con ia y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: Escalabilidad significa crecer sin romper el sistema. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La escalabilidad y el rendimiento son indicadores de madurez arquitectónica. Un sistema que puede crecer sin perder calidad no solo sirve mejor, sino que también reduce riesgos operativos y costos de corrección a largo plazo.

Un sistema no se vuelve bueno solo porque “anda en el momento”, sino porque puede resistir fallos y seguir entregando valor. La resiliencia es una de las habilidades más importantes de una arquitectura moderna.

## Preguntas para preparar la grabación
- ¿Mi sistema está preparado para crecer en usuarios, tráfico o complejidad?
- ¿Qué cuellos de botella reales existen hoy?
- ¿Qué pasa si uno de mis servicios falla hoy?
- ¿Mi sistema degrada de forma controlada o colapsa por completo?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
