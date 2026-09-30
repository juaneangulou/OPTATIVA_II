# Video 29: Criterio, liderazgo y arquitectura responsable

## Fuente de este video
- [Sabiduría y criterio en arquitectura de software](https://platzi.com/cursos/software-avanzado/sabiduria-y-criterio-en-arquitectura-de/)

## Navegación
[⬅️ Video anterior: Fitness Functions, OpenTelemetry y caos](video-28.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: cierre y defensa](video-30.md)

## Para estudiar por tu cuenta
No existe una solución que sea la mejor para todos los sistemas. Este capítulo no repite la negociación del video 13: entrena cómo decidir cuando aparecen datos nuevos, fallas observadas o restricciones que obligan a revisar una elección anterior.

En esta clase vas a practicar una decisión con necesidades en conflicto: permitir que soporte investigue retrasos sin exponer datos personales de repartidores más allá de lo necesario.

## 1. Qué es criterio arquitectónico
El **criterio arquitectónico** es la capacidad de elegir y explicar una solución a partir de información incompleta, considerando a las personas afectadas y los costos de cada alternativa.

No equivale a:

- elegir la tecnología más nueva;
- repetir un patrón conocido sin revisar si aplica;
- defender la primera idea para no reconocer que cambió el contexto;
- ocultar costos porque una alternativa parece más elegante.

El criterio se puede observar en la explicación y en las pruebas que la sostienen, no solo en el título profesional de quien decide.

## 2. Una decisión con intereses distintos
Soporte necesita investigar entregas tardías. Una opción es conservar la ubicación precisa del repartidor durante muchas horas; otra es guardar únicamente estados y horas de actualización.

La primera opción puede aportar detalle para una investigación, pero aumenta exposición de datos y necesidades de acceso. La segunda reduce la ubicación almacenada, aunque quizá no permita reconstruir algunos recorridos.

Antes de decidir, pregunta:

- ¿Qué incidencia concreta necesita investigar soporte?
- ¿Qué datos son indispensables para resolverla?
- ¿Cuánto tiempo se necesitan?
- ¿Quién puede consultarlos?
- ¿Qué riesgo queda si guardamos menos detalle?

## 3. Separa evidencia, hipótesis y decisión
- **Evidencia:** datos observados o pruebas reproducibles, como cuántos reclamos de demora recibe soporte.
- **Hipótesis:** explicación todavía no confirmada, como “guardar toda la ruta reducirá los reclamos”.
- **Decisión:** opción elegida con base en el contexto actual.
- **Condición de revisión:** señal que justificaría cambiarla.

Una hipótesis puede ser razonable y aun así resultar falsa. El documento de decisión debe dejar claro qué parte se conoce y qué parte se probará.

## 4. Método breve para decidir
1. Describe el problema sin incluir la solución propuesta.
2. Identifica a quién afecta y qué dato o proceso está en riesgo.
3. Reúne hechos disponibles y enumera incertidumbres.
4. Compara al menos dos alternativas viables.
5. Explica qué gana y qué costo acepta cada alternativa.
6. Elige una opción para el contexto actual.
7. Define cómo comprobarla y cuándo revisarla.

## 5. Decisión trabajada
**Problema:** soporte necesita investigar por qué algunos pedidos llegaron tarde.

**Hecho:** se registran la hora estimada y los cambios de estado de la entrega.

**Suposición por comprobar:** la posición precisa del repartidor es necesaria para resolver la mayoría de las incidencias.

**Alternativa A:** conservar cada posición precisa durante el recorrido.
- Beneficio: mayor detalle para reconstruir el trayecto.
- Costo: más información sensible almacenada, mayor necesidad de restringir y auditar accesos.

**Alternativa B:** conservar cambios de estado, hora y zona aproximada durante un período definido.
- Beneficio: soporte puede revisar la secuencia sin guardar toda la ruta precisa.
- Costo: algunas investigaciones no podrán reconstruir el recorrido exacto.

**Decisión inicial:** usar B y registrar qué incidencias no se pueden resolver con esos datos. Si esas incidencias resultan frecuentes y requieren ubicación precisa, revisar la política con privacidad, operación y representantes de repartidores.

**Comprobación:** toma una muestra de incidencias, intenta resolverlas con el historial reducido y registra cuáles requieren otro dato.

La decisión es responsable si permite investigar el problema y protege los datos que no son necesarios; no porque una opción sea siempre moralmente superior.

## 6. Comunica sin imponer
Una explicación útil puede decir:

> “Elegimos guardar estados y zonas aproximadas porque resuelven la mayoría de las investigaciones observadas y reducen la cantidad de ubicación precisa almacenada. Aceptamos que algunos casos requerirán información adicional. Revisaremos la política si esos casos superan el límite acordado”.

Esta forma de explicar reconoce intereses, razón, costo y condición de revisión. También permite que alguien cuestione la decisión con nueva evidencia.

## 7. Actividad de autoestudio
La operación quiere añadir un nuevo servicio de mapas porque podría mejorar las rutas.

1. Escribe el problema actual sin nombrar mapas.
2. Anota qué datos existen y qué dato falta.
3. Formula una hipótesis que pueda comprobarse.
4. Compara usar el proveedor nuevo con mejorar la planificación actual.
5. Nombra los costos de datos, disponibilidad, pago y mantenimiento.
6. Propón una prueba pequeña y el resultado que te haría continuar o detenerte.

### Respuesta modelo
Problema: algunas entregas tardan más que la estimación y se desconoce si las rutas son la causa. Hipótesis: considerar el tráfico real reducirá los retrasos sin aumentar demasiado el costo por pedido.

Antes de contratar el proveedor, mediría retrasos y compararía una muestra de rutas históricas. Probaría el servicio en modo de cálculo sin asignar repartidores, cotejaría estimación y tiempo real, y revisaría costo y errores. Seguiría solo si mejora la medida acordada y no expone información innecesaria.

## Comprueba lo que aprendiste
1. ¿Qué diferencia hay entre evidencia e hipótesis?
2. ¿Qué debe explicar una decisión además de la solución elegida?
3. ¿Por qué una decisión debe tener una condición de revisión?
4. ¿Qué hace responsable una decisión con impacto en personas?

### Respuestas
1. La evidencia se observa o reproduce; una hipótesis todavía debe comprobarse.
2. El problema, las alternativas, los costos y la forma de verificar el resultado.
3. Permite cambiarla cuando el contexto o los datos contradicen las razones iniciales.
4. Considera quién recibe beneficios y riesgos, limita daños evitables y define controles verificables.

## Taller aplicado: revisar una decisión con nueva evidencia
La decisión inicial fue mostrar estado y zona aproximada del repartidor. Después de un mes aparecen dos datos: las consultas de soporte bajaron, pero aumentaron los accesos fuera de entregas activas.

1. Separa los dos resultados en evidencia, no en opiniones.
2. Identifica qué condición de la decisión original dejó de cumplirse.
3. Compara mantener, limitar o retirar la zona aproximada.
4. Explica qué costo acepta cada alternativa.
5. Define una prueba de privacidad y una métrica de experiencia.
6. Registra una decisión revisada con fecha y responsable.

El criterio no consiste en defender la primera elección. Consiste en reconocer cuándo sus supuestos cambiaron y ajustar el diseño de forma trazable.

## Conclusión
La sabiduría arquitectónica no es tener una respuesta permanente. Es aprender a tomar decisiones proporcionales al problema, hacer visibles sus consecuencias y revisarlas cuando la evidencia cambie.