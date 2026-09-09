# Video 05: Principios de diseño, acoplamiento y cohesión

## Fuentes oficiales
- [Fundamentos de diseño y principios de arquitectura](https://platzi.com/cursos/fundamentos-arquitectura-software/costo-total-de-operacion-en-arquitectura/)
- [Acoplamiento, cohesión y calidad estructural](https://platzi.com/cursos/fundamentos-arquitectura-software/alineacion-de-arquitectura-de-software-c/)

## 🔗 Navegación
[⬅️ Video anterior](video-04.md) | [➡️ Video siguiente](video-06.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: principios de diseño, acoplamiento y cohesión. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Fundamentos de diseño y principios de arquitectura**
Este video presenta los fundamentos del diseño arquitectónico: cómo una solución técnica debe estructurarse para ser clara, sostenible y adaptable. La arquitectura no se basa solo en elegir herramientas, sino en aplicar principios que guíen la organización del sistema. Entre esos principios están la modularidad, la separación de responsabilidades, la reutilización con sentido y la reducción del acoplamiento.

La idea central es que un sistema bien diseñado no solo funciona, sino que es más fácil de entender, mantener y evolucionar. Los principios de arquitectura sirven como brújula para tomar decisiones con criterio, especialmente cuando el proyecto crece en complejidad.

**Fuente 2: Acoplamiento, cohesión y calidad estructural**
Este video explica dos conceptos centrales en arquitectura: acoplamiento y cohesión. El acoplamiento mide cuán dependientes son componentes entre sí; la cohesión mide qué tan relacionadas están las responsabilidades dentro de un mismo módulo o servicio. La mejor arquitectura busca baja dependencia entre partes y alta claridad dentro de cada parte.

Cuando el acoplamiento es alto, hacer cambios implica romper varias piezas del sistema. Cuando la cohesión es baja, una entidad se vuelve confusa y difícil de mantener. La calidad estructural del software se mejora cuando se reducen dependencias innecesarias y se ordenan bien las responsabilidades.

## Ideas que debes conservar
- El diseño arquitectónico no es un detalle opcional.
- Los principios ayudan a sostener decisiones de largo plazo.
- La modularidad mejora la claridad y la evolución del sistema.
- La separación de responsabilidades reduce complejidad.
- El acoplamiento alto genera fragilidad.
- La cohesión alta mejora claridad y mantenibilidad.
- La arquitectura debe disminuir dependencias innecesarias.
- Un sistema con responsabilidades bien definidas es más fácil de evolucionar.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: principios de diseño, acoplamiento y cohesión. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **principios de diseño, acoplamiento y cohesión**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: El diseño arquitectónico no es un detalle opcional.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos principios de diseño, acoplamiento y cohesión al flujo.
    2. **Actor prioritario de principios de diseño, acoplamiento y cohesión:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en principios de diseño, acoplamiento y cohesión:** escribe la condición que debe permanecer verdadera y relaciónala con el diseño arquitectónico no es un detalle opcional..
    4. **Punto de decisión para principios de diseño, acoplamiento y cohesión:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de principios de diseño, acoplamiento y cohesión:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **principios de diseño, acoplamiento y cohesión**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa principios de diseño, acoplamiento y cohesión y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: el diseño arquitectónico no es un detalle opcional.
3. Identifica el actor que recibe el impacto de principios de diseño, acoplamiento y cohesión y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para principios de diseño, acoplamiento y cohesión; compara sus costos y riesgos.
5. Elige una opción para principios de diseño, acoplamiento y cohesión, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: principios de diseño, acoplamiento y cohesión debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué parte de mi sistema tiene responsabilidades mezcladas?

**Respuesta concreta:** La decisión sobre principios de diseño, acoplamiento y cohesión afecta directamente a el cliente: necesita recibir un estado de entrega confiable. Por eso protegería esta regla: no mostrar una entrega como completada sin evidencia válida. En la arquitectura cambiaría la responsabilidad para que el componente que conoce esa regla la valide antes de comunicar el resultado. Acepto el costo de agregar una validación y una prueba porque el riesgo de afectar a el cliente es mayor. Lo verificaría simulando el caso y comprobando el resultado observable para ese actor.

### ❓ ¿Qué principio arquitectónico me está faltando aplicar?

**Respuesta concreta:** Para principios de diseño, acoplamiento y cohesión, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué tan acoplado está mi sistema en este momento?

**Respuesta concreta:** Para principios de diseño, acoplamiento y cohesión, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué modulos tienen demasiadas responsabilidades mezcladas?

**Respuesta concreta:** La decisión sobre principios de diseño, acoplamiento y cohesión afecta directamente a el equipo de soporte: necesita reconstruir qué ocurrió durante un incidente. Por eso protegería esta regla: tener eventos, errores y estados observables. En la arquitectura cambiaría la responsabilidad para que el componente que conoce esa regla la valide antes de comunicar el resultado. Acepto el costo de agregar una validación y una prueba porque el riesgo de afectar a el equipo de soporte es mayor. Lo verificaría simulando el caso y comprobando el resultado observable para ese actor.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa principios de diseño, acoplamiento y cohesión y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de principios de diseño, acoplamiento y cohesión:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para principios de diseño, acoplamiento y cohesión:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de principios de diseño, acoplamiento y cohesión:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El diseño arquitectónico no es un detalle opcional. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a principios de diseño, acoplamiento y cohesión: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de principios de diseño, acoplamiento y cohesión, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Principios de diseño, acoplamiento y cohesión:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Los principios de diseño son la base para crear sistemas más claros, más sostenibles y más fáciles de hacer crecer con seguridad.

La calidad estructural de un sistema está marcada por la forma en que se separan sus responsabilidades y cómo se gestionan sus dependencias.

## Preguntas para preparar la grabación
- ¿Qué parte de mi sistema tiene responsabilidades mezcladas?
- ¿Qué principio arquitectónico me está faltando aplicar?
- ¿Qué tan acoplado está mi sistema en este momento?
- ¿Qué modulos tienen demasiadas responsabilidades mezcladas?

## Evidencia para el repositorio
Guarda la explicación de principios de diseño, acoplamiento y cohesión, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
