# Ruta Unificada de Arquitectura de Software

## De la decisión arquitectónica al software limpio y comprobable

**Periodo:** 3 de agosto al 29 de noviembre de 2026  
**Nivel:** Básico a intermedio  
**Clases:** 48  
**Contenido audiovisual de referencia:** aproximadamente 5 h 50 min  
**Práctica guiada:** 24 horas, 30 minutos por clase  
**Proyecto:** arquitectura evolutiva de un producto digital

## La idea del curso

Una arquitectura no se aprende memorizando nombres de patrones. Se aprende tomando decisiones con información incompleta, haciendo visibles sus costos y construyendo límites que permitan cambiar el sistema sin romperlo.

Esta ruta une dos momentos de aprendizaje:

1. **Entender el problema:** negocio, usuarios, requisitos, costo, riesgo y estilo arquitectónico.
2. **Construir una solución resistente:** dominio, casos de uso, dependencias, integraciones, persistencia y pruebas.

El estudiante no entrega dos proyectos separados. Durante las 48 clases construye un único **expediente de arquitectura evolutiva** para un producto digital pequeño. Cada sesión agrega una decisión, un modelo, una implementación o una prueba.

## Resultados de aprendizaje

Al finalizar, el estudiante podrá:

1. Analizar problemas de arquitectura y separar decisiones esenciales de detalles incidentales.
2. Traducir objetivos de negocio en requisitos y atributos de calidad verificables.
3. Comparar monolitos, arquitecturas por capas, servicios, eventos y microservicios.
4. Elegir una solución proporcional al tamaño, riesgo, equipo y presupuesto del producto.
5. Diseñar un dominio con entidades, objetos de valor, invariantes y casos de uso.
6. Aplicar SOLID, inversión de dependencias, puertos, adaptadores y repositorios.
7. Construir una API y aislar persistencia e integraciones externas.
8. Definir una estrategia de pruebas unitarias, integración y aceptación.
9. Documentar decisiones, trade-offs, riesgos y un plan de evolución.
10. Sustentar una arquitectura con argumentos técnicos y de negocio.

## Mapa de módulos

| Módulo | Clases | Periodo | Resultado |
|---|---:|---|---|
| 1. Pensamiento arquitectónico | 1-6 | 3 al 20 de agosto | Problema, actores y decisiones iniciales |
| 2. Valor, requisitos y riesgo | 7-10 | 31 de agosto al 10 de septiembre | Requisitos priorizados y presupuesto de calidad |
| 3. Formas de estructurar sistemas | 11-16 | 14 de septiembre al 1 de octubre | Estilo arquitectónico elegido |
| 4. Diseño mantenible | 17-19 | 12 al 19 de octubre | Reglas de diseño y límites del código |
| 5. De arquitectura a dominio | 25-29 | 27 de octubre al 10 de noviembre | Modelo de dominio y dependencias protegidas |
| 6. Casos de uso y aplicación | 30-33 | 12 al 19 de noviembre | Flujo de aplicación y CQRS proporcional |
| 7. Infraestructura e integración | 34-38 | 20 al 26 de noviembre | API, persistencia y adaptadores |
| 8. Calidad, evolución y defensa | 39-48 | 27 al 29 de noviembre | Pruebas, documentación y sustentación |

> Las fechas de las clases son una guía de trabajo. Las entregas se organizan alrededor de los hitos institucionales del semestre.

## Ruta de aprendizaje

