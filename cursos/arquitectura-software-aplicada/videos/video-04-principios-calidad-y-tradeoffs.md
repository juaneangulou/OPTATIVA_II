# Video 4: Trunk Based Development con rulesets en GitHub

## Título
Trunk Based Development con rulesets en GitHub

## Resumen
Trunk Based Development busca integrar cambios pequeños y frecuentes en la rama principal. El equipo puede usar ramas breves para trabajar, probar los cambios y volver a integrarlos pronto. En GitHub, los rulesets establecen protecciones, como exigir revisiones y pruebas antes de aceptar cambios.

La práctica reduce ramas que se separan durante mucho tiempo, pero no garantiza por sí sola que el código sea correcto. Las pruebas, la revisión y una forma de desactivar una función incompleta completan el proceso.

## Ideas principales
- Una rama corta reduce el tiempo durante el cual los cambios divergen.
- `main` debe protegerse con reglas acordes al proyecto.
- Las pruebas automáticas pueden impedir integrar cambios que rompen comportamientos importantes.
- Un feature flag puede mantener oculta una función que aún no está lista.
- Los rulesets controlan el flujo de integración, no garantizan la calidad total.

## Preguntas para pensar
- ¿Qué riesgo aparece cuando una rama permanece semanas sin integrarse?
- ¿Qué pruebas deberían ser obligatorias antes de modificar `main`?
- ¿Cómo integrarías código que aún no quieres mostrar a los clientes?
