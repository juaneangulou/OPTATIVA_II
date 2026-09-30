# Video 16: Monorepos, trunk-based development y calidad

## Fuentes de este video
- [Monorepos con Pantsbuild en proyectos reales](https://platzi.com/cursos/software-avanzado/monorepos-con-pantsbuild-en-proyectos-re/)
- [Trunk Based Development con rulesets en GitHub](https://platzi.com/cursos/software-avanzado/trunk-based-development-con-rulesets-en/)

## Para estudiar por tu cuenta
En este capítulo vas a combinar dos decisiones de trabajo: cómo guardar varios proyectos relacionados en un repositorio y cómo integrar sus cambios con frecuencia sin dejar desprotegida la rama principal.

Usaremos Pedidos, Entregas y una biblioteca compartida para direcciones. El objetivo es seguir un cambio pequeño desde que se edita hasta que se integra con pruebas.

## 1. Monorepo: varios proyectos en un solo repositorio
Un **repositorio** guarda archivos y el historial de cambios. Un **monorepo** contiene varios proyectos relacionados en el mismo repositorio.

```text
plataforma/
  servicios/pedidos/
  servicios/entregas/
  bibliotecas/direcciones/
```

Los proyectos pueden seguir compilándose y desplegándose por separado. Compartir repositorio no significa compartir una base de datos, ejecutar todo en un solo proceso ni publicar todos los servicios al mismo tiempo.

Un monorepo puede ayudar cuando un cambio tiene que actualizar un servicio y una biblioteca en la misma revisión. También exige reglas claras para dependencias, pruebas y permisos.

## 2. Qué aporta Pantsbuild
Pantsbuild es una herramienta para describir proyectos, sus dependencias y las tareas de construcción o prueba que se pueden ejecutar sobre ellos.

Un **target** es una unidad nombrada de trabajo, como construir la biblioteca de direcciones o probar el servicio de Pedidos. Los archivos de configuración, por ejemplo `BUILD`, describen targets y relaciones.

Si Entregas depende de Direcciones, esa relación debe aparecer en la configuración. Así Pantsbuild puede ayudar a identificar qué tareas probar cuando cambia la biblioteca. La herramienta no adivina dependencias que el equipo no declaró.

Un comando ilustrativo podría ser:

```text
./pants test servicios/pedidos::
```

El significado de `::`, la ruta y las opciones dependen de la configuración de Pants del proyecto. Antes de usar un comando, revisa el `README` y la versión configurada; no lo copies a ciegas en un repositorio distinto.

## 3. Trunk Based Development: integrar cambios pequeños
La rama principal suele llamarse `main`. En Trunk Based Development, las personas integran cambios pequeños a esa rama con frecuencia.

Se pueden usar ramas de trabajo, pero se mantienen cortas. Una rama que vive semanas se aleja de `main` y puede acumular diferencias difíciles de combinar.

Una **integración continua** ejecuta comprobaciones cada vez que se propone o integra un cambio. Por ejemplo: compilar, ejecutar pruebas y revisar reglas de arquitectura.

## 4. Qué son los rulesets de GitHub
Un **ruleset** configura condiciones para proteger una rama. En `main`, podrías exigir que los cambios lleguen por Pull Request, que pasen ciertas pruebas o que alguien revise la modificación.

Estas reglas protegen el proceso, no certifican que el diseño sea correcto. Si una prueba no verifica nada útil, que aparezca como “verde” no protege el sistema.

Un **feature flag** es un interruptor que permite mantener desactivada una función aunque su código ya esté integrado. Sirve si la funcionalidad todavía no está lista para mostrarse, pero no elimina la necesidad de probarla ni de retirar el flag cuando ya no haga falta.

## 5. Cambio guiado: ajustar la dirección de entrega
La biblioteca de direcciones necesita distinguir entre dirección escrita y dirección confirmada. Pedidos y Entregas usan esta biblioteca.

### Paso 1: delimita el cambio
Decide qué campo cambia y qué compatibilidad necesitan sus consumidores. No modifiques contratos de tres proyectos si la necesidad solo afecta a uno.

### Paso 2: actualiza dependencias y pruebas
Pants debe conocer qué proyectos consumen la biblioteca. Añade o ajusta pruebas de la biblioteca, Pedidos y Entregas para que el cambio no pase inadvertido.

### Paso 3: prepara una rama corta
Actualiza tu rama con `main`, crea una rama de trabajo para este cambio y evita acumular funcionalidades distintas en la misma propuesta.

### Paso 4: ejecuta tareas relevantes
Ejecuta las pruebas de los proyectos afectados y revisa el cambio completo. En un repositorio Pants, usa los targets y comandos definidos por ese mismo repositorio.

### Paso 5: abre una Pull Request
Explica qué problema resuelve el cambio, qué proyectos afecta y qué pruebas ejecutaste. Una persona revisa la propuesta y GitHub aplica las reglas configuradas.

### Paso 6: integra y limpia
Cuando las comprobaciones y la revisión pasan, integra el cambio y elimina la rama corta. Si la función no debe estar visible todavía, controla su activación con una configuración o feature flag documentado.

## 6. Qué no debes confundir
- **Monorepo** responde dónde se guardan varios proyectos.
- **Pantsbuild** ayuda a declarar relaciones y ejecutar tareas.
- **Trunk Based Development** describe cómo integrar cambios.
- **Rulesets** establecen protecciones para la rama.

Puedes tener monorepo sin Pantsbuild, y puedes trabajar con ramas cortas sin monorepo. Son herramientas y prácticas que se pueden combinar si responden a una necesidad real.

## 7. Costos y decisiones
| Decisión | Beneficio posible | Costo o riesgo |
|---|---|---|
| Monorepo | Revisar juntos cambios coordinados | Repositorio grande y reglas de permisos más cuidadosas |
| Pantsbuild | Tareas y dependencias explícitas | Configuración que el equipo debe aprender y mantener |
| Ramas cortas | Detectar conflictos y fallos pronto | Requiere mantener cambios pequeños y probar a menudo |
| Rulesets | Evitar integraciones sin revisión o pruebas | Puede bloquear trabajo si exige comprobaciones mal definidas |

No apliques todas las opciones por moda. Primero identifica el problema: por ejemplo, “no sabemos qué pruebas ejecutar cuando cambia la biblioteca compartida”. Luego decide si Pantsbuild aporta valor para esa escala.

## 8. Actividad de autoestudio
Una modificación de la biblioteca `Direcciones` cambia cómo se valida el código postal. La usan Pedidos y Entregas.

1. Dibuja los tres proyectos y sus dependencias.
2. Anota qué pruebas correrías y por qué.
3. Escribe los pasos que seguirías desde la rama de trabajo hasta `main`.
4. Propón dos reglas para proteger `main`.
5. Explica qué puede salir mal si la rama permanece sin integrar durante tres semanas.
6. Decide si necesitas Pantsbuild para este repositorio; explica qué información te falta.

### Pistas
- Una biblioteca compartida puede romper un consumidor aunque sus propias pruebas pasen.
- Una regla de GitHub es útil solo si corresponde a una comprobación importante.
- Un monorepo pequeño no necesita automáticamente una herramienta de construcción avanzada.

## 9. Respuesta modelo
Pedidos y Entregas dependen de `Direcciones`. Ejecutaría pruebas de la biblioteca y de los dos consumidores, porque ambos pueden interpretar la validación de manera distinta.

Trabajaría en una rama corta, abriría una Pull Request con la explicación y resultados, esperaría las pruebas exigidas y una revisión, integraría y eliminaría la rama. Rulesets razonables podrían impedir el borrado de `main` y exigir las pruebas de los consumidores antes de integrar.

Tres semanas sin integrar aumentan la posibilidad de conflictos, incompatibilidades y errores tardíos. Pantsbuild podría servir si el número de proyectos o el costo de ejecutar pruebas completas crece; primero habría que conocer la escala del repositorio y sus tiempos de construcción.

## Comprueba lo que aprendiste
1. ¿Un monorepo implica desplegar todos los proyectos juntos?
2. ¿Qué tarea automatiza Pantsbuild y qué debe declarar el equipo?
3. ¿Trunk Based Development prohíbe ramas de trabajo?
4. ¿Qué garantiza un ruleset?

### Respuestas
1. No; los proyectos pueden desplegarse por separado.
2. Ayuda a construir y probar targets; el equipo debe declarar proyectos y dependencias.
3. No; permite ramas breves que se integran con frecuencia.
4. Que se siguen las condiciones configuradas, no que el código sea correcto en todos los sentidos.

## Conclusión
Un monorepo puede facilitar cambios coordinados; Pantsbuild puede ayudar a ejecutar pruebas de los proyectos afectados; Trunk Based Development busca integrar cambios pequeños; GitHub rulesets protege el flujo. Cada decisión tiene costos y debe responder a una dificultad real del equipo.