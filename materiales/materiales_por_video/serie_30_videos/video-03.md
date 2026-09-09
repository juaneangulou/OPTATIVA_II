# Video 03: Documentación y decisiones explícitas

## Fuentes oficiales
- [Platzi: Documentar decisiones y mantener claridad](https://platzi.com/cursos/fundamentos-arquitectura-software/malas-practicas-de-arquitectura-y-como-e/)
- [Platzi: Documentación y decisiones explícitas](https://platzi.com/cursos/software-avanzado/api-gateway-como-capa-de-abstraccion-en/)

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
Analiza cómo este tema afecta pedidos, inventario, ruteo, entregas, notificaciones, incidentes y operación. Elige un flujo concreto y explica qué responsabilidad, dependencia o atributo de calidad queda protegido.

## Actividad de construcción
1. Resume en tus palabras la idea central de cada fuente.
2. Combina esas ideas en un problema arquitectónico único.
3. Propón dos alternativas de solución.
4. Compara costo inicial, calidad, riesgo, operación y facilidad de cambio.
5. Elige una alternativa para el MVP y declara qué condición obligaría a revisarla.
6. Produce una evidencia: ADR, diagrama, contrato, código C#, prueba, métrica o plan de evolución.

## Respuesta orientadora
Una respuesta sólida conecta las fuentes con el caso. No basta decir que una tecnología es mejor: debes explicar qué problema resuelve, qué costo introduce, qué alternativa descartas y cómo comprobarás la decisión.

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
