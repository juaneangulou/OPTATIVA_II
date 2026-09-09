# Video 13: Liderazgo, negociación e impacto social

## Fuentes oficiales
- [Comunicación, liderazgo y negociación técnica](https://platzi.com/cursos/fundamentos-arquitectura-software/evolucion-del-software-personal-hacia-el/)
- [Arquitectura con impacto social y valor real](https://platzi.com/cursos/fundamentos-arquitectura-software/preguntas-clave-que-todo-arquitecto-de-s/)

## 🔗 Navegación
[⬅️ Video anterior](video-12.md) | [➡️ Video siguiente](video-14.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Comunicación, liderazgo y negociación técnica**
Este video destaca que una gran parte del trabajo del arquitecto no está en el código, sino en la conversación. Cuando se diseña un sistema, se necesita comunicar decisiones, negociar prioridades y hacer que diferentes actores comprendan por qué se elige una solución y no otra. La arquitectura se fortalece cuando hay claridad, diálogo y liderazgo.

El arquitecto debe ser capaz de escuchar, explicar trade-offs, escuchar preocupaciones y alinear decisiones entre negocio, equipo y usuarios. La negociación técnica no es improvisación; es la capacidad de construir consenso con criterio y equilibrio.

**Fuente 2: Arquitectura con impacto social y valor real**
Este video cierra la dimensión ética y social de la arquitectura. Un sistema no solo debe cumplir con requisitos técnicos; también debe generar valor real para las personas, mejorar procesos y no causar daño. La arquitectura industrial y de software termina teniendo un impacto humano y social, incluso cuando no se nota a simple vista.

La idea es que el valor de una solución no se mide solo por su complejidad o performance, sino por el beneficio real que produce, la confianza que genera y la responsabilidad con quienes la usan. La arquitectura más valiosa es la que crea impacto positivo sin ignorar el contexto social.

## Ideas que debes conservar
- La comunicación es una habilidad arquitectónica central.
- Las decisiones de arquitectura implican balancear intereses distintos.
- El liderazgo técnico ayuda a alinear equipo y visión.
- La negociación permite tomar decisiones sin improvisación.
- La tecnología tiene impacto sobre personas y comunidades.
- El valor real no se mide solo por complejidad o volumen.
- La arquitectura debe generar utilidad y confianza.
- La responsabilidad técnica incluye consecuencias sociales.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **liderazgo, negociación e impacto social**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La comunicación es una habilidad arquitectónica central.
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
### ❓ ¿Estoy logrando explicar bien mis decisiones técnicas?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la comunicación es una habilidad arquitectónica central. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué conflictos de prioridad están bloqueando el proyecto?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con las decisiones de arquitectura implican balancear intereses distintos. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué impacto social tiene mi solución?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el liderazgo técnico ayuda a alinear equipo y visión. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Está generando valor real o solo cumpliendo un requisito técnico?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la negociación permite tomar decisiones sin improvisación. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa liderazgo, negociación e impacto social y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La comunicación es una habilidad arquitectónica central. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La arquitectura no solo se diseña; también se comunica y se negocia. Un buen arquitecto no solo toma decisiones, sino que logra que el equipo y la organización las entienda y las apoye.

Una buena arquitectura no solo es eficiente técnicamente; también genera valor real para la sociedad y para quienes interactúan con el sistema.

## Preguntas para preparar la grabación
- ¿Estoy logrando explicar bien mis decisiones técnicas?
- ¿Qué conflictos de prioridad están bloqueando el proyecto?
- ¿Qué impacto social tiene mi solución?
- ¿Está generando valor real o solo cumpliendo un requisito técnico?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
