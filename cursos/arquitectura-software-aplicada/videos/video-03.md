# Video 3: Monorepos con Pantsbuild en proyectos reales

## Título
Monorepos con Pantsbuild en proyectos reales

## Resumen
Un monorepo guarda varios proyectos relacionados en un solo repositorio, aunque cada servicio pueda construirse y desplegarse por separado. Pantsbuild ayuda a describir dependencias y coordinar tareas como construir y probar esos proyectos.

El video usa varios servicios de una plataforma logística para mostrar cómo un cambio en una biblioteca compartida puede afectar a sus consumidores. La herramienta ayuda a encontrar y ejecutar trabajos relacionados; el equipo sigue siendo responsable de organizar los límites y mantener las pruebas correctas.

## Ideas principales
- Un monorepo es una forma de organizar el código, no una arquitectura de despliegue obligatoria.
- Pantsbuild usa configuración para describir proyectos, dependencias y tareas.
- Las dependencias explícitas ayudan a probar consumidores afectados por un cambio.
- Un monorepo facilita algunos cambios coordinados, pero requiere organización.
- La herramienta no decide si todos los proyectos deberían compartir repositorio.

## Preguntas para pensar
- ¿Qué podría romperse si cambias una biblioteca sin probar sus consumidores?
- ¿Qué ventaja tendría revisar juntos un cambio de servicio y biblioteca?
- ¿Un monorepo obliga a desplegar todos los servicios al mismo tiempo?
