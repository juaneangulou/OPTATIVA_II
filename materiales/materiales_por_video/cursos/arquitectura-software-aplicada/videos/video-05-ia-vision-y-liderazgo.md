# Video 5: Behavior Driven Development para alinear equipos técnicos y de negocio

## Para estudiar por tu cuenta
Behavior Driven Development, o **BDD**, ayuda a expresar el comportamiento esperado de un sistema mediante ejemplos que las personas del negocio y quienes construyen el software puedan revisar juntos.

La idea no es llenar documentos ni reemplazar todas las pruebas. Es descubrir qué significa un requisito usando situaciones concretas antes de asumir que dos personas entienden lo mismo.

## 1. Un requisito que puede entenderse de varias maneras
“El pedido se confirma si hay inventario suficiente” parece claro, pero aún deja preguntas:

- ¿La cantidad debe estar disponible en un almacén específico?
- ¿Qué pasa si solo hay parte de los productos?
- ¿La reserva queda guardada aunque el pago falle?

BDD convierte esas dudas en ejemplos concretos que se pueden discutir y luego probar.

## 2. El formato Dado-Cuando-Entonces
Un escenario BDD suele escribirse con tres partes:

- **Dado:** el contexto inicial.
- **Cuando:** la acción que ocurre.
- **Entonces:** el resultado observable esperado.

Ejemplo:

```text
Escenario: confirmar un pedido con existencias suficientes
Dado que el almacén tiene 3 unidades del producto A
Cuando el cliente solicita 2 unidades
Entonces el pedido queda confirmado
Y quedan 1 unidad disponible
```

El escenario evita hablar solo de código: define qué debe ver quien usa el sistema.

## 3. Un ejemplo de caso límite
```text
Escenario: rechazar un pedido si falta inventario
Dado que el almacén tiene 1 unidad del producto A
Cuando el cliente solicita 2 unidades
Entonces el pedido no queda confirmado
Y se informa que la cantidad no está disponible
```

El segundo ejemplo descubre una condición que el primero no cubría. Los ejemplos normales y de error ayudan a aclarar el comportamiento.

## 4. De la conversación a una prueba
El flujo es:

1. Escribe una necesidad en palabras del usuario.
2. Crea un ejemplo con cantidades y resultado observable.
3. Revisa si el ejemplo responde las dudas de negocio.
4. Convierte el ejemplo en una prueba automatizada cuando sea útil.
5. Si la prueba falla, determina si el sistema o el ejemplo necesitan corrección.

En C#, una prueba automatizada puede invocar el caso de uso de confirmación con inventario de prueba y verificar el estado y la cantidad restante. El formato escrito y la prueba deben expresar el mismo comportamiento.

## 5. Cuándo BDD ayuda y cuándo estorba
BDD puede ayudar cuando existen reglas de negocio ambiguas, varias áreas deben acordar resultados o un error afecta una operación importante.

Puede estorbar si cada detalle técnico se escribe en escenarios largos que nadie revisa. Evita duplicar la implementación en una prosa demasiado específica. Describe el comportamiento que importa, no los pasos internos de cada método.

## 6. Actividad de autoestudio
Define dos escenarios para una entrega:

1. El repartidor marca el paquete como entregado y adjunta evidencia.
2. El repartidor intenta marcarlo como entregado sin evidencia.

Para cada escenario, completa Dado-Cuando-Entonces. Asegúrate de que el resultado se pueda observar y probar.

### Respuesta modelo
```text
Escenario: registrar una entrega con evidencia
Dado que el pedido 245 está en camino
Cuando el repartidor registra una evidencia válida de recepción
Entonces el pedido queda marcado como entregado
Y se guarda la hora de confirmación
```

```text
Escenario: rechazar una entrega sin evidencia
Dado que el pedido 245 está en camino
Cuando el repartidor intenta marcarlo como entregado sin evidencia
Entonces el pedido conserva el estado en camino
Y se informa que falta la evidencia requerida
```

## Comprueba lo que aprendiste
1. ¿Qué expresa Dado, Cuando y Entonces?
2. ¿BDD significa que todas las pruebas deben escribirse en frases?
3. ¿Por qué conviene escribir un escenario de error además del camino exitoso?

**Respuestas:** contexto inicial, acción y resultado; no, las pruebas pueden tener distintos niveles y formatos; el caso de error descubre límites y reglas que el camino feliz no muestra.

## Conclusión
BDD usa ejemplos de comportamiento para que negocio y tecnología puedan revisar el mismo significado. Su valor no está en la sintaxis, sino en detectar ambigüedades y convertir acuerdos importantes en pruebas repetibles.
