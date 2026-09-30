# Video extra 9: Cache-Aside en C#: acelerar consultas sin perder control

## Para estudiar por tu cuenta
El tablero consulta repetidamente la información pública de zonas de entrega. Leer la base en cada solicitud puede ser costoso. Una caché puede acelerar lecturas, pero también puede devolver datos antiguos.

En este capítulo aprenderás el flujo Cache-Aside, cómo invalidar una entrada y qué decisiones de consistencia debes tomar.

## 1. ¿Qué es una caché?
Una **caché** conserva temporalmente datos que pueden volver a solicitarse pronto. La aplicación puede responder desde esa copia rápida en vez de consultar siempre la fuente principal.

En el patrón **Cache-Aside**, la aplicación administra la lectura:

1. Busca una clave en la caché.
2. Si existe, devuelve el valor (cache hit).
3. Si no existe (cache miss), consulta la fuente principal.
4. Guarda temporalmente el resultado y lo devuelve.

```text
Aplicación -> Caché
              | hit: devolver
              | miss
              v
          Base de datos -> guardar en caché -> devolver
```

## 2. Flujo ilustrativo en C#
```csharp
public async Task<ZonaDto?> ObtenerZonaAsync(
    string zonaId,
    CancellationToken cancellationToken)
{
    var cacheKey = $"zona:{zonaId}";
    var cached = await _cache.GetStringAsync(
        cacheKey,
        cancellationToken);

    if (cached is not null)
        return JsonSerializer.Deserialize<ZonaDto>(cached);

    var zona = await _db.Zonas
        .AsNoTracking()
        .Where(item => item.Id == zonaId)
        .Select(item => new ZonaDto(item.Id, item.Nombre, item.Activa))
        .SingleOrDefaultAsync(cancellationToken);

    if (zona is null)
        return null;

    await _cache.SetStringAsync(
        cacheKey,
        JsonSerializer.Serialize(zona),
        new DistributedCacheEntryOptions
        {
            AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5)
        },
        cancellationToken);

    return zona;
}
```

El ejemplo usa abstracciones comunes de ASP.NET Core. Los tipos `ZonaDto`, `_cache` y `_db` deben estar definidos e inyectados en tu aplicación. El código necesita manejo de errores de serialización y una política para disponibilidad de caché en producción.

## 3. Qué pasa cuando cambian los datos
Si una zona se desactiva pero la caché conserva `Activa = true`, algunas solicitudes pueden recibir información antigua.

Estrategias comunes:

- **Vencimiento:** aceptar datos antiguos durante un periodo corto.
- **Invalidación:** borrar la clave al actualizar la zona.
- **Versión de clave:** cambiar la versión para dejar de usar entradas anteriores.

En Cache-Aside, la actualización suele guardar primero en la base y después invalidar la caché. Si invalidar falla, el vencimiento limita cuánto tiempo dura el dato viejo. El orden y el riesgo aceptable dependen de la regla del negocio.

## 4. El valor correcto no siempre debe almacenarse
Cachea datos que sean reutilizados y cuyo nivel de frescura sea compatible con el usuario. No caches a ciegas:

- datos personales de un usuario bajo una clave compartida;
- autorizaciones que deben revocarse inmediatamente;
- respuestas que varían por identidad sin incluir esa identidad en la clave;
- consultas que casi nadie repite y que son baratas de obtener.

Una clave debe incluir los factores que cambian el resultado, como zona, idioma o versión. Si dos solicitudes diferentes comparten clave por error, pueden intercambiar respuestas incorrectamente.

## 5. Stampede y caídas
Cuando una clave expira y llegan muchas solicitudes al mismo tiempo, todas pueden consultar la base. Ese fenómeno se conoce como **cache stampede**. Según la escala, se puede agrupar la carga, usar expiraciones con dispersión o limitar la reconstrucción simultánea.

La caché puede estar caída. Decide si la aplicación consulta directamente la base, devuelve un error o usa un dato temporal si el negocio lo permite. No conviertas un error de caché en una espera ilimitada.

## 6. Medir antes de cachear
Registra tasa de aciertos, fallos, latencia, errores y volumen de entradas. Compara la carga y latencia de la fuente principal antes y después. Si no mejora una necesidad observada, quizá solo se añadió complejidad.

## 7. Actividad de autoestudio
El precio de envío cambia varias veces al día; el nombre de una zona cambia raramente. Decide qué cachear.

1. ¿Qué duración inicial probarías para cada dato y por qué?
2. ¿Qué invalidarías al editar una zona?
3. ¿Qué clave usarías para una tarifa que depende de zona y tipo de servicio?
4. ¿Qué dato jamás compartirías entre usuarios sin revisar la clave?
5. ¿Qué métrica observarías para saber si la caché sirve?

### Respuesta modelo
La duración depende de cuánta antigüedad tolere el negocio; la zona puede admitir varios minutos, mientras la tarifa puede requerir una duración menor o invalidación explícita. Al editar, se borra `zona:{id}`. La clave de tarifa incluiría zona y tipo de servicio, además de otros parámetros que afecten el cálculo. Una respuesta personalizada no debe compartirse con una clave genérica. La tasa de aciertos junto con latencia y carga de base permite evaluar el beneficio.

## Comprueba lo que aprendiste
1. ¿Qué hace la aplicación ante un cache miss?
2. ¿Cache-Aside actualiza automáticamente la caché al cambiar la base?
3. ¿Qué riesgo crea una clave incompleta?
4. ¿Qué estrategia limita la antigüedad de una entrada si falla la invalidación?

### Respuestas
1. Lee la fuente principal, guarda el resultado por un tiempo y lo devuelve.
2. No; la aplicación debe actualizarla o invalidarla.
3. Puede devolver a una solicitud datos calculados para otra.
4. El vencimiento con una duración adecuada.

## Cierre
Cache-Aside puede reducir latencia y lecturas repetidas, pero introduce un segundo lugar donde vive temporalmente el dato. Diseña claves, expiración, invalidación y comportamiento ante fallas como parte del requisito.
