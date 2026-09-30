# Video 1: Intuición vs método en arquitectura de software

## Para estudiar por tu cuenta
Cuando aparece un problema de software, es natural pensar rápido en una solución. Esa primera idea puede ser útil, pero todavía no sabemos si resuelve la necesidad real o si crea dificultades más adelante.

En esta clase practicarás cómo pasar de una intuición a una decisión que puedas explicar y comprobar. No necesitas experiencia como arquitecto ni conocimientos técnicos avanzados.

## 1. El ejemplo: consultar una entrega
La plataforma logística quiere mostrar al cliente dónde está su pedido. Una primera idea podría ser: “guardemos el estado en la pantalla”. Antes de implementarla, conviene averiguar:

- ¿Qué parte del sistema conoce el estado verdadero de la entrega?
- ¿Qué debe ver el cliente si todavía no existe una ubicación?
- ¿Cómo evitamos que una persona consulte el pedido de otra?
- ¿Qué ocurre si el servicio que informa la ubicación deja de responder?

Estas preguntas no impiden avanzar. Evitan convertir la primera idea en una decisión sin revisar sus efectos.

## 2. Intuición y método
La **intuición** es una primera idea basada en experiencia o en señales que reconocemos. Puede ayudarnos a encontrar alternativas.

Un **método** es una serie de pasos que nos permite examinar el problema, lo que sabemos, las opciones y los riesgos antes de decidir.

No hay que elegir entre intuición y método. La intuición propone “quizás la aplicación consulte directamente al servicio de entregas”. El método pregunta si esa parte tiene el dato, cómo se protege el acceso y qué mostrará la aplicación si no recibe respuesta.

## 3. Una forma sencilla de tomar decisiones
1. **Describe la necesidad sin nombrar herramientas.** “El cliente necesita consultar el estado de su pedido”.
2. **Identifica a las personas afectadas.** Cliente, repartidor y soporte pueden necesitar información distinta.
3. **Separa hechos y suposiciones.** “Cada pedido tiene un identificador” es un hecho del ejemplo. “El servicio siempre estará disponible” es una suposición.
4. **Compara opciones.** Por ejemplo, consultar directamente al servicio responsable o guardar una copia del estado en otro lugar.
5. **Explica qué cuesta cada opción.** Una copia puede ser rápida de consultar, pero quedar desactualizada.
6. **Define una comprobación.** La persona puede ver su propio pedido y no puede ver uno ajeno.

## 4. Ejemplo resuelto
**Necesidad:** el cliente consulta el estado actual de su entrega.

**Hechos:** el servicio de Entregas registra los cambios; cada pedido tiene un identificador.

**Suposición:** la aplicación podrá comunicarse siempre con Entregas. Esta idea se debe comprobar; no es garantía.

**Opción A:** copiar el estado dentro de la aplicación. Es fácil mostrarlo, pero puede quedar desactualizado cuando Entregas cambia el estado.

**Opción B:** consultar al servicio de Entregas cuando el cliente abre el seguimiento. El dato viene de su fuente responsable, pero la aplicación necesita manejar una espera o una falla.

**Decisión inicial:** usar la opción B y mostrar un mensaje claro si no hay respuesta. Comprobaría que el cliente ve su propio pedido, que no puede consultar otro y que un fallo no muestra una ubicación inventada.

La decisión podría cambiar si se observa una demora importante o si aumentan mucho las consultas. Registrar qué señal motivaría revisarla evita defenderla por costumbre.

## 5. Actividad de autoestudio
La empresa quiere avisar al cliente cuando una entrega vaya retrasada.

1. Escribe la necesidad sin proponer una tecnología.
2. Nombra dos personas o áreas afectadas.
3. Anota dos hechos y una suposición que debas comprobar.
4. Compara una forma manual y una automática de detectar retrasos.
5. Elige una opción; explica un beneficio y un costo.
6. Propón una prueba que muestre cuándo se envía el aviso y cuándo no.

### Respuesta modelo
“El cliente necesita saber si la entrega no llegará en la hora prevista”. Las personas afectadas son el cliente y soporte. Un hecho puede ser que existe una hora estimada; una suposición por comprobar es que esa estimación se actualiza cuando cambia la ruta.

La revisión manual es sencilla, pero puede detectar tarde el retraso. Una revisión automática avisa con más rapidez, pero necesita definir cuándo se considera retraso y puede generar avisos falsos. Una prueba podría comprobar que una entrega vencida sin actualización genera un aviso y que una entrega que todavía está dentro del plazo no lo genera.

## Comprueba lo que aprendiste
1. ¿La intuición debe eliminarse al tomar decisiones?
2. ¿Por qué conviene separar hechos de suposiciones?
3. ¿Qué dato o resultado te permitiría revisar una decisión?

**Respuestas:** no; la intuición sirve para proponer opciones. Separar hechos y suposiciones muestra qué falta comprobar. Una decisión se puede revisar cuando aparece evidencia que contradice una hipótesis o cuando cambian las necesidades.

## Conclusión
La intuición ayuda a proponer una solución; el método ayuda a comparar sus consecuencias. Una decisión arquitectónica es más sólida cuando parte de una necesidad, reconoce lo que aún no sabemos y define cómo comprobar si elegimos bien.
