"""Capa de datos de mi proyecto: funciones con ?, sin tablero interactivo."""
import sqlite3
from pathlib import Path

AQUI = Path(__file__).parent  # la carpeta de este archivo


def conectar():
    """Abre base.db. Si no existe, la crea con esquema.sql y semilla.sql."""
    nueva = not (AQUI / "base.db").exists()
    conn = sqlite3.connect(AQUI / "base.db", check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    if nueva:
        conn.executescript((AQUI / "esquema.sql").read_text(encoding="utf-8"))
        conn.executescript((AQUI / "semilla.sql").read_text(encoding="utf-8"))
        conn.commit()
    return conn


def consultar(conn, parametro):
    """Consulta (TPS): filas de mi tabla de hechos filtradas por parametro."""
    sql = """SELECT id, codigo_vuelo, fecha_salida, origen, destino, pasajeros_registrados
             FROM vuelos
             WHERE cod_avion = ?
             ORDER BY fecha_salida"""
    return conn.execute(sql, (parametro,)).fetchall()


def reportar(conn, parametro):
    """Reporte (MIS): resumen con JOIN y GROUP BY, filtrado por parametro."""
    sql = """SELECT a.modelo, COUNT(v.id) AS total_vuelos, SUM(v.pasajeros_registrados) AS total_pasajeros
             FROM vuelos v JOIN aviones a ON a.cod_avion = v.cod_avion
             WHERE v.origen = ?
             GROUP BY a.modelo
             ORDER BY total_pasajeros DESC"""
    return conn.execute(sql, (parametro,)).fetchall()


def registrar(conn, codigo_vuelo, cod_avion, fecha_salida, origen, destino, pasajeros_registrados):
    """Registro (TPS): True si la base acepta la fila; False si la rechaza."""
    sql = """INSERT INTO vuelos (codigo_vuelo, cod_avion, fecha_salida, origen, destino, pasajeros_registrados)
             VALUES (?, ?, ?, ?, ?, ?)"""
    try:
        conn.execute(sql, (codigo_vuelo, cod_avion, fecha_salida, origen, destino, pasajeros_registrados))
        conn.commit()
        return True
    except sqlite3.IntegrityError as error:
        conn.rollback()
        print("Rechazado por la base:", error)
        return False