| # | Fecha | Módulo | Clase | Duración | Evidencia |
|---:|---|---|---|---:|---|
| 1 | 03 ago | Pensamiento | La arquitectura como conjunto de decisiones | 02:51 | Registro de decisión inicial |
| 2 | 06 ago | Pensamiento | El costo invisible de elegir mal | 04:48 | Mapa de consecuencias |
| 3 | 10 ago | Pensamiento | El arquitecto y las conversaciones difíciles | 06:05 | Mapa de actores |
| 4 | 13 ago | Pensamiento | Problema esencial, síntoma y detalle técnico | 07:43 | Árbol de problemas |
| 5 | 17 ago | Pensamiento | Deuda, acoplamiento y malas señales | 07:48 | Diagnóstico de riesgos |
| 6 | 20 ago | Pensamiento | Del problema a las fronteras del sistema | 08:16 | Diagrama de contexto |
| 7 | 31 ago | Valor | Requisitos que cambian el diseño | 05:54 | Catálogo priorizado |
| 8 | 03 sep | Valor | Calidad medible: seguridad, rendimiento y cambio | 07:13 | Escenarios de calidad |
| 9 | 07 sep | Valor | Costo total de operación y costo de cambio | 04:22 | Modelo de costos |
| 10 | 10 sep | Valor | Diseñar para la incertidumbre | 03:36 | Registro de supuestos |
| 11 | 14 sep | Estructura | Cómo elegir una estructura sin seguir modas | 02:56 | Matriz de decisión |
| 12 | 17 sep | Estructura | Cliente-servidor y capas que sí protegen | 03:36 | Flujo de una solicitud |
| 13 | 21 sep | Estructura | Monolito modular: empezar pequeño sin encerrarse | 03:58 | Mapa de módulos |
| 14 | 24 sep | Estructura | Servicios y contratos que pueden evolucionar | 02:59 | Contrato de servicio |
| 15 | 28 sep | Estructura | Eventos, consistencia y fallos parciales | 05:43 | Diagrama de evento |
| 16 | 01 oct | Estructura | Microservicios: cuándo el remedio empeora el problema | 04:50 | Decisión de no sobrediseñar |
| 17 | 12 oct | Diseño | SOLID para reducir decisiones acopladas | 12:13 | Refactor justificado |
| 18 | 15 oct | Diseño | Dependencias: dirección, límites y costo | 04:29 | Regla de dependencias |
| 19 | 19 oct | Diseño | Patrones que resuelven problemas reales | 04:01 | Dos patrones comparados |
| 20 | 22 oct | Diseño | Arquitectura MVP: el primer corte útil | 10:30 | Arquitectura inicial |
| 21 | 26 oct | Diseño | Evolucionar sin reescribir el producto | 02:08 | Plan de evolución |
| 22 | 27 oct | Diseño | De producto personal a sistema de equipo | 03:17 | Escenario de crecimiento |
| 23 | 29 oct | Diseño | Revisión de arquitectura entre pares | 05:24 | Informe de revisión |
| 24 | 30 oct | Diseño | Puente hacia el dominio y el código | 01:53 | Backlog arquitectónico |
| 25 | 03 nov | Dominio | Qué protege una arquitectura limpia | 02:02 | Diagnóstico de acoplamiento |
| 26 | 04 nov | Dominio | Por qué MVC y tres capas llegan a sus límites | 04:07 | Mapa de dependencias |
| 27 | 05 nov | Dominio | Clean, Hexagonal y Onion: una misma intención | 07:31 | Comparación de modelos |
| 28 | 06 nov | Dominio | Adoptar arquitectura limpia sin dogmatismo | 04:54 | Decisión de adopción |
| 29 | 10 nov | Dominio | Encapsulamiento, invariantes y modelo de dominio | 08:53 | Entidades y objetos de valor |
| 30 | 12 nov | Aplicación | Transaction Script o dominio rico | 08:25 | Alternativa argumentada |
| 31 | 13 nov | Aplicación | Inyección de dependencias desde el borde | 07:40 | Composición de dependencias |
| 32 | 16 nov | Aplicación | Servicios de aplicación que no se vuelven gigantes | 04:19 | Contrato de aplicación |
| 33 | 17 nov | Aplicación | Casos de uso como intención del negocio | 07:08 | Caso de uso implementado |
| 34 | 18 nov | Aplicación | CQRS cuando separar sí agrega valor | 11:59 | Flujo de comando y consulta |
| 35 | 19 nov | Infraestructura | Persistencia detrás de un puerto | 06:03 | Puerto y adaptador de datos |
| 36 | 20 nov | Infraestructura | Repository: contrato útil, no abstracción vacía | 08:17 | Repositorio orientado al caso de uso |
| 37 | 23 nov | Infraestructura | API REST como adaptador de entrada | 05:27 | Endpoint conectado al dominio |
| 38 | 24 nov | Infraestructura | Integraciones externas con Adapter | 09:06 | Adaptador con manejo de fallos |
| 39 | 25 nov | Calidad | Probar reglas, no detalles accidentales | 05:38 | Pruebas unitarias del dominio |
| 40 | 26 nov | Calidad | Mocks, stubs y pruebas de integración | 09:26 | Pirámide de pruebas |
| 41 | 27 nov | Calidad | Contratos, errores y observabilidad mínima | 08:00 | Matriz de operación |
| 42 | 27 nov | Calidad | Seguridad como responsabilidad distribuida | 08:00 | Amenazas y controles |
| 43 | 28 nov | Evolución | Migrar por fronteras, no por carpetas | 08:00 | Plan de migración |
| 44 | 28 nov | Evolución | Datos, transacciones y consistencia | 08:00 | Decisión de consistencia |
| 45 | 29 nov | Evolución | Revisar costo, calidad y mantenibilidad | 08:00 | Scorecard arquitectónico |
| 46 | 29 nov | Defensa | Contar la historia de una decisión | 08:00 | Presentación técnica |
| 47 | 29 nov | Defensa | Defender trade-offs ante escenarios nuevos | 08:00 | Simulación de comité |
| 48 | 29 nov | Defensa | Cierre: arquitectura como práctica continua | 08:00 | Expediente final y reflexión |

