# Aerolínea Comercial

**App:** SalesianAir
**Repositorio:** Github

**Necesidad:** Monitorear y registrar información de las reservas de vuelo para la aerolínea SalesianAir. Visualizar un reporte de la cantidad de reservas para un vuelo para la toma de decisiones para gerencia

## Componentes del sistema de información

- **hardware:** Servidor central de base de datos local y computadores de la aerolínea SalesianAir
- **software:** Sistema Operativo Linux Server, SQLite 3, Python 3 y Solara
- **datos:** Se pueden hacer registros para reservar vuelos y a la vez se puede  observar el reporte de la cantidad de reservas por vuelo
- **personas:** Agente de abordaje que registra reservas de vuelo, Coordinador de logística que consulta itinerarios y Director que toma decisiones
- **tic:** Red de área local (LAN) de SalesianAir

## Proceso

1. Registro de los datos del vuelo e itinerario del avión
2. Consulta de vuelos programados por código de avión u origen
3. Generación del reporte consolidado de vuelos y pasajeros por ciudad de origen

## Cómo se usa

1. En la sección de consulta, la persona puede buscar los vuelos registrados utilizando el código del avión.
2. En la sección de reportes, puede consultar un resumen de vuelos y pasajeros según la ciudad de origen.
3. En la sección de registro, puede ingresar los datos de un nuevo vuelo, incluyendo código, avión, fecha, origen, destino y cantidad de pasajeros.
4. Con esta información puede consultar los vuelos disponibles, revisar la actividad registrada y llevar un mejor control de las operaciones de la aerolínea.


## Datos personales (Ley 1581 de 2012)


El sistema almacena información operativa de los vuelos, como el código del vuelo, la matrícula del avión, la fecha de salida, el origen, el destino y la cantidad de pasajeros registrados.
Estos datos no incluyen nombres, documentos de identidad, teléfonos ni otros datos personales de los pasajeros. Su finalidad es permitir la consulta, el registro y la generación de reportes sobre las operaciones de la aerolínea.
De acuerdo con la Ley 1581 de 2012 de Colombia, el tratamiento de datos personales debe respetar los derechos de privacidad de las personas. Este proyecto utiliza información operativa y evita recopilar datos personales innecesarios.
## Prompts de IA (Gemini)

1. Por favor para éste código para la vista de consulta haz que se pueda buscar también por: código de vuelo y documento. Y para la vista de reportes haz que también se pueda buscar por la ciudad de Origen.

## Correr en su equipo

```
conda activate si2026
solara run app.py
```
