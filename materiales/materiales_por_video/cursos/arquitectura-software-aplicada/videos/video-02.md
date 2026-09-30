# Video 2: Cómo analizar una licitación real con inteligencia artificial

## Para estudiar por tu cuenta
Una **licitación** es un documento donde una organización explica qué necesita contratar, qué condiciones debe cumplir una propuesta y cómo se evaluarán las ofertas. Puede incluir funciones, seguridad, soporte, fechas y requisitos legales.

En esta clase aprenderás a usar una herramienta de inteligencia artificial para organizar esa información sin dejar que invente respuestas ni decida por ti si un producto cumple.

## 1. El problema
La empresa logística necesita contratar una plataforma que registre pedidos, consulte inventario y muestre entregas. La licitación ocupa muchas páginas. Si lees rápido y anotas “cumple” sin evidencia, puedes comprometer al equipo a entregar algo que el producto no ofrece.

El objetivo es convertir el documento en preguntas verificables y conservar la ubicación de cada requisito.

## 2. Prepara la información antes de usar IA
1. Confirma que tienes permiso para compartir el documento con la herramienta.
2. No subas información confidencial, datos personales o secretos comerciales si no está autorizado.
3. Comprueba que el archivo se puede leer. Un PDF escaneado puede confundir letras, tablas y notas al pie.
4. Conserva el nombre y la versión del documento; una licitación puede cambiar entre revisiones.

La IA solo puede analizar lo que recibe. Si una tabla se leyó mal, su respuesta también puede estar equivocada.

## 3. Convierte requisitos en una matriz
Una **matriz de requisitos** es una tabla para registrar qué se exige, dónde aparece y qué evidencia tienes de que se cumple.

| ID | Requisito | Tipo | Fuente | Estado | Pregunta pendiente |
|---|---|---|---|---|---|
| R-01 | El cliente puede consultar el estado del pedido | Funcional | Sección 3, párrafo 2 | Por validar | ¿Qué perfiles pueden verlo? |
| R-02 | Los datos se protegen durante el envío | Seguridad | Sección 5, requisito 4 | Por validar | ¿Qué datos y conexiones incluye? |

“Por validar” significa que aún no hay evidencia suficiente. Es más seguro que inventar una respuesta.

## 4. Pide a la IA una extracción verificable
Puedes usar una instrucción como esta:

```text
Extrae del texto los requisitos que se solicitan.
Para cada requisito, indica la sección o frase que lo respalda.
Separa funciones, seguridad, operación, integración y plazos.
Si no encuentras evidencia, escribe “sin evidencia localizada”.
No decidas si nuestro producto cumple; solo organiza la información.
```

Después compara cada cita con el documento original. La IA puede sugerir categorías, pero tú verificas si interpretó bien la exigencia.

## 5. Del texto a una decisión
Para cada requisito:

1. Escríbelo como una obligación concreta.
2. Clasifícalo: funcional, calidad, seguridad, integración, operación o legal.
3. Registra dónde está la evidencia.
4. Compara el requisito con lo que el producto ya puede demostrar.
5. Marca “Cumple”, “Parcial”, “No cumple” o “Por validar”.
6. Anota qué pregunta necesitas resolver y quién puede responderla.

Una frase como “el sistema debe ser rápido” no se puede verificar todavía. Necesita una condición más clara, por ejemplo, el tiempo máximo esperado y cuántas consultas se medirán. El valor exacto debe acordarse con el negocio; no lo inventes.

## 6. Caso trabajado
Requisito de ejemplo: “El cliente debe recibir una actualización cuando se retrase su entrega”.

- **Necesidad funcional:** enviar un aviso ante un retraso.
- **Ambigüedad:** no define cuánto retraso cuenta ni qué hora es la referencia.
- **Evidencia:** localizar la frase exacta y anotar la sección.
- **Pregunta pendiente:** ¿se compara con la hora prometida al cliente o con una hora interna de operación?
- **Validación del producto:** demostrar con una prueba que se envía un aviso cuando se cumple la condición acordada y que no se envía antes.

La IA puede encontrar y reformular la frase. No puede decidir el significado comercial de “retraso” sin información acordada.

## 7. Actividad de autoestudio
Usa este requisito ficticio: “El sistema registrará la entrega y permitirá consultar su estado”.

1. Divídelo si contiene más de una obligación.
2. Clasifica cada obligación.
3. Escribe qué evidencia del producto buscarías.
4. Formula una pregunta para cada frase ambigua.
5. Escribe una instrucción para que una IA extraiga requisitos con sus fuentes.

### Respuesta modelo
- “Registrar la entrega” y “consultar su estado” son dos funciones distintas.
- Evidencia: una prueba de creación y una consulta con un pedido de prueba.
- Pregunta: ¿qué significa registrar: crear la entrega, asignar un repartidor o guardar la hora de salida?
- Pregunta: ¿qué estados se deben mostrar y quién puede consultarlos?
- La instrucción a la IA debe exigir una cita por requisito y marcar “sin evidencia” cuando no encuentre soporte.

## Comprueba lo que aprendiste
1. ¿Por qué la matriz conserva la sección de origen?
2. ¿Qué significa “Por validar”?
3. ¿La respuesta de una IA demuestra que el producto cumple?

**Respuestas:** la fuente permite revisar la interpretación; “Por validar” indica que falta evidencia o una decisión; no, el cumplimiento debe confirmarse con capacidades y pruebas reales.

## Conclusión
La IA puede acelerar la extracción y organización de requisitos. La responsabilidad de comprobar el documento, aclarar ambigüedades y decidir si el producto cumple sigue siendo tuya. Conserva la fuente y no transformes una sugerencia automática en una promesa contractual sin evidencia.
