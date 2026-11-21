import json
from pathlib import Path
import solara

FICHA = json.loads((Path(__file__).parent / "ficha.json").read_text(encoding="utf-8"))


@solara.component
def Encabezado():
    solara.Markdown("# " + FICHA["organizacion"] + "\n\n" + FICHA["necesidad"])
    for k in ["hardware", "software", "datos", "personas", "tic"]:
        solara.Markdown(f"- **{k}:** {FICHA[k]}")
