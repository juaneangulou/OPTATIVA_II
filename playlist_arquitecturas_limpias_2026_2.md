# Curso de Arquitecturas Limpias para Desarrollo de Software

## Ruta intermedia de diseño, dominio y testing

**Periodo:** 4 de agosto al 29 de noviembre de 2026  
**Nivel:** Intermedio  
**Clases:** 24  
**Contenido audiovisual de referencia:** aproximadamente 3 horas  
**Práctica guiada:** 12 horas, 30 minutos por clase  
**Tecnologías de aplicación:** Java o C#

Esta ruta complementa el curso de Fundamentos de Arquitectura de Software. El foco cambia de elegir un estilo arquitectónico a proteger el dominio, controlar dependencias, diseñar casos de uso, integrar infraestructura y comprobar el comportamiento mediante pruebas.

## Resultados de aprendizaje

Al finalizar el curso, el estudiante podrá:

1. Explicar los límites de MVC y de una arquitectura tradicional de tres capas.
2. Comparar Clean Architecture, Hexagonal Architecture y Onion Architecture.
3. Modelar entidades, reglas de negocio y casos de uso sin depender de frameworks.
4. Aplicar inversión de dependencias, puertos, adaptadores y repositorios.
5. Diseñar APIs, integraciones y operaciones CQRS con límites claros.
6. Construir una estrategia de pruebas unitarias, de integración y de aceptación.
7. Evaluar los costos y riesgos de aplicar arquitectura limpia en un proyecto real.

## Ruta de aprendizaje

| # | Fecha | Unidad | Clase | Video | Producto de la sesión |
|---:|---|---|---|---:|---|
| 1 | 04 ago | Introducción | Qué es una arquitectura limpia y qué problema resuelve | 02:02 | Diagnóstico de dependencias del proyecto |
| 2 | 07 ago | Fundamentos | Límites de MVC y de la arquitectura de tres capas | 04:07 | Mapa de acoplamientos actuales |
| 3 | 11 ago | Fundamentos | Características que hacen limpia una arquitectura | 07:31 | Criterios de evaluación arquitectónica |
| 4 | 14 ago | Fundamentos | Cuándo usar y cuándo evitar Clean Architecture | 04:54 | Decisión de adopción con trade-offs |
| 5 | 18 ago | Fundamentos | SOLID aplicado a arquitecturas limpias | 08:53 | Refactor de una responsabilidad mezclada |
| 6 | 21 ago | Referencias | Arquitectura hexagonal: puertos y adaptadores | 06:59 | Diagrama de puertos y adaptadores |
| 7 | 25 ago | Referencias | Arquitectura Onion: dependencias hacia el centro | 05:08 | Comparación Hexagonal versus Onion |
| 8 | 28 ago | Referencias | Desglose de capas en Clean Architecture | 03:20 | Diagrama de capas y reglas de dependencia |
| 9 | 01 sep | Referencias | Clean Architecture en productos pequeños y grandes | 10:06 | Análisis de escala y contexto |
| 10 | 04 sep | Referencias | Adaptar la arquitectura al proyecto existente | 03:59 | Plan de migración incremental |
| 11 | 08 sep | Dominio | Errores que rompen el encapsulamiento | 08:36 | Reglas de invariantes del dominio |
| 12 | 11 sep | Dominio | Transaction Script: cuándo conviene y sus límites | 08:25 | Comparación con modelo de dominio |
| 13 | 15 sep | Dominio | Inyección de dependencias e inversión de control | 07:40 | Composición de dependencias |
| 14 | 18 sep | Dominio | Modelo de dominio en programación orientada a objetos | 06:43 | Entidades, objetos de valor y servicios |
| 15 | 22 sep | Aplicación | Capa de servicios y patrón Fachada | 04:19 | Servicio de aplicación con contrato claro |
| 16 | 25 sep | Aplicación | Casos de uso como entrada al sistema | 07:08 | Caso de uso implementado y documentado |
| 17 | 29 sep | Aplicación | CQRS: separar comandos y consultas | 11:59 | Flujo CQRS con criterios de separación |
| 18 | 02 oct | Infraestructura | Acceso a datos sin contaminar el dominio | 06:03 | Puerto de persistencia y adaptador |
| 19 | 06 oct | Infraestructura | Repository: abstraer datos sin ocultar problemas | 08:17 | Repositorio con contrato verificable |
| 20 | 09 oct | Infraestructura | API REST dentro de una arquitectura limpia | 05:27 | Endpoint conectado a un caso de uso |
| 21 | 13 oct | Infraestructura | Integraciones y patrón Adapter | 09:06 | Adaptador para un servicio externo |
| 22 | 16 oct | Calidad | Pruebas unitarias de reglas de negocio | 05:38 | Suite de pruebas del dominio |
| 23 | 20 oct | Calidad | Mocks, stubs y pruebas de integración | 09:26 | Pirámide de pruebas y dobles de prueba |
| 24 | 23 oct | Cierre | Desafíos reales al aplicar arquitectura limpia | 04:27 | Sustentación del proyecto y lecciones aprendidas |

