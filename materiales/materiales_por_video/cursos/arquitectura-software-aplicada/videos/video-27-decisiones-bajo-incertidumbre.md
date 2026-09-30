# Video 27: Fitness Functions para medir tu arquitectura

## Para estudiar por tu cuenta
Una decisión arquitectónica puede quedar escrita en un documento y luego olvidarse. ¿Cómo detectamos si los cambios futuros están respetando una regla importante?

En esta clase aprenderás qué es una **fitness function** (función de adecuación arquitectónica): una comprobación repetible que revisa una característica importante del sistema y avisa cuando se degrada.

## 1. Una regla escrita no se vigila sola
Supongamos que el equipo decide: “Las reglas de negocio no deben consultar directamente la base de datos”. La decisión queda en la documentación, pero alguien agrega meses después una conexión directa para resolver una tarea rápida.

El documento no necesariamente avisa que ocurrió. Una comprobación automática puede revisar cada cambio y señalar la dependencia prohibida antes de que llegue a producción.

## 2. ¿Qué es una fitness function?
Una **fitness function** es una prueba o medición repetible que ayuda a saber si el sistema sigue cumpliendo una característica arquitectónica importante.

No significa que una función le asigne una nota total a la arquitectura. Cada comprobación observa una pregunta concreta, por ejemplo:

- ¿Se mantiene la separación entre negocio y base de datos?
- ¿La búsqueda de un pedido responde dentro del tiempo acordado?
- ¿El servicio funciona si una dependencia no responde?
- ¿El tamaño de una imagen o paquete no supera un límite útil?

Puede ser una prueba automática ejecutada cada vez que se integra un cambio o una medición periódica del sistema funcionando.

## 3. Una buena comprobación nace de una necesidad
No empieces diciendo “necesitamos fitness functions”. Empieza por una preocupación real.

### Preocupación
Cuando aumentan los pedidos, la consulta de seguimiento se vuelve tan lenta que los clientes vuelven a tocar el botón y crean solicitudes repetidas.

### Característica que queremos proteger
La consulta debe responder rápidamente incluso con una carga representativa.

### Comprobación posible
Simular un número acordado de consultas y medir cuánto tardan. Si la duración supera el límite acordado, la comprobación avisa.

El **límite** no es universal. Se define según lo que necesita el usuario, el nivel de tráfico, la infraestructura y el costo que el negocio puede asumir.

## 4. Tres ejemplos de comprobaciones

### Ejemplo A: dirección de dependencias
**Regla:** el módulo que contiene las reglas del pedido no importa directamente el componente que habla con la base de datos.

**Comprobación:** una prueba revisa las dependencias y falla si encuentra una conexión prohibida.

**Qué protege:** evita que una decisión rápida convierta una regla central en una parte difícil de probar o cambiar.

### Ejemplo B: tiempo de respuesta
**Regla:** una consulta de seguimiento debe responder dentro del nivel que el producto acordó bajo una carga representativa.

**Comprobación:** una prueba de rendimiento envía varias solicitudes y mide sus tiempos.

Si se mide el **percentil 95 (p95)**, se ordenan los tiempos de menor a mayor y se observa el punto por debajo del cual cae el 95% de las respuestas. Esto ayuda a no ocultar experiencias lentas detrás de un promedio. No necesitas calcularlo a mano; basta entender que muestra una parte de las respuestas más lentas sin elegir únicamente el peor caso.

### Ejemplo C: recuperación ante una dependencia caída
**Regla:** si el servicio de rutas no responde, el seguimiento debe informar que falta la ubicación sin declarar falsamente que el pedido fue entregado.

**Comprobación:** una prueba simula que rutas no contesta y verifica el mensaje y el estado que devuelve el sistema.

## 5. Una comprobación puede ser automática o requerir revisión
Algunas características son fáciles de medir con una prueba, como “el módulo no importa la base de datos”. Otras requieren revisión humana, como “la explicación del cambio es comprensible para soporte”.

La idea de una fitness function es repetir la comprobación para observar si el sistema mantiene una cualidad acordada. No toda pregunta importante se puede convertir en un número confiable.

## 6. Cómo crear una fitness function, paso a paso
1. **Nombra la característica.** Ejemplo: “Una entrega no se marca como completada sin evidencia”.
2. **Explica por qué importa.** El cliente y soporte podrían recibir un estado falso.
3. **Define qué se observará.** ¿Qué dato o comportamiento demuestra la condición?
4. **Elige una prueba o medición.** Por ejemplo, una prueba de estados que intenta completar la entrega sin evidencia.
5. **Define qué resultado pasa y qué resultado falla.** La comprobación debe ser clara y repetible.
6. **Decide cuándo se ejecuta.** Puede correr al revisar cambios o en pruebas periódicas.
7. **Asigna quién investiga una falla.** Una alerta sin responsable suele convertirse en ruido.
8. **Revisa si sigue siendo útil.** Si cambió la necesidad, actualiza o retira la comprobación.

