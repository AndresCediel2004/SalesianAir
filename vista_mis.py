import matplotlib.pyplot as plt
import pandas as pd
import solara
import datos

COLUMNAS = ["Vuelo", "Origen", "Destino", "Salida", "Reservados", "Capacidad", "Ocupación %"]


@solara.component
def ReporteMIS(conn, argumento):
    codigo, set_codigo = solara.use_state(str(argumento))
    solara.InputText("Reporte por código de vuelo (SA101) o por origen (BOG)", value=codigo, on_value=set_codigo)
    filas = datos.reportar(conn, codigo)
    if not filas:
        solara.Markdown("**No hay vuelos con ese código u origen.**")
        return
    tabla = pd.DataFrame(filas, columns=COLUMNAS)
    solara.DataFrame(tabla)
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.barh(tabla["Vuelo"], tabla["Reservados"], color="#2a6fdb")
    ax.invert_yaxis()
    ax.set_xlabel("asientos reservados")
    ax.spines[["top", "right"]].set_visible(False)
    solara.FigureMatplotlib(fig)
    plt.close(fig)
