import json
from pathlib import Path

import pandas as pd
import solara
import datos

EJ = json.loads((Path(__file__).parent / "ejemplos.json").read_text(encoding="utf-8"))
busqueda = solara.reactive(str(EJ["consulta"][1][0]))
NOMBRES = {"vuelo": "código de vuelo", "reserva": "código de reserva", "documento": "documento del pasajero"}


@solara.component
def VistaOperativa(conn):
    solara.InputText("Código de vuelo (SA101), de reserva (R00001) o documento", value=busqueda)
    tipo = datos.tipo_de_busqueda(busqueda.value)
    filas = datos.consultar(conn, busqueda.value)
    if filas:
        solara.Markdown(f"Búsqueda por **{NOMBRES[tipo]}**")
        solara.DataFrame(pd.DataFrame(filas, columns=datos.COLUMNAS_CONSULTA[tipo]))
    else:
        solara.Markdown(f"**No hay resultados** para ese {NOMBRES[tipo]}.")
