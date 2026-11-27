import inspect
import json
import re
from pathlib import Path

import solara
import datos

EJ = json.loads((Path(__file__).parent / "ejemplos.json").read_text(encoding="utf-8"))
REGISTRO = getattr(datos, EJ["registro_valido"][0])
CAMPOS = list(inspect.signature(REGISTRO).parameters)[1:]
campos = {c: solara.reactive("") for c in CAMPOS}
mensaje = solara.reactive("")
detalle = solara.reactive("")


def procesar(conn, valores):
    """Valida y registra. Devuelve 'Registrado' o 'Rechazado: ...'."""
    v = {c: str(valores.get(c, "")).strip() for c in CAMPOS}
    vacios = [c for c, valor in v.items() if valor == ""]
    if vacios:
        return "Rechazado: hay campos vacíos (" + ", ".join(vacios) + ")"
    v["codigo_vuelo"] = v["codigo_vuelo"].upper()
    v["asiento"] = v["asiento"].upper()
    if not re.fullmatch(r"[A-Z]{2}\d{3,4}", v["codigo_vuelo"]):
        return "Rechazado: el código del vuelo debe verse así: SA101"
    if not re.fullmatch(r"\d{5,15}", v["documento"]):
        return "Rechazado: el documento debe ser un número de 5 a 15 dígitos"
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", v["correo"]):
        return "Rechazado: el correo no tiene un formato válido"
    if not re.fullmatch(r"\d{1,2}[A-F]", v["asiento"]):
        return "Rechazado: el asiento debe ser fila y letra, por ejemplo 14C"
    detalle.set("")
    if datos.registrar(conn, *(v[c] for c in CAMPOS)):
        detalle.set("Código de reserva: **" + datos.codigo_de_reserva(conn, v["codigo_vuelo"], v["documento"]) + "**")
        return "Registrado"
    return "Rechazado: la base no aceptó el registro (vuelo inexistente o lleno, asiento ocupado o pasajero ya registrado en ese vuelo)"


@solara.component
def Registro(conn):
    for nombre, estado in campos.items():
        solara.InputText(nombre, value=estado)

    def guardar():
        try:
            mensaje.set(procesar(conn, {k: e.value for k, e in campos.items()}))
        except Exception as error:  # un fallo inesperado se muestra en pantalla, no se calla
            mensaje.set(f"Rechazado: no se pudo registrar ({type(error).__name__}: {error})")

    solara.Button("Guardar", on_click=guardar, color="primary")
    solara.Markdown(mensaje.value)
    solara.Markdown(detalle.value)
