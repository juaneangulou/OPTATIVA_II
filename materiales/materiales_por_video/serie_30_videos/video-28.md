# Video 28: Fitness Functions, OpenTelemetry y caos

## Fuentes oficiales
- [Decisiones bajo incertidumbre](https://platzi.com/cursos/software-avanzado/fitness-functions-para-medir-tu-arquitec/)
- [Arquitectura con impacto social y ético](https://platzi.com/cursos/software-avanzado/observabilidad-en-sistemas-con-opentelem/)

## 🔗 Navegación
[⬅️ Video anterior](video-27.md) | [➡️ Video siguiente](video-29.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: fitness functions, opentelemetry y caos. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

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
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: fitness functions, opentelemetry y caos. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **fitness functions, opentelemetry y caos**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La incertidumbre es parte normal de la arquitectura.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos fitness functions, opentelemetry y caos al flujo.
    2. **Actor prioritario de fitness functions, opentelemetry y caos:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en fitness functions, opentelemetry y caos:** escribe la condición que debe permanecer verdadera y relaciónala con la incertidumbre es parte normal de la arquitectura..
    4. **Punto de decisión para fitness functions, opentelemetry y caos:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de fitness functions, opentelemetry y caos:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **fitness functions, opentelemetry y caos**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa fitness functions, opentelemetry y caos y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la incertidumbre es parte normal de la arquitectura.
3. Identifica el actor que recibe el impacto de fitness functions, opentelemetry y caos y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para fitness functions, opentelemetry y caos; compara sus costos y riesgos.
5. Elige una opción para fitness functions, opentelemetry y caos, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: fitness functions, opentelemetry y caos debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Estoy tomando decisiones con datos suficientes o con suposiciones no verificadas?

**Respuesta concreta:** La prioridad de fitness functions, opentelemetry y caos es proteger a el cliente, porque recibir un estado de entrega confiable. Aplicaría un control que impida violar la regla 'no mostrar una entrega como completada sin evidencia válida', limitaría el acceso a los datos necesarios y registraría los intentos rechazados. El costo es mayor complejidad de autorización y auditoría; lo comprobaría con pruebas de acceso permitido y denegado.

### ❓ ¿Qué tan reversible es esta decisión si cambian los requerimientos?

**Respuesta concreta:** Para fitness functions, opentelemetry y caos, elegiría la alternativa que garantice que el operador logístico pueda reasignar una ruta sin perder el historial del pedido. La opción sencilla reduce el costo inicial, pero puede dejar débil la regla 'conservar trazabilidad de cada cambio'; la opción más estructurada cuesta más, pero facilita probarla y cambiarla. Para el MVP escogería la segunda solo si el riesgo es crítico y documentaría la condición de revisión.

### ❓ ¿Qué impacto social tiene mi sistema?

**Respuesta concreta:** La decisión sobre fitness functions, opentelemetry y caos afecta directamente a el repartidor: necesita recibir una instrucción vigente y consistente. Por eso protegería esta regla: evitar dos asignaciones activas para la misma entrega. En la arquitectura cambiaría la responsabilidad para que el componente que conoce esa regla la valide antes de comunicar el resultado. Acepto el costo de agregar una validación y una prueba porque el riesgo de afectar a el repartidor es mayor. Lo verificaría simulando el caso y comprobando el resultado observable para ese actor.

### ❓ ¿Estoy considerando accesibilidad, inclusión y responsabilidad en el diseño?

**Respuesta concreta:** La decisión sobre fitness functions, opentelemetry y caos afecta directamente a el equipo de soporte: necesita reconstruir qué ocurrió durante un incidente. Por eso protegería esta regla: tener eventos, errores y estados observables. En la arquitectura cambiaría la responsabilidad para que el componente que conoce esa regla la valide antes de comunicar el resultado. Acepto el costo de agregar una validación y una prueba porque el riesgo de afectar a el equipo de soporte es mayor. Lo verificaría simulando el caso y comprobando el resultado observable para ese actor.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa fitness functions, opentelemetry y caos y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de fitness functions, opentelemetry y caos:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para fitness functions, opentelemetry y caos:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de fitness functions, opentelemetry y caos:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La incertidumbre es parte normal de la arquitectura. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a fitness functions, opentelemetry y caos: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de fitness functions, opentelemetry y caos, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Fitness Functions, OpenTelemetry y caos:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
No hace falta conocer todo para tomar una buena decisión arquitectónica. Lo esencial es saber evaluar riesgos, mantener opciones abiertas y decidir con criterio en medio de la incertidumbre.

La arquitectura no es neutral. Sus decisiones tienen impacto social y ético. Un buen diseño considera el efecto real que tendrá en las personas y en la sociedad, no solo en la lógica de la aplicación.

## Preguntas para preparar la grabación
- ¿Estoy tomando decisiones con datos suficientes o con suposiciones no verificadas?
- ¿Qué tan reversible es esta decisión si cambian los requerimientos?
- ¿Qué impacto social tiene mi sistema?
- ¿Estoy considerando accesibilidad, inclusión y responsabilidad en el diseño?

## Evidencia para el repositorio
Guarda la explicación de fitness functions, opentelemetry y caos, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
