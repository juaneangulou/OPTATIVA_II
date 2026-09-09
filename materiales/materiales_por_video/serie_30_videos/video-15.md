# Video 15: Método arquitectónico e inteligencia artificial

## Fuentes oficiales
- [Intuición vs método en arquitectura de software](https://platzi.com/cursos/software-avanzado/intuicion-vs-metodo-en-arquitectura-de-s/)
- [Del código funcional a la solución sostenible](https://platzi.com/cursos/software-avanzado/como-analizar-una-licitacion-real-con-ia/)

## 🔗 Navegación
[⬅️ Video anterior](video-14.md) | [➡️ Video siguiente](video-16.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Intuición vs método en arquitectura de software**
El video parte de una idea clave: muchas personas logran construir software funcional usando solo intuición, experiencia y prueba y error. Eso puede funcionar a corto plazo, pero cuando el sistema crece, aparecen problemas de mantenimiento, complejidad, escalabilidad y entendimiento del negocio. La arquitectura de software deja de ser solo “programar bien” y pasa a ser tomar decisiones con criterio, fundamento y visión de largo plazo.

La discusión central compara dos enfoques: por un lado, la intuición, que permite improvisar y avanzar rápido; por otro, el método, que ayuda a pensar en el sistema como un conjunto de decisiones estratégicas, no solo soluciones técnicas. El video deja claro que el arquitecto no debe depender de la suerte ni de la improvisación constante: debe analizar contexto, restricciones, objetivos de negocio y riesgos.

**Fuente 2: Del código funcional a la solución sostenible**
Este video enfatiza el cambio de mentalidad que ocurre cuando un desarrollador deja de pensar solo en entregar una funcionalidad rápida y empieza a pensar en la calidad del sistema completo. El objetivo ya no es solo que el código compile o que la funcionalidad funcione, sino que el sistema pueda evolucionar, soportar cambios y ser mantenido por más personas.

La diferencia entre un código funcional y una solución sostenible radica en la capacidad de estructurar el problema. Cuando se ignora la arquitectura, el sistema suele volverse difícil de entender, frágil ante cambios y costoso de mantener. El video presenta esta transición como un paso importante en la carrera profesional: de ser alguien que resuelve tareas puntuales a alguien que diseña soluciones con visión de producto y negocio.

## Ideas que debes conservar
- La intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento.
- Un software puede “servir” sin ser realmente bueno si no está construido para sostener cambios.
- La arquitectura de software implica decisiones sobre estructura, acoplamiento, escalabilidad, evolución y costos.
- El método permite reducir la incertidumbre y tomar decisiones con más base técnica y de negocio.
- Un sistema que funciona puede seguir siendo una mala solución si no está bien diseñado.
- La mantenibilidad es una dimensión clave del valor de una arquitectura.
- El diseño debe facilitar cambios futuros y no solo la entrega inicial.
- Los problemas reales aparecen cuando el software crece en complejidad, usuarios, reglas de negocio y dependencias.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **método arquitectónico e inteligencia artificial**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento.
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
### ❓ ¿Qué tan frecuente es resolver problemas solo con intuición en mi trabajo?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué problemas aparecen cuando el sistema crece sin una base metodológica?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con un software puede “servir” sin ser realmente bueno si no está construido para sostener cambios. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué tan sostenible es la solución que estoy construyendo hoy?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura de software implica decisiones sobre estructura, acoplamiento, escalabilidad, evolución y costos. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué parte del sistema es difícil de cambiar y por qué?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el método permite reducir la incertidumbre y tomar decisiones con más base técnica y de negocio. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa método arquitectónico e inteligencia artificial y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La diferencia entre intuición y método no es que uno sea bueno y el otro malo; más bien, la intuición es una base de partida y el método es lo que convierte una solución improvisada en una solución sostenible. La arquitectura de software exige pensar más allá del código y decidir con propósito.

El salto del “código que funciona” al “sistema que sobrevive” es lo que marca la diferencia entre un desarrollador ordinario y un arquitecto de software. El valor no está solo en resolver el problema del momento, sino en construir una base que permita seguir creciendo sin perder calidad.

## Preguntas para preparar la grabación
- ¿Qué tan frecuente es resolver problemas solo con intuición en mi trabajo?
- ¿Qué problemas aparecen cuando el sistema crece sin una base metodológica?
- ¿Qué tan sostenible es la solución que estoy construyendo hoy?
- ¿Qué parte del sistema es difícil de cambiar y por qué?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
