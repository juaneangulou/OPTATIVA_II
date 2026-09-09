# Video 24: Mensajes, eventos y productor-consumidor

## Fuentes oficiales
- [Madurez arquitectónica y evolución continua](https://platzi.com/cursos/software-avanzado/mensajes-vs-eventos-en-microservicios/)
- [Cierre del curso y próximos pasos](https://platzi.com/cursos/software-avanzado/patron-productor-consumidor-vs-fan-in-y/)

## 🔗 Navegación
[⬅️ Video anterior](video-23.md) | [➡️ Video siguiente](video-25.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: mensajes, eventos y productor-consumidor. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Madurez arquitectónica y evolución continua**
Este video reflexiona sobre la madurez de una arquitectura: no se trata de llegar a una solución “perfecta” de una vez, sino de ir desarrollando capacidades para manejar complejidad, cambios y crecimiento sin perder control. La madurez arquitectónica se observa cuando un equipo es capaz de aprender del sistema, ajustar decisiones, evolucionar sus procesos y mantener calidad aunque el negocio cambie.

La evolución continua es parte esencial de la arquitectura moderna. Un sistema no debe quedar congelado en una decisión inicial; debe poder adaptarse a nuevos requerimientos, nuevas tecnologías y nuevos riesgos. Esa capacidad de evolución depende tanto del diseño como del hábito de revisión, observación y mejora constante.

**Fuente 2: Cierre del curso y próximos pasos**
El curso culmina con una visión integradora: la arquitectura de software es una disciplina de pensamiento, decisión y responsabilidad. No se trata de seguir patrones por moda ni de aplicar herramientas por entusiasmo, sino de construir sistemas que resuelvan problemas reales, respeten el contexto y puedan evolucionar con el tiempo. La arquitectura exige equilibrio entre rigor técnico, sensibilidad de negocio y capacidad de liderazgo.

El cierre invita a la reflexión sobre el camino profesional: el arquitecto no nace solo con conocimiento, sino con la habilidad de combinar criterio, experiencia, observación y mejora constante. La invitación final es continuar aprendiendo, enfrentando problemas reales, cuestionando decisiones y construyendo software con propósito. La diferencia entre un buen desarrollador y un buen arquitecto no está en la cantidad de herramientas que conoce, sino en cómo piensa y decide ante la complejidad.

## Ideas que debes conservar
- La madurez arquitectónica se construye con el tiempo.
- Un sistema no se vuelve mejor solo por agregar más tecnología.
- La evolución continua permite mantener claridad a medida que crece la complejidad.
- El equipo debe aprender a revisar decisiones y rediseñar cuando sea necesario.
- La arquitectura es una disciplina de decisión y pensamiento, no solo de herramientas.
- La práctica real es donde se desarrollan las habilidades arquitectónicas.
- Los mejores arquitectos combinan técnica, estrategia y criterio humano.
- La evolución profesional se construye con experiencia, análisis y reflexión.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: mensajes, eventos y productor-consumidor. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **mensajes, eventos y productor-consumidor**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La madurez arquitectónica se construye con el tiempo.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos mensajes, eventos y productor-consumidor al flujo.
    2. **Actor prioritario de mensajes, eventos y productor-consumidor:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en mensajes, eventos y productor-consumidor:** escribe la condición que debe permanecer verdadera y relaciónala con la madurez arquitectónica se construye con el tiempo..
    4. **Punto de decisión para mensajes, eventos y productor-consumidor:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de mensajes, eventos y productor-consumidor:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **mensajes, eventos y productor-consumidor**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa mensajes, eventos y productor-consumidor y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la madurez arquitectónica se construye con el tiempo.
3. Identifica el actor que recibe el impacto de mensajes, eventos y productor-consumidor y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para mensajes, eventos y productor-consumidor; compara sus costos y riesgos.
5. Elige una opción para mensajes, eventos y productor-consumidor, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: mensajes, eventos y productor-consumidor debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Mi arquitectura está creciendo con el sistema o volviéndose rígida?

**Respuesta concreta:** Para mensajes, eventos y productor-consumidor, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy revisando mis decisiones de forma periódica?

**Respuesta concreta:** Para mensajes, eventos y productor-consumidor, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué aspectos del curso más me impactaron como profesional?

**Respuesta concreta:** Para mensajes, eventos y productor-consumidor, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué decisiones arquitectónicas quiero aplicar en mis proyectos reales?

**Respuesta concreta:** Para mensajes, eventos y productor-consumidor, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa mensajes, eventos y productor-consumidor y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de mensajes, eventos y productor-consumidor:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para mensajes, eventos y productor-consumidor:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de mensajes, eventos y productor-consumidor:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La madurez arquitectónica se construye con el tiempo. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a mensajes, eventos y productor-consumidor: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de mensajes, eventos y productor-consumidor, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Mensajes, eventos y productor-consumidor:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La madurez arquitectónica no es un estado final; es un proceso de aprendizaje, ajuste y mejora constante. La arquitectura más sólida es la que puede evolucionar sin perder coherencia ni calidad.

El curso se cierra con una idea clave: el software de calidad no se construye solo con código, sino con visión, método, criterio y responsabilidad. Los próximos pasos consisten en aplicar estas ideas en proyectos reales, seguir aprendiendo y asumir la arquitectura como una práctica de crecimiento profesional y de impacto real.

## Preguntas para preparar la grabación
- ¿Mi arquitectura está creciendo con el sistema o volviéndose rígida?
- ¿Estoy revisando mis decisiones de forma periódica?
- ¿Qué aspectos del curso más me impactaron como profesional?
- ¿Qué decisiones arquitectónicas quiero aplicar en mis proyectos reales?

## Evidencia para el repositorio
Guarda la explicación de mensajes, eventos y productor-consumidor, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
