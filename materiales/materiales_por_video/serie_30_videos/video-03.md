# Video 03: Documentación y decisiones explícitas

## Fuentes oficiales
- [Documentar decisiones y mantener claridad](https://platzi.com/cursos/fundamentos-arquitectura-software/malas-practicas-de-arquitectura-y-como-e/)
- [Documentación y decisiones explícitas](https://platzi.com/cursos/software-avanzado/api-gateway-como-capa-de-abstraccion-en/)

## 🔗 Navegación
[⬅️ Video anterior](video-02.md) | [➡️ Video siguiente](video-04.md)

## Propósito
En esta clase vas a aprender a convertir una decisión que hoy está en la cabeza de una persona en un registro que el equipo pueda leer, discutir y revisar dentro de seis meses. No vamos a hablar de documentación como burocracia: vamos a usarla para evitar que el proyecto dependa de la memoria de quien escribió el código.

## Qué explican las fuentes
La primera fuente plantea que una decisión arquitectónica debe dejar claro el contexto, la intención, las restricciones, los riesgos y las alternativas descartadas. La segunda amplía la idea: documentar no es llenar páginas, sino registrar lo que permite a otra persona entender por qué el sistema se construyó de esa manera.

Las dos fuentes convergen en una regla: una decisión no está realmente tomada hasta que el equipo puede responder qué problema resolvía, qué opción eligió, qué costo aceptó y cuándo debería revisarla.

## Escena de la plataforma logística
El lunes, la arquitecta que definió la integración con el proveedor de mapas sale de vacaciones. El miércoles, el proveedor empieza a responder lento. El operador logístico informa que las rutas llegan tarde; soporte ve errores, pero nadie sabe por qué existe un timeout de dos segundos ni qué alternativa se descartó.

Aquí el actor principal no es el repartidor: es **el equipo de soporte y el nuevo desarrollador**. Ambos necesitan reconstruir una decisión sin depender de la memoria de la arquitecta. La regla que debemos proteger es: **toda integración crítica debe tener un registro visible de propósito, límite, timeout, alternativa y responsable**.

## La decisión que vamos a documentar
La plataforma debe consultar un proveedor externo de mapas para estimar rutas. Tenemos dos opciones:

### Opción A: llamar al proveedor desde el módulo de pedidos
Es rápida de implementar y parece suficiente para el MVP. El riesgo es que pedidos conozca detalles del proveedor, que el timeout esté repartido en varios lugares y que una caída del servicio bloquee la creación de pedidos.

### Opción B: crear un adaptador de rutas con un contrato explícito
El módulo de pedidos solicita una estimación mediante una interfaz. El adaptador contiene la URL, credenciales, timeout, reintentos y transformación de errores. El costo es crear una capa adicional, pero el proveedor puede cambiar sin contaminar la regla de negocio.

Para este caso elegiría la opción B. No porque “las capas sean mejores”, sino porque el proveedor es externo, puede fallar y soporte necesita saber dónde observar y cambiar el comportamiento.

## El ADR que construiríamos juntos
Un ADR puede ser breve. Para esta decisión, escribe lo siguiente:

```markdown
# ADR-001: Aislar la estimación de rutas detrás de un adaptador

## Contexto
El proveedor de mapas puede responder lento o no estar disponible.

## Decisión
El caso de uso de crear pedido dependerá de IRouteEstimator.
La infraestructura implementará ese contrato con el proveedor externo.

## Alternativas descartadas
Llamar la API de mapas directamente desde el módulo de pedidos.

## Consecuencias
Ganamos aislamiento y pruebas más simples. Aceptamos mantener un adaptador.

## Revisión
Revisar si el timeout supera 2 segundos en más del 5% de solicitudes.
```

## Preguntas y respuestas
### ¿Estoy escribiendo solo el resultado o también el razonamiento detrás de la solución?

No basta escribir “usamos un adaptador”. Debes registrar que el proveedor externo puede fallar, que pedidos no debe conocer su protocolo y que se descartó la llamada directa. Así, el nuevo desarrollador entiende el porqué y no elimina la capa pensando que es innecesaria.

### ¿Qué decisiones clave podrían perderse si se cambia de equipo?

Se pueden perder el timeout elegido, el motivo de los reintentos, qué error se muestra al operador y por qué la estimación de ruta no bloquea todo el pedido. El ADR conserva esas decisiones y asigna un responsable para revisarlas.

### ¿Estoy documentando solo la solución final o también el porqué?

Debes documentar ambos. La solución final es “usar IRouteEstimator”; el porqué es que una dependencia externa no debe controlar la creación de pedidos. Sin el porqué, nadie sabrá cuándo mantener, cambiar o eliminar la decisión.

## Actividad: documenta una decisión real

1. Elige una decisión de la plataforma: rutas, inventario, notificaciones o pagos.
2. Describe el contexto y el problema en máximo cinco líneas.
3. Escribe dos alternativas posibles.
4. Elige una y declara al menos un costo que aceptas.
5. Define una condición medible para revisar la decisión.
6. Crea un ADR en `docs/adr/ADR-00X.md`.
7. Pide a otra persona que lea el ADR y responda: “¿entiendo el porqué, la alternativa descartada y cuándo revisar la decisión?”. Si no puede responder, mejora el documento.

## Cómo comprobar que lo resolviste
Tu actividad está bien resuelta cuando un compañero que no participó en la decisión puede explicar: qué problema existía, qué alternativa se descartó, qué costo se aceptó y qué evento obligaría a revisar el ADR.

## Cierre
Documentar no significa escribir más; significa dejar menos espacio para que el equipo adivine. En el siguiente video vas a usar esta claridad para conectar responsabilidad técnica, escalabilidad, seguridad y ética.
