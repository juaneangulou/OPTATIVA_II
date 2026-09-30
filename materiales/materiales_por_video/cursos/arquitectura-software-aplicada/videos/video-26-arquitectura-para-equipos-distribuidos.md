# Video 26: Técnicas SAST, DAST y pentesting para seguridad en software

## Para estudiar por tu cuenta
Una aplicación puede guardar direcciones, teléfonos y estados de entrega. ¿Cómo buscamos fallas de seguridad antes de que alguien las use para ver datos que no le corresponden?

En esta clase compararás tres formas complementarias de revisar seguridad: **SAST**, **DAST** y **pentesting**. Verás qué examina cada una, cuándo sirve y por qué ninguna por sí sola puede demostrar que un sistema es completamente seguro.

## 1. El ejemplo: consultar el pedido de otra persona
En la plataforma logística, una persona inicia sesión y consulta su pedido. La aplicación recibe un identificador, busca el pedido y muestra el resultado.

Un riesgo aparece si el sistema confía solamente en el número que envía la pantalla. Una persona podría intentar consultar un pedido que pertenece a alguien más. La seguridad no consiste solo en ocultar botones; el sistema debe verificar que la persona tenga permiso para cada información solicitada.

Para revisar esta clase de riesgo, podemos estudiar el código, probar la aplicación funcionando y pedir una revisión especializada. Esas actividades se relacionan con SAST, DAST y pentesting.

## 2. SAST: revisar el código sin ejecutar la aplicación
**SAST** significa *Static Application Security Testing*, o análisis estático de seguridad de aplicaciones.

“Estático” significa que la herramienta analiza el código sin tener que ejecutar la aplicación. Busca patrones que puedan señalar riesgos, como contraseñas escritas directamente en archivos o una consulta construida de manera insegura.

Es parecido a revisar los planos de una casa para encontrar una puerta que no debería estar ahí, antes de construirla.

### Qué puede aportar
- Se puede ejecutar durante el desarrollo y revisar cambios con frecuencia.
- Puede señalar código que merece atención antes de publicar.
- Puede ayudar a que un desarrollador encuentre el lugar probable del problema.

### Qué no demuestra
- No siempre entiende el contexto completo ni sabe si el problema realmente se puede explotar.
- Puede omitir riesgos que dependen de la configuración o del funcionamiento real.
- Un resultado limpio no certifica que la aplicación sea segura.

Una herramienta puede marcar un posible problema que no aplica en ese caso; el equipo debe analizarlo, no ignorarlo ni aceptarlo automáticamente.

## 3. DAST: revisar la aplicación mientras está funcionando
**DAST** significa *Dynamic Application Security Testing*, o análisis dinámico de seguridad de aplicaciones.

“Dinámico” significa que se prueba una aplicación en ejecución. La herramienta o la persona envía solicitudes y observa las respuestas, normalmente sin leer el código fuente.

Es parecido a probar las puertas y ventanas de un edificio ya construido: intentas entrar por las rutas permitidas y observas si alguna deja pasar a quien no corresponde.

En el ejemplo logístico, una prueba controlada puede iniciar sesión con una cuenta de ensayo y confirmar que esa cuenta no puede consultar el pedido de otra.

### Qué puede aportar
- Revisa el comportamiento real de la aplicación y algunas configuraciones visibles.
- Puede encontrar problemas que solo aparecen cuando se conectan varios componentes.
- Ayuda a comprobar que las protecciones responden como se espera.

### Qué no demuestra
- Solo revisa las páginas y funciones a las que logra llegar.
- No sabe siempre qué resultado era el correcto para cada persona.
- Puede causar cambios si se ejecuta contra datos reales sin control.

Por eso se ejecuta en un entorno autorizado y preparado para pruebas, con cuentas y datos de ensayo.

## 4. Pentesting: una persona intenta encontrar y demostrar riesgos
**Pentesting** significa prueba de penetración. Es una revisión controlada donde una persona con autorización busca maneras de superar las protecciones y demostrar qué impacto tendría una falla.

Un pentester puede combinar información del diseño, pruebas de la aplicación y razonamiento humano. Por ejemplo, podría comprobar si una persona puede consultar pedidos de otras cuentas y documentar qué datos quedarían expuestos.

Antes de comenzar se acuerda el **alcance**: qué sistemas pueden probarse, en qué fechas, qué métodos están permitidos y a quién avisar si aparece un riesgo grave. Sin permiso y límites claros, una prueba puede afectar a usuarios reales o convertirse en una intrusión.

El informe debe explicar:

- Qué riesgo se encontró.
- Qué condiciones permitieron llegar a él.
- Qué impacto podría tener.
- Qué corrección se recomienda.
- Cómo repetir una prueba segura para confirmar que fue corregido.

Un pentest es una evaluación en un momento y un alcance determinados; no garantiza que nunca habrá nuevas fallas.

## 5. Comparación rápida
| Técnica | Qué revisa | Cuándo suele usarse | Ejemplo en la plataforma |
|---|---|---|---|
| SAST | Código fuente sin ejecutar la aplicación | Durante el desarrollo y revisión de cambios | Detectar una posible consulta insegura en el módulo de pedidos |
| DAST | Aplicación en funcionamiento | En un entorno de prueba antes de publicar y en revisiones periódicas | Comprobar que una cuenta no consulte pedidos ajenos |
| Pentesting | Sistema dentro de un alcance acordado, con revisión humana | Antes de una publicación importante o en una evaluación planificada | Seguir distintos caminos para comprobar si datos de clientes pueden quedar expuestos |