## Contenido didáctico por clase

### Unidad 1. Introducción y fundamentos

**1. Qué es una arquitectura limpia y qué problema resuelve**  
Se presenta la separación entre reglas de negocio y detalles externos. El estudiante identifica qué partes de su proyecto deberían sobrevivir aunque cambien la base de datos, la interfaz o el framework.

**2. Límites de MVC y de la arquitectura de tres capas**  
Se analizan los casos en que una estructura convencional deja de controlar el acoplamiento. La práctica dibuja las dependencias reales de un proyecto y ubica sus puntos de fragilidad.

**3. Características que hacen limpia una arquitectura**  
Se trabajan independencia del dominio, testabilidad, dirección de dependencias y separación de responsabilidades. El producto es una lista de criterios verificables para revisar una solución.

**4. Cuándo usar y cuándo evitar Clean Architecture**  
Se estudia el costo de agregar capas, abstracciones y ceremonias. El estudiante redacta una decisión de arquitectura que justifica adoptar, simplificar o posponer el enfoque.

**5. SOLID aplicado a arquitecturas limpias**  
Se conectan SOLID, cohesión y acoplamiento mediante un ejemplo práctico. La actividad refactoriza una clase o módulo que concentra reglas, persistencia y presentación.

### Unidad 2. Arquitecturas de referencia

**6. Arquitectura hexagonal: puertos y adaptadores**  
Se distinguen puertos de entrada, puertos de salida y adaptadores concretos. El estudiante representa cómo el dominio se comunica con usuarios, bases de datos y servicios externos.

**7. Arquitectura Onion: dependencias hacia el centro**  
Se compara el modelo de anillos con el enfoque hexagonal. La práctica identifica qué dependencias pueden entrar a cada anillo y cuáles deben invertirse.

**8. Desglose de capas en Clean Architecture**  
Se organizan entidades, casos de uso, interfaces y frameworks sin convertir las capas en carpetas vacías. El estudiante define reglas explícitas para evitar dependencias incorrectas.

**9. Clean Architecture en productos pequeños y grandes**  
Se evalúa cómo cambia la decisión con el tamaño del equipo, la vida útil, el riesgo y la velocidad requerida. La evidencia compara dos escenarios y recomienda una variante proporcional.

**10. Adaptar la arquitectura al proyecto existente**  
Se trabaja la migración gradual en lugar de reescribir todo. El estudiante prioriza un módulo, define una frontera y prepara una secuencia de cambios reversibles.

### Unidad 3. Dominio y aplicación

**11. Errores que rompen el encapsulamiento**  
Se revisan setters indiscriminados, entidades anémicas, reglas fuera del dominio y modelos expuestos a infraestructura. La práctica formula invariantes y puntos únicos de validación.

**12. Transaction Script: cuándo conviene y sus límites**  
Se compara una operación procedural con un modelo de dominio rico. El estudiante elige el enfoque según complejidad, frecuencia de cambio y cantidad de reglas.

**13. Inyección de dependencias e inversión de control**  
Se explica cómo componer objetos sin que el dominio conozca el contenedor. La actividad construye un grafo de dependencias y define su composición en el borde de la aplicación.

**14. Modelo de dominio en programación orientada a objetos**  
Se modelan entidades, objetos de valor, agregados y servicios de dominio. El producto es un modelo pequeño con reglas expresadas en el lenguaje del negocio.

