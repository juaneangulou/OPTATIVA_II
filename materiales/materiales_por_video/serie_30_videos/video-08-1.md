# Video 08.1: Actividad 2: requisitos y decisión estructural

## 📚 Fuentes relacionadas
- [APIs y contratos de integración](https://platzi.com/cursos/fundamentos-arquitectura-software/que-son-las-arquitecturas-monoliticas-y/)
- [Infraestructura, despliegue y entorno de ejecución](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitecturas-orientadas-a-servicios-con/)

## 🔗 Navegación
[⬅️ Video anterior](video-08.md) | [➡️ Video siguiente](video-09.md)

## Propósito de esta actividad
Esta clase independiente sirve para convertir necesidades del negocio en criterios arquitectónicos y comparar alternativas. Aquí no agregamos teoría nueva por acumular contenido: convertimos los videos del bloque anterior en una entrega concreta del proyecto.

## Caso obligatorio
la aplicación móvil necesita crear pedidos sin romperse cuando se agrega una ventana de entrega y el sistema debe soportar picos de campaña.

## Qué debes resolver

1. Define el problema sin empezar por una tecnología.
2. Identifica actores, necesidades y restricciones.
3. Delimita qué está dentro y fuera del sistema.
4. Propón al menos dos alternativas.
5. Compara costos, riesgos, calidad y facilidad de cambio.
6. Elige una opción y declara el trade-off.
7. Define cómo comprobarás que la decisión funciona.

## Entregables
requisitos priorizados, escenarios de calidad, matriz de alternativas, ADR estructural, trade-offs y criterios de revisión.

Todos los entregables deben quedar en GitHub con commits que muestren evolución y con un video de explicación y sustentación.

## Resolución modelo
Elegimos un monolito modular con contratos HTTP versionados, adaptadores de infraestructura y métricas de latencia; dejamos la extracción de Ruteo como decisión condicionada por evidencia.

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
