# Actividad 2: Requisitos y decisión estructural

## Objetivo

Convertir las necesidades del negocio en criterios arquitectónicos y elegir una estructura apropiada para el sistema.

## Entregables obligatorios

- Enlace al repositorio de GitHub con el resultado de la actividad, documentos, README e historial de commits.
- Enlace al video de sustentación publicado en YouTube, Google Drive o Microsoft Teams.
- No adjuntar el archivo de video directamente; entregar únicamente su enlace de acceso.

## ¿Qué se evalúa?

- requisitos funcionales priorizados,
- escenarios de calidad,
- comparación entre dos alternativas,
- justificación técnico-negocio,
- decisión estructural con trade-offs.

## Conceptos clave

### 1. Requisitos funcionales
Son lo que el sistema debe hacer.

Ejemplos:

- crear usuario,
- reservar horario,
- pagar con tarjeta,
- enviar notificación,
- consultar historial.

### 2. Requisitos no funcionales
Son atributos de calidad.

Ejemplos:

- rendimiento,
- seguridad,
- disponibilidad,
- mantenibilidad,
- escalabilidad,
- facilidad de cambio.

### 3. Alternativas estructurales
Puedes comparar, por ejemplo:

- monolito modular,
- arquitectura por capas,
- cliente-servidor,
- microservicios,
- enfoque basado en eventos.

## Recomendación metodológica

### Paso 1: Priorizar requisitos
Usa una matriz con:

- requisito,
- prioridad,
- impacto en negocio,
- impacto en arquitectura,
- nivel de complejidad.

### Paso 2: Definir escenarios de calidad
Ejemplo:

- un usuario debe consultar su pedido en menos de 2 segundos,
- el sistema debe soportar 1.000 transacciones por hora,
- la información sensible debe estar cifrada,
- el cambio de reglas de negocio no debe requerir cambiar toda la app.

### Paso 3: Evaluar alternativas
Haz una tabla con criterios como:

- complejidad,
- costo,
- rapidez de implementación,
- facilidad de evolución,
- riesgo operativo,
- alineación con negocio.

### Paso 4: Tomar la decisión
La decisión no es “la mejor arquitectura”. Es la más apropiada para este caso concreto.

## Ejemplo de comparación para este caso

### Opción A: Monolito modular con límites claros
Ventajas:

- es más rápido de construir para una operación con crecimiento moderado,
- permite definir dominios por pedido, inventario, entregas e incidencias,
- reduce complejidad operativa inicial,
- facilita la trazabilidad y mantenimiento.

Desventajas:

- puede convertirse en una base de código acoplada si no se definen límites bien,
- el crecimiento de la operación puede exigir refactorización más adelante.

### Opción B: Arquitectura distribuida por dominios y servicios
Ventajas:

- separa mejor inventario, entrega y soporte,
- permite crecimiento por módulos o equipos,
- facilita integración con varios sistemas externos.

Desventajas:

- aumenta la complejidad operativa,
- exige más coordinación técnica y más infraestructura,
- puede sobrediseñarse si el negocio aún no lo requiere.

Para la plataforma logística, la decisión correcta suele ser una estructura con dominio bien separado y una implementación modular, evitando introducir microservicios innecesarios antes de tener evidencia de que el crecimiento los justifica.

## Estructura de entrega sugerida

- catálogo de requisitos,
- matriz de calidad,
- comparación de alternativas,
- decisión final,
- ADR o registro de decisiones.

## Qué debe explicar tu video

- cuáles fueron las principales necesidades del negocio,
- cómo priorizaste los requisitos,
- qué alternativas comparaste,
- qué criterios fueron decisivos,
- por qué la opción elegida reduce riesgo y costo.

## Checklist final

- [ ] requisitos funcionales claros
- [ ] requisitos no funcionales definidos
- [ ] escenarios de calidad con métricas
- [ ] al menos dos alternativas comparadas
- [ ] decisión argumentada con trade-offs
- [ ] documento de registro de decisión
- [ ] video de sustentación entregado

## Regla de oro

La mejor arquitectura es la que se adapta al problema, no la que parece más moderna.
