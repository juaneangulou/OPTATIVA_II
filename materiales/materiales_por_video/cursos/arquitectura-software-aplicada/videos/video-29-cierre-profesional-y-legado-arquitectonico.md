# Video 29: Sabiduría y criterio en arquitectura de software

## Para estudiar por tu cuenta
En este video final de conceptos practicarás una habilidad que conecta todo lo anterior: elegir una solución adecuada para el problema real, explicar por qué y reconocer qué podría hacerte cambiar de opinión.

El **criterio arquitectónico** no es adivinar la mejor tecnología ni saber nombrar muchos patrones. Es usar contexto, evidencia y juicio para comparar alternativas y aceptar conscientemente sus costos.

## 1. Una situación para decidir
La plataforma logística necesita que sus clientes consulten el estado de sus pedidos. El sistema actual es pequeño y el equipo conoce sus partes. A futuro podría crecer, pero todavía no se conoce cuánto ni cuándo.

Alguien propone dividirlo ahora en muchos microservicios porque “así escalará mejor”. Otra persona propone mantenerlo como una aplicación organizada por módulos y revisar la decisión cuando el crecimiento lo requiera.

No podemos elegir correctamente con una frase como “los microservicios son mejores” o “un monolito siempre es más simple”. Necesitamos conocer qué problema existe hoy, quién se ve afectado y qué evidencia justifica el costo de cada alternativa.

## 2. Seis preguntas para ejercer criterio

### 1. ¿Qué problema concreto queremos resolver?
Describe el problema sin nombrar todavía la tecnología. Por ejemplo: “Los cambios de seguimiento requieren coordinar tres equipos y provocan demoras”, no “necesitamos microservicios”.

### 2. ¿A quién afecta?
Identifica las personas o áreas afectadas. Para la consulta de pedidos pueden ser clientes que esperan información, soporte que recibe llamadas y el equipo que mantiene el sistema.

### 3. ¿Qué sabemos y qué estamos suponiendo?
Separa hechos de hipótesis. “Tenemos 300 consultas al día” podría ser una medición. “El sistema no crecerá” sería una predicción que hay que revisar.

### 4. ¿Qué alternativas tenemos?
Compara más de una forma viable de resolverlo. Incluye la opción sencilla actual y la opción más elaborada; no compares una alternativa real con una caricatura.

### 5. ¿Qué ganamos y qué aceptamos pagar?
Cada decisión tiene costos: tiempo de desarrollo, infraestructura, operación, seguridad, aprendizaje, dificultad para cambiar o riesgo para el cliente. Explica el beneficio y el costo con palabras concretas.

### 6. ¿Cómo sabremos si debemos revisar la decisión?
Define una señal observable: más errores, demoras, cambios que se bloquean o un costo que supera lo previsto. Una decisión sin condición de revisión puede quedarse por costumbre incluso cuando ya no sirve.

## 3. Ejemplo trabajado: modular o separar en servicios
Usaremos supuestos explícitos para practicar; no son mediciones de una empresa real.

### Lo que sabemos en el ejercicio
- El sistema necesita registrar pedidos y mostrar su seguimiento.
- Un solo equipo mantiene ambas capacidades.
- No hay evidencia de que la carga actual exceda la capacidad.
- El equipo tiene experiencia limitada operando muchos servicios.

### Alternativa A: una aplicación modular
Una **aplicación modular** se despliega como una sola unidad, pero sus partes tienen responsabilidades y límites internos claros.

**Ventajas:** menos componentes que operar, comunicación directa dentro de la aplicación y una forma sencilla de empezar.

**Costos:** si los límites se ignoran, el código puede enredarse; algunos cambios y despliegues afectan a toda la aplicación.

### Alternativa B: servicios independientes
Cada capacidad importante se despliega y opera como servicio separado.

**Ventajas:** los equipos pueden desplegar algunas partes por separado y ajustar recursos de manera independiente, si el sistema y la operación lo permiten.

**Costos:** aparecen comunicaciones por red, más despliegues, monitoreo, fallas parciales y necesidad de coordinar contratos y datos.

### Decisión razonada para este escenario
Con la información disponible, empezaríamos con una aplicación modular. La razón no es que los servicios independientes sean malos: es que todavía no hay una necesidad medida que justifique su costo y el equipo tendría que operar complejidad adicional.

Dejamos límites claros entre Pedidos y Seguimiento, medimos tiempos y observamos si los cambios de una parte bloquean a la otra. Revisaremos la decisión si la carga supera la capacidad acordada o si los equipos necesitan desplegar esas capacidades por separado con frecuencia.

Otra organización podría tomar una decisión distinta si tiene cargas, equipos o requisitos diferentes. El criterio está en la explicación y la evidencia, no en elegir siempre la misma opción.

## 4. Una decisión se puede revisar sin que haya sido un error
Una decisión arquitectónica se toma con la información disponible. Si el contexto cambia, revisarla puede ser una señal de aprendizaje y no una confesión de fracaso.

