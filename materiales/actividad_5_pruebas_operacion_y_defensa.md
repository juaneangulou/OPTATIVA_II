# Actividad 5: Pruebas, operación y defensa final

## Objetivo

Comprobar que el sistema se comporta correctamente, evaluar su operación y defender la arquitectura adoptada con argumentos técnicos y de negocio.

## Entregables obligatorios

- Enlace al repositorio de GitHub con el resultado final, pruebas, documentos e historial de commits.
- Enlace al video de sustentación final publicado en YouTube, Google Drive o Microsoft Teams.
- No adjuntar el archivo de video directamente; entregar únicamente su enlace de acceso.

## ¿Qué se evalúa?

- pruebas unitarias de reglas críticas,
- pruebas de integración relevantes,
- observabilidad y riesgos operativos,
- capacidad de explicar decisiones y trade-offs,
- defensa final del expediente arquitectónico.

## Conceptos clave

### 1. Pruebas unitarias
Validan reglas del dominio y lógicas de negocio.

Ejemplo:

- un pedido no puede confirmarse si el inventario es insuficiente,
- una entrega fallida debe registrarse con causa y responsable,
- un repartidor no puede aceptar dos entregas simultáneas en rutas incompatibles,
- una devolución debe requerir un pedido válido y un motivo de devolución.

### 2. Pruebas de integración
Validan que dos o más partes del sistema trabajan juntas.

Ejemplo:

- controller + caso de uso + repositorio,
- endpoint + base de datos + validación.

### 3. Observabilidad mínima
Debe haber forma de saber:

- qué falló,
- dónde falló,
- qué evento ocurrió,
- qué métricas o logs ayudan a diagnosticar.

### 4. Riesgos operativos
Incluye:

- tiempo de caída,
- errores de integración,
- fallas de validación,
- coste de operación,
- dificultad de evolución.

## Siempre responde estas preguntas

- ¿Qué se está probando y por qué?
- ¿Qué riesgo representa cada caso?
- ¿Qué pasa si falla una integración?
- ¿Cuál es el costo de mantener este diseño?
- ¿Qué cambiaría en la siguiente versión?

## Estructura recomendada de entrega

- suite de pruebas,
- resultados o evidencia de ejecución,
- análisis de riesgos,
- plan de evolución,
- documento final del proyecto.

## Video de sustentación

Tu defensa final debe sintetizar:

1. el problema que resolviste,
2. la arquitectura elegida,
3. por qué usaste esas decisiones,
4. cómo probaste la solución,
5. qué riesgos quedaron y cómo se mitigan,
6. qué harías en una próxima versión.

## Checklist final

- [ ] pruebas unitarias implementadas
- [ ] pruebas de integración ejecutadas
- [ ] riesgo operativo identificado
- [ ] observabilidad mínima documentada
- [ ] plan de evolución claro
- [ ] expediente final completo
- [ ] sustentación final con argumentos profesionales

## Regla final

La mejor arquitectura no es la más compleja ni la más elegante. Es la que se puede sostener, entender, probar y evolucionar con claridad.
