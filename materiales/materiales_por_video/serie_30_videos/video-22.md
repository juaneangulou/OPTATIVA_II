# Video 22: Bases de datos y API Gateway

## Fuentes de este video
- [Migraciones de base de datos con Flyway](https://platzi.com/cursos/software-avanzado/migraciones-de-base-de-datos-con-flyway/)
- [API Gateway como capa de abstracción](https://platzi.com/cursos/software-avanzado/api-gateway-como-capa-de-abstraccion-en/)

## Navegación
[⬅️ Video anterior: métricas y migración](video-21.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: Bounded Context e infraestructura como código](video-23.md)

## Para estudiar por tu cuenta
Una nueva pantalla de seguimiento puede exigir cambiar la base de datos y la respuesta de la API al mismo tiempo. Si cambias solo una parte, clientes antiguos podrían fallar; si modificas datos sin planear los pedidos existentes, podrías perder información.

Este capítulo conecta dos temas: usar Flyway para aplicar cambios de base de datos en orden y usar una API Gateway como entrada estable entre clientes y servicios.

## 1. El caso: agregar una hora estimada
La plataforma guarda pedidos y estados, pero ahora quiere mostrar una hora estimada de llegada. Esa hora se calcula o recibe desde Entregas y debe llegar al cliente mediante la API.

Participan tres piezas:

- **Base de datos:** conserva el nuevo dato cuando existe.
- **Servicio de Entregas:** conoce o calcula la estimación.
- **API Gateway:** recibe la consulta del cliente y dirige la solicitud al servicio que puede responder.

La Gateway no es dueña de la hora ni decide cómo se calcula. La base de datos tampoco decide si la estimación es confiable. Cada pieza tiene una responsabilidad diferente.

## 2. Preparar el cambio de base de datos con Flyway
Una **migración** es un cambio planeado en la estructura o los datos guardados. Flyway ejecuta archivos de migración numerados y registra cuáles ya se aplicaron.

Un archivo podría llamarse:

```text
V4__Agregar_hora_estimada.sql
```

`V4` indica el orden de la migración; el resto describe su propósito. En un proyecto real, verifica el historial y el formato que la configuración de Flyway espera.

Antes de aplicarlo, pregunta qué ocurre con los pedidos anteriores, que no tienen hora estimada. Una respuesta puede ser dejar el campo vacío hasta obtener un cálculo, no inventar un valor.

## 3. Mantener compatibilidad durante el despliegue
La base de datos y la aplicación no siempre se actualizan en el mismo instante. Puede seguir activa una versión antigua de la API mientras se aplica una migración nueva.

Un enfoque gradual consiste en:

1. Añadir un campo opcional que las versiones antiguas puedan ignorar.
2. Aplicar la migración en un entorno de pruebas y comprobar pedidos existentes.
3. Publicar el servicio que calcula y devuelve la estimación.
4. Actualizar el contrato de la API para incluir el campo opcional.
5. Verificar que clientes antiguos sigan funcionando.
6. Si en el futuro se vuelve obligatorio, preparar otro cambio y una actualización de datos antes de imponerlo.

Este enfoque se suele llamar **expandir y contraer**: primero agregas una capacidad compatible; después migras consumidores; por último eliminas lo antiguo solo cuando ya nadie depende de ello.

## 4. ¿Qué hace la API Gateway?
La **API Gateway** es una puerta de entrada que recibe solicitudes de las aplicaciones y las dirige a los servicios apropiados. Puede ofrecer una dirección estable aunque internamente cambien los servicios.

Cuando el cliente pide el pedido 245, la Gateway puede dirigir la consulta a Entregas y devolver un contrato como:

```text
Estado: En camino
Hora estimada: 14:30 (estimación; actualizada 14:05)
```

El **contrato** define qué datos devuelve la API y qué significan. Si la hora todavía no existe, el contrato debe indicar si el campo se omite, se devuelve vacío o se informa de otra manera; no dejes esa decisión implícita.

La Gateway puede adaptar o combinar respuestas según el diseño, pero no debería guardar su propia copia del estado ni duplicar la regla de Entregas.

## 5. Datos y API deben evolucionar juntos
Para cada nuevo campo pregunta:

- ¿Quién produce el dato?
- ¿Quién lo guarda?
- ¿Quién lo devuelve al cliente?
- ¿Es obligatorio o puede faltar?
- ¿Qué ven las versiones anteriores de la aplicación?
- ¿Qué información no debe exponerse a todos los clientes?

Si el nuevo campo contiene una estimación, el contrato debe distinguirla de una hora garantizada. Una etiqueta como “estimada” evita que el cliente interprete el dato como promesa exacta.

## 6. Qué probar antes de publicar
- Ejecutar Flyway sobre una copia de la base y verificar que los pedidos antiguos sigan disponibles.
- Confirmar que la nueva versión del servicio puede leer el campo opcional.
- Comprobar que la Gateway conserva el formato anterior y agrega el nuevo dato de forma compatible.
- Consultar con una versión antigua del cliente.
- Probar el caso en que todavía no existe una hora estimada.
- Verificar permisos: el cliente solo puede consultar pedidos que le pertenecen.

Una migración aplicada no demuestra que la API esté bien, y una API que compila no demuestra que los datos antiguos sean válidos. Comprueba ambos límites.

## 7. Actividad de autoestudio
La plataforma quiere agregar `hora_estimada` al seguimiento:

1. Decide si puede faltar para pedidos antiguos.
2. Escribe el nombre de una migración posterior a `V3__Crear_tabla_pedidos.sql`.
3. Describe el orden de cambios entre base de datos, servicio y Gateway.
4. Especifica qué devuelve la API si no hay estimación.
5. Propón tres pruebas para versiones antiguas y nuevas.
6. Indica qué harías si la migración funciona pero el cliente recibe un formato distinto al esperado.

### Respuesta modelo
La migración puede ser `V4__Agregar_hora_estimada.sql`, si V4 es la siguiente versión libre. El campo empieza opcional; Flyway se prueba primero en una copia; luego se publica el servicio y se extiende el contrato de la Gateway.

Si no existe estimación, la API puede omitir el dato o devolverlo como no disponible, siempre de manera consistente con el contrato. Las pruebas verificarían pedidos antiguos, pedidos nuevos con estimación y compatibilidad con cliente antiguo.

Si el formato de la API no coincide, se detiene la ampliación y se corrige el contrato o el adaptador antes de continuar; no se debe cambiar silenciosamente el significado del campo.

## Comprueba lo que aprendiste
1. ¿Qué registra Flyway?
2. ¿Qué significa mantener compatibilidad durante una migración?
3. ¿Quién es responsable de calcular la hora estimada?
4. ¿Por qué la API debe indicar que una hora es estimada?

### Respuestas
1. Qué archivos de migración se aplicaron y en qué orden.
2. Que las versiones que conviven sigan pudiendo leer y producir los datos necesarios.
3. El servicio del dominio responsable de seguimiento o rutas, no la Gateway por defecto.
4. Para que el cliente no confunda una predicción con una garantía.

## Conclusión
Una migración de base de datos y un cambio de API son partes coordinadas de la misma evolución. Flyway mantiene el orden de los cambios persistentes; la Gateway puede proteger una entrada estable; el contrato explica qué ve el cliente.

El cambio es seguro cuando considera pedidos existentes, clientes antiguos, datos opcionales, pruebas y una forma de detener la publicación si algo no coincide.