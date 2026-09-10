# Video 12.1: Actividad 3: diseño y dominio

## 📚 Fuentes relacionadas
- [Estrategia tecnológica y roadmap](https://platzi.com/cursos/fundamentos-arquitectura-software/evolucionar-un-mvp-sin-rearquitectar-des/)
- [Arquitectura con impacto social y ético](https://platzi.com/cursos/software-avanzado/observabilidad-en-sistemas-con-opentelem/)

## 🔗 Navegación
[⬅️ Video anterior](video-12.md) | [➡️ Video siguiente](video-13.md)

## Propósito de esta actividad
Esta clase independiente sirve para proteger reglas del negocio mediante entidades, límites y casos de uso. Aquí no agregamos teoría nueva por acumular contenido: convertimos los videos del bloque anterior en una entrega concreta del proyecto.

## Caso obligatorio
Pedidos, Inventario, Ruteo y Entregas usan conceptos parecidos como disponibilidad, pero cada contexto tiene una regla distinta.

## Qué debes resolver

1. Define el problema sin empezar por una tecnología.
2. Identifica actores, necesidades y restricciones.
3. Delimita qué está dentro y fuera del sistema.
4. Propón al menos dos alternativas.
5. Compara costos, riesgos, calidad y facilidad de cambio.
6. Elige una opción y declara el trade-off.
7. Define cómo comprobarás que la decisión funciona.

## Entregables
modelo de dominio, entidades, objetos de valor, invariantes, casos de uso, puertos, adaptadores y decisiones de diseño.

Todos los entregables deben quedar en GitHub con commits que muestren evolución y con un video de explicación y sustentación.

## Resolución modelo
Separamos los contextos y protegemos sus reglas con modelos propios; el caso de uso coordina contratos y no modifica directamente infraestructura ni entidades ajenas.

## 🧾 Ejemplo de entrega resuelta

### Problema de dominio
La palabra “disponible” significa stock para Inventario, ruta viable para Ruteo y repartidor asignable para Entregas.

### Límites
Pedidos confirma la compra; Inventario reserva unidades; Ruteo calcula viabilidad; Entregas asigna una persona.

### Decisión
Usar un monolito modular con modelos separados y contratos entre contextos. No compartir una entidad `Order` gigante ni acceder directamente a tablas ajenas.

### Invariante
Una entrega no puede tener dos repartidores activos al mismo tiempo.

### Evidencia
Mapa de contextos, entidades, objeto de valor `RouteEstimate`, interfaces de puertos y prueba de la invariante.


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
