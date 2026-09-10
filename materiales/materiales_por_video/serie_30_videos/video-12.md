# Video 12: Estrategia tecnológica y roadmap

## 📚 Lecturas de referencia: decidir qué construir después
- [Estrategia tecnológica y roadmap](https://platzi.com/cursos/fundamentos-arquitectura-software/evolucionar-un-mvp-sin-rearquitectar-des/)
- [Arquitectura con impacto social y ético](https://platzi.com/cursos/software-avanzado/observabilidad-en-sistemas-con-opentelem/)

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

## Cómo construir el roadmap paso a paso

### Paso 1: empieza por un resultado de negocio
No escribas “migrar a microservicios”. Escribe “reducir las entregas tardías del 18% al 10% sin aumentar el costo por pedido”. La tecnología aparece después del resultado.

### Paso 2: conecta capacidades con resultados
Para reducir entregas tardías necesitamos conocer capacidad de ruteo, tiempos de respuesta, disponibilidad de repartidores, calidad de direcciones y tratamiento de incidentes. Cada capacidad debe tener un propietario y una evidencia.

### Paso 3: ordena dependencias
No puedes extraer Ruteo de forma segura si antes no tienes un contrato estable, trazas y manejo de timeouts. No puedes medir puntualidad si el estado de entrega no es confiable. El roadmap debe mostrar qué trabajo habilita al siguiente.

### Paso 4: asigna capacidad real
Supón que el equipo tiene cuatro semanas y 40 puntos de capacidad. No puedes prometer todas las iniciativas. Una planificación razonable podría ser:

| Iniciativa | Capacidad | Dependencia | Resultado |
|---|---:|---|---|
| Métricas de Ruteo | 5 | Ninguna | Línea base p95 |
| Contrato de Ruteo | 8 | Modelo de dominio | Interfaz estable |
| Pruebas de timeout | 5 | Contrato | Fallo controlado |
| Dashboard de incidentes | 8 | Métricas | Diagnóstico operativo |
| Política de ventanas | 13 | Contrato y pruebas | Experimento |
| Reserva de contingencia | 1 | Ninguna | Atención de imprevistos |

### Paso 5: define una condición de avance
Ruteo no se separa porque esté en el roadmap. Se separa si durante dos campañas el p95 supera dos segundos, el equipo puede operar el servicio y la extracción reduce el impacto medido. Sin condición de avance, el roadmap es una lista de deseos.

## Decisiones que quedan fuera

Para este trimestre no construiremos microservicios para Inventario, no cambiaremos de nube y no reescribiremos toda la plataforma. No son necesariamente malas ideas; quedan fuera porque no están respaldadas por el riesgo prioritario ni por la capacidad disponible. Esta exclusión también es una decisión arquitectónica.

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

### Entrega modelo

**Objetivo:** reducir entregas tardías del 18% al 10% en tres meses sin aumentar más del 10% el costo por pedido.

**Mes 1: conocer y estabilizar.** Medir p95 de Ruteo, estados estancados y errores del proveedor. Crear trazas y contratos mínimos.

**Mes 2: experimentar.** Activar una política de ventanas para el 5% de pedidos y construir un tablero de incidentes. Comparar puntualidad, kilómetros y latencia.

**Mes 3: decidir.** Mantener la política si cumple los umbrales; extraer Ruteo solo si la evidencia muestra saturación independiente y existe capacidad operativa.

**Fuera del alcance:** reescritura completa, microservicios para todos los dominios y migración de nube. Se revisarán cuando cambien los datos o aparezca un riesgo que lo justifique.

## Cierre
Una estrategia tecnológica no predice todo el futuro. Define cómo vamos a aprender, qué riesgos atenderemos primero y qué señales justificarán la siguiente inversión. En el próximo video trabajaremos cómo comunicar estas decisiones a personas con intereses diferentes.
