# Aerolínea Comercial Salesiana Air

**App:** (pendiente)  
**Repositorio:** (pendiente)

**Necesidad:** Monitorear la programación de vuelos, ocupación e itinerarios por origen y destino para tomar decisiones operativas de flota.. **Quién decide:** Director de Operaciones de Vuelo y Gerente Comercial. **Tipo de SI:** MIS.

## Componentes del sistema de información

- **hardware:** Servidor central de base de datos local y computadores terminales en salas de abordaje
- **software:** Sistema Operativo Linux Server, SQLite 3, Python 3 y Solara Web App
- **datos:** Una fila = Un registro individual de vuelo con su código, avión asignado, itinerario y cantidad de pasajeros
- **personas:** Agente de abordaje que registra vuelos, Coordinador de logística que consulta itinerarios y Director que toma decisiones
- **tic:** Red de área local (LAN) de la aerolínea y API de datos SQLite

## Proceso

1. 1. Registro de los datos del vuelo e itinerario del avión
2. 2. Consulta de vuelos programados por código de avión u origen
3. 3. Generación del reporte consolidado de vuelos y pasajeros por ciudad de origen

## Cómo se usa


1. En la sección de consulta, la persona puede buscar los vuelos registrados utilizando el código del avión.
2. En la sección de reportes, puede consultar un resumen de vuelos y pasajeros según la ciudad de origen.
3. En la sección de registro, puede ingresar los datos de un nuevo vuelo, incluyendo código, avión, fecha, origen, destino y cantidad de pasajeros.
4. Con esta información puede consultar los vuelos disponibles, revisar la actividad registrada y llevar un mejor control de las operaciones de la aerolínea.


## Datos personales (Ley 1581 de 2012)


El sistema almacena información operativa de los vuelos, como el código del vuelo, la matrícula del avión, la fecha de salida, el origen, el destino y la cantidad de pasajeros registrados.
Estos datos no incluyen nombres, documentos de identidad, teléfonos ni otros datos personales de los pasajeros. Su finalidad es permitir la consulta, el registro y la generación de reportes sobre las operaciones de la aerolínea.
De acuerdo con la Ley 1581 de 2012 de Colombia, el tratamiento de datos personales debe respetar los derechos de privacidad de las personas. Este proyecto utiliza información operativa y evita recopilar datos personales innecesarios.


## Correr en su equipo

```
conda activate si2026
solara run app.py
```
