# Actividad 1: Diagnóstico y contexto arquitectónico

## Objetivo

Comprender el problema antes de elegir tecnologías, frameworks, capas o estructuras. La arquitectura comienza con el contexto, no con el código.

## Entregables obligatorios

- Enlace al repositorio de GitHub con el resultado de la actividad, documentos, README e historial de commits.
- Enlace al video de sustentación publicado en YouTube, Google Drive o Microsoft Teams.
- No adjuntar el archivo de video directamente; entregar únicamente su enlace de acceso.

## ¿Qué se evalúa?

- claridad del problema,
- identificación de actores,
- definición de alcance,
- comprensión de riesgos,
- calidad del diagrama de contexto,
- capacidad de justificar decisiones iniciales.

## Conceptos clave

### 1. Problema
Un problema no se formula solo como “necesitamos una app”. Debe describirse como necesidad, frustración, oportunidad o restricción de negocio.

Ejemplo:

- Problema: los clientes no saben cuándo llegará su pedido ni el operador no puede gestionar entregas por falta de información centralizada.

### 2. Contexto del sistema
El contexto define:

- quién usa el sistema,
- qué procesos ejecuta,
- qué sistemas externos interactúan,
- qué límites existen.

### 3. Actores
Incluye usuarios, clientes, administradores, proveedores, analistas, terceros externos, sistemas o APIs.

### 4. Riesgos
Los riesgos son los puntos donde el sistema puede fallar o causar pérdidas.

Ejemplos:

- retrasos en entregas,
- pérdida de información,
- baja seguridad,
- mala experiencia de usuario,
- crecimiento descontrolado del sistema.

## Estructura recomendada de entrega

### A. Resumen ejecutivo
Incluye:

- nombre del producto,
- problema principal,
- usuarios,
- objetivos,
- alcance.

### B. Diagrama de contexto
Debes mostrar:

- usuario,
- sistema principal,
- sistemas externos,
- flujos de información,
- límites del sistema.

### C. Análisis del problema
Responde:

- ¿Qué ocurre hoy?
- ¿Por qué es un problema?
- ¿Qué consecuencias tiene?
- ¿Qué variables importan?

### D. Supuestos y decisiones iniciales
Escribe:

- qué asumes,
- qué decisiones ya tomas,
- qué aún no sabes,
- qué habrá que confirmar luego.

## Caso obligatorio del proyecto

La plataforma es una solución de gestión logística de última milla para una empresa de retail digital.

### Problema
La empresa recibe pedidos desde varios canales, maneja inventarios distribuidos, coordina entregas con diferentes rutas y repartidores, y no cuenta con una vista centralizada del estado real de cada pedido. Esto genera duplicación de información, retrasos, errores operativos y poca trazabilidad.

### Actores
- cliente,
- operador de comercio o tienda,
- administrador de almacén,
- repartidor,
- soporte al cliente,
- sistema de pagos,
- servicio de geolocalización,
- sistema de notificaciones,
- ERP o CRM interno.

### Riesgos
- duplicación de pedidos,
- inconsistencias de inventario,
- entregas fallidas o retrasadas,
- pérdida de trazabilidad,
- mala coordinación entre almacén, rutas y soporte,
- crecimiento operativo sin control.

### Decisión inicial
Se propone una plataforma centralizada que permita registrar pedidos, validar inventario, asignar rutas, rastrear entregas y gestionar incidencias desde un único sistema.

## Guía para el video de sustentación

Haz un video de 5 a 8 minutos:

1. presenta el problema,
2. explica usuarios y contexto,
3. muestra el diagrama de contexto,
4. nombra los riesgos principales,
5. explica por qué tu solución inicial es coherente con el negocio.

## Checklist final

- [ ] problema definido con claridad
- [ ] usuarios y actores identificados
- [ ] alcance delimitado
- [ ] diagrama de contexto
- [ ] riesgos principales listados
- [ ] supuestos explícitos
- [ ] decisiones iniciales justificadas
- [ ] video de sustentación entregado

## Consejo importante

No intentes “resolver todo” en esta actividad. El objetivo es formular bien el problema, no diseñar la solución final.
