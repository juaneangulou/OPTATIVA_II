# Video 8: Agentes de IA que revisan tu código en GitHub

## Para estudiar por tu cuenta
Un agente de inteligencia artificial puede revisar una propuesta de cambios y señalar errores o riesgos antes de integrarla. No es una persona responsable del sistema ni una garantía de seguridad: su salida es una sugerencia que tú debes verificar.

En esta clase aprenderás a usar un agente con un alcance acotado, a revisar lo que propone y a proteger el código y los datos del proyecto.

## 1. ¿Qué es una revisión de código?
Una **revisión de código** es la lectura de cambios antes de integrarlos en la rama principal. Busca problemas como una regla rota, un caso de error olvidado, una prueba faltante o un cambio difícil de mantener.

GitHub muestra los cambios en una **Pull Request**: una propuesta para integrar una rama en otra. Personas y herramientas pueden dejar comentarios sobre líneas concretas.

## 2. Qué puede hacer un agente de IA
Según su configuración y permisos, un agente puede:

- resumir los archivos modificados;
- buscar patrones repetidos o posibles defectos;
- proponer pruebas para casos límite;
- señalar dependencias o validaciones que parecen faltar;
- sugerir una explicación más clara del cambio.

El agente no conoce automáticamente todos los requisitos del negocio. Puede malinterpretar una regla o proponer una corrección que compila pero cambia el comportamiento deseado.

## 3. Del cambio al resultado, paso a paso
1. Abre una Pull Request pequeña, con un objetivo claro.
2. Proporciona al agente contexto relevante: qué comportamiento se espera y qué parte está fuera del alcance.
3. Pídele que cite archivos o líneas concretas para cada hallazgo.
4. Revisa cada sugerencia contra el requisito y el código.
5. Acepta solo los cambios que comprendes y puedes probar.
6. Ejecuta pruebas y análisis automáticos.
7. Una persona revisa el resultado final y decide si se integra.

Una instrucción útil pide al agente que separe “defecto probable”, “pregunta” y “sugerencia”, y que no cambie archivos sin autorización explícita.

## 4. Límites y precauciones
- No compartas contraseñas, tokens ni información personal con un agente que no tenga autorización para verla.
- Limita los permisos del agente a lo que necesita para la tarea.
- No permitas que una sugerencia cambie reglas del negocio sin comprobarlas.
- Trata comentarios del agente como hipótesis, no como hechos.
- Revisa cambios generados automáticamente antes de ejecutarlos.
- Las pruebas automáticas y la revisión humana siguen siendo necesarias.

Un agente puede pasar por alto un problema y también puede advertir un problema inexistente. La calidad de la revisión depende del contexto, del alcance y de la verificación.

## 5. Ejemplo: cambio en el estado de entrega
Cambias el estado de una entrega para que solo pase a “Entregada” después de registrar evidencia de recepción.

Una solicitud de revisión podría pedir:

- localizar la regla que permite cambiar el estado;
- comprobar si existe un camino sin evidencia;
- revisar si se añadieron pruebas para éxito y rechazo;
- citar el código que respalda cada hallazgo;
- no asumir que los estados de otros módulos tienen el mismo significado.

Si el agente dice “falta validar el repartidor”, debes revisar si esa condición forma parte del requisito. No la agregues solo porque la IA la mencionó.

## 6. Actividad de autoestudio
Escribe un prompt para revisar una Pull Request que cambia el estado de una entrega. Incluye:

1. El comportamiento esperado.
2. Dos casos que deben probarse.
3. Qué debe citar el agente si encuentra un problema.
4. Qué información no debe solicitar ni imprimir.
5. Qué decisiones no puede tomar automáticamente.

### Respuesta modelo
El prompt puede pedir revisar que una entrega no pase a “Entregada” sin evidencia, verificar pruebas para éxito y rechazo, citar las líneas relacionadas y no mostrar datos personales. Debe aclarar que el agente no debe cambiar la regla, aceptar la Pull Request ni afirmar cumplimiento sin evidencia.

## Comprueba lo que aprendiste
1. ¿La respuesta de un agente demuestra que el cambio es correcto?
2. ¿Qué debe hacer una persona ante un hallazgo de IA?
3. ¿Por qué hay que limitar los permisos y el contexto compartido?

**Respuestas:** no, debe comprobarse; verificar el hallazgo con el requisito, el código y las pruebas; para reducir exposición de datos y limitar el impacto de acciones equivocadas.

## Conclusión
Un agente de IA puede ampliar la revisión de una Pull Request, pero no reemplaza el conocimiento del requisito ni la responsabilidad de quien integra el cambio. Úsalo con contexto y permisos limitados, exige evidencia y comprueba cada sugerencia.
