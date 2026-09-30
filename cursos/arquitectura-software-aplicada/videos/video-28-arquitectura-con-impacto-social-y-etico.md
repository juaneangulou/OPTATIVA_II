# Video 28: Observabilidad con OpenTelemetry e ingeniería del caos

## Título
Entender qué ocurre y probar cómo responde el sistema ante una falla

## Resumen
Cuando una consulta de seguimiento pasa por varios servicios, saber que la aplicación está encendida no basta para entender por qué se demoró. Las **métricas** muestran cantidades y tiempos, los **logs** registran hechos y las **trazas** siguen una solicitud por los distintos componentes.

**OpenTelemetry (OTel)** ayuda a producir y transportar esos datos; normalmente se conecta a otras herramientas que los guardan y muestran. La **ingeniería del caos** prueba una hipótesis de recuperación mediante una falla controlada, con alcance, límites y plan de restauración definidos.

## Ejemplo del video
Se detiene temporalmente el servicio de rutas en un entorno de pruebas. El equipo observa si el estado confirmado del pedido sigue disponible, cuánto espera la Gateway y qué mensaje recibe la persona. La prueba se detiene si sale del alcance o supera el límite acordado.

## Ideas principales
- Una métrica resume; un log cuenta un hecho; una traza muestra un recorrido.
- OTel facilita la instrumentación y el envío de telemetría, pero no necesariamente almacena ni visualiza los datos.
- Un experimento de caos comienza con una hipótesis comprobable.
- Las pruebas controladas necesitan autorización, alcance, límites y restauración.
- Observar el fallo ayuda a saber qué mejorar; probar sin una pregunta produce poco aprendizaje.

## Preguntas para comprobar tu comprensión
- ¿Qué diferencia hay entre una métrica y una traza?
- ¿Qué componente puede ayudar a seguir una consulta entre servicios?
- ¿Qué debe definirse antes de simular una falla?
- ¿Qué resultado comprobaría que la hipótesis del ejemplo se cumplió?
