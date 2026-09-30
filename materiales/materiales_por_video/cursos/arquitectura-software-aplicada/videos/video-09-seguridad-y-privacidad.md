# Video 9: Estructura del archivo Architecture.md para proyectos de software

## Para estudiar por tu cuenta
Cuando alguien nuevo entra al proyecto, ¿cómo descubre qué hace el sistema, cómo ejecutarlo y por qué se tomaron sus decisiones principales? Un archivo `Architecture.md` puede reunir esa orientación en un lugar versionado junto al código.

No es una carpeta para copiar todo el código en texto ni un documento que se escribe una vez y se olvida. Su objetivo es ayudar a comprender el sistema y encontrar información vigente.

## 1. Qué debe responder
Un buen archivo responde preguntas prácticas:

- ¿Qué problema resuelve el sistema y quién lo usa?
- ¿Cuáles son sus partes principales y cómo se comunican?
- ¿Dónde viven las reglas importantes y los datos?
- ¿Cómo se ejecuta y prueba el proyecto?
- ¿Qué riesgos, límites y decisiones debería conocer quien hace un cambio?

Evita explicar cada clase: el código ya lo hace mejor. Documenta el propósito, los límites y las decisiones que no se pueden deducir fácilmente al leer un archivo.

## 2. Una estructura inicial
```markdown
# Architecture

## Propósito y alcance
## Actores y casos principales
## Vista general del sistema
## Componentes y responsabilidades
## Flujo principal de datos
## Seguridad y privacidad
## Operación y observabilidad
## Decisiones arquitectónicas
## Cómo ejecutar y probar
## Riesgos y límites conocidos
```

Adapta los títulos al proyecto. Una estructura útil permite encontrar respuestas; no tienes que conservar una sección vacía solo porque aparezca en una plantilla.

## 3. Ejemplo aplicado
Para la plataforma logística, la vista general podría indicar que la aplicación permite registrar pedidos y consultar entregas. Los componentes Pedidos e Inventario mantienen responsabilidades distintas y se comunican mediante una operación acordada.

El flujo de seguimiento puede decir:

1. El cliente solicita un pedido.
2. La API comprueba identidad y autorización.
3. Pedidos confirma que el cliente puede consultarlo.
4. Seguimiento devuelve el último estado conocido y su hora.

Si el proveedor de ubicación no responde, la pantalla no debe inventar el dato; debe explicar que la ubicación está temporalmente disponible solo hasta la última actualización.

## 4. Documenta las decisiones importantes aparte
Un **ADR** (registro de decisión arquitectónica) guarda una decisión significativa, sus alternativas y consecuencias. `Architecture.md` puede enlazar los ADR en vez de repetir cada análisis completo.

Ejemplo de registro breve:

```text
Decisión: la API consulta el estado del pedido al módulo responsable.
Alternativa descartada: copiar el estado en el perfil del cliente.
Razón: la copia puede quedar desactualizada.
Costo aceptado: la consulta depende de que el servicio responda.
Revisión: reconsiderar si el tiempo de respuesta supera el objetivo acordado.
```

## 5. Mantén el documento útil
- Actualiza la página cuando cambie el comportamiento, los límites o el modo de operar.
- Mantén diagramas pequeños y con flechas explicadas.
- Enlaza pruebas y decisiones que respalden afirmaciones importantes.
- No registres secretos ni datos personales reales.
- Si una sección describe algo que ya no existe, corrígela o elimínala.
- Incluye quién mantiene el documento o cómo proponer una corrección.

## 6. Actividad de autoestudio
Redacta una versión inicial de `Architecture.md` para el flujo de consulta de pedidos. Incluye propósito, actores, un diagrama sencillo descrito con texto, flujo normal, respuesta cuando falta la ubicación y una decisión con alternativa descartada.

### Respuesta modelo
El documento identifica al cliente y soporte, describe Pedidos como responsable de autorizar la consulta y Seguimiento como responsable de la última ubicación. Explica que la API no muestra una ubicación inventada si el proveedor falla y enlaza una prueba que verifica que el cliente no pueda consultar pedidos ajenos.

Una decisión puede preferir consultar la fuente responsable en lugar de duplicar el estado. Debe mencionar como costo que la consulta depende de esa fuente y qué métrica o señal haría revisar la solución.

## Comprueba lo que aprendiste
1. ¿Qué diferencia hay entre Architecture.md y un duplicado del código?
2. ¿Qué información conviene guardar en un ADR?
3. ¿Cuándo debes actualizar el archivo?

**Respuestas:** el archivo explica propósito, límites y decisiones, no copia cada clase; un ADR conserva contexto, alternativas, elección y consecuencias; se actualiza cuando esos elementos cambian o el documento deja de ser cierto.

## Conclusión
Architecture.md sirve como punto de entrada para entender, ejecutar y modificar un sistema con contexto. Su calidad depende de que responda preguntas reales y siga coincidiendo con el comportamiento actual, no de que sea largo.
