# Video 15: Migraciones de base de datos con Flyway

## Título
Cómo cambiar la información que guarda un programa sin perder lo que ya existe

## De qué trata
Una empresa de entregas quiere que cada pedido muestre si está pendiente, en camino o entregado. Su programa ya guarda miles de pedidos, pero todavía no tiene un espacio para guardar ese estado. El equipo no puede pensar solo en los pedidos nuevos: también debe decidir qué hacer con los pedidos que ya existen.

En este video llamamos **base de datos** al lugar organizado donde el programa conserva información. Una **migración** es un cambio planificado a esa organización o a los datos que contiene. **Flyway** ayuda a aplicar esos cambios en orden y a recordar cuáles ya se hicieron.

## Lo que aprenderás
- Por qué agregar un dato nuevo también afecta a los pedidos antiguos.
- Cómo Flyway usa cambios numerados para que el equipo siga los mismos pasos.
- Por qué primero probamos en una copia y después verificamos el resultado.
- Qué hacer cuando no conocemos el estado real de un pedido antiguo.
- Por qué el registro de Flyway no reemplaza un respaldo.

## El ejemplo de la clase
La empresa tiene pedidos cuyo estado aparece en una hoja de trabajo aparte. Quiere guardar ese estado junto con cada pedido.

1. El equipo averigua qué datos guarda el programa y quién los utiliza.
2. Define qué significan “Pendiente”, “En camino”, “Entregado” y “Por confirmar”.
3. Prepara un archivo numerado que describe el cambio.
4. Prueba en una copia que no se pierdan pedidos ni se inventen estados.
5. Flyway aplica el cambio pendiente y registra que ya se ejecutó.
6. El equipo verifica que la aplicación siga consultando y mostrando los pedidos correctamente.

Si no hay información confiable sobre un pedido antiguo, mostrar “Por confirmar” es más responsable que inventar que está pendiente o entregado.

## Ideas para recordar
- Flyway ejecuta y registra cambios que el equipo preparó; no decide qué necesita el negocio.
- Las migraciones deben considerar la información que ya está guardada.
- Una prueba en una copia permite detectar problemas antes de afectar pedidos reales.
- Los archivos que ya se ejecutaron no se editan; una corrección se registra como un cambio nuevo.
- Flyway no guarda una copia de seguridad ni garantiza que cualquier cambio pueda deshacerse fácilmente.

## Preguntas para pensar
- ¿Qué riesgo existe si todos los pedidos antiguos reciben automáticamente el estado “Pendiente”?
- ¿Qué revisarías en una copia antes de cambiar la base de datos real?
- ¿Qué diferencia hay entre que Flyway recuerde un cambio y tener un respaldo de los pedidos?
- ¿Qué dato de la plataforma logística te gustaría agregar y qué harías con los pedidos anteriores?

## Conclusión
Flyway ayuda a que los cambios en una base de datos tengan un orden y un historial. La seguridad de la información depende también de las decisiones del equipo: entender los datos existentes, probar el cambio y comprobar que el programa sigue funcionando.
