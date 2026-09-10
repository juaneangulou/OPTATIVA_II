# Video 04.1: Actividad 1: diagnóstico y contexto arquitectónico

## 📚 Fuentes relacionadas
- [Arquitectura como responsabilidad humana](https://platzi.com/cursos/fundamentos-arquitectura-software/espacio-de-problema-vs-solucion-en-arqui/)
- [Escalabilidad, seguridad y ética](https://platzi.com/cursos/fundamentos-arquitectura-software/requisitos-funcionales-y-no-funcionales/)

## 🔗 Navegación
[⬅️ Video anterior](video-04.md) | [➡️ Video siguiente](video-05.md)

## Propósito de esta actividad
Esta clase independiente sirve para comprender el problema antes de elegir tecnologías. Aquí no agregamos teoría nueva por acumular contenido: convertimos los videos del bloque anterior en una entrega concreta del proyecto.

## Caso obligatorio
una tormenta obliga a reasignar 400 entregas mientras operaciones solicita ubicación GPS amplia y acceso para todos los supervisores.

## Qué debes resolver

1. Define el problema sin empezar por una tecnología.
2. Identifica actores, necesidades y restricciones.
3. Delimita qué está dentro y fuera del sistema.
4. Propón al menos dos alternativas.
5. Compara costos, riesgos, calidad y facilidad de cambio.
6. Elige una opción y declara el trade-off.
7. Define cómo comprobarás que la decisión funciona.

## Entregables
README con resumen ejecutivo, definición del problema, actores, alcance, restricciones, riesgos, diagrama de contexto y decisiones iniciales.

Todos los entregables deben quedar en GitHub con commits que muestren evolución y con un video de explicación y sustentación.

## Resolución modelo
Elegimos un módulo de reasignación dentro de un monolito modular, protegemos la ubicación por roles, registramos auditoría y dejamos fuera la separación en microservicios hasta tener evidencia de volumen y operación.

La solución no se evalúa por usar la tecnología más compleja. Se evalúa por comprender el problema, justificar la decisión y dejar evidencia verificable.

## Guion para la sustentación

1. Presenta el problema y explica por qué importa.
2. Identifica los actores afectados.
3. Muestra las alternativas consideradas.
4. Defiende la alternativa elegida.
5. Explica qué costo aceptaste.
6. Muestra la evidencia y la condición que obligaría a revisar la decisión.

## Criterio de cierre
La actividad está completa cuando una persona externa puede entender qué problema resolviste, por qué elegiste esa arquitectura y cómo sabrás si la decisión sigue siendo válida.
