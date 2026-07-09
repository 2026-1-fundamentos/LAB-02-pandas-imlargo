"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd


def pregunta_10():

    tabla = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    resultado = tabla.groupby("c1", sort=True)["c2"].apply(
        lambda serie: ":".join(serie.astype(str).tolist())
    )
    resultado.index.name = "_c1"
    return resultado.to_frame()
