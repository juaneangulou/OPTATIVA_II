# Video 12: Cómo el pre-mortem guía tus tests de arquitectura

## Título
Cómo el pre-mortem guía tus pruebas de arquitectura

## Resumen
Un riesgo anticipado es más útil cuando se convierte en una prueba concreta. Este video conecta el pre-mortem con las comprobaciones del sistema: describe qué podría fallar, qué comportamiento debe protegerse y qué resultado permitiría detectarlo.

Por ejemplo, si se teme que un mensaje repetido cree dos entregas, la prueba puede enviar dos veces la misma solicitud y comprobar que solo exista una asignación activa. Así el análisis de riesgos deja de ser una lista y se convierte en evidencia verificable.

## Ideas principales
- Un escenario de pre-mortem debe producir una pregunta comprobable.
- Una prueba describe contexto, acción y resultado esperado.
- El nivel de prueba depende del riesgo: unitario, integración o arquitectura.
- Verifica tanto lo que debe ocurrir como lo que no debe ocurrir.
- Guarda el resultado y vuelve a probar cuando cambie el flujo protegido.

## Preguntas para pensar
- ¿Qué prueba detectaría una asignación duplicada?
- ¿Qué dato o resultado demostraría que la regla se cumplió?
- ¿Cómo distinguirías una prueba de una suposición sobre el sistema?
