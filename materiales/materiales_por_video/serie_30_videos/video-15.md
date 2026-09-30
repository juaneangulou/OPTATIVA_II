# Video 15: Método arquitectónico e inteligencia artificial

## Fuentes de este video
- [Intuición vs método en arquitectura de software](https://platzi.com/cursos/software-avanzado/intuicion-vs-metodo-en-arquitectura-de-s/)
- [Cómo analizar una licitación real con IA](https://platzi.com/cursos/software-avanzado/como-analizar-una-licitacion-real-con-ia/)

## Para estudiar por tu cuenta
Este capítulo conecta dos habilidades: decidir con método y usar inteligencia artificial para analizar información extensa sin delegarle la responsabilidad de decidir.

La primera fuente explica por qué una intuición puede servir como punto de partida, pero no basta para justificar una arquitectura. La segunda muestra cómo una herramienta de IA puede ayudar a revisar una licitación. Juntas ofrecen una secuencia útil: entender el problema, reunir evidencia, usar IA para organizar información y comprobar sus resultados antes de decidir.

## 1. El caso: preparar una propuesta logística
La empresa de última milla quiere contratar o construir una plataforma que registre pedidos, verifique inventario, organice entregas y permita consultar estados.

Recibes una licitación extensa. Una primera reacción podría ser pedirle a una IA “resume el documento y dime qué tecnología usar”. Esa respuesta parece rápida, pero mezcla dos tareas distintas:

- **Analizar qué pide el documento.** La IA puede ayudar a extraer requisitos y señalar dónde aparecen.
- **Decidir qué arquitectura proponer.** Requiere entender el negocio, comprobar capacidades, evaluar riesgos y justificar costos.

La IA puede apoyar la primera y ayudar a explorar la segunda, pero no conoce automáticamente el producto ni puede certificar que se cumple un requisito.

## 2. Intuición como hipótesis, no como veredicto
La **intuición** es una idea inicial basada en experiencia. Por ejemplo: “La licitación habla de mucho crecimiento; quizá necesitemos microservicios”.

El **método** consiste en convertir esa intuición en preguntas comprobables:

1. ¿La licitación especifica el volumen de pedidos?
2. ¿Qué plazo de respuesta exige?
3. ¿Hay equipos distintos que necesiten publicar cambios por separado?
4. ¿Qué capacidad operativa tiene la empresa para manejar varios servicios?
5. ¿Qué evidencia demostraría que una separación aporta valor?

Si la licitación no da números, anota “sin evidencia localizada” y prepara una pregunta para aclararlo. No conviertas “alto crecimiento” en una predicción técnica que el documento no hace.

## 3. Usa IA para organizar, no para certificar
Una **licitación** es un documento de requisitos, condiciones y criterios de evaluación. Una **matriz de requisitos** convierte sus declaraciones en filas que puedes revisar.

| Identificador | Requisito | Fuente exacta | Estado | Pregunta pendiente |
|---|---|---|---|---|
| R-01 | El cliente consulta el estado del pedido | Sección 2, párrafo 4 | Por validar | ¿Qué perfiles pueden verlo? |
| R-02 | Se registran entregas fallidas | Anexo B, requisito 7 | Parcial | ¿Qué campos y retención exige? |
| R-03 | Tiempo de respuesta menor a lo acordado | Sin evidencia localizada | Por validar | ¿Qué tiempo y qué carga se medirán? |

Estados claros evitan confundir “lo encontré en el documento” con “el producto ya cumple”.

## 4. Una instrucción para extraer evidencia
Puedes pedir a una herramienta de IA que organice una parte del documento:

```text
Extrae los requisitos de esta sección.
Para cada requisito, copia una frase breve y señala el título o número de sección.
Clasifica cada uno como funcional, calidad, seguridad, operación o integración.
Si la fuente no establece un valor, escribe “no especificado”.
No concluyas que nuestro producto cumple.
```

Después abre la licitación y verifica la frase original. La IA puede equivocarse con tablas, anexos, notas al pie o un PDF escaneado.

Antes de subir cualquier documento, confirma que puedes compartirlo con esa herramienta. No incluyas información confidencial, datos personales, tokens ni secretos comerciales sin autorización.

## 5. De los requisitos a una propuesta
Para cada requisito importante, completa el razonamiento:

1. **Qué solicita:** copia la obligación en palabras precisas.
2. **Qué significa:** aclara términos ambiguos.
3. **Qué actor lo necesita:** cliente, soporte, operación, almacén o repartidor.
4. **Qué parte del sistema respondería:** Pedidos, Inventario, Entregas u otra.
5. **Qué opciones hay:** por ejemplo, una aplicación modular o servicios desplegados por separado.
6. **Qué evidencia falta:** prueba, medición, contrato o pregunta.
7. **Qué riesgo y costo acepta la propuesta.**

La arquitectura se justifica con esa cadena, no con una palabra popular encontrada en la licitación.

## 6. Ejemplo resuelto
La licitación dice: “La solución deberá permitir seguimiento de pedidos en tiempo real”.

### Lectura literal
La frase no define qué significa “tiempo real”, quién puede consultar ni cuántos pedidos deben atenderse. La anotamos como requisito ambiguo, no la completamos con nuestra imaginación.

### Preguntas que faltan
- ¿Qué demora máxima entre un reporte y la pantalla considera aceptable la entidad?
- ¿La ubicación debe ser exacta o basta el estado de entrega?
- ¿Qué roles pueden consultar el recorrido?
- ¿Qué ocurre cuando el repartidor pierde conexión?

### Propuesta inicial verificable
Podemos proponer mostrar el último estado confirmado y la hora de actualización. Si el sistema no tiene una ubicación nueva, avisa que el dato está atrasado en vez de presentarlo como actual.

### Evidencia
Una prueba puede simular que no llega una actualización y comprobar que la interfaz conserva la hora anterior y la marca claramente. El objetivo de demora debe acordarse con la entidad; no lo inventamos.

## 7. Ejercicio de autoestudio
Analiza este requisito ficticio: “La plataforma debe garantizar continuidad y protección de información”.

1. Señala qué términos no tienen una medida concreta.
2. Divide la frase en requisitos comprobables.
3. Escribe una pregunta de aclaración para cada requisito.
4. Propón qué tarea pedirías a una IA y qué evidencia debe devolver.
5. Nombra qué datos no compartirías con una herramienta no autorizada.
6. Explica qué información necesitas antes de recomendar una arquitectura.

### Pistas
- “Continuidad” puede referirse a disponibilidad, recuperación o funcionamiento parcial.
- “Protección” puede referirse a acceso, cifrado, auditoría o privacidad; pide alcance.
- Para recomendar una arquitectura necesitas necesidades y restricciones, no solo el nombre de una tecnología.

## 8. Respuesta modelo
Dividiría la frase en, al menos, dos preguntas: cuánto tiempo puede estar indisponible la plataforma y cuánto tiempo se permite para recuperarse; además, qué datos se consideran sensibles y quién puede consultarlos.

Pediría a la IA extraer requisitos y referencias exactas, sin solicitarle que certifique el cumplimiento. Verificaría cada resultado en el documento original.

No compartiría documentos restringidos ni datos personales sin autorización. Antes de proponer arquitectura pediría volumen, integraciones, perfiles de acceso, objetivos de disponibilidad, presupuesto y capacidad operativa.

## Comprueba lo que aprendiste
1. ¿Qué diferencia hay entre una intuición y una decisión comprobada?
2. ¿Qué salida concreta debe producir la IA para que puedas revisar una extracción?
3. ¿Por qué “no especificado” es preferible a inventar una medida?
4. ¿Quién es responsable de aprobar que el sistema cumple?

### Respuestas
1. La intuición propone una hipótesis; una decisión comprobada tiene evidencia y pruebas que la respaldan.
2. Una frase del documento junto con la sección de donde se obtuvo.
3. Porque mantiene visible la incertidumbre y permite hacer una pregunta formal.
4. El equipo y la organización que ofertan, después de validar el producto; no la IA.

## Conclusión
Usa IA para acelerar la lectura, no para reemplazar el juicio. Conserva la fuente de cada requisito, distingue hechos de suposiciones, pregunta por las ambigüedades y propone una arquitectura solo cuando puedas explicar qué necesidad resuelve y cómo comprobarla.