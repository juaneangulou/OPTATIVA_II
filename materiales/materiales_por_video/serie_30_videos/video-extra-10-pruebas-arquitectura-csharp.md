# Video extra 10: Pruebas de arquitectura en C# para proteger los límites del sistema

## Para estudiar por tu cuenta
Una regla de arquitectura escrita en un documento puede olvidarse durante un cambio. Por ejemplo, el dominio de Pedidos no debería depender de EF Core ni de una API externa. Una prueba puede convertir esa intención en una condición que se ejecuta con el resto del proyecto.

En este capítulo aprenderás qué verifican las pruebas de arquitectura, cómo elegir entre prueba unitaria e integración y qué límites conviene proteger.

## 1. Tipos de prueba y preguntas distintas
- **Prueba unitaria:** comprueba una regla o unidad aislada, por ejemplo que un pedido entregado no se cancele.
- **Prueba de integración:** comprueba que dos partes reales cooperan, por ejemplo que EF Core guarda y recupera un pedido.
- **Prueba de arquitectura:** comprueba restricciones estructurales, por ejemplo que el proyecto de dominio no referencia infraestructura.

Ninguna reemplaza a las demás. Una prueba de arquitectura puede confirmar dependencias permitidas, pero no demuestra que el flujo de negocio sea correcto.

## 2. Una regla estructural
Supongamos esta separación de proyectos:

```text
Logistica.Domain
Logistica.Application -> Logistica.Domain
Logistica.Infrastructure -> Logistica.Application + Logistica.Domain
Logistica.Api -> Logistica.Application + Logistica.Infrastructure
```

La regla importante: `Logistica.Domain` no debe depender de `Logistica.Infrastructure` ni de ASP.NET Core.

Puedes verificar dependencias de ensamblados con una biblioteca de pruebas de arquitectura .NET, por ejemplo NetArchTest. El siguiente fragmento es ilustrativo; verifica la API y versión de la biblioteca que instales:

```csharp
[Fact]
public void Dominio_no_debe_depender_de_Infraestructura()
{
    var resultado = Types
        .InAssembly(typeof(Pedido).Assembly)
        .ShouldNot()
        .HaveDependencyOn("Logistica.Infrastructure")
        .GetResult();

    Assert.True(resultado.IsSuccessful);
}
```

La prueba inspecciona el ensamblado de dominio y falla si detecta una dependencia hacia infraestructura. Asegúrate de que los nombres de ensamblado y espacios de nombres coincidan con tu solución.

## 3. Proteger reglas de capas
Otra regla puede exigir que los controladores vivan en la API y que el dominio no contenga tipos HTTP. Las bibliotecas de análisis permiten expresar reglas por nombres, atributos o capas, pero las reglas deben corresponder a una decisión arquitectónica real.

No prohíbas dependencias útiles sin entenderlas. Una regla demasiado amplia puede forzar excepciones y terminar ignorada.

## 4. Prueba unitaria de una regla
```csharp
[Fact]
public void No_permite_cancelar_un_pedido_entregado()
{
    var pedido = Pedido.Crear(Guid.NewGuid(), Guid.NewGuid());
    pedido.MarcarEntregado();

    Assert.Throws<InvalidOperationException>(() => pedido.Cancelar());
}
```

Esta prueba verifica comportamiento, no estructura. Debe ser rápida y no necesita base de datos.

## 5. Prueba de integración de persistencia
Una prueba de persistencia debe comprobar el proveedor y la configuración importantes para el sistema. EF Core InMemory no reproduce todas las características de una base relacional; puede ser útil para algunos casos, pero no demuestra que una consulta SQL, restricción o transacción funcione igual.

Para reglas dependientes del proveedor, usa una base de ensayo apropiada o un contenedor de prueba si el entorno lo permite. Asegúrate de limpiar datos y no apuntar accidentalmente a producción.

## 6. Pruebas como documentación ejecutable
Una prueba bien nombrada explica qué arquitectura se espera:

```text
Domain_no_depende_de_Infrastructure
Application_no_usa_EntityFrameworkDirectamente
Un_pedido_entregado_no_se_cancela
```

Cuando alguien cambia una dependencia, el fallo señala qué decisión debe revisarse. Si la arquitectura evoluciona legítimamente, actualiza la regla y la prueba de forma deliberada, no simplemente la desactives.

## 7. Actividad de autoestudio
Tu equipo decide que los casos de uso no deben importar clases de EF Core.

1. ¿Es una regla de comportamiento, integración o arquitectura?
2. ¿Qué proyecto revisarías?
3. ¿Qué prueba unitaria acompaña la regla de negocio de confirmar?
4. ¿Por qué una base InMemory no siempre reemplaza la prueba contra el motor real?
5. ¿Qué harías si una nueva decisión técnica requiere una excepción?

### Respuesta modelo
Es una regla de arquitectura. Revisaría el ensamblado de Application buscando dependencias a EF Core. Una prueba unitaria verifica que no se confirme un pedido con inventario insuficiente. InMemory puede comportarse distinto al motor relacional en transacciones, traducción de consultas y restricciones. Si existe una excepción, documentaría su razón, la limitaría al módulo necesario y actualizaría la regla con revisión consciente.

## Comprueba lo que aprendiste
1. ¿Qué demuestra una prueba de arquitectura?
2. ¿Qué tipo de prueba comprueba una regla de estado del pedido?
3. ¿Qué valida una prueba de integración?
4. ¿Por qué no conviene silenciar una prueba que falla tras un cambio?

### Respuestas
1. Que se respetan restricciones estructurales definidas para el código.
2. Una prueba unitaria.
3. Que componentes reales cooperan con la configuración usada en la prueba.
4. Porque puede estar señalando que se rompió un límite importante; primero hay que entender el cambio.

## Cierre de la ruta extra
Has recorrido decisiones que se complementan: organizar módulos, aislar reglas, persistir cambios, separar escritura y lectura, añadir comportamientos transversales, manejar eventos, coordinar procesos distribuidos, resistir fallas de red, acelerar lecturas y proteger límites con pruebas.

No conviertas los patrones en una lista obligatoria. Para cada uno, formula el problema concreto que resuelve, el costo que introduce y la prueba que demostraría que la solución funciona.
