import json
from pathlib import Path
import pandas as pd
import solara
import datos

EJ = json.loads((Path(__file__).parent / "ejemplos.json").read_text(encoding="utf-8"))
parametro = solara.reactive(str(EJ["consulta"][1][0]))


@solara.component
def VistaOperativa(conn):
    solara.InputText("Parámetro", value=parametro)
    solara.DataFrame(pd.DataFrame(getattr(datos, EJ["consulta"][0])(conn, parametro.value)))
