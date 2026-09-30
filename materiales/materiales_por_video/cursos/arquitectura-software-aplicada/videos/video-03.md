# Video 3: Monorepos con Pantsbuild en proyectos reales

## Para estudiar por tu cuenta
Cuando un producto tiene varios servicios, cada equipo podría guardarlos en repositorios distintos o mantenerlos juntos. Un **monorepo** es un repositorio que contiene varios proyectos relacionados. Pantsbuild es una herramienta que ayuda a describir, construir y probar proyectos dentro de un repositorio grande.

En esta clase aprenderás qué problema resuelve cada idea y por qué usar un monorepo no obliga a desplegar todos los servicios juntos.

## 1. El ejemplo de la plataforma logística
El sistema tiene Pedidos, Entregas y una biblioteca compartida que valida direcciones.

```text
plataforma-logistica/
	servicios/pedidos/
	servicios/entregas/
	bibliotecas/direcciones/
```

Este árbol es una posible organización, no una estructura obligatoria. Los servicios pueden construirse y publicarse por separado aunque estén guardados en el mismo repositorio.

## 2. Qué problema aparece al crecer
Una persona cambia la biblioteca de direcciones. Pedidos sigue funcionando, pero Entregas esperaba un resultado diferente. Si solo se prueban los archivos de la biblioteca, el error puede descubrirse cuando la entrega ya está en uso.

Un monorepo permite revisar en una propuesta el cambio compartido y sus consumidores. También requiere reglas para saber qué proyectos dependen de cada componente y qué pruebas ejecutar.

## 3. Pantsbuild explicado
Una herramienta de **build** coordina tareas como compilar, probar y empaquetar proyectos.

Pantsbuild usa archivos de configuración, como `BUILD`, para describir objetivos y dependencias. Un **target** es una tarea identificable, por ejemplo, “construir el servicio de Pedidos” o “ejecutar sus pruebas”. La configuración exacta depende de la versión y del proyecto; no copies un ejemplo sin verificarlo.

Con dependencias descritas, la herramienta puede ayudar a identificar qué trabajos deben repetirse cuando cambia una biblioteca. Esto evita que cada persona mantenga una lista manual diferente.

## 4. Del cambio a las pruebas
Si cambias la validación de direcciones:

1. Identifica qué proyectos usan la biblioteca.
2. Ejecuta las pruebas de la biblioteca.
3. Ejecuta las pruebas de Pedidos y Entregas que dependen del cambio.
4. Revisa los resultados antes de integrar.

La herramienta puede ayudar a elegir tareas afectadas, pero el equipo debe confirmar que las dependencias estén declaradas correctamente.

## 5. Cuándo considerar un monorepo
Puede ser útil si los proyectos cambian juntos, comparten bibliotecas o necesitan revisar cambios coordinados en una sola propuesta.

Varios repositorios pueden ser más convenientes cuando equipos y productos evolucionan de forma independiente. Pantsbuild no decide qué estructura organizacional conviene; ayuda a automatizar tareas una vez elegida.

## 6. Actividad de autoestudio
La biblioteca de direcciones cambió y la usan Pedidos y Entregas.

1. Dibuja los tres proyectos y sus dependencias.
2. Escribe qué pruebas ejecutarías.
3. Explica qué puede fallar si pruebas solo la biblioteca.
4. Nombra un beneficio y un costo de usar un monorepo.
5. Si el proyecto ya utiliza Pantsbuild, busca en su configuración qué target ejecuta las pruebas afectadas. No supongas que otro repositorio usa los mismos nombres.

### Respuesta modelo
Pedidos y Entregas dependen de la biblioteca de direcciones. Ejecutaría primero sus pruebas y después las de ambos consumidores. Probar solo la biblioteca no detecta si uno interpreta su respuesta de forma incompatible.

El monorepo facilita revisar el cambio compartido en un lugar, pero requiere organizar permisos, dependencias y pruebas. La decisión depende de cómo cambian los equipos y proyectos.

## Comprueba lo que aprendiste
1. ¿Un monorepo obliga a publicar todos los proyectos juntos?
2. ¿Qué describen los archivos `BUILD` en Pantsbuild?
3. ¿Pantsbuild decide si tu empresa necesita un monorepo?

**Respuestas:** no; describen objetivos de trabajo y dependencias; no, esa decisión depende del producto y de cómo trabaja el equipo.

## Conclusión
Un monorepo reúne proyectos relacionados. Pantsbuild ayuda a hacer explícitas sus dependencias y coordinar construcción y pruebas. La herramienta no sustituye el diseño de límites ni garantiza que una prueba omitida no rompa un consumidor.
