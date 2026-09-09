# Video 27: Máquinas de estado y seguridad de aplicaciones

## Fuentes oficiales
- [Riesgos, costos y sostenibilidad financiera](https://platzi.com/cursos/software-avanzado/maquinas-de-estado-finito-en-el-front-en/)
- [Arquitectura para equipos distribuidos](https://platzi.com/cursos/software-avanzado/tecnicas-sast-dast-y-pen-testing-para-se/)

## 🔗 Navegación
[⬅️ Video anterior](video-26.md) | [➡️ Video siguiente](video-28.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Riesgos, costos y sostenibilidad financiera**
La arquitectura de software también tiene implicaciones económicas. Un sistema no solo debe funcionar desde el punto de vista técnico; también debe ser viable desde el punto de vista financiero, operativo y de mantenimiento. Este video muestra que las decisiones de arquitectura implican costos directos e indirectos: infraestructura, equipos, tiempo, soporte, seguridad, correcciones y capacidad de adaptación.

La sostenibilidad financiera no es solo una preocupación del negocio; también afecta la arquitectura. Si el sistema es demasiado costoso de operar o difícil de mantener, su valor real disminuye. Por ello, el arquitecto debe ser capaz de medir el costo total de una solución y no solo el costo inicial de desarrollo.

**Fuente 2: Arquitectura para equipos distribuidos**
Cuando los equipos trabajan de forma distribuida, la arquitectura necesita ser más clara y más explícita. La comunicación, la coordinación y la documentación se vuelven críticos, porque el sistema no puede depender exclusivamente de la familiaridad entre personas. Un diseño bien estructurado permite que diferentes miembros del equipo trabajen en paralelo sin generar fricción o conflictos por responsabilidades ambiguas.

El video enfatiza que una arquitectura fuerte es también una herramienta de colaboración. Si el sistema está bien dividido, la documentación es clara y las interfaces están bien definidas, el equipo puede avanzar con menos fricción. Esto reduce errores de integración, soporta trabajo distribuido y mejora el flujo global del proyecto.

## Ideas que debes conservar
- La arquitectura tiene un costo real en infraestructura, operación y mantenimiento.
- Los riesgos técnicos y financieros deben evaluarse en conjunto.
- Un diseño barato al principio puede volverse muy costoso después.
- La sostenibilidad financiera depende del equilibrio entre valor y costo.
- La arquitectura facilita o complica el trabajo en equipo.
- Equipos distribuidos necesitan más claridad en interfaces y responsabilidades.
- La documentación y la comunicación son parte de la arquitectura efectiva.
- El diseño debe facilitar coordinación, no solo funcionalidad.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **máquinas de estado y seguridad de aplicaciones**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La arquitectura tiene un costo real en infraestructura, operación y mantenimiento.
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
### ❓ ¿Qué costo total real tiene mi solución?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura tiene un costo real en infraestructura, operación y mantenimiento. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy optimizando solo el desarrollo inicial o la sostenibilidad del sistema?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con los riesgos técnicos y financieros deben evaluarse en conjunto. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan claro está el sistema para otros miembros del equipo?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un diseño barato al principio puede volverse muy costoso después. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Hay dependencias ocultas que bloquean el trabajo colaborativo?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la sostenibilidad financiera depende del equilibrio entre valor y costo. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa máquinas de estado y seguridad de aplicaciones y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La arquitectura tiene un costo real en infraestructura, operación y mantenimiento. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
El software no es solo una decisión técnica: es también una decisión financiera y estratégica. Una arquitectura sostenible es la que crea valor sin generar costos ocultos que la vuelvan inviable con el tiempo.

La arquitectura no solo sirve para resolver un problema técnico; también permite que múltiples personas trabajen de manera coordinada y sostenida. En un equipo distribuido, la claridad arquitectónica es una ventaja de productividad y calidad.

## Preguntas para preparar la grabación
- ¿Qué costo total real tiene mi solución?
- ¿Estoy optimizando solo el desarrollo inicial o la sostenibilidad del sistema?
- ¿Qué tan claro está el sistema para otros miembros del equipo?
- ¿Hay dependencias ocultas que bloquean el trabajo colaborativo?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
