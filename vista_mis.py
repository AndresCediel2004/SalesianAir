import json
from pathlib import Path
import pandas as pd
import solara
import datos

EJ = json.loads((Path(__file__).parent / "ejemplos.json").read_text(encoding="utf-8"))


@solara.component
def ReporteMIS(conn, argumento):
    solara.DataFrame(pd.DataFrame(getattr(datos, EJ["reporte"][0])(conn, argumento)))
