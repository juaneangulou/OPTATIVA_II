# Video 04: Responsabilidad, escalabilidad, seguridad y ética

## Fuentes oficiales
- [Arquitectura como responsabilidad humana](https://platzi.com/cursos/fundamentos-arquitectura-software/espacio-de-problema-vs-solucion-en-arqui/)
- [Escalabilidad, seguridad y ética](https://platzi.com/cursos/fundamentos-arquitectura-software/requisitos-funcionales-y-no-funcionales/)

## 🔗 Navegación
[⬅️ Video anterior](video-03.md) | [➡️ Video siguiente](video-05.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: responsabilidad, escalabilidad, seguridad y ética. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Arquitectura como responsabilidad humana**
Este video conecta la arquitectura con la responsabilidad y el impacto humano. Un gran poder en tecnología trae grandes consecuencias. Cuando se crea software crítico o de alto impacto, cada decisión tiene un peso mucho mayor. La arquitectura ya no es solo un problema técnico; es una responsabilidad con personas, usuarios y contextos reales.

La idea es que un sistema puede cambiar vidas, facilitar decisiones o poner en riesgo seguridad, salud o confianza. Por eso, el arquitecto debe ser consciente de que el software no es neutral ni inofensivo: tiene un impacto concreto en la sociedad.

**Fuente 2: Escalabilidad, seguridad y ética**
Este video reúne varios ejes esenciales de la arquitectura: escalabilidad, seguridad y ética. La idea es que un sistema no puede considerarse bueno solo porque escala bien o porque funciona bajo carga. Si no protege datos, no piensa en accesibilidad ni considera el impacto humano, termina generando problemas más allá de lo técnico.

La arquitectura debe equilibrar rendimiento con responsabilidad. Un diseño escalable y seguro es valioso, pero si ignora principios éticos o de inclusión, su impacto puede ser negativo. La arquitectura debe pensarse como un conjunto de decisiones integradas, no como políticas aisladas.

## Ideas que debes conservar
- El poder técnico conlleva responsabilidad.
- Los sistemas críticos requieren más rigor y criterio.
- La arquitectura afecta más que el rendimiento técnico.
- La responsabilidad humana es central en la toma de decisiones.
- Escalabilidad sin seguridad es una solución incompleta.
- La seguridad debe pensarse desde el diseño, no como parche final.
- La ética no es un tema ajeno; forma parte del valor del sistema.
- Un sistema debe ser útil y responsable al mismo tiempo.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: responsabilidad, escalabilidad, seguridad y ética. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **responsabilidad, escalabilidad, seguridad y ética**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: El poder técnico conlleva responsabilidad.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos responsabilidad, escalabilidad, seguridad y ética al flujo.
    2. **Actor prioritario de responsabilidad, escalabilidad, seguridad y ética:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en responsabilidad, escalabilidad, seguridad y ética:** escribe la condición que debe permanecer verdadera y relaciónala con el poder técnico conlleva responsabilidad..
    4. **Punto de decisión para responsabilidad, escalabilidad, seguridad y ética:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de responsabilidad, escalabilidad, seguridad y ética:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **responsabilidad, escalabilidad, seguridad y ética**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa responsabilidad, escalabilidad, seguridad y ética y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: el poder técnico conlleva responsabilidad.
3. Identifica el actor que recibe el impacto de responsabilidad, escalabilidad, seguridad y ética y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para responsabilidad, escalabilidad, seguridad y ética; compara sus costos y riesgos.
5. Elige una opción para responsabilidad, escalabilidad, seguridad y ética, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: responsabilidad, escalabilidad, seguridad y ética debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué tipo de impacto tiene el software que estoy diseñando?

**Respuesta concreta:** La decisión sobre responsabilidad, escalabilidad, seguridad y ética afecta directamente a el cliente: necesita recibir un estado de entrega confiable. Por eso protegería esta regla: no mostrar una entrega como completada sin evidencia válida. En la arquitectura cambiaría la responsabilidad para que el componente que conoce esa regla la valide antes de comunicar el resultado. Acepto el costo de agregar una validación y una prueba porque el riesgo de afectar a el cliente es mayor. Lo verificaría simulando el caso y comprobando el resultado observable para ese actor.

### ❓ ¿Estoy asumiendo una responsabilidad real con las personas que lo usan?

**Respuesta concreta:** La decisión sobre responsabilidad, escalabilidad, seguridad y ética afecta directamente a el operador logístico: necesita reasignar una ruta sin perder el historial del pedido. Por eso protegería esta regla: conservar trazabilidad de cada cambio. En la arquitectura cambiaría la responsabilidad para que el componente que conoce esa regla la valide antes de comunicar el resultado. Acepto el costo de agregar una validación y una prueba porque el riesgo de afectar a el operador logístico es mayor. Lo verificaría simulando el caso y comprobando el resultado observable para ese actor.

### ❓ ¿Mi sistema considera cuestiones de seguridad y ética desde el inicio?

**Respuesta concreta:** La prioridad de responsabilidad, escalabilidad, seguridad y ética es proteger a el repartidor, porque recibir una instrucción vigente y consistente. Aplicaría un control que impida violar la regla 'evitar dos asignaciones activas para la misma entrega', limitaría el acceso a los datos necesarios y registraría los intentos rechazados. El costo es mayor complejidad de autorización y auditoría; lo comprobaría con pruebas de acceso permitido y denegado.

### ❓ ¿Qué tan preparado está para crecer sin perder responsabilidad?

**Respuesta concreta:** La decisión sobre responsabilidad, escalabilidad, seguridad y ética afecta directamente a el equipo de soporte: necesita reconstruir qué ocurrió durante un incidente. Por eso protegería esta regla: tener eventos, errores y estados observables. En la arquitectura cambiaría la responsabilidad para que el componente que conoce esa regla la valide antes de comunicar el resultado. Acepto el costo de agregar una validación y una prueba porque el riesgo de afectar a el equipo de soporte es mayor. Lo verificaría simulando el caso y comprobando el resultado observable para ese actor.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa responsabilidad, escalabilidad, seguridad y ética y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de responsabilidad, escalabilidad, seguridad y ética:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para responsabilidad, escalabilidad, seguridad y ética:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de responsabilidad, escalabilidad, seguridad y ética:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El poder técnico conlleva responsabilidad. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a responsabilidad, escalabilidad, seguridad y ética: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de responsabilidad, escalabilidad, seguridad y ética, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Responsabilidad, escalabilidad, seguridad y ética:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La arquitectura de software tiene un lado humano muy claro. Un buen diseño no solo resuelve un problema; también protege a quienes lo usan y respeta la responsabilidad del creador.

La arquitectura sólida combina crecimiento, protección y responsabilidad. Un sistema digno de confianza debe pensar en la gente que lo usa, no solo en la eficiencia técnica.

## Preguntas para preparar la grabación
- ¿Qué tipo de impacto tiene el software que estoy diseñando?
- ¿Estoy asumiendo una responsabilidad real con las personas que lo usan?
- ¿Mi sistema considera cuestiones de seguridad y ética desde el inicio?
- ¿Qué tan preparado está para crecer sin perder responsabilidad?

## Evidencia para el repositorio
Guarda la explicación de responsabilidad, escalabilidad, seguridad y ética, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