**15. Capa de servicios y patrón Fachada**  
Se diferencia una fachada útil de un servicio que se convierte en un nuevo objeto gigante. El estudiante diseña una interfaz de aplicación que coordina sin absorber reglas del dominio.

**16. Casos de uso como entrada al sistema**  
Se organiza cada operación como una intención verificable del usuario o del negocio. La práctica documenta entradas, salidas, errores y transacción de un caso de uso.

**17. CQRS: separar comandos y consultas**  
Se estudia cuándo separar modelos de lectura y escritura y cuándo esa separación sería innecesaria. El estudiante diseña un flujo CQRS pequeño con sus riesgos de consistencia.

### Unidad 4. Infraestructura e integración

**18. Acceso a datos sin contaminar el dominio**  
Se ubican persistencia, mapeos y transacciones fuera de las reglas centrales. La actividad define un puerto de datos y un adaptador que puede sustituirse en pruebas.

**19. Repository: abstraer datos sin ocultar problemas**  
Se revisa qué debe expresar un repositorio y qué consultas no conviene esconder detrás de una interfaz genérica. El estudiante crea un contrato orientado al caso de uso.

**20. API REST dentro de una arquitectura limpia**  
Se conectan controlador, caso de uso, DTOs y respuestas HTTP. La evidencia incluye un endpoint con validación, manejo de errores y dependencias dirigidas hacia el dominio.

**21. Integraciones y patrón Adapter**  
Se modela un proveedor externo como detalle reemplazable. La práctica implementa un adaptador con timeout, traducción de errores y contrato probado.

### Unidad 5. Calidad y cierre

**22. Pruebas unitarias de reglas de negocio**  
Se priorizan pruebas rápidas y deterministas sobre entidades, objetos de valor y casos de uso. El estudiante construye una suite que protege las decisiones más importantes del dominio.

**23. Mocks, stubs y pruebas de integración**  
Se elige el doble de prueba según el objetivo y se evita probar la implementación en lugar del comportamiento. La actividad define una pirámide de pruebas y sus límites.

**24. Desafíos reales al aplicar arquitectura limpia**  
Se revisan sobreingeniería, resistencia del equipo, costo de migración, rendimiento y mantenimiento. La sustentación final defiende la arquitectura, sus compromisos y el siguiente paso técnico.

## Entregas y fechas clave

| Fecha | Actividad | Evidencia |
|---|---|---|
| 30 ago | Cierre de fundamentos | Diagnóstico de dependencias y decisión de adopción |
| 06 sep | Cierre de arquitecturas de referencia | Diagrama de capas y plan de migración |
| 27 sep | Cierre de dominio y aplicación | Modelo de dominio y casos de uso |
| 18 oct | Cierre de infraestructura | API, persistencia e integración con adaptadores |
| 01 nov | Corte institucional del 60% | Evidencias de las unidades iniciales |
| 15 nov | Preentrega del proyecto | Arquitectura implementada y estrategia de pruebas |
| 23-29 nov | Evaluación final | Sustentación, pruebas y reflexión técnica |
| 29 nov | Cierre institucional | Registro del 100% |

## Proyecto integrador

El estudiante toma un módulo de un sistema existente o construye un caso de negocio pequeño y lo reorganiza con una arquitectura limpia proporcional. La entrega debe incluir:

- Diagnóstico del acoplamiento inicial.
- Diagrama de capas, puertos y adaptadores.
- Modelo de dominio con reglas e invariantes.
- Casos de uso con entradas, salidas y errores.
- Persistencia o integración externa aislada.
- Pruebas unitarias y de integración.
- Registro de decisiones, costos y limitaciones.

## Actividad práctica transversal

Cada sesión aporta una parte del mismo proyecto. La práctica acumulada equivale a 12 horas y se evalúa por la calidad del diseño, la dirección de dependencias, la protección del dominio, la claridad de las pruebas y la capacidad de explicar qué complejidad se decidió no introducir.

## Enlaces de referencia

Los tiempos y temas audiovisuales se basan en la playlist proporcionada por el estudiante. El material original está disponible en el [curso de Arquitecturas Limpias para Desarrollo de Software de Platzi](https://platzi.com/cursos/arquitecturas-limpias/). Esta propuesta agrega prácticas, productos y evaluación para convertir la referencia en una ruta académica aplicada.
