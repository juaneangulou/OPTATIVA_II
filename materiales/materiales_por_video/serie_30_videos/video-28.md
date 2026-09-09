# Video 28: Fitness Functions, OpenTelemetry y caos

## Fuentes oficiales
- [Decisiones bajo incertidumbre](https://platzi.com/cursos/software-avanzado/fitness-functions-para-medir-tu-arquitec/)
- [Arquitectura con impacto social y ético](https://platzi.com/cursos/software-avanzado/observabilidad-en-sistemas-con-opentelem/)

## 🔗 Navegación
[⬅️ Video anterior](video-27.md) | [➡️ Video siguiente](video-29.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Decisiones bajo incertidumbre**
La arquitectura de software ocurre en un contexto de incertidumbre. No siempre se conocen todos los requerimientos, ni todas las tecnologías, ni el comportamiento real del sistema en producción. El arquitecto debe tomar decisiones con información incompleta, y por eso necesita comprender riesgos, hipótesis y probabilidades. El video enseña que la arquitectura no es un acto de perfección, sino de decisión inteligente bajo condiciones imperfectas.

Cuando se enfrenta la incertidumbre, la mejor práctica no es esperar a tener toda la información; es diseñar de forma que el sistema pueda cambiar, aprender y soportar errores de suposición. En otras palabras, la habilidad de decidir bajo incertidumbre es una competencia clave del arquitecto.

**Fuente 2: Arquitectura con impacto social y ético**
El video introduce un enfoque humanista y ético en la arquitectura de software. Un sistema no solo afecta procesos técnicos y económicos, sino también personas, comunidades y valores. Por eso, la arquitectura debe considerar implicaciones sociales, de privacidad, accesibilidad, inclusión y responsabilidad. Un sistema que funciona técnicamente puede causar daño si no se diseña con criterio ético.

Esto invita a pensar que el arquitecto no actúa solo como técnico, sino también como responsable del impacto de sus decisiones. Cuando se diseña software para personas, su contexto social y sus necesidades humanas deben integrarse en la solución. Este enfoque aporta más valor y reduce consecuencias negativas en el largo plazo.

## Ideas que debes conservar
- La incertidumbre es parte normal de la arquitectura.
- No siempre se dispone de toda la información antes de diseñar.
- Las decisiones deben evaluarse por riesgo y reversibilidad.
- Diseñar para cambiar reduce el impacto de la incertidumbre.
- La tecnología tiene impacto real sobre personas, comunidades y decisiones humanas.
- La ética no es ajena a la arquitectura; es parte de la responsabilidad del diseño.
- La privacidad, la accesibilidad y la inclusión deben considerarse en el sistema.
- Un sistema puede tener éxito técnico y aun así fallar socialmente.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **fitness functions, opentelemetry y caos**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La incertidumbre es parte normal de la arquitectura.
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
### ❓ ¿Estoy tomando decisiones con datos suficientes o con suposiciones no verificadas?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la incertidumbre es parte normal de la arquitectura. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan reversible es esta decisión si cambian los requerimientos?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con no siempre se dispone de toda la información antes de diseñar. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué impacto social tiene mi sistema?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con las decisiones deben evaluarse por riesgo y reversibilidad. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy considerando accesibilidad, inclusión y responsabilidad en el diseño?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con diseñar para cambiar reduce el impacto de la incertidumbre. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa fitness functions, opentelemetry y caos y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La incertidumbre es parte normal de la arquitectura. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
No hace falta conocer todo para tomar una buena decisión arquitectónica. Lo esencial es saber evaluar riesgos, mantener opciones abiertas y decidir con criterio en medio de la incertidumbre.

La arquitectura no es neutral. Sus decisiones tienen impacto social y ético. Un buen diseño considera el efecto real que tendrá en las personas y en la sociedad, no solo en la lógica de la aplicación.

## Preguntas para preparar la grabación
- ¿Estoy tomando decisiones con datos suficientes o con suposiciones no verificadas?
- ¿Qué tan reversible es esta decisión si cambian los requerimientos?
- ¿Qué impacto social tiene mi sistema?
- ¿Estoy considerando accesibilidad, inclusión y responsabilidad en el diseño?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
