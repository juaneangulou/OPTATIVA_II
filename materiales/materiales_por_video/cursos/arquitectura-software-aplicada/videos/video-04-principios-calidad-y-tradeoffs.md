# Video 4: Trunk Based Development con rulesets en GitHub

## Para estudiar por tu cuenta
Este video explica cómo integrar cambios pequeños y frecuentes en una rama principal compartida, y cómo usar reglas de GitHub para protegerla. La meta no es prohibir todo trabajo en ramas: es evitar que las diferencias permanezcan aisladas durante semanas y aparezcan conflictos grandes al integrarlas.

## 1. ¿Qué es una rama?
Una **rama** es una línea de trabajo dentro del historial de Git. Permite cambiar archivos sin modificar inmediatamente la línea principal del proyecto.

La rama principal suele llamarse `main`. En **Trunk Based Development**, el equipo integra cambios pequeños a esa rama con frecuencia. Si se usan ramas de trabajo, deben ser de vida corta y volver a `main` pronto.

## 2. El problema de las ramas largas
Imagina que una persona trabaja dos semanas en la nueva pantalla de seguimiento y otra cambia durante ese tiempo el contrato del pedido. Cuando intentan unir sus cambios, puede ser difícil combinar los archivos y descubrir errores.

La **integración** es unir cambios de distintas personas en la línea principal. Integrar más seguido permite detectar conflictos cuando todavía son pequeños.

## 3. Flujo sencillo
1. Actualiza tu copia con los cambios recientes de `main`.
2. Crea una rama corta para una tarea pequeña.
3. Haz un cambio que pueda revisarse con claridad.
4. Ejecuta las pruebas relevantes.
5. Abre una solicitud de cambios (Pull Request) hacia `main`.
6. Atiende la revisión y espera las comprobaciones automáticas requeridas.
7. Integra el cambio y elimina la rama de trabajo.

También hay equipos que integran directamente en `main` con revisiones y pruebas automáticas. El flujo concreto depende del tamaño y las reglas del equipo; lo importante es integrar con frecuencia y proteger la rama principal.

## 4. ¿Qué es un ruleset?
Un **ruleset** es un conjunto de reglas configuradas en GitHub para controlar qué cambios pueden entrar a una rama. Por ejemplo, puede exigir una revisión, impedir borrar `main` o requerir que ciertas pruebas terminen correctamente.

En la plataforma logística, `main` podría exigir:

- una Pull Request en vez de cambios sin revisión;
- que las pruebas de pedidos pasen;
- una aprobación antes de integrar;
- impedir que se borre o reescriba el historial principal.

Un ruleset protege el procedimiento. No demuestra que las pruebas sean suficientes ni que el cambio sea correcto.

## 5. ¿Qué pasa si una función aún no está lista?
Una rama corta no significa que una función incompleta deba ser visible para todos. Un **feature flag** (interruptor de funcionalidad) permite integrar el código, pero mantener la función desactivada hasta que esté lista.

Ejemplo: el cálculo nuevo de rutas puede integrarse y probarse en el entorno de ensayo mientras permanece apagado para clientes. Los flags también necesitan limpieza; dejar interruptores antiguos para siempre hace más difícil entender el sistema.

## 6. Ejercicio de autoestudio
Una mejora del seguimiento requiere cambiar la API y la pantalla. Una persona planea trabajar sola durante tres semanas en una rama.

1. Explica dos riesgos de esperar tres semanas para integrar.
2. Divide el trabajo en dos o tres cambios pequeños.
3. Escribe dos comprobaciones que exigirías antes de integrar a `main`.
4. Si la pantalla no debe aparecer aún al cliente, ¿cómo podrías integrar el código sin activarla?

### Respuesta modelo
La rama larga puede separarse de `main` y acumular conflictos; además, los errores se descubrirían tarde. Podría integrar primero el contrato de respuesta, luego el manejo de datos en la pantalla y después la presentación, siempre que cada paso mantenga las pruebas funcionando.

El ruleset podría exigir revisión y pruebas automatizadas. Un feature flag puede mantener apagada la pantalla nueva hasta que el flujo esté listo.

## Comprueba lo que aprendiste
1. ¿Trunk Based Development prohíbe absolutamente las ramas?
2. ¿Qué controla un ruleset y qué no puede garantizar?
3. ¿Para qué sirve un feature flag durante una entrega gradual?

**Respuestas:** no, permite ramas cortas; el ruleset controla requisitos para integrar, pero no garantiza que el cambio sea correcto; un feature flag puede dejar integrado el código y controlar cuándo se habilita la función.

## Conclusión
Trunk Based Development busca que los cambios lleguen a la rama principal con frecuencia y sin acumulaciones grandes. Los rulesets establecen protecciones para integrar con más seguridad; las pruebas, revisiones y flags completan el flujo según la necesidad.
