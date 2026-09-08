# Caso base obligatorio para el curso: Plataforma de gestión logística de última milla

## 1. Contexto del problema

Una empresa de retail digital está creciendo rápidamente y ya no puede operar con procesos manuales y hojas de cálculo. Los pedidos llegan desde varios canales digitales, el inventario se gestiona en distintas ubicaciones, los repartidores trabajan con distintas rutas, y la atención al cliente se vuelve ineficiente porque no existe una vista única del estado del pedido.

El negocio presenta varios problemas reales:

- los pedidos se duplican o se mezclan en la operación,
- el estado del pedido no es consistente entre almacén, clientes y soporte,
- las entregas se retrasan por falta de coordinación de rutas,
- no hay trazabilidad clara de devoluciones ni entregas fallidas,
- la evolución del sistema se vuelve difícil porque cada área usa herramientas distintas,
- la empresa quiere crecer sin destruir la operación actual.

## 2. Definición del problema

La empresa necesita una plataforma centralizada para gestionar el ciclo completo de una entrega: desde la creación del pedido hasta la entrega final, pasando por inventario, asignación de rutas, coordinación de repartidores, gestión de incidencias, seguimiento en tiempo real y atención al cliente.

La plataforma debe permitir:

- registrar y validar pedidos de clientes,
- sincronizar inventario entre almacenes y puntos de venta,
- asignar entregas a rutas y repartidores,
- rastrear la ubicación y el estado de cada entrega,
- analizar retrasos, fallas y devoluciones,
- integrar servicios externos de pagos, geolocalización, mensajería y notificaciones,
- soportar crecimiento sin romper el sistema operativo.

## 3. Objetivo del sistema

Construir una plataforma digital que permita a la empresa operar de forma coordinada y escalable, con información confiable, tiempos de respuesta razonables y capacidad de evolución frente al crecimiento del negocio.

## 4. Usuarios y actores principales

### 4.1 Cliente
- consulta el estado de su pedido,
- recibe actualizaciones de entrega,
- puede reportar una incidencia,
- recibe reprogramación o notificación de retraso.

### 4.2 Operador de comercio o tienda
- revisa pedidos entrantes,
- confirma disponibilidad,
- gestiona cierres de venta y devoluciones,
- recibe alertas por stock o entregas fallidas.

### 4.3 Administrador de almacén
- valida preparación del producto,
- registra salidas y recepciones,
- revisa inconsistencias de inventario,
- coordina reabastecimiento.

### 4.4 Repartidor
- recibe asignaciones de rutas,
- actualiza estado de entrega,
- reporta entregas, fallas o rechazos,
- comparte ubicación aproximada o real.

### 4.5 Soporte al cliente
- consulta historial de pedidos,
- reabre casos,
- gestiona reembolsos o seguimiento,
- comunica incidencias internas.

### 4.6 Sistema externo
- gateway de pago,
- servicio de geolocalización,
- servicio de notificaciones,
- proveedor de envíos o transporte,
- sistema de inventario externo,
- CRM o ERP del negocio.

## 5. Casos de negocio principales

- creación de un pedido desde una tienda digital,
- validación de stock y disponibilidad,
- asignación de entrega a un repartidor,
- seguimiento del pedido en tiempo real,
- entrega exitosa o fallida,
- reintento de entrega o cambio de horario,
- devolución de producto,
- control de SLA y tiempos de entrega,
- gestión de incidencias por parte del soporte,
- análisis de rendimiento del servicio.

## 6. Requisitos funcionales principales

1. Registrar pedidos con múltiples líneas de producto.
2. Validar stock disponible por almacén y punto de venta.
3. Crear una ruta de entrega y asignarla a un repartidor.
4. Actualizar el estado del pedido en cada etapa.
5. Permitir seguimiento para clientes y soporte.
6. Gestionar devoluciones y reembolsos básicos.
7. Registrar incidencias con prioridad, causa y resolución.
8. Generar reportes de rendimiento por zona, repartidor y tipo de entrega.
9. Integrar con servicios externos de pago, envío y notificaciones.
10. Crear una auditoría de cambios importantes en la operación.

## 7. Requisitos no funcionales esperados

- disponibilidad alta para la operación crítica,
- tiempos de respuesta razonables en consultas de estado,
- seguridad en datos personales y transacciones,
- trazabilidad de cambios y eventos,
- capacidad de evolución ante aumento de pedidos,
- consistencia adecuada en operaciones críticas,
- registro de errores y observabilidad mínima,
- escalabilidad horizontal razonable para picos de demanda.

## 8. Restricciones del negocio

- la operación actual ya está en producción,
- no se puede detener toda la operación para reescribir sistemas,
- el crecimiento es acelerado pero no uniforme,
- existen varios canales de venta y varios puntos de operación,
- se requiere que el sistema pueda evolucionar sin caos,
- la empresa prioriza tiempo de entrega y confiabilidad antes que una arquitectura “perfecta”.

## 9. Complejidad técnica esperada

Este problema es una plataforma compleja porque integra:

- múltiples tipos de usuarios,
- varios procesos de negocio,
- múltiples sistemas externos,
- decisiones de consistencia y coordinación,
- reglas de negocio sensibles (stock, entregas, incidencias),
- necesidad de trazabilidad y operación real.

## 10. Decisión arquitectónica esperada

El sistema no debe resolverse como una sola función aislada. Debe plantearse como una solución con:

- dominio central bien definido,
- manejo claro de casos de uso,
- segregación entre negocio e infraestructura,
- adaptadores para pagos, notificaciones, geolocalización y gestión de inventario,
- apalancamiento de pruebas para reglas críticas,
- decisiones explícitas sobre consistencia, fallos y observabilidad.

## 11. Proyecto para el curso

Los estudiantes deben trabajar con este mismo caso base en todas las actividades:

- Actividad 1: diagnóstico, contexto y actores.
- Actividad 2: requisitos, calidad y elección estructural.
- Actividad 3: dominio, reglas, invariantes y límites del diseño.
- Actividad 4: implementación de un flujo funcional completo.
- Actividad 5: pruebas, operación, riesgos y defensa final.

## 12. Resultado esperado

El proyecto debe entregar una arquitectura inicial viable para una plataforma de gestión logística de última milla, con una propuesta clara, justificable y evolutiva, sin sobrediseñar ni inventar tecnologías innecesarias.