No se reemplazan entre sí. SAST ayuda a encontrar señales en el código; DAST observa el comportamiento en ejecución; el pentesting combina exploración y análisis humano dentro de límites autorizados.

## 6. El mismo riesgo, revisado de tres maneras
Queremos comprobar que la cuenta de Ana no pueda consultar el pedido de Luis.

### Revisión SAST
Revisamos el código donde se busca el pedido y vemos si la consulta incluye una comprobación de pertenencia o autorización. El análisis automático puede señalar una búsqueda que usa solo el número del pedido.

**Pregunta que responde:** “¿Veo en el código una posible falta de comprobación?”.

### Revisión DAST
En un entorno de ensayo, iniciamos sesión como Ana e intentamos consultar un identificador de pedido de Luis. Observamos si la respuesta oculta los datos y registra el acceso rechazado.

**Pregunta que responde:** “¿La aplicación funcionando responde de manera segura ante esta solicitud?”.

### Pentesting
Una revisión autorizada examina además si existen otros caminos, como una pantalla, una API diferente o una secuencia de pasos que permita alcanzar los datos. Se documenta el alcance y el impacto demostrado.

**Pregunta que responde:** “¿Puede una persona, combinando rutas permitidas dentro del alcance, superar las protecciones y con qué consecuencia?”.

Los tres resultados se complementan. Aunque una prueba DAST bloquee esta consulta, podría existir otro camino no probado.

## 7. Un flujo posible de seguridad
1. Durante el cambio, ejecuta análisis SAST y revisa los hallazgos relevantes.
2. Prepara una versión de prueba con cuentas y datos que no sean reales.
3. Ejecuta pruebas DAST sobre los recorridos de mayor riesgo.
4. Antes de una publicación importante, considera un pentest con alcance y autorización por escrito.
5. Corrige los problemas según impacto y urgencia.
6. Repite las pruebas que verifican la corrección.
7. Registra qué se revisó y qué quedó fuera.

No todas las aplicaciones necesitan exactamente el mismo calendario. La información financiera, de salud o personal merece controles más cuidadosos que una página sin datos privados.

## 8. Errores frecuentes
- **Confiar solo en herramientas:** las herramientas ayudan a encontrar señales, pero las personas deben interpretar resultados.
- **Creer que “cero hallazgos” significa “cero riesgo”:** cada técnica tiene límites y puede no revisar ciertos caminos.
- **Ejecutar DAST sobre producción sin plan:** una prueba podría cambiar datos o afectar el servicio.
- **Hacer un pentest sin permiso escrito:** las pruebas deben tener alcance, responsable y plan de comunicación.
- **No volver a probar después de corregir:** el cambio puede no resolver el problema o romper otra cosa.
- **No priorizar:** un hallazgo que expone pedidos ajenos requiere atención distinta a un aviso informativo sin impacto demostrado.

## 9. Actividad de autoestudio
La aplicación logística tiene una pantalla para consultar el estado de un pedido y otra para actualizarlo desde el área de operaciones.

1. Escribe un riesgo posible para la consulta del cliente y otro para la actualización del operador.
2. Para cada riesgo, elige si SAST, DAST o pentesting podría aportar evidencia y explica por qué.
3. Indica qué datos y cuentas de prueba prepararías.
4. Escribe qué no debería hacerse sin autorización.
5. Define cómo comprobarías que una falla corregida no volvió a aparecer.

### Pistas
- SAST revisa el código; DAST observa la aplicación funcionando.
- Pentesting necesita permiso y alcance definido.
- La aplicación debe validar permisos en el servidor, no solo ocultar un botón en la pantalla.

## 10. Respuesta modelo
- **Riesgo del cliente:** Ana puede consultar el pedido de Luis cambiando el identificador. DAST puede probar el comportamiento; SAST puede revisar el lugar donde se consulta y autoriza el pedido; un pentest puede buscar rutas adicionales dentro del alcance.
- **Riesgo del operador:** una cuenta sin permiso modifica el estado de entrega. Se pueden revisar controles en código, probar permisos en una aplicación de ensayo y pedir una evaluación humana autorizada.
- **Datos de prueba:** cuentas de ensayo con permisos distintos y pedidos ficticios que no contengan información privada real.
- **Límite:** no probar cuentas o sistemas de terceros ni ejecutar pruebas invasivas fuera del alcance acordado.
- **Verificación:** repetir la prueba negativa —Ana intenta consultar el pedido de Luis— y confirmar que no se exponen datos; además, revisar que Ana sí pueda consultar su propio pedido.

## 11. Comprueba lo que aprendiste
1. ¿Cuál de estas técnicas revisa el código sin ejecutar la aplicación?
2. ¿Cuál prueba el sistema en funcionamiento?
3. ¿Qué necesita quedar acordado antes de un pentest?
4. ¿Por qué una herramienta sin hallazgos no demuestra seguridad completa?

### Respuestas
1. SAST.
2. DAST.
3. El permiso, el alcance, las fechas, los sistemas y métodos permitidos, y a quién avisar ante un riesgo.
4. Cada revisión tiene límites y solo cubre los casos que pudo analizar o recorrer.

## Conclusión
SAST revisa señales en el código, DAST examina una aplicación funcionando y el pentesting realiza una evaluación humana autorizada. Juntas pueden dar una visión más completa, pero ninguna sustituye el diseño seguro, la protección de datos ni la corrección de hallazgos.

Al planear una revisión, pregunta qué quieres proteger, qué técnica puede aportar evidencia, qué queda fuera del alcance y cómo confirmarás que una corrección funciona.
