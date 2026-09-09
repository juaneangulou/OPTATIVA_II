# Video 08: APIs, contratos e infraestructura

## Fuentes oficiales
- [Platzi: APIs y contratos de integración](https://platzi.com/cursos/fundamentos-arquitectura-software/que-son-las-arquitecturas-monoliticas-y/)
- [Platzi: Infraestructura, despliegue y entorno de ejecución](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitecturas-orientadas-a-servicios-con/)

## 🔗 Navegación
[⬅️ Video anterior](video-07.md) | [➡️ Video siguiente](video-09.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: APIs y contratos de integración**
Este video centra la atención en la forma en que los sistemas se integran entre sí. Las APIs son contratos entre partes: representan cómo se comunica un servicio con otro y cómo se comparte información. Cuando esos contratos son claros, la integración es más productiva y menos frágil. Cuando no lo son, se vuelven fuentes de errores, incompatibilidades y cambios difíciles de gestionar.

El diseño de APIs incluye no solo endpoints o rutas, sino también formato, validaciones, errores, versionado y políticas de evolución. Una buena API debe ser clara, estable y fácil de consumirse por el equipo o por sistemas externos.

**Fuente 2: Infraestructura, despliegue y entorno de ejecución**
Este video muestra que la arquitectura incluye también la infraestructura que ejecuta el sistema. Un diseño puede ser excelente en código, pero si el entorno de ejecución es caótico, manual o poco reproducible, la aplicación no será sostenible. La arquitectura debe considerar tanto la capa lógica como la capa operativa que la pone en marcha.

La infraestructura debe ser fácil de reproducir, detectar fallos y trasladar entre entornos. Los despliegues automatizados y los procesos de entorno ayudan a reducir errores humanos y mejorar la confianza del sistema en producción.

## Ideas que debes conservar
- Las APIs son acuerdos de comunicación entre sistemas.
- Los contratos deben ser claros y bien documentados.
- El versionado reduce riesgos de romper dependencias.
- Una mala API genera fragilidad en la integración.
- La infraestructura es parte del diseño arquitectónico.
- El entorno debe ser reproducible y consistente.
- Un despliegue manual aumenta riesgos y errores.
- La infraestructura debe soportar diferentes contextos: desarrollo, prueba y producción.

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
El diseño de APIs es una parte central de la arquitectura. Un buen contrato de integración mejora la evolución del sistema y reduce errores de colaboración entre equipos.

La arquitectura no termina en el código: incluye cómo se ejecuta, se despliega y se mantiene. Un sistema bien diseñado también necesita un entorno bien pensado.

## Preguntas para preparar la grabación
- ¿Mis interfaces están bien definidas y documentadas?
- ¿Qué pasa si un cliente usa una versión anterior?
- ¿Mi entorno es reproducible y consistente?
- ¿Qué tan fácil es desplegar una versión nueva sin riesgos innecesarios?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
