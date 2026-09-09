# Video 10: Testing, DevOps y entrega continua

## Fuentes oficiales
- [Testing y validación de arquitectura](https://platzi.com/cursos/fundamentos-arquitectura-software/paradigmas-y-principios-solid-explicados/)
- [DevOps y automatización de entrega](https://platzi.com/cursos/fundamentos-arquitectura-software/que-hace-limpia-a-una-arquitectura-de-so/)

## 🔗 Navegación
[⬅️ Video anterior](video-09.md) | [➡️ Video siguiente](video-11.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Testing y validación de arquitectura**
En este video se explica que la arquitectura no debe validarse solo con la ejecución del sistema en un entorno feliz. También debe evaluarse mediante pruebas, simulaciones, revisión de calidad y validación de dependencias. La validación arquitectónica permite corroborar que el sistema cumple con expectativas de rendimiento, confiabilidad, seguridad y facilidad de evolución.

Cuando se hace testing de arquitectura, se busca detectar problemas estructurales antes de que creen deuda técnica o incidentes en producción. La calidad de una solución no siempre se ve al principio, por eso se requiere una evaluación más profunda que la simple funcionalidad básica.

**Fuente 2: DevOps y automatización de entrega**
Este video conecta arquitectura con entrega continua. La forma en que se construye, prueba, despliega y opera una aplicación influye directamente en su calidad. Si el proceso de entrega es manual y poco repetible, el sistema será más frágil incluso si su diseño inicial es bueno. Por eso DevOps y automatización son parte interesante de la arquitectura moderna.

La entrega automatizada permite reducir errores humanos, aumentar velocidad, mejorar reusabilidad y hacer más segura la evolución del sistema. El objetivo no es solo desplegar más rápido, sino hacerlo de manera controlada y confiable.

## Ideas que debes conservar
- La arquitectura debe validarse con criterios más allá del “funciona”.
- Las pruebas ayudan a detectar riesgos estructurales.
- La validación reduce la probabilidad de fallos costosos.
- La calidad del diseño se confirma con observación y pruebas.
- La entrega continua es parte de la arquitectura.
- La automatización reduce errores y acelera cambios seguros.
- Las pruebas y despliegues deben ser repetibles y controlados.
- La operación y el desarrollo deben alinearse en un mismo flujo.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **testing, devops y entrega continua**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La arquitectura debe validarse con criterios más allá del “funciona”.
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
### ❓ ¿Qué tan bien validamos la estructura de mi sistema?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura debe validarse con criterios más allá del “funciona”. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan fácil es detectar un problema arquitectónico antes de producción?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con las pruebas ayudan a detectar riesgos estructurales. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan automatizado está mi proceso de entrega?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la validación reduce la probabilidad de fallos costosos. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué riesgos se reducen o aumentan con el flujo actual?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la calidad del diseño se confirma con observación y pruebas. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa testing, devops y entrega continua y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La arquitectura debe validarse con criterios más allá del “funciona”. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Un sistema técnico no queda validado solo por tener casos de éxito; necesita pruebas y evaluación que confirmen que su estructura soporta el presente y el crecimiento futuro.

La automatización de entrega no es solo una práctica operativa, sino una decisión arquitectónica que mejora confiabilidad, velocidad y sostenibilidad.

## Preguntas para preparar la grabación
- ¿Qué tan bien validamos la estructura de mi sistema?
- ¿Qué tan fácil es detectar un problema arquitectónico antes de producción?
- ¿Qué tan automatizado está mi proceso de entrega?
- ¿Qué riesgos se reducen o aumentan con el flujo actual?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
