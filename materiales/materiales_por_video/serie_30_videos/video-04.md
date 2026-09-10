# Video 04: Responsabilidad, escalabilidad, seguridad y ética

## 📚 Lecturas de referencia: responsabilidad y seguridad
- [Arquitectura como responsabilidad humana](https://platzi.com/cursos/fundamentos-arquitectura-software/espacio-de-problema-vs-solucion-en-arqui/)
- [Escalabilidad, seguridad y ética](https://platzi.com/cursos/fundamentos-arquitectura-software/requisitos-funcionales-y-no-funcionales/)

## 🔗 Continúa el recorrido
[⬅️ Video anterior](video-03.md) | [➡️ Video siguiente](video-04-1.md)

## 🎯 La decisión de esta clase
En esta clase vas a tomar una decisión incómoda: cómo usar datos de ubicación para mejorar una entrega sin convertir al repartidor ni al cliente en una fuente de vigilancia permanente. La arquitectura no se evalúa solo por velocidad; también se evalúa por las personas que quedan expuestas cuando el sistema toma una decisión.

## Las ideas que unimos
La primera fuente recuerda que el software puede afectar confianza, seguridad y bienestar. La segunda agrega que escalar no basta: un sistema que responde rápido pero expone datos, excluye usuarios o toma decisiones injustas sigue siendo una mala solución.

Juntas nos obligan a diseñar con cuatro preguntas: ¿qué valor entregamos?, ¿a quién protegemos?, ¿qué datos son necesarios?, ¿qué costo aceptamos para mantener el sistema confiable cuando crezca?

## Escena: la reasignación urgente
Es viernes a las 7:00 p. m. y una tormenta bloquea varias vías. La plataforma necesita reasignar 400 entregas. El área de operaciones pide ubicación GPS en tiempo real de todos los repartidores, historial completo de trayectos y acceso a esos datos para cualquier supervisor. El objetivo es reducir retrasos, pero la propuesta expone más información de la necesaria y puede afectar la seguridad personal de los repartidores.

Aquí aparecen dos actores centrales:

- **El cliente** necesita saber si su pedido llegará y recibir una explicación confiable si cambia la promesa.
- **El repartidor** necesita una ruta y una asignación justa, sin que su ubicación histórica se convierta en información disponible para personas que no la necesitan.

La regla que vamos a proteger es esta: **la plataforma solo puede usar y conservar la ubicación necesaria para coordinar una entrega activa, con acceso limitado y trazable**.

## Dos opciones reales
### Opción A: recopilar y compartir toda la ubicación disponible
Operaciones obtiene más datos de inmediato y puede reaccionar rápido. El costo oculto es alto: exceso de datos personales, mayor superficie de ataque, posibilidad de uso indebido y dificultad para explicar quién consultó la ubicación. Esta opción optimiza la urgencia, pero no protege al repartidor.

### Opción B: ubicación mínima, temporal y con acceso por rol
El sistema guarda la ubicación solo durante una entrega activa, redondea la precisión cuando no es necesaria, elimina o anonimiza el historial según la política definida y registra cada consulta. Operaciones conserva la información que necesita para reasignar; soporte puede auditar accesos; el repartidor no queda expuesto innecesariamente.

Para este caso elijo la opción B. Aceptamos más trabajo: control de roles, expiración de datos, auditoría y pruebas de autorización. Lo aceptamos porque el sistema no puede sacrificar privacidad y seguridad para ganar algunos segundos de coordinación.

## Cómo se diseña la solución
1. El módulo de asignación solicita la ubicación actual solo de repartidores candidatos a una entrega activa.
2. Un servicio de privacidad verifica que quien consulta tenga el rol correcto y una razón operacional válida.
3. La API devuelve la precisión mínima necesaria para decidir, no el historial completo.
4. Cada consulta genera una auditoría: quién consultó, para qué pedido, a qué hora y con qué resultado.
5. Un proceso de retención elimina la ubicación detallada cuando termina la ventana operativa acordada.
6. El cliente recibe una actualización de entrega sin conocer datos personales del repartidor.

## 💬 Preguntas que debemos resolver sobre datos y confianza
### ¿Qué impacto tiene el software que estoy diseñando?

El impacto es directo: una decisión sobre GPS puede mejorar la puntualidad del cliente, pero también puede poner en riesgo la privacidad y seguridad del repartidor. Por eso la arquitectura debe limitar datos, roles y tiempo de retención. La evidencia será una auditoría que muestre que ningún usuario sin autorización consultó ubicaciones.

### ¿Estoy asumiendo una responsabilidad real con las personas que usan el sistema?

Sí, cuando el diseño reconoce que el repartidor no es solo una coordenada en un mapa. La responsabilidad se traduce en reglas: propósito definido, acceso mínimo, consentimiento cuando corresponda y capacidad de revisar quién vio los datos. El costo es implementar controles; el beneficio es proteger confianza y reducir abuso.

### ¿Mi sistema considera seguridad y ética desde el inicio?

Lo hace si la seguridad aparece antes de desplegar: roles, cifrado, retención, auditoría y pruebas de acceso denegado son parte del diseño. No sirve agregar una política de privacidad después de almacenar todo el historial de rutas.

### ¿Qué pasa si el volumen se multiplica durante una emergencia?

No habilitamos acceso ilimitado a los datos. Escalamos el cálculo de candidatos, usamos colas para las reasignaciones y mantenemos el mismo control de autorización. El sistema debe crecer sin degradar las protecciones que justifican la confianza de quienes lo usan.

## Actividad: diseño responsable de reasignación

1. Dibuja el flujo de reasignación de una entrega retrasada.
2. Marca qué dato personal entra, quién lo usa y cuánto tiempo se conserva.
3. Escribe dos reglas de acceso y una regla de retención.
4. Compara la opción de datos completos con la de datos mínimos.
5. Elige una alternativa y redacta un ADR con el riesgo aceptado.
6. Define dos pruebas: una de acceso permitido para operaciones y otra de acceso denegado para un usuario sin rol.
7. Añade una métrica: porcentaje de consultas de ubicación auditadas y porcentaje de datos eliminados al finalizar la retención.

## Cómo comprobar que la actividad está resuelta
Tu propuesta está completa si puedes demostrar tres cosas: el cliente recibe una actualización útil, el operador puede reasignar una entrega y un usuario no autorizado no puede consultar ni reconstruir el historial de ubicación del repartidor.

## ✅ Cierre: velocidad sin daño innecesario
La escalabilidad tiene valor cuando mantiene el servicio bajo presión. La seguridad tiene valor cuando protege a las personas. La ética tiene valor cuando impide que una solución rápida normalice un daño innecesario. En el siguiente video vamos a bajar de estas decisiones al código: principios de diseño, acoplamiento y cohesión.

