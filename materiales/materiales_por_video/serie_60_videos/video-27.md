# Video 27: Acoplamiento, cohesión y calidad estructural

## Título
Acoplamiento, cohesión y calidad estructural

## Resumen
Este video estudia acoplamiento, cohesión y calidad estructural con el objetivo de organizar responsabilidades y dependencias para que el sistema pueda crecer sin propagar cambios. El tema se conecta con el proyecto de la plataforma logística porque pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. La discusión no se limita a nombrar un patrón o una herramienta: exige identificar el problema, establecer criterios y anticipar las consecuencias de la decisión.

En la práctica, el equipo debe explicar qué cambia en el diseño, qué costo introduce y cómo comprobará que la solución funciona. Una decisión útil es la que puede comunicarse, implementarse gradualmente y revisarse cuando aparezca nueva evidencia.

## Ideas principales
- Una frontera útil define responsabilidad, contrato y propietario.
- La estructura elegida debe ser proporcional al tamaño del equipo y al riesgo operativo.
- La dirección de las dependencias protege las reglas importantes frente a detalles externos.
- El ejemplo debe documentarse junto con sus supuestos, trade-offs y evidencia de validación.

## Ejemplo en C#
```csharp
public interface IOrderRepository
{
    Task SaveAsync(Order order);
}
```

La aplicación depende de una abstracción y la infraestructura implementa el adaptador.

## Conclusión
Acoplamiento, cohesión y calidad estructural aporta una forma concreta de trabajar sobre la arquitectura del sistema. Su valor aparece cuando conecta el contexto del negocio con una estructura implementable, medible y capaz de evolucionar. Para el caso logístico, la decisión debe dejar claro qué comportamiento se protege, qué dependencias se aceptan y cómo se responderá ante cambios o fallos.

## Preguntas para reflexión
- ¿Qué responsabilidad pertenece realmente a cada módulo?
- ¿Qué dependencia sería más costosa de cambiar?
- ¿La estructura propuesta resuelve un problema real o agrega complejidad?
