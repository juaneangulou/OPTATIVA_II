# Video 12: Estrategia tecnológica y roadmap

## 📚 Lecturas de referencia: decidir qué construir después
- [Estrategia tecnológica y roadmap](https://platzi.com/cursos/fundamentos-arquitectura-software/evolucionar-un-mvp-sin-rearquitectar-des/)
- [Estrategia tecnológica y roadmap](https://platzi.com/cursos/fundamentos-arquitectura-software/evolucionar-un-mvp-sin-rearquitectar-des/)

## 🔗 De riesgos aislados a una dirección tecnológica
[⬅️ Video anterior](video-11.md) | [➡️ Video siguiente](video-12-1.md)

## 🎯 La situación que vamos a ordenar
La plataforma logística tiene más solicitudes que capacidad: mejorar rutas, crear una aplicación para operadores, agregar otro proveedor de mapas, automatizar incidentes y construir reportes. Si todo se considera urgente, el equipo no tiene estrategia; solo reacciona.

Un roadmap arquitectónico no es una lista de deseos. Es una secuencia de decisiones vinculada a objetivos de negocio, riesgos y capacidad del equipo.

## Objetivo estratégico
Durante el próximo trimestre queremos reducir entregas tardías sin aumentar el costo operativo por pedido. Esa frase permite ordenar las iniciativas: una mejora que no ayuda a puntualidad, costo, confiabilidad o capacidad de aprendizaje no es prioritaria para este ciclo.

## Roadmap propuesto

### Horizonte 1: estabilizar el MVP
- Medir p95 de rutas y pedidos estancados.
- Crear contratos para Inventario, Ruteo y Entregas.
- Automatizar pruebas y despliegue.
- Definir logs, métricas y trazas mínimas.

**Salida:** sabemos dónde está el problema y podemos publicar cambios con control.

### Horizonte 2: mejorar la operación
- Probar una política de rutas con ventanas horarias.
- Agregar tablero de incidentes para operaciones.
- Reducir consultas innecesarias al proveedor de mapas.
- Definir retención de datos de ubicación.

**Salida:** mejoramos puntualidad sin distribuir componentes prematuramente.

### Horizonte 3: separar solo lo justificado
- Extraer Ruteo si las métricas muestran saturación independiente.
- Agregar un segundo proveedor mediante el mismo puerto.
- Versionar contratos externos.
- Preparar recuperación ante fallos del proveedor.

**Salida:** la inversión en distribución responde a evidencia, no a una moda.

## Cómo priorizar una iniciativa
Usa esta tabla antes de incluir trabajo en el roadmap:

| Iniciativa | Valor | Riesgo reducido | Esfuerzo | Decisión |
|---|---:|---:|---:|---|
| Medir p95 de Ruteo | Alto | Alto | Bajo | Primero |
| Reescribir toda la plataforma | Incierto | Alto | Muy alto | Esperar evidencia |
| Segundo proveedor de mapas | Medio | Alto | Medio | Experimento |
| Dashboard de incidentes | Alto | Medio | Medio | Segundo horizonte |

El roadmap debe permitir decir no. Si todo entra, nada está priorizado.

## Preguntas y respuestas
### ¿Qué dirección tecnológica está tomando el proyecto?

La dirección es evolucionar desde un monolito modular observable hacia separaciones selectivas. Primero medimos y automatizamos; después aislamos Ruteo solo si las métricas muestran que necesita autonomía.

### ¿Qué diferencia hay entre estrategia y lista de tareas?

Una tarea dice “crear un dashboard”. Una estrategia dice “reducir el tiempo de diagnóstico para disminuir entregas tardías”. El dashboard es una inversión solo si produce evidencia para ese objetivo.

### ¿Cómo sé qué dejar fuera del roadmap?

Deja fuera lo que no reduzca el riesgo prioritario, no tenga capacidad disponible o no pueda verificarse. No incluiría microservicios completos ni una reescritura hasta contar con métricas y un equipo capaz de operarlos.

## Actividad: construye el roadmap de la plataforma

1. Define un objetivo de negocio medible para los próximos tres meses.
2. Lista diez iniciativas tecnológicas o arquitectónicas.
3. Puntúa valor, riesgo, esfuerzo y reversibilidad.
4. Organiza las iniciativas en estabilizar, mejorar y evolucionar.
5. Define una métrica de salida para cada horizonte.
6. Escribe una decisión que explícitamente dejarás fuera y por qué.
7. Presenta el roadmap al equipo y registra qué prioridad cambió después de la conversación.

## Cierre
Una estrategia tecnológica no predice todo el futuro. Define cómo vamos a aprender, qué riesgos atenderemos primero y qué señales justificarán la siguiente inversión. En el próximo video trabajaremos cómo comunicar estas decisiones a personas con intereses diferentes.
