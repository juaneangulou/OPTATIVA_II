# Video 19: Architecture.md y Domain Driven Design

## Fuentes de este video
- [Estructura del archivo Architecture.md para proyectos de software](https://platzi.com/cursos/software-avanzado/estructura-del-archivo-architecture-md-p/)
- [Domain Driven Design para arquitectura limpia](https://platzi.com/cursos/software-avanzado/domain-driven-design-para-arquitectura-l/)

## Navegación
[⬅️ Video anterior: documentación viva y revisión con IA](video-18.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: pre-mortem y pruebas de arquitectura](video-20.md)

## Para estudiar por tu cuenta
Domain Driven Design (DDD) ayuda a convertir el lenguaje del negocio en reglas y modelos implementables. `Architecture.md` deja por escrito cómo esas decisiones se reflejan en el código y cómo otra persona puede orientarse en el proyecto. A diferencia del video 6, que delimitó contextos a nivel conceptual, aquí producirás un documento y una verificación que puedan acompañar un repositorio real.

En esta clase combinarás ambos enfoques para documentar el proceso de pedidos y entregas de la plataforma logística. El objetivo es que una persona nueva pueda entender el dominio antes de modificar el código.

## 1. DDD comienza con el lenguaje del negocio
El **dominio** es el área de actividad que el sistema ayuda a resolver. En logística incluye pedidos, inventario, asignaciones y entregas.

Un **lenguaje ubicuo** es un conjunto de términos cuyo significado se acuerda entre quienes conocen el negocio y quienes construyen el sistema. Por ejemplo, “pedido confirmado” y “entrega completada” no son necesariamente lo mismo: una compra puede confirmarse antes de que el paquete llegue al cliente.

Si el equipo usa la misma palabra para estados diferentes, el código puede tomar una decisión válida para un área y equivocada para otra. DDD invita a aclarar esos significados y las reglas asociadas.

## 2. Entidades y reglas del modelo
Una **entidad** conserva su identidad mientras sus datos cambian. El pedido 245 sigue siendo el pedido 245 aunque su estado pase de “Pendiente” a “En camino”.

Una **regla del dominio** es una condición que el negocio exige cumplir. Ejemplo: “Una entrega no queda completada sin evidencia de recepción”. La regla debe poder explicarse sin mencionar una pantalla o una marca de base de datos.

Los **límites de contexto** separan zonas donde los términos y reglas tienen significados propios. En Compras, “pedido confirmado” puede indicar que la compra se aceptó; en Entregas, “reparto asignado” indica que un repartidor aceptó el trabajo.

## 3. ¿Qué es Architecture.md?
`Architecture.md` es un documento de entrada al proyecto. No reemplaza el código ni copia todas sus clases. Resume lo que un lector necesita para entender y modificar el sistema sin adivinar:

- qué problema resuelve y quién lo usa;
- qué partes principales existen y qué responsabilidad tiene cada una;
- qué recorrido sigue un pedido;
- qué decisiones importantes se tomaron y por qué;
- cómo ejecutar y probar el sistema;
- qué riesgos y límites siguen pendientes.

Una decisión detallada puede escribirse en un **ADR** (registro de decisión arquitectónica) y enlazarse desde `Architecture.md`. Un ADR explica contexto, alternativas, elección y consecuencias.

## 4. Del dominio al documento
Usa este flujo para documentar:

1. Anota los términos del negocio y confirma qué significan.
2. Agrupa reglas relacionadas, por ejemplo Compra y Entrega.
3. Identifica qué información pertenece a cada área.
4. Dibuja las partes y las relaciones necesarias.
5. Registra decisiones que afecten límites, datos, seguridad u operación.
6. Incluye cómo comprobar las reglas importantes.
7. Actualiza la documentación cuando cambie el comportamiento real.

El diagrama y el documento deben contar la misma arquitectura que el código. Si difieren, el lector no sabe cuál es la fuente confiable.

## 5. Ejemplo de sección Architecture.md
```markdown
## Dominio y términos
- Pedido confirmado: compra aceptada por el proceso comercial.
- Entrega asignada: existe un repartidor responsable del traslado.
- Entrega completada: el cliente recibió el paquete y existe evidencia.

## Responsabilidades
- Pedidos conserva la compra, sus líneas y su estado comercial.
- Entregas conserva asignación, seguimiento y evidencia de recepción.

## Regla importante
Una entrega no se marca como completada sin evidencia de recepción.

## Verificación
Una prueba intenta completar la entrega sin evidencia y confirma que el sistema lo rechaza.
```

Este ejemplo es breve a propósito: registra significados y una regla comprobable. El documento final puede enlazar otros diagramas, ADR y guías más detalladas.

## 6. Cómo comprobar que el documento sirve
Imagina que una persona nueva debe corregir el estado de una entrega. Antes de abrir el código, debería poder responder:

- ¿Qué diferencia hay entre pedido confirmado y entrega completada?
- ¿Qué componente mantiene la evidencia de recepción?
- ¿Qué prueba comprueba la regla?
- ¿Dónde se describe el recorrido del dato?

Si no puede encontrar una respuesta, añade o corrige la sección adecuada. Si el documento repite muchas páginas del código, acórtalo y enlaza la fuente más específica.

## 7. Actividad de autoestudio
Documenta en tu `Architecture.md` el flujo “pedido confirmado → entrega asignada → entrega completada”.

1. Define los tres estados sin usar frases ambiguas.
2. Indica qué módulo es responsable de cada información.
3. Describe qué dato pasa de Pedidos a Entregas.
4. Escribe una regla que proteja al cliente y al repartidor.
5. Añade una prueba que pueda comprobarla.
6. Registra una decisión importante y una alternativa que descartaste.

### Respuesta modelo
“Pedido confirmado” indica que la compra se aceptó; “entrega asignada” indica que existe un repartidor; “entrega completada” exige recepción confirmada.

Pedidos conserva la compra y comparte el identificador, la dirección y los productos necesarios. Entregas registra al repartidor, el recorrido y la evidencia de entrega. Una prueba intenta marcar como completado un pedido sin evidencia y comprueba que el estado no cambie.

La documentación también puede explicar qué decisión se tomó sobre guardar estados dentro de una aplicación o dividirlos en módulos. Debe incluir la razón y el costo, no solo el nombre de la opción.

## Comprueba lo que aprendiste
1. ¿Cómo ayuda DDD a escribir `Architecture.md`?
2. ¿Qué diferencia hay entre la responsabilidad de Pedidos y la de Entregas?
3. ¿Qué debe contener un ADR?
4. ¿Cuándo está desactualizado un documento de arquitectura?

### Respuestas
1. Aclara términos, reglas y límites que el documento debe explicar.
2. Pedidos conserva la compra y su estado comercial; Entregas conserva el traslado y su evidencia.
3. El problema, las alternativas, la decisión y sus consecuencias.
4. Cuando ya no describe el comportamiento, los límites o las decisiones vigentes del sistema.

## Conclusión
DDD ayuda a modelar el negocio y `Architecture.md` ayuda a compartir ese modelo y las decisiones del sistema. Juntos reducen ambigüedades cuando las personas cambian y facilitan que el proyecto pueda mantenerse sin depender de memoria oral.