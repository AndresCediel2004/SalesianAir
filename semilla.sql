INSERT INTO aviones (cod_avion, modelo) VALUES
    ('HK-1001', 'Airbus A320'),
    ('HK-2002', 'Boeing 737'),
    ('HK-3003', 'Airbus A319'),
    ('HK-4004', 'Boeing 787');

INSERT INTO vuelos (codigo_vuelo, cod_avion, fecha_salida, origen, destino, pasajeros_registrados) VALUES
    ('V-100', 'HK-1001', '2026-09-25 08:00', 'Bogota', 'Medellin', 150),
    ('V-101', 'HK-2002', '2026-09-25 10:30', 'Medellin', 'Cartagena', 120),
    ('V-102', 'HK-3003', '2026-09-26 14:00', 'Bogota', 'Cartagena', 110),
    ('V-103', 'HK-1001', '2026-09-27 08:00', 'Bogota', 'Medellin', 145),
    ('V-104', 'HK-4004', '2026-09-28 09:00', 'Bogota', 'Cali', 220),
    ('V-105', 'HK-2002', '2026-09-29 11:00', 'Bogota', 'Cartagena', 135),
    ('V-106', 'HK-3003', '2026-09-30 16:30', 'Medellin', 'Bogota', 95),
    ('V-107', 'HK-1001', '2026-10-01 07:15', 'Cali', 'Bogota', 140);
