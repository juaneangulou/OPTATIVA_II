# Video 28: Fitness Functions, OpenTelemetry y caos

## Fuentes oficiales
- [Platzi: Decisiones bajo incertidumbre](https://platzi.com/cursos/software-avanzado/fitness-functions-para-medir-tu-arquitec/)
- [Platzi: Arquitectura con impacto social y ético](https://platzi.com/cursos/software-avanzado/observabilidad-en-sistemas-con-opentelem/)

## 🔗 Navegación
[⬅️ Video anterior](video-27.md) | [➡️ Video siguiente](video-29.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

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
No hace falta conocer todo para tomar una buena decisión arquitectónica. Lo esencial es saber evaluar riesgos, mantener opciones abiertas y decidir con criterio en medio de la incertidumbre.

La arquitectura no es neutral. Sus decisiones tienen impacto social y ético. Un buen diseño considera el efecto real que tendrá en las personas y en la sociedad, no solo en la lógica de la aplicación.

## Preguntas para preparar la grabación
- ¿Estoy tomando decisiones con datos suficientes o con suposiciones no verificadas?
- ¿Qué tan reversible es esta decisión si cambian los requerimientos?
- ¿Qué impacto social tiene mi sistema?
- ¿Estoy considerando accesibilidad, inclusión y responsabilidad en el diseño?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
