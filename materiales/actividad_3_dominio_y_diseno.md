# Actividad 3: Diseño y dominio

## Objetivo

Diseñar un sistema que proteja la lógica de negocio, minimice el acoplamiento y defina límites claros entre dominio, aplicación y infraestructura.

## Entregables obligatorios

- Enlace al repositorio de GitHub con el resultado de la actividad, documentos, código e historial de commits.
- Enlace al video de sustentación publicado en YouTube, Google Drive o Microsoft Teams.
- No adjuntar el archivo de video directamente; entregar únicamente su enlace de acceso.

## ¿Qué se evalúa?

- modelo de dominio,
- entidades y objetos de valor,
- invariantes y reglas del negocio,
- casos de uso,
- separación entre capas,
- decisiones de diseño con dependencia correcta.

## Conceptos clave

### 1. Dominio
Es la parte del sistema que representa el negocio: reglas, conceptos, procesos, restricciones, políticas.

### 2. Entidad
Es un objeto con identidad propia.

Ejemplo:

- cliente,
- pedido,
- empleado,
- reserva.

### 3. Objeto de valor
No tiene identidad propia; se describe por sus atributos.

Ejemplo:

- monto,
- dirección,
- fecha de entrega,
- prioridad.

### 4. Invariante
Es una regla que siempre debe cumplirse.

Ejemplo:

- una reserva no puede superarse en capacidad,
- un pedido no puede estar en dos estados contradictorios,
- un usuario no puede tener dos roles conflictivos.

## Principios importantes

### SOLID
- S: responsabilidad única,
- O: abierto/cerrado,
- L: sustitución de Liskov,
- I: segregación de interfaces,
- D: inversión de dependencias.

### Inversión de dependencias
Las capas internas no deberían depender de elementos externos. El dominio debería estar protegido.

## Estructura recomendada

- dominio: entidades, reglas, casos de uso,
- aplicación: contratos, orquestación, servicios,
- infraestructura: persistencia, APIs, notificaciones, mensajería.

## Casos de uso y contratos

Un caso de uso responde a la pregunta: ¿qué necesita hacer el usuario o el sistema?

Ejemplo:

- Crear reserva,
- Cancelar reserva,
- Confirmar pago,
- Obtener historial de pedidos.

Cada caso de uso debe tener una intención clara, sin mezclarse con detalles de base de datos o HTTP.

## Ejemplo de modelo de dominio

Para la plataforma logística de última milla:

- Cliente
- Pedido
- LíneaPedido
- Inventario
- Almacén
- Ruta
- Repartidor
- EstadoEntrega
- Incidencia
- Devolución

Reglas:

- un pedido no puede confirmarse si el stock solicitado no está disponible,
- una entrega no puede asignarse a un repartidor si la ruta ya está saturada,
- una incidencia no puede cerrarse sin registrar resolución ni responsable,
- una devolución debe estar asociada a un pedido válido y a un motivo concreto.

## Diagramas que puedes incluir

- diagrama de componentes,
- diagrama de capas,
- diagrama de dependencias,
- mapa de entidades y relaciones.

## Video de sustentación

Explica:

- qué es el dominio,
- cuántas capas usaste y por qué,
- dónde están las reglas críticas,
- cómo evitas acoplar el negocio a la infraestructura,
- qué decisiones de diseño fueron clave.

## Checklist final

- [ ] modelo de dominio definido
- [ ] entidades y objetos de valor diferenciados
- [ ] invariantes listados
- [ ] casos de uso principales descritos
- [ ] dependencias dirigidas correctamente
- [ ] diagrama de capas o componentes
- [ ] video entregado

## Consejo importante

La lógica de negocio debe poder cambiar sin depender de una base de datos, una API externa o un framework concreto.