Ejemplo: se eligió una aplicación modular porque había un equipo y poca carga. Un año después hay varios equipos, cambios independientes frecuentes y una carga que exige ampliar una parte sin ampliar las demás. Esos nuevos hechos pueden justificar estudiar una separación.

Lo valioso es que la decisión inicial conserve sus razones y señales de revisión. Así, el equipo puede entender por qué se eligió y qué cambió desde entonces.

## 5. Cómo comunicar una decisión sin esconder sus costos
Una explicación breve puede seguir esta forma:

> “Elegimos ___ porque el problema principal es ___. Consideramos ___, pero por ahora la descartamos porque ___. Aceptamos el costo de ___. Revisaremos la decisión cuando observemos ___”.

Una explicación débil dice “usamos esta tecnología porque es la mejor”. Una explicación útil nombra el contexto, la necesidad, la alternativa, el costo y la evidencia para revisar.

## 6. Errores que debilitan el criterio
- **Elegir por moda:** popularidad no demuestra que la opción resuelva el problema.
- **Diseñar para un crecimiento imaginario:** una posibilidad no equivale a una necesidad medida.
- **Ocultar costos:** toda decisión los tiene, incluso no hacer nada.
- **Comparar sin criterios:** “más moderno” no indica qué experiencia o riesgo mejora.
- **Tratar las suposiciones como hechos:** escribe cómo las comprobarás.
- **Defender una decisión para siempre:** una decisión útil hoy puede necesitar revisión mañana.
- **Medir solo lo técnico:** también importan el trabajo del equipo, la privacidad, el costo y las personas usuarias.

## 7. Actividad de autoestudio: justifica una decisión
Elige una decisión para la plataforma logística:

- ¿Una sola aplicación modular o varios servicios?
- ¿Estado actual de pedidos o historial completo de eventos?
- ¿Una Gateway común o llamadas directas a servicios?
- ¿Reintentar automáticamente una entrega fallida o enviarla a revisión?

Completa:

1. **Problema:** ¿qué debe mejorar y quién lo necesita?
2. **Hechos:** ¿qué datos conoces?
3. **Suposiciones:** ¿qué estás imaginando y cómo lo comprobarías?
4. **Alternativas:** ¿qué opciones reales consideraste?
5. **Elección:** ¿cuál recomiendas y por qué?
6. **Costo aceptado:** ¿qué dificultad o riesgo aceptas?
7. **Evidencia:** ¿qué prueba, métrica, diagrama o comportamiento comprobará el resultado?
8. **Revisión:** ¿qué señal te haría cambiar la decisión?

### Pistas
- Si la respuesta dice solo el nombre de una tecnología, todavía no explica la decisión.
- Si no nombras ningún costo, revisa las alternativas.
- Si no puedes decir qué resultado cambiaría tu opinión, quizá falta una hipótesis comprobable.

## 8. Respuesta modelo
**Decisión:** mantener Pedidos y Seguimiento en una sola aplicación modular por ahora.

**Problema:** la plataforma necesita consultar entregas y el equipo actual puede mantener ambas capacidades.

**Hechos del escenario:** no se midió una carga que exceda la capacidad; un equipo mantiene el sistema.

**Alternativa descartada:** separar en servicios ahora. Podría permitir despliegues independientes más adelante, pero hoy agregaría operación, monitoreo y comunicación distribuida sin evidencia de que haga falta.

**Costo aceptado:** si una parte necesita crecer de manera independiente, separar después exigirá preparar límites y cambios de integración.

**Verificación:** medir tiempos de consulta, fallas y frecuencia con que cambios de una capacidad bloquean la otra.

**Condición de revisión:** si se observa durante un período acordado que la demanda o la independencia de despliegue excede la capacidad de la estructura actual, evaluar una separación con esos datos.

Esta respuesta es válida para los hechos del ejercicio. Si tus datos cambian, tu decisión puede cambiar también.

## 9. Comprueba lo que aprendiste
1. ¿Qué diferencia hay entre un hecho y una suposición?
2. ¿Por qué hay que describir costos además de beneficios?
3. ¿Revisar una decisión demuestra que fue equivocada?
4. ¿Qué vuelve defendible una decisión arquitectónica?

### Respuestas
1. Un hecho tiene evidencia disponible; una suposición es algo que creemos y aún necesitamos comprobar.
2. Porque toda alternativa exige recursos o introduce riesgos que deben ser aceptados conscientemente.
3. No. Puede demostrar que cambiaron el contexto o la evidencia.
4. Conectar el problema, las personas afectadas, los hechos, las alternativas, los costos, la verificación y la condición de revisión.

## Conclusión
El criterio arquitectónico se practica al tomar decisiones proporcionales al problema, explicarlas con claridad y estar dispuesto a revisarlas cuando cambie la evidencia.

No busques una arquitectura perfecta ni una tecnología universal. Busca una solución que responda al contexto actual, protege lo importante y deja claro qué aprenderás después de ponerla en uso.
