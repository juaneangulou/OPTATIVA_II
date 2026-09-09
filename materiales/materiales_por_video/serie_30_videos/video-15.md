# Video 15: Método arquitectónico e inteligencia artificial

## Fuentes oficiales
- [Intuición vs método en arquitectura de software](https://platzi.com/cursos/software-avanzado/intuicion-vs-metodo-en-arquitectura-de-s/)
- [Del código funcional a la solución sostenible](https://platzi.com/cursos/software-avanzado/como-analizar-una-licitacion-real-con-ia/)

## 🔗 Navegación
[⬅️ Video anterior](video-14.md) | [➡️ Video siguiente](video-16.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: método arquitectónico e inteligencia artificial. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

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
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: método arquitectónico e inteligencia artificial. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **método arquitectónico e inteligencia artificial**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos método arquitectónico e inteligencia artificial al flujo.
    2. **Actor prioritario de método arquitectónico e inteligencia artificial:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en método arquitectónico e inteligencia artificial:** escribe la condición que debe permanecer verdadera y relaciónala con la intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento..
    4. **Punto de decisión para método arquitectónico e inteligencia artificial:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de método arquitectónico e inteligencia artificial:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **método arquitectónico e inteligencia artificial**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa método arquitectónico e inteligencia artificial y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento.
3. Identifica el actor que recibe el impacto de método arquitectónico e inteligencia artificial y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para método arquitectónico e inteligencia artificial; compara sus costos y riesgos.
5. Elige una opción para método arquitectónico e inteligencia artificial, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: método arquitectónico e inteligencia artificial debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué tan frecuente es resolver problemas solo con intuición en mi trabajo?

**Respuesta concreta:** Para método arquitectónico e inteligencia artificial, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué problemas aparecen cuando el sistema crece sin una base metodológica?

**Respuesta concreta:** Para método arquitectónico e inteligencia artificial, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué tan sostenible es la solución que estoy construyendo hoy?

**Respuesta concreta:** Para método arquitectónico e inteligencia artificial, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué parte del sistema es difícil de cambiar y por qué?

**Respuesta concreta:** Para método arquitectónico e inteligencia artificial, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa método arquitectónico e inteligencia artificial y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de método arquitectónico e inteligencia artificial:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para método arquitectónico e inteligencia artificial:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de método arquitectónico e inteligencia artificial:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a método arquitectónico e inteligencia artificial: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de método arquitectónico e inteligencia artificial, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Método arquitectónico e inteligencia artificial:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La diferencia entre intuición y método no es que uno sea bueno y el otro malo; más bien, la intuición es una base de partida y el método es lo que convierte una solución improvisada en una solución sostenible. La arquitectura de software exige pensar más allá del código y decidir con propósito.

El salto del “código que funciona” al “sistema que sobrevive” es lo que marca la diferencia entre un desarrollador ordinario y un arquitecto de software. El valor no está solo en resolver el problema del momento, sino en construir una base que permita seguir creciendo sin perder calidad.

## Preguntas para preparar la grabación
- ¿Qué tan frecuente es resolver problemas solo con intuición en mi trabajo?
- ¿Qué problemas aparecen cuando el sistema crece sin una base metodológica?
- ¿Qué tan sostenible es la solución que estoy construyendo hoy?
- ¿Qué parte del sistema es difícil de cambiar y por qué?

## Evidencia para el repositorio
Guarda la explicación de método arquitectónico e inteligencia artificial, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
