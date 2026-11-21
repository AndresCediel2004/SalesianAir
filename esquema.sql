CREATE TABLE aviones (
    cod_avion TEXT PRIMARY KEY,
    modelo    TEXT NOT NULL
);

CREATE TABLE vuelos (
    id                    INTEGER PRIMARY KEY,
    codigo_vuelo          TEXT NOT NULL,
    cod_avion             TEXT NOT NULL REFERENCES aviones(cod_avion),
    fecha_salida          TEXT NOT NULL,
    origen                TEXT NOT NULL,
    destino               TEXT NOT NULL,
    pasajeros_registrados INTEGER NOT NULL CHECK (pasajeros_registrados >= 0)
);
