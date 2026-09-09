# Video 01: Qué es la arquitectura y por qué importa

## Fuentes oficiales
- [Decisiones de arquitectura de software y sus consecuencias reales](https://platzi.com/cursos/fundamentos-arquitectura-software/decisiones-de-arquitectura-de-software-y/)
- [¿Por qué importa la arquitectura?](https://platzi.com/cursos/fundamentos-arquitectura-software/ia-en-arquitectura-herramienta-o-amenaza/)

## 🔗 Navegación
[➡️ Video siguiente](video-02.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: qué es la arquitectura y por qué importa. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Decisiones de arquitectura de software y sus consecuencias reales**
Este video abre con una historia impactante: la tragedia del Boeing 737 MAX. La idea principal es que un fallo grave no siempre es un simple bug aislado, sino una mala decisión arquitectónica. Cuando se prioriza velocidad o costo por encima de seguridad, las consecuencias pueden ser humanas y devastadoras.

A partir de ese ejemplo, el curso presenta la arquitectura de software como una decisión con impacto real. No se trata solo de elegir tecnologías o dibujar diagramas; se trata de diseñar sistemas que sean seguros, confiables, sostenibles y responsables. Cada decisión técnica puede influir en escalabilidad, seguridad, privacidad, accesibilidad y ética.

**Fuente 2: ¿Por qué importa la arquitectura?**
Este video responde una pregunta central: ¿por qué la arquitectura de software es importante si al final un sistema solo necesita funcionar? La respuesta es que un sistema no se mide solo por su funcionamiento inmediato, sino por su capacidad de crecer, proteger datos, ser usable y responder a nuevas necesidades sin romperse.

La arquitectura influye en varios aspectos del software: escalabilidad, seguridad, accesibilidad, privacidad y ética. Si un sistema está mal diseñado, puede funcionar al inicio y luego volverse difícil de mantener, poco seguro y muy costoso de evolucionar. La arquitectura es la diferencia entre un producto resistente y uno frágil.

## Ideas que debes conservar
- Las decisiones de software tienen consecuencias reales y humanas.
- No todo fallo es un bug aislado; a veces es un problema de diseño.
- La arquitectura afecta seguridad, escalabilidad, privacidad y confiabilidad.
- Priorizar costos o velocidad sin analizar el impacto puede ser peligroso.
- La arquitectura determina el futuro del sistema.
- Un sistema puede trabajar hoy y fallar mañana si no está bien diseñado.
- La escalabilidad implica crecer sin perder rendimiento ni estabilidad.
- La seguridad y la privacidad son decisiones de diseño, no de última hora.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: qué es la arquitectura y por qué importa. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **qué es la arquitectura y por qué importa**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: Las decisiones de software tienen consecuencias reales y humanas.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos qué es la arquitectura y por qué importa al flujo.
    2. **Actor prioritario de qué es la arquitectura y por qué importa:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en qué es la arquitectura y por qué importa:** escribe la condición que debe permanecer verdadera y relaciónala con las decisiones de software tienen consecuencias reales y humanas..
    4. **Punto de decisión para qué es la arquitectura y por qué importa:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de qué es la arquitectura y por qué importa:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **qué es la arquitectura y por qué importa**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa qué es la arquitectura y por qué importa y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: las decisiones de software tienen consecuencias reales y humanas.
3. Identifica el actor que recibe el impacto de qué es la arquitectura y por qué importa y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para qué es la arquitectura y por qué importa; compara sus costos y riesgos.
5. Elige una opción para qué es la arquitectura y por qué importa, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: qué es la arquitectura y por qué importa debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué decisiones técnicas están afectando la seguridad o confiabilidad de mis sistemas?

**Respuesta concreta:** La prioridad de qué es la arquitectura y por qué importa es proteger a el cliente, porque recibir un estado de entrega confiable. Aplicaría un control que impida violar la regla 'no mostrar una entrega como completada sin evidencia válida', limitaría el acceso a los datos necesarios y registraría los intentos rechazados. El costo es mayor complejidad de autorización y auditoría; lo comprobaría con pruebas de acceso permitido y denegado.

### ❓ ¿Estoy priorizando velocidad por encima de calidad y sostenibilidad?

**Respuesta concreta:** Para qué es la arquitectura y por qué importa, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué impacto tiene la arquitectura sobre la calidad general del sistema?

**Respuesta concreta:** La decisión sobre qué es la arquitectura y por qué importa afecta directamente a el repartidor: necesita recibir una instrucción vigente y consistente. Por eso protegería esta regla: evitar dos asignaciones activas para la misma entrega. En la arquitectura cambiaría la responsabilidad para que el componente que conoce esa regla la valide antes de comunicar el resultado. Acepto el costo de agregar una validación y una prueba porque el riesgo de afectar a el repartidor es mayor. Lo verificaría simulando el caso y comprobando el resultado observable para ese actor.

### ❓ ¿Qué parte de mi proyecto es frágil por falta de diseño?

**Respuesta concreta:** La parte frágil de qué es la arquitectura y por qué importa es la que permite que el equipo de soporte reciba un resultado incorrecto: reconstruir qué ocurrió durante un incidente. La corregiría colocando la regla 'tener eventos, errores y estados observables' en un límite explícito, en lugar de dejarla repartida entre la interfaz y la infraestructura. El costo será reorganizar el flujo y agregar pruebas; la evidencia será un cambio aislado que no rompa los demás módulos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa qué es la arquitectura y por qué importa y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de qué es la arquitectura y por qué importa:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para qué es la arquitectura y por qué importa:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de qué es la arquitectura y por qué importa:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: Las decisiones de software tienen consecuencias reales y humanas. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a qué es la arquitectura y por qué importa: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de qué es la arquitectura y por qué importa, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Qué es la arquitectura y por qué importa:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La arquitectura de software no es solo una disciplina técnica; es una responsabilidad. Cada decisión define no solo cómo funciona el sistema, sino también su impacto en personas, negocios y sociedad.

La arquitectura importa porque define la calidad, la sostenibilidad y la responsabilidad del sistema. Un diseño bien pensado protege el negocio, al equipo y a las personas que usan la solución.

## Preguntas para preparar la grabación
- ¿Qué decisiones técnicas están afectando la seguridad o confiabilidad de mis sistemas?
- ¿Estoy priorizando velocidad por encima de calidad y sostenibilidad?
- ¿Qué impacto tiene la arquitectura sobre la calidad general del sistema?
- ¿Qué parte de mi proyecto es frágil por falta de diseño?

## Evidencia para el repositorio
Guarda la explicación de qué es la arquitectura y por qué importa, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
