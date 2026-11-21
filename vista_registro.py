
import solara
import ipyvuetify as v
import datos

campos = {
    "codigo_vuelo": solara.reactive("V-108"),
    "cod_avion": solara.reactive("HK-1001"),
    "fecha_salida": solara.reactive("2026-10-02 09:00"),
    "origen": solara.reactive("Bogota"),
    "destino": solara.reactive("Medellin"),
    "pasajeros_registrados": solara.reactive("140")
}

mensaje = solara.reactive("")

def procesar(conn, valores):
    """Valida y registra un vuelo."""
    if any(str(x).strip() == "" for x in valores.values()):
        return "Rechazado: hay campos vacíos"

    try:
        pasajeros = int(valores["pasajeros_registrados"])
    except (ValueError, TypeError):
        return "Rechazado: pasajeros_registrados debe ser un número entero"

    ok = datos.registrar(
        conn,
        valores["codigo_vuelo"],
        valores["cod_avion"],
        valores["fecha_salida"],
        valores["origen"],
        valores["destino"],
        pasajeros
    )

    return "Registrado" if ok else "Rechazado por la base (avión inexistente o código duplicado)"

@solara.component
def Registro(conn):
    for nombre, estado in campos.items():
        solara.InputText(nombre, value=estado)

    def guardar():
        valores = {k: e.value for k, e in campos.items()}
        mensaje.set(procesar(conn, valores))

    solara.Button("Guardar", on_click=guardar, color="primary")
    solara.Markdown(mensaje.value)