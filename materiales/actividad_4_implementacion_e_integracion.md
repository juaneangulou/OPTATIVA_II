# Actividad 4: Implementación e integración

## Objetivo

Construir una parte funcional del sistema con una arquitectura coherente, conectando entrada, negocio, persistencia e integración externa sin contaminar el dominio.

## Entregables obligatorios

- Enlace al repositorio de GitHub con el resultado de la actividad, código ejecutable, README e historial de commits.
- Enlace al video de demostración y sustentación publicado en YouTube, Google Drive o Microsoft Teams.
- No adjuntar el archivo de video directamente; entregar únicamente su enlace de acceso.

## ¿Qué se evalúa?

- implementación funcional del flujo principal,
- uso correcto de capas y límites,
- conexión con repositorios o adaptadores,
- manejo básico de errores,
- trazabilidad entre diseño e implementación.

## Conceptos clave

### 1. Vertical slice
Es una porción del sistema que incluye todo el recorrido funcional: entrada, aplicación, dominio e persistencia.

### 2. Puerto y adaptador
El dominio define el puerto. La implementación concreta queda en el adaptador.

Ejemplo:

- puerto: guardar reserva,
- adaptador: repositorio PostgreSQL,
- adaptador externo: servicio de notificaciones.

### 3. API o entrada del sistema
Puede ser REST, CLI, manejador HTTP, servicio interno o evento.

### 4. Manejo de errores
No basta con “fallar”. Hay que decidir:

- reintentar,
- registrar el error,
- devolver un mensaje claro,
- fallar de forma controlada.

## Qué debes implementar

Preferiblemente, un caso de uso completo del problema obligatorio, por ejemplo:

- crear un pedido desde un canal digital,
- validar disponibilidad de inventario,
- asignar la entrega a una ruta y repartidor,
- actualizar el estado del pedido,
- registrar una incidencia de entrega fallida,
- consultar historial de un pedido o devolución.

## Capa por capa

### Capa de entrada
- controller,
- endpoint,
- DTO,
- validación.

### Capa de aplicación
- casos de uso,
- orquestación,
- validación de reglas,
- coordinación entre dependencias.

### Capa de dominio
- entidades,
- reglas,
- invariantes,
- servicios de dominio.

### Capa de infraestructura
- repositorio,
- conexión a base de datos,
- notificaciones,
- integraciones externas.

## Recomendación de prueba

Te debe quedar una evidencia de que el flujo funciona de extremo a extremo.

Ejemplo:

- se llama al endpoint,
- se valida la operación,
- se ejecuta el caso de uso,
- se guarda la información,
- se responde con resultado correcto.

## Video de sustentación

Incluye:

- la funcionalidad implementada,
- recorrido del flujo,
- dónde está cada capa,
- cómo se protege el dominio,
- qué errores y adaptadores manejaste.

## Checklist final

- [ ] flujo funcional implementado
- [ ] arquitectura con capas o límites claros
- [ ] persistencia o integración externa aislada
- [ ] manejo de errores básico
- [ ] README con instrucciones de ejecución
- [ ] evidencia de pruebas o ejecución
- [ ] video de sustentación

## Consejo importante

La implementación debe demostrar que el dominio es la pieza central y que la infraestructura solo acompaña la solución.