## Práctica transversal

Cada clase requiere 30 minutos de trabajo sobre el mismo producto. La práctica no consiste en copiar diagramas: obliga a observar el sistema, formular una hipótesis, tomar una decisión y dejar evidencia de sus consecuencias.

El expediente final debe reunir:

- Descripción del problema, usuarios y objetivos.
- Requisitos funcionales y escenarios de calidad.
- Mapa de contexto, módulos, capas y dependencias.
- Registro de decisiones con alternativas y trade-offs.
- Modelo de dominio, entidades, objetos de valor e invariantes.
- Casos de uso, puertos, adaptadores y repositorios.
- API o interfaz de entrada e integración externa aislada.
- Pruebas unitarias, integración y criterios de aceptación.
- Riesgos, costos, seguridad, observabilidad y plan de evolución.

## Evaluación

| Evidencia | Porcentaje | Criterio principal |
|---|---:|---|
| Actividad 1: Diagnóstico y contexto | 15% | Comprende el problema antes de elegir tecnología |
| Actividad 2: Requisitos y decisión estructural | 15% | Relaciona valor, calidad, costo y riesgo |
| Actividad 3: Diseño y dominio | 30% | Protege reglas del negocio y controla dependencias |
| Actividad 4: Implementación e integración | 25% | Conecta infraestructura sin contaminar el dominio |
| Actividad 5: Pruebas, operación y defensa final | 15% | Comprueba comportamiento y sustenta decisiones con trade-offs |
| **Total** | **100%** | |

## Enunciados de actividades (formato de entrega)

Las actividades se publican como enunciados formales y se entregan con evidencias verificables.

### Requisito obligatorio para todas las actividades

- **Entregable 1 (obligatorio):** repositorio en GitHub con historial de trabajo, estructura del proyecto y README.
- **Entregable 2 (obligatorio):** video de explicación y sustentación técnica de la actividad.

**Regla de calificación institucional:**

- Si no se entrega el repositorio de GitHub, la calificación de la actividad es **0.0**.
- Si no se entrega el video de sustentación, la calificación de la actividad es **0.0**.
- Si falta cualquiera de los dos entregables obligatorios, la actividad se califica con **0.0**.

### Actividad 1 (15%): Diagnóstico y contexto arquitectónico

**Propósito:** comprender el problema antes de diseñar la solución.

**Se solicita:**

- Definición del problema, objetivos del producto y alcance inicial.
- Identificación de actores, restricciones y riesgos principales.
- Diagrama de contexto del sistema.
- Registro de decisiones iniciales y supuestos.

**Evidencias en GitHub:**

- README con resumen ejecutivo.
- Carpeta `/docs/actividad-1` con diagramas y análisis.
- Commits que muestren evolución (no carga única final).

**Video de sustentación (5 a 8 minutos):**

- Explica problema, decisiones iniciales y riesgos.
- Justifica por qué el contexto definido es consistente con el negocio.

### Actividad 2 (15%): Requisitos y decisión estructural

**Propósito:** convertir necesidades del negocio en criterios de arquitectura.