## 7. ¿Dónde se ejecutan?
Una comprobación de arquitectura puede ejecutarse:

- **Al revisar un cambio:** impide integrar una dependencia prohibida.
- **Antes de publicar:** prueba carga o comportamiento con una versión candidata.
- **Periódicamente con el sistema activo:** detecta cambios de rendimiento o capacidad.
- **Después de un experimento controlado:** confirma que el sistema se recuperó como se esperaba.

No hace falta ejecutar todas las comprobaciones en cada momento. El equipo elige el momento que permita encontrar el problema antes de que afecte a las personas, sin hacer el proceso innecesariamente lento.

## 8. Límites y errores habituales
- **Medir algo que nadie necesita:** produce números sin guiar una decisión.
- **Fijar un umbral sin contexto:** un límite arbitrario puede generar fallos falsos o dejar pasar problemas reales.
- **Optimizar una sola medida:** reducir el tiempo de respuesta podría aumentar mucho el costo o debilitar seguridad.
- **Ignorar alertas repetidas:** si hay demasiadas alertas sin acción, el equipo deja de atenderlas.
- **Convertir cada preferencia en una regla automática:** algunas decisiones requieren contexto y revisión humana.
- **Suponer que pasar todas las comprobaciones prueba la calidad completa:** solo sabemos que se revisaron las características incluidas.

Una buena comprobación tiene una pregunta clara, un resultado interpretable y alguien que actúa si falla.

## 9. Actividad de autoestudio
El equipo quiere proteger dos características de la plataforma logística:

1. No se debe marcar una entrega como “Entregada” sin registrar evidencia de recepción.
2. La consulta de seguimiento no debe empeorar de manera notable después de un cambio.

Para cada característica, escribe:

- ¿Por qué le importa al usuario?
- ¿Qué se puede observar o medir?
- ¿Qué prueba automática podrías repetir?
- ¿Qué resultado consideras aceptable y cómo justificarías ese límite?
- ¿Cuándo ejecutarías la comprobación?
- ¿Quién investigaría un resultado inesperado?

### Pistas
- Para la primera característica, intenta el cambio de estado sin evidencia.
- Para la segunda, compara la misma carga antes y después; no uses un umbral inventado sin contexto.
- Una prueba puede detectar una regresión, pero alguien debe decidir cómo corregirla.

## 10. Solución modelo
### Entrega con evidencia
- Importa porque una falsa confirmación afecta al cliente, al repartidor y al soporte.
- Se observa si existe un registro de recepción vinculado a la entrega.
- Una prueba intenta cambiar el estado a “Entregada” sin evidencia y verifica que el sistema lo rechace.
- El resultado aceptable es que ningún camino permita confirmar sin evidencia; el equipo debe revisar que la prueba cubra la regla acordada.
- Se ejecuta al integrar cambios que afectan el flujo de entrega.

### Rendimiento del seguimiento
- Importa porque una pantalla lenta causa esperas y consultas repetidas.
- Se observa el tiempo de respuesta bajo una carga definida y representativa.
- Se ejecuta la misma prueba antes y después del cambio.
- El límite se acuerda con el producto según la experiencia que necesita el cliente y la capacidad disponible; no se copia un número de otro sistema.
- Se ejecuta antes de publicar cambios relevantes y, si hace falta, periódicamente.

## 11. Comprueba lo que aprendiste
1. ¿Qué característica protege una fitness function?
2. ¿Por qué debe tener un resultado claro y un responsable?
3. ¿Una métrica aislada certifica que toda la arquitectura es buena?
4. ¿Cómo eliges un umbral de rendimiento?

### Respuestas
1. Una propiedad o regla importante del sistema, como el límite entre módulos o un nivel de respuesta.
2. Para que el equipo sepa qué significa el fallo y quién debe investigarlo.
3. No; cada comprobación cubre solo una pregunta.
4. Se acuerda según la experiencia requerida, la carga, el costo y el contexto real del producto.

## Conclusión
Una fitness function convierte una característica arquitectónica importante en una comprobación que se puede repetir. Ayuda a detectar cuándo un cambio debilita una regla o una cualidad del sistema.

La comprobación no decide todo por el equipo. Debe medir lo que importa, tener un límite justificado, ejecutarse en el momento adecuado y producir un resultado que alguien pueda investigar.
