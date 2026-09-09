# Video 03: Documentación y decisiones explícitas

## Fuentes oficiales
- [Documentar decisiones y mantener claridad](https://platzi.com/cursos/fundamentos-arquitectura-software/malas-practicas-de-arquitectura-y-como-e/)
- [Documentación y decisiones explícitas](https://platzi.com/cursos/software-avanzado/api-gateway-como-capa-de-abstraccion-en/)

## 🔗 Navegación
[⬅️ Video anterior](video-02.md) | [➡️ Video siguiente](video-04.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Documentar decisiones y mantener claridad**
Este video profundiza en la importancia de dejar explícitas las decisiones de arquitectura. Muchas veces el problema no es solo que el sistema funcione, sino que se vuelva difícil de entender por quien lo revisa después. Cuando las decisiones no se documentan, cada persona asume una interpretación distinta y eso termina generando inconsistencias.

La idea es documentar el contexto, la intención, los riesgos, las restricciones y las alternativas descartadas. Esa práctica no solo ayuda al mantenimiento, sino también a que el equipo pueda evaluar si una solución sigue siendo apropiada con el tiempo. La documentación debe ser clara, viva y útil.

**Fuente 2: Documentación y decisiones explícitas**
La documentación de arquitectura no es un lujo ni una actividad burocrática superficial; es una herramienta clave para que el sistema pueda entenderse, evolucionar y sostenerse en el tiempo. Cuando las decisiones se documentan de forma clara, el equipo puede reducir ambigüedad, evitar errores de interpretación y mantener continuidad incluso con cambios de personal. El video hace hincapié en que la arquitectura debe dejarse escrita, no solo en la cabeza de unos pocos.

Esto incluye explicar trade-offs, restricciones, decisiones tomadas y alternativas descartadas. Cuando un proyecto se basa en decisiones implícitas, cada integrante empieza a hacer su propia “lectura” del sistema. La documentación ayuda a que el diseño sea compartido, revisado y mejorado con base en evidencia.

## Ideas que debes conservar
- Las decisiones de arquitectura deben dejarse escritas.
- La documentación ayuda a preservar conocimiento y continuidad.
- Debe aclarar intención, restricciones, riesgos y alternativas.
- La arquitectura viva reduce la ambigüedad y mejora la evolución.
- La documentación reduce ambigüedad y ayuda a la continuidad del proyecto.
- Las decisiones arquitectónicas deben ser explícitas, no solo inferidas.
- Documentar no significa escribir mucho por escrito; significa registrar lo relevante.
- Se deben reflejar restricciones, decisiones, alternativas y razones.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **documentación y decisiones explícitas**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: Las decisiones de arquitectura deben dejarse escritas.
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
### ❓ ¿Estoy escribiendo solo el resultado o también el razonamiento detrás de la solución?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con las decisiones de arquitectura deben dejarse escritas. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué decisiones clave del proyecto podrían perderse si se cambia de equipo?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la documentación ayuda a preservar conocimiento y continuidad. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué decisiones importantes de mi proyecto están aún en la cabeza de una sola persona?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con debe aclarar intención, restricciones, riesgos y alternativas. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy documentando solo la solución final o también el porqué?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura viva reduce la ambigüedad y mejora la evolución. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa documentación y decisiones explícitas y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: Las decisiones de arquitectura deben dejarse escritas. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La documentación no es burocracia: es una forma de mantener la claridad del sistema y evitar que el conocimiento se pierda. La arquitectura se vuelve más sólida cuando está documentada y compartida.

La documentación arquitectónica es una forma de preservar el conocimiento y de evitar que el sistema se vuelva incomprensible con el tiempo. Un buen diseño debe ser enseñable, comprensible y defendible.

## Preguntas para preparar la grabación
- ¿Estoy escribiendo solo el resultado o también el razonamiento detrás de la solución?
- ¿Qué decisiones clave del proyecto podrían perderse si se cambia de equipo?
- ¿Qué decisiones importantes de mi proyecto están aún en la cabeza de una sola persona?
- ¿Estoy documentando solo la solución final o también el porqué?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