**Se solicita:**

- Requisitos funcionales priorizados.
- Escenarios de calidad (rendimiento, seguridad, mantenibilidad, disponibilidad).
- Evaluación de al menos dos alternativas estructurales.
- Decisión estructural argumentada con trade-offs.

**Evidencias en GitHub:**

- Documento de priorización de requisitos.
- Matriz de evaluación de alternativas.
- ADR (Architecture Decision Record) con decisión final.

**Video de sustentación (6 a 10 minutos):**

- Presenta alternativas comparadas y criterio de selección.
- Explica impactos en costo, riesgo y evolución.

### Actividad 3 (30%): Diseño y dominio

**Propósito:** proteger reglas de negocio y controlar dependencias.

**Se solicita:**

- Modelo de dominio (entidades, objetos de valor, invariantes).
- Casos de uso principales y contratos de aplicación.
- Definición de puertos, límites y reglas de dependencia.
- Propuesta de estructura del código alineada con arquitectura limpia.

**Evidencias en GitHub:**

- Carpeta `/src` organizada por dominio y aplicación.
- Documento de decisiones de diseño y dependencias.
- Diagramas de componentes/capas actualizados.

**Video de sustentación (8 a 12 minutos):**

- Recorrido del dominio y justificación de límites.
- Explicación de cómo se evita el acoplamiento innecesario.

### Actividad 4 (25%): Implementación e integración

**Propósito:** conectar infraestructura sin contaminar el dominio.

**Se solicita:**

- Implementación de un vertical slice funcional (entrada, caso de uso, dominio, persistencia/integración).
- API o interfaz de entrada operativa.
- Adaptador de persistencia o integración externa con manejo básico de errores.
- Evidencia de trazabilidad entre diseño e implementación.

**Evidencias en GitHub:**

- Código fuente ejecutable y documentado.
- Instrucciones de ejecución en README.
- Evidencias de pruebas de integración o pruebas manuales guiadas.

**Video de sustentación (8 a 12 minutos):**

- Demo funcional del flujo implementado.
- Explicación de decisiones técnicas en infraestructura y límites.

### Actividad 5 (15%): Pruebas, operación y defensa final

**Propósito:** comprobar comportamiento y defender decisiones arquitectónicas.

**Se solicita:**

- Pruebas unitarias de reglas de dominio críticas.
- Pruebas de integración de al menos un flujo relevante.
- Riesgos operativos, observabilidad mínima y plan de evolución.
- Sustentación final del expediente arquitectónico.

**Evidencias en GitHub:**

- Suite de pruebas y resultados.
- Documento final del expediente de arquitectura evolutiva.
- Registro de riesgos, deuda técnica y siguientes pasos.

**Video de sustentación (10 a 15 minutos):**

- Presentación integral del expediente.
- Defensa de trade-offs ante escenarios de cambio.

## Hitos académicos

| Fecha | Hito | Entrega |
|---|---|---|
| 30 ago | Hito 1: entender el problema | Contexto, actores, requisitos iniciales y riesgos |
| 11 oct | Hito 2: decidir la estructura | Alternativas, costos y estilo elegido |
| 01 nov | Corte institucional del 60% | Evidencias de diagnóstico, requisitos y estructura |
| 18 nov | Hito 3: construir la solución | Dominio, casos de uso, API e infraestructura |
| 22 nov | Preentrega | Expediente, pruebas y revisión entre pares |
| 23-29 nov | Evaluación final | Sustentación y defensa técnica |
| 29 nov | Cierre institucional | Registro del 100% |

## Proyecto integrador

**Reto:** tomar un producto digital pequeño, diseñar una arquitectura proporcional y construir un vertical slice que atraviese la entrada, el caso de uso, el dominio, la persistencia o integración y las pruebas.

La solución puede desarrollarse en Java o C#. Se calificará el razonamiento y la calidad de los límites, no la cantidad de frameworks utilizados.

## Nota de diseño curricular

Los cursos de referencia aportan temas y tiempos audiovisuales. Esta ruta no los reproduce como contenido literal: los reorganiza en una progresión única, agrega clases de conexión y crea un proyecto acumulativo para que cada concepto se pruebe dentro de una decisión real.
