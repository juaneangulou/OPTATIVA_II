# Video 01: Qué es la arquitectura y por qué importa

## Fuentes oficiales
- [Decisiones de arquitectura de software y sus consecuencias reales](https://platzi.com/cursos/fundamentos-arquitectura-software/decisiones-de-arquitectura-de-software-y/)
- [¿Por qué importa la arquitectura?](https://platzi.com/cursos/fundamentos-arquitectura-software/ia-en-arquitectura-herramienta-o-amenaza/)

## 🔗 Navegación
[➡️ Video siguiente](video-02.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Decisiones de arquitectura de software y sus consecuencias reales**
Este video abre con una historia impactante: la tragedia del Boeing 737 MAX. La idea principal es que un fallo grave no siempre es un simple bug aislado, sino una mala decisión arquitectónica. Cuando se prioriza velocidad o costo por encima de seguridad, las consecuencias pueden ser humanas y devastadoras.

A partir de ese ejemplo, el curso presenta la arquitectura de software como una decisión con impacto real. No se trata solo de elegir tecnologías o dibujar diagramas; se trata de diseñar sistemas que sean seguros, confiables, sostenibles y responsables. Cada decisión técnica puede influir en escalabilidad, seguridad, privacidad, accesibilidad y ética.

**Fuente 2: ¿Por qué importa la arquitectura?**
Este video responde una pregunta central: ¿por qué la arquitectura de software es importante si al final un sistema solo necesita funcionar? La respuesta es que un sistema no se mide solo por su funcionamiento inmediato, sino por su capacidad de crecer, proteger datos, ser usable y responder a nuevas necesidades sin romperse.

La arquitectura influye en varios aspectos del software: escalabilidad, seguridad, accesibilidad, privacidad y ética. Si un sistema está mal diseñado, puede funcionar al inicio y luego volverse difícil de mantener, poco seguro y muy costoso de evolucionar. La arquitectura es la diferencia entre un producto resistente y uno frágil.

## Ideas que debes conservar
- Las decisiones de software tienen consecuencias reales y humanas.
- No todo fallo es un bug aislado; a veces es un problema de diseño.
- La arquitectura afecta seguridad, escalabilidad, privacidad y confiabilidad.
- Priorizar costos o velocidad sin analizar el impacto puede ser peligroso.
- La arquitectura determina el futuro del sistema.
- Un sistema puede trabajar hoy y fallar mañana si no está bien diseñado.
- La escalabilidad implica crecer sin perder rendimiento ni estabilidad.
- La seguridad y la privacidad son decisiones de diseño, no de última hora.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **qué es la arquitectura y por qué importa**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: Las decisiones de software tienen consecuencias reales y humanas.
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
### ❓ ¿Qué decisiones técnicas están afectando la seguridad o confiabilidad de mis sistemas?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con las decisiones de software tienen consecuencias reales y humanas. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy priorizando velocidad por encima de calidad y sostenibilidad?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con no todo fallo es un bug aislado; a veces es un problema de diseño. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué impacto tiene la arquitectura sobre la calidad general del sistema?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura afecta seguridad, escalabilidad, privacidad y confiabilidad. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué parte de mi proyecto es frágil por falta de diseño?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con priorizar costos o velocidad sin analizar el impacto puede ser peligroso. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa qué es la arquitectura y por qué importa y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: Las decisiones de software tienen consecuencias reales y humanas. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La arquitectura de software no es solo una disciplina técnica; es una responsabilidad. Cada decisión define no solo cómo funciona el sistema, sino también su impacto en personas, negocios y sociedad.

La arquitectura importa porque define la calidad, la sostenibilidad y la responsabilidad del sistema. Un diseño bien pensado protege el negocio, al equipo y a las personas que usan la solución.

## Preguntas para preparar la grabación
- ¿Qué decisiones técnicas están afectando la seguridad o confiabilidad de mis sistemas?
- ¿Estoy priorizando velocidad por encima de calidad y sostenibilidad?
- ¿Qué impacto tiene la arquitectura sobre la calidad general del sistema?
- ¿Qué parte de mi proyecto es frágil por falta de diseño?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
