# Video 18: Infraestructura como código en monorepos para microservicios

## Título
Cómo describir y revisar los recursos que necesitan varios servicios

## Situación
La plataforma logística tiene un servicio de Pedidos y otro de Entregas. Pedidos necesita dejar tareas en una cola para que Entregas las procese. Si cada entorno se configura manualmente, desarrollo, pruebas y producción pueden terminar distintos sin que el equipo sepa por qué.

**Infraestructura como código** significa describir mediante archivos los recursos del sistema, como una cola, una base de datos y sus permisos. **Monorepo** significa guardar varios proyectos relacionados en un mismo repositorio. No son lo mismo: uno describe cómo preparar recursos; el otro describe dónde guarda el equipo sus proyectos.

## Cómo funciona el cambio
1. El equipo aclara qué necesita: Pedidos debe enviar tareas y Entregas debe leerlas.
2. Describe la cola y sus permisos en archivos del proyecto.
3. Revisa el cambio junto con los cambios de ambos servicios.
4. Previsualiza qué recursos se crearán, cambiarán o borrarán antes de aplicarlo.
5. Lo prueba en desarrollo o pruebas antes de producción.
6. Comprueba que la tarea llegue al servicio correcto.

Un monorepo puede facilitar revisar en una sola propuesta el código de los servicios y los recursos que necesitan. No obliga a desplegar todos los servicios juntos ni garantiza que los cambios sean seguros.

## Cuidados importantes
- Las contraseñas y claves de acceso son secretos: no deben escribirse directamente en los archivos del repositorio.
- La previsualización debe revisarse para descubrir reemplazos o eliminaciones inesperadas.
- Los permisos deben limitarse a lo que cada servicio necesita.
- Si alguien cambia un entorno manualmente y no actualiza los archivos, la descripción puede dejar de coincidir con la realidad.
- Infraestructura como código no garantiza por sí sola una configuración correcta; el equipo debe probarla y verificarla.

## Preguntas para comprobar tu comprensión
- ¿Qué diferencia hay entre infraestructura como código y monorepo?
- ¿Qué revisarías antes de aplicar un cambio a producción?
- ¿Qué riesgo existe si se guarda una contraseña en el repositorio?
- ¿Por qué un monorepo no significa que todos los servicios se despliegan juntos?
